"""Closed-loop check of the Task 1 transect autopilot without ROS or Gazebo.

A pinhole bottom camera (90 degree HFOV, image up = forward) renders the pool
fly_transect geometry on light tiles; a simple vehicle model applies the
autopilot's MANUAL_CONTROL commands with ALT_HOLD-style heave deadband.
Run: python3 Software2026/src/real_joy/test/check_transect.py
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from mako_station.transect import TransectTask, RailTracker

WIDTH,HEIGHT=640,360
FOCAL=WIDTH/2
RADIUS=0.0105
X0,X1=1.0,4.0                       # rail ends in the pool (world X)
RAILS=[(-4.15,'red'),(-3.75,'blue'),(-3.25,'blue'),(-2.85,'red')]
COLOURS={'red':(217,6,9),'blue':(6,31,204),'black':(6,6,6),'yellow':(255,217,4)}
TILE=np.array((174,221,230),float)
U,V=np.meshgrid(np.arange(WIDTH)-WIDTH/2+.5,np.arange(HEIGHT)-HEIGHT/2+.5)


def render(x,y,yaw,height):
    """Bottom camera image at world pose (x, y, yaw) and camera height above the floor."""
    right=U/FOCAL*height;forward=-V/FOCAL*height
    wx=x+forward*math.cos(yaw)+right*math.sin(yaw)
    wy=y+forward*math.sin(yaw)-right*math.cos(yaw)
    image=np.empty((HEIGHT,WIDTH,3));image[:]=TILE
    grout=((np.mod(wx,0.125)<0.006)|(np.mod(wy,0.125)<0.006))
    image[grout]=TILE*0.9
    for rail_y,colour in RAILS:
        image[(np.abs(wy-rail_y)<RADIUS)&(wx>=X0)&(wx<=X1)]=COLOURS[colour]
    for end in (X0,X1):
        across=np.abs(wx-end)<RADIUS
        image[across&(wy>=-4.15)&(wy<-3.75)]=COLOURS['yellow']
        image[across&(wy>=-3.75)&(wy<=-3.25)]=COLOURS['black']
        image[across&(wy>-3.25)&(wy<=-2.85)]=COLOURS['yellow']
    return image.astype(np.uint8)


def red_pixels(image):
    r,g,b=(image[...,i].astype(int) for i in range(3))
    return int(((r>150)&(g<60)&(b<60)).sum())


def red_visible(image):
    return red_pixels(image)>0


def fly(x,y,yaw,height,drift=0.02,seconds=120):
    task=TransectTask(now=0.0);dt=1/15;t=0.0
    forward_speed=lateral_speed=0.0;red_tracking=0;states=[];forward_with_red=0;red_seen=False
    while t<seconds and not task.finished:
        image=render(x,y,yaw,height)
        command=task.update(image,now=t)
        if task.state=='track' and red_visible(image):red_tracking+=1
        # With red clearly visible: never forward while descending, and never forward while tracking.
        if red_pixels(image)>=0.003*WIDTH*HEIGHT and task.state in ('align','track'):
            red_seen=True
            if command.x>0 and (command.z<500 or task.state=='track'):forward_with_red+=1
        if not states or states[-1]!=task.state:states.append(task.state)
        forward_speed+=(command.x/1000*0.6-forward_speed)*0.25
        lateral_speed+=(command.y/1000*0.5-lateral_speed)*0.25
        yaw-=command.r/1000*1.2*dt                     # positive r turns clockwise (right)
        heave=command.z-500
        climb=0 if abs(heave)<100 else math.copysign((abs(heave)-100)/400*0.4,heave)
        height=max(0.15,height+climb*dt)
        x+=(forward_speed*math.cos(yaw)+lateral_speed*math.sin(yaw))*dt
        y+=(forward_speed*math.sin(yaw)-lateral_speed*math.cos(yaw)-drift)*dt
        t+=dt
    return task,dict(x=x,y=y,yaw=yaw,height=height,time=t,red_tracking=red_tracking,states=states,
                     forward_with_red=forward_with_red,red_seen=red_seen)


def check(name,result,end_x=(3.75,4.35)):
    task,final=result
    print(f"{name}: {task.state} after {final['time']:.1f}s at x={final['x']:.2f} y={final['y']:.2f} "
          f"height={final['height']:.2f} yaw={math.degrees(final['yaw']):.1f}deg states={final['states']} "
          f"red frames while tracking={final['red_tracking']}  ({task.status})")
    assert task.state=='done',task.status
    assert end_x[0]<=final['x']<=end_x[1],final
    assert abs(final['y']+3.5)<0.15,final
    assert final['red_tracking']==0,final
    assert final['forward_with_red']==0,'Moved forward while red rails were in view'


# Detection on single frames.
tracker=RailTracker()
observation=tracker.analyze(render(2.5,-3.5,0.0,0.45),now=0.0)
assert observation.rails==2 and abs(observation.offset)<0.03 and abs(observation.angle)<0.02,observation
assert abs(observation.spacing-0.5/(2*0.45))<0.02 and not observation.red_left and not observation.red_right,observation
observation=RailTracker().analyze(render(2.5,-3.6,0.0,0.45),now=0.0)
assert observation.offset<-0.1,'Corridor should appear left when the ROV is right of centre'
observation=RailTracker().analyze(render(2.5,-3.5,0.2,0.45),now=0.0)
assert observation.angle>0.1,'Rails should point to the right when the ROV is yawed left'
observation=RailTracker().analyze(render(2.5,-3.5,0.0,1.0),now=0.0)
assert observation.red_left and observation.red_right and observation.spacing<0.3,observation
observation=RailTracker().analyze(render(3.95,-3.5,0.0,0.45),now=0.0)
assert observation.bar is not None and observation.rails_behind_bar and not observation.rails_ahead_of_bar,observation
observation=RailTracker().analyze(render(1.05,-3.5,0.0,0.45),now=0.0)
assert observation.bar is not None and observation.rails_ahead_of_bar and not observation.rails_behind_bar,observation
print('PASS: single-frame rail, offset, angle, spacing, red and marker detection')

result=fly(0.6,-3.35,0.15,1.6);check('In front, high, offset and yawed',result)
assert result[1]['red_seen'],'The high start should show the red rails first'
# Above the corridor but high: red and blue visible, so it must descend in place before moving on.
task=TransectTask(now=0.0);command=task.update(render(1.6,-3.5,0.0,1.2),now=0.0)
assert command.x==0 and command.z<500 and 'descending' in task.status,(command,task.status)
check('Above the start bar, low',fly(1.0,-3.6,-0.1,0.5))
# Above the corridor and high: red and blue visible. It must descend with no forward command
# until the red rails leave the picture.
task=TransectTask(now=0.0);height=1.4;t=0.0
while red_pixels(render(1.8,-3.5,0.0,height))>0 and t<30:
    command=task.update(render(1.8,-3.5,0.0,height),now=t)
    assert command.x==0,('Moved forward while red was visible',height,command,task.status)
    climb=0 if abs(command.z-500)<100 else (abs(command.z-500)-100)/400*0.4*(1 if command.z>500 else -1)
    height+=climb/15;t+=1/15
assert t<30 and height<0.65,(t,height)
print(f'Above the corridor, high: descended from 1.40 m to {height:.2f} m in {t:.1f}s with no forward command until only blue was visible')
check('Already inside the corridor',fly(1.8,-3.5,0.0,0.6,drift=-0.03))
task,final=fly(-3.0,0.0,0.0,0.45,seconds=20)
assert task.state=='failed' and 'not visible' in task.status,task.status
print('PASS: closed-loop transect runs descend in place while red is visible, then stop above the end marker; missing rails stop safely')
