"""Bounded ROS image delivery: overwrite latest frames instead of Qt queues."""
import math
import os
import queue
import threading
import time
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage
from .simulation import DOMAIN
from .transect import TransectTask

AUTOPILOT_TOPIC='/mako/autopilot/manual_control'
NEUTRAL=(0.,0.,500.,0.)
KEY_RAMP=120     # per 50 ms: keyboard commands reach full scale in about 0.4 s
# The Mako's ArduSub forward/right axes point opposite to the ZED camera's view
# (realjoy uses invert_forward for the same reason). Commands here are in camera
# terms, so forward and lateral are flipped before they are sent.
FORWARD_SIGN=-1
LATERAL_SIGN=-1
TASKS={'Task 1':TransectTask}

VIEWS={'First person':'/zed2i/zed_node/left/image_rect_color',
       'Third person':'/third_person_camera/image_raw'}


def image_to_qimage(message):
    formats={'rgb8':QImage.Format_RGB888,'bgr8':QImage.Format_BGR888,
             'rgba8':QImage.Format_RGBA8888,'mono8':QImage.Format_Grayscale8}
    if message.encoding not in formats:raise ValueError('Unsupported RGB encoding: '+message.encoding)
    if message.width<=0 or message.height<=0 or len(message.data)<message.step*message.height:
        raise ValueError('Incomplete camera image')
    return QImage(bytes(message.data),message.width,message.height,message.step,
                  formats[message.encoding]).copy()


def image_to_rgb(message):
    channels={'rgb8':3,'bgr8':3,'rgba8':4,'bgra8':4}
    if message.encoding not in channels:raise ValueError('Unsupported RGB encoding: '+message.encoding)
    count=channels[message.encoding]
    rows=np.frombuffer(message.data,dtype=np.uint8,count=message.step*message.height).reshape(message.height,message.step)
    image=rows[:,:message.width*count].reshape(message.height,message.width,count)[...,:3]
    return image[...,::-1] if message.encoding.startswith('bgr') else image


class RosWorker(QThread):
    message=pyqtSignal(str)

    def __init__(self,domain=DOMAIN):
        super().__init__()
        self.domain=domain;self.lock=threading.Lock();self.frames={};self.telemetry={}
        self.requested_view='First person'
        self.commands=queue.Queue();self.stopping=threading.Event()
        # Autopilot state is only used on the ROS thread.
        self.task=None;self.task_name=None;self.task_command=None;self.task_frame_time=0
        self.published=[];self.override_since=None;self.release_until=0
        self.task_started=0;self.forward_time=0;self.forwarded=False
        # Keyboard target (x, y, z, r) from the UI thread; None when keyboard piloting is off.
        self.keyboard=None;self.keyboard_output=None

    def set_view(self,view):
        if view not in VIEWS:raise ValueError('Unknown camera view')
        with self.lock:
            self.requested_view=view;self.frames.pop('main',None)

    def clear_session(self):
        self.abort_task()
        with self.lock:self.frames.clear();self.telemetry.clear()

    def snapshot(self):
        with self.lock:return dict(self.frames),dict(self.telemetry)

    def frame(self,message,name,view=None):
        image=image_to_qimage(message)
        now=time.monotonic()
        if name=='bottom' and self.task and not self.task.finished:
            try:self.task_command=self.task.update(image_to_rgb(message),now)
            except Exception as error:self.end_task('Task stopped: '+str(error))
            else:
                self.task_frame_time=now
                if self.task.finished:self.end_task(self.task.status)
                else:self.set_task_status(self.task.status)
        with self.lock:
            if name=='main' and view!=self.requested_view:return
            previous=self.frames.get(name)
            period=now-previous[1] if previous else 0
            fps=(.8*previous[2]+.2/period) if previous and period>.001 else 0
            self.frames[name]=(image,now,fps)
            if name=='bottom':self.telemetry['bottom_time']=now

    def state(self,message):
        with self.lock:self.telemetry.update(connected=message.connected,armed=message.armed,
                                             mode=message.mode,state_time=time.monotonic())
        if self.task and (not message.connected or not message.armed):self.end_task('Vehicle disarmed; task stopped.')

    def pwm(self,message):
        with self.lock:self.telemetry['pwm']=list(message.channels[:6])

    def odometry(self,message):
        q=message.pose.pose.orientation
        yaw=math.atan2(2*(q.w*q.z+q.x*q.y),1-2*(q.y*q.y+q.z*q.z))
        velocity=message.twist.twist.linear
        with self.lock:self.telemetry.update(depth=max(0,-message.pose.pose.position.z),
            heading=(270-math.degrees(yaw))%360,
            speed=math.sqrt(velocity.x**2+velocity.y**2+velocity.z**2),nav_time=time.monotonic())

    def request_arm(self,armed):self.commands.put(('arm',armed))
    def request_mode(self,mode):self.commands.put(('mode',mode))
    def start_task(self,name):self.commands.put(('task',name))
    def set_keyboard(self,target):
        with self.lock:self.keyboard=target

    def next_command(self,now):
        """MANUAL_CONTROL values to publish now, or None to leave the joystick in charge."""
        command=self.camera_command(now)
        if command is None:return None
        x,y,z,r=command
        return (FORWARD_SIGN*x,LATERAL_SIGN*y,z,r)

    def camera_command(self,now):
        # x forward and y right as seen by the pilot cameras.
        with self.lock:keyboard=self.keyboard
        if self.task and keyboard and keyboard!=NEUTRAL:self.end_task('Keyboard input; task stopped.')
        if keyboard is None and self.keyboard_output is not None:
            self.keyboard_output=None;self.release_until=max(self.release_until,now+.5)
        if self.task:
            if now-self.task_frame_time>1.0:self.end_task('Bottom camera stalled; task stopped.')
            else:self.check_forwarding(now)
        if self.task:
            command=self.task_command
            return (float(command.x),float(command.y),float(command.z),float(command.r)) if command else NEUTRAL
        if keyboard is not None:
            current=self.keyboard_output or NEUTRAL
            self.keyboard_output=tuple(a+max(-KEY_RAMP,min(KEY_RAMP,b-a)) for a,b in zip(current,keyboard))
            return self.keyboard_output
        return NEUTRAL if now<self.release_until else None
    def abort_task(self):self.commands.put(('task',None))

    def set_task_status(self,text):
        with self.lock:
            changed=self.telemetry.get('task_status')!=text
            self.telemetry.update(task_status=text,task_active=self.task is not None)
        if changed:self.message.emit((self.task_name or 'Task')+': '+text)

    def end_task(self,text):
        # Send neutral briefly, then stop publishing so the joystick takes over again.
        if self.task is None:return
        self.set_task_status(text)
        self.task=None;self.task_command=None;self.published.clear();self.override_since=None
        self.release_until=time.monotonic()+.5
        with self.lock:self.telemetry['task_active']=False

    def begin_task(self,name):
        with self.lock:telemetry=dict(self.telemetry)
        fresh=time.monotonic()-telemetry.get('state_time',0)<3 and telemetry.get('connected')
        if self.task:self.message.emit(self.task_name+' is already running.');return False
        if not fresh or not telemetry.get('armed'):
            self.message.emit(name+': arm the ROV first.');return False
        if time.monotonic()-telemetry.get('bottom_time',0)>1.5:
            self.message.emit(name+': bottom camera has no live image.');return False
        self.task=TASKS[name]();self.task_name=name;self.task_command=None
        self.task_started=self.task_frame_time=time.monotonic();self.release_until=0
        self.forward_time=0;self.forwarded=False;self.override_since=None
        self.set_task_status(self.task.status)
        return True

    def manual_sent(self,message):
        # realjoy forwards autopilot commands unless the pilot moves a stick.
        if not self.task or not self.published:return
        sent=(message.x,message.y,message.z,message.r)
        if any(max(abs(a-b) for a,b in zip(sent,command))<=2 for command in self.published):
            self.forward_time=time.monotonic();self.forwarded=True;self.override_since=None
        elif self.override_since is None:self.override_since=time.monotonic()

    def check_forwarding(self,now):
        if self.forwarded and self.override_since and now-self.override_since>.3:
            self.end_task('Pilot moved the joystick; task stopped.')
        elif now-max(self.forward_time,self.task_started)>1.5:
            self.end_task('Autopilot commands are not reaching the vehicle. Rebuild Software2026 '
                          '(realjoy_node forwards them), then restart the simulation.')

    def run(self):
        node=None;context=None;executor=None
        try:
            os.environ['ROS_DOMAIN_ID']=str(self.domain)
            import rclpy
            from rclpy.context import Context
            from rclpy.node import Node
            from rclpy.executors import SingleThreadedExecutor
            from rclpy.qos import QoSProfile,ReliabilityPolicy,HistoryPolicy
            from rclpy.parameter import Parameter
            from sensor_msgs.msg import Image
            from nav_msgs.msg import Odometry
            from mavros_msgs.msg import State,RCOut,ManualControl
            from mavros_msgs.srv import CommandBool,SetMode
            context=Context();rclpy.init(context=context)
            node=Node('mako_pilot_station',context=context,parameter_overrides=[Parameter('use_sim_time',value=True)])
            executor=SingleThreadedExecutor(context=context);executor.add_node(node)
            qos=QoSProfile(depth=1,history=HistoryPolicy.KEEP_LAST,reliability=ReliabilityPolicy.BEST_EFFORT)
            node.create_subscription(State,'/mavros/state',self.state,qos)
            node.create_subscription(RCOut,'/mavros/rc/out',self.pwm,qos)
            node.create_subscription(Odometry,'/odometry/gz',self.odometry,qos)
            node.create_subscription(Image,'/bottom_camera/image_raw',lambda msg:self.frame(msg,'bottom'),qos)
            arming=node.create_client(CommandBool,'/mavros/cmd/arming')
            mode=node.create_client(SetMode,'/mavros/set_mode')
            autopilot=node.create_publisher(ManualControl,AUTOPILOT_TOPIC,10)
            node.create_subscription(ManualControl,'/mavros/manual_control/send',self.manual_sent,10)
            active_view=None;video=None;last_autopilot=0
            while not self.stopping.is_set():
                with self.lock:view=self.requested_view
                if view!=active_view:
                    if video:node.destroy_subscription(video)
                    video=node.create_subscription(Image,VIEWS[view],lambda msg,view=view:self.frame(msg,'main',view),qos)
                    active_view=view
                try:action,value=self.commands.get_nowait()
                except queue.Empty:pass
                else:
                    if action=='task':
                        if value is None:
                            if self.task:self.end_task('Aborted by the pilot.')
                            continue
                        if not self.begin_task(value):continue
                        # The task controls depth with climb-rate commands.
                        with self.lock:current=self.telemetry.get('mode')
                        if current=='ALT_HOLD':continue
                        action,value='mode','ALT_HOLD'
                    client=arming if action=='arm' else mode
                    if not client.service_is_ready():self.message.emit('Autopilot is not ready for this command.')
                    else:
                        request=CommandBool.Request(value=value) if action=='arm' else SetMode.Request(custom_mode=value)
                        future=client.call_async(request)
                        def done(future,action=action,value=value):
                            try:
                                response=future.result()
                                accepted=response.success if action=='arm' else response.mode_sent
                                self.message.emit(f'{action.title()} {value}: '+('accepted' if accepted else 'rejected by autopilot'))
                            except Exception as error:self.message.emit(str(error))
                        future.add_done_callback(done)
                now=time.monotonic()
                command=self.next_command(now) if now-last_autopilot>=.05 else None
                if command is not None:
                    message=ManualControl();message.x,message.y,message.z,message.r=command
                    autopilot.publish(message);last_autopilot=now
                    if self.task:
                        self.published.append(command);del self.published[:-4]
                executor.spin_once(timeout_sec=.025)
        except Exception as error:self.message.emit('ROS connection error: '+str(error))
        finally:
            if executor:executor.shutdown(timeout_sec=1)
            if node:node.destroy_node()
            if context and context.ok():context.shutdown()

    def stop(self):
        self.stopping.set();self.wait(2500)
