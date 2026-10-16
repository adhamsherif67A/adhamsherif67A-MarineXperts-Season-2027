"""Task 1 autopilot: fly the transect between the blue rails with the bottom camera.

The pool transect (robot_description fly_transect) is four parallel 3 m rails on
the floor: red outer rails and blue inner rails, 0.5 m between the blue centres and
0.4 m from each blue rail to its red rail. Each end has a black bar between the
blue rails. The vehicle flies along the blue corridor, low enough that the red
rails stay outside the bottom camera, and stops above the far black bar. Whenever
red is in view it stops moving forward and descends/centres until only blue remains
(if the rails are still ahead, it first creeps over them at constant depth).

Bottom camera: 90 degree horizontal field of view, image up = vehicle forward,
image right = vehicle right. Commands use ArduSub MANUAL_CONTROL units:
x forward(+), y right(+), r yaw clockwise(+) in -1000..1000; z 0..1000, 500 neutral.
"""
import math
import time
from dataclasses import dataclass
import numpy as np

# Flip these if a real camera mounting differs from the simulated one.
IMAGE_UP_IS_FORWARD=True
IMAGE_RIGHT_IS_RIGHT=True

ANALYSIS_WIDTH=320          # images are subsampled to about this width
TARGET_SPACING=0.55         # blue spacing / image width: about 0.45 m above the rails
SPACING_TOLERANCE=0.05
FORWARD_COMMAND=220         # cruise thrust along the corridor
APPROACH_COMMAND=150        # used while the rails are not yet visible
LATERAL_GAIN=600;LATERAL_LIMIT=350
YAW_GAIN=900;YAW_LIMIT=300
HEAVE_GAIN=900;HEAVE_LIMIT=260
HEAVE_DEADBAND=110          # ALT_HOLD ignores small throttle offsets around 500
RED_PUSH=220
ALIGN_SECONDS=1.0
APPROACH_TIMEOUT=10.0
LOST_TIMEOUT=1.5
TASK_TIMEOUT=150.0


def classify(rgb):
    """Boolean masks for the blue, red and black pipes on light pool tiles."""
    r,g,b=(rgb[...,i].astype(np.int16) for i in range(3))
    blue=(b>45)&(b>2*r)&(2*b>5*g)
    red=(r>45)&(2*r>5*g)&(2*r>5*b)
    black=np.maximum(np.maximum(r,g),b)<50
    return blue,red,black


def row_runs(mask):
    """Centres of horizontal True runs, grouped by row: {row: array of centres}."""
    step=np.diff(mask.astype(np.int8),axis=1,prepend=0,append=0)
    rows,starts=np.nonzero(step==1)
    _,ends=np.nonzero(step==-1)
    centres=(starts+ends-1)/2.0
    result={}
    if len(rows):
        split=np.flatnonzero(np.diff(rows))+1
        for row,group in zip(rows[np.r_[0,split]],np.split(centres,split)):result[int(row)]=group
    return result


def fit_line(ys,xs):
    """Robust x = a*y + b fit; None when the points are too few or too short."""
    ys=np.asarray(ys,float);xs=np.asarray(xs,float)
    if len(ys)<6 or np.ptp(ys)<8:return None
    a,b=np.polyfit(ys,xs,1)
    residual=np.abs(xs-(a*ys+b));keep=residual<=max(2.0,3*np.median(residual))
    if keep.sum()>=6 and not keep.all():a,b=np.polyfit(ys[keep],xs[keep],1)
    return float(a),float(b)


@dataclass
class Observation:
    rails:int=0                 # 0, 1 or 2 blue rails found
    offset:float=0.0            # corridor centre, -1 (left edge) .. 1 (right edge)
    angle:float=0.0             # rail direction, radians; positive = rails turn right ahead
    spacing:float=None          # blue spacing / image width, corrected for angle
    red_left:bool=False
    red_right:bool=False
    rails_end:float=None        # lowest rail row, 0 (top/ahead) .. 1 (bottom/behind)
    bar:float=None              # black bar row, 0 (top/ahead) .. 1 (bottom/behind)
    rails_ahead_of_bar:bool=False
    rails_behind_bar:bool=False


class RailTracker:
    """Find the two blue rails in successive bottom-camera frames."""

    def __init__(self):
        self.left=None;self.right=None;self.spacing_px=None;self.width=None;self.seen=0.0

    def analyze(self,rgb,now=None):
        now=time.monotonic() if now is None else now
        stride=max(1,rgb.shape[1]//ANALYSIS_WIDTH)
        image=rgb[::stride,::stride,:3]
        if not IMAGE_UP_IS_FORWARD:image=image[::-1]
        if not IMAGE_RIGHT_IS_RIGHT:image=image[:,::-1]
        height,width=image.shape[:2]
        if self.width!=width:self.left=self.right=self.spacing_px=None;self.width=width
        if now-self.seen>1.0:self.left=self.right=self.spacing_px=None
        blue,red,black=classify(image)
        observation=Observation()
        minimum=max(4,int(0.0005*height*width))   # a short stretch of pipe is enough
        observation.red_left=int(red[:,:width//2].sum())>=minimum
        observation.red_right=int(red[:,width//2:].sum())>=minimum

        left_points=([],[]);right_points=([],[]);rows_with_rails=set()
        for row,centres in row_runs(blue).items():
            if self.left and self.right:
                predicted=(self.left[0]*row+self.left[1],self.right[0]*row+self.right[1])
                gate=max(6.0,0.3*abs(predicted[1]-predicted[0]))
                for x in centres:
                    side=int(abs(x-predicted[1])<abs(x-predicted[0]))
                    if abs(x-predicted[side])<=gate:
                        (right_points if side else left_points)[0].append(row)
                        (right_points if side else left_points)[1].append(x);rows_with_rails.add(row)
            elif len(centres)==2 and centres[1]-centres[0]>0.08*width:
                left_points[0].append(row);left_points[1].append(centres[0])
                right_points[0].append(row);right_points[1].append(centres[1]);rows_with_rails.add(row)
        left=fit_line(*left_points);right=fit_line(*right_points)
        if left and right and abs(left[0]-right[0])>0.35:
            # The rails are parallel: drop the shorter, less reliable fit.
            if len(left_points[0])<len(right_points[0]):left=None
            else:right=None
        reference=height/2.0
        if left and right:
            xl=left[0]*reference+left[1];xr=right[0]*reference+right[1]
            if xr-xl<0.06*width:left=right=None
            else:self.spacing_px=xr-xl
        observation.rails=int(left is not None)+int(right is not None)
        # One rail visible: place the other one at the last measured spacing.
        if left and not right and self.spacing_px:right=(left[0],left[1]+self.spacing_px)
        if right and not left and self.spacing_px:left=(right[0],right[1]-self.spacing_px)
        if not (left and right):
            observation.rails=0;self.left=self.right=None;return observation
        self.left,self.right,self.seen=left,right,now
        if rows_with_rails:observation.rails_end=max(rows_with_rails)/height
        slope=(left[0]+right[0])/2.0
        observation.angle=math.atan(-slope)
        centre=((left[0]+right[0])*reference+left[1]+right[1])/2.0
        observation.offset=(centre-width/2.0)/(width/2.0)
        if observation.rails==2:
            observation.spacing=(self.spacing_px/width)*math.cos(observation.angle)

        # A black bar fills most of the corridor between the rails for a few rows.
        bar_rows=[]
        for row in range(height):
            xl=int(round(left[0]*row+left[1]))+3;xr=int(round(right[0]*row+right[1]))-2
            xl=max(0,xl);xr=min(width,xr)
            if xr-xl>=6 and black[row,xl:xr].mean()>0.5:bar_rows.append(row)
        if len(bar_rows)>=2:
            bar=float(np.median(bar_rows));gap=max(3,int(0.04*height))
            above=[row for row in rows_with_rails if row<bar-gap]
            below=[row for row in rows_with_rails if row>bar+gap]
            observation.bar=bar/height
            observation.rails_ahead_of_bar=len(above)>=max(3,0.3*max(1,bar-gap))
            observation.rails_behind_bar=len(below)>=max(3,0.3*max(1,height-bar-gap))
        return observation


@dataclass
class Command:
    x:float=0.0
    y:float=0.0
    z:float=500.0
    r:float=0.0


def clip(value,limit):
    return max(-limit,min(limit,value))


class TransectTask:
    """State machine: approach, descend/align over the corridor, track, stop on the far bar."""

    def __init__(self,now=None):
        now=time.monotonic() if now is None else now
        self.tracker=RailTracker();self.state='approach';self.started=now;self.state_since=now
        self.last_rails=None;self.aligned_since=None;self.command=Command()
        self.red_frames=0;self.track_frames=0;self.passed_start=False
        self.status='Looking for the blue rails'

    @property
    def finished(self):
        return self.state in ('done','failed')

    def set_state(self,state,status,now):
        self.state=state;self.status=status;self.state_since=now

    def update(self,rgb,now=None):
        now=time.monotonic() if now is None else now
        observation=self.tracker.analyze(rgb,now)
        if self.finished:return Command()
        if now-self.started>TASK_TIMEOUT:
            self.set_state('failed','Stopped: time limit reached',now);return Command()
        if observation.rails:self.last_rails=now
        command=Command()

        if self.state=='approach':
            if observation.rails:self.set_state('align','Rails found: descending and centring',now)
            elif now-self.state_since>APPROACH_TIMEOUT:
                self.set_state('failed','Stopped: blue rails not visible. Position the ROV in front of the transect.',now)
                return Command()
            else:
                command.x=APPROACH_COMMAND;self.command=command;return command

        if not observation.rails:
            lost=now-(self.last_rails or now)
            if self.state=='track' and lost>LOST_TIMEOUT and now-self.state_since>4.0:
                self.set_state('done','Task 1 complete: end of the rails reached',now);return Command()
            if lost>4.0:
                self.set_state('failed','Stopped: lost the blue rails',now);return Command()
            # Briefly coast with the last steering, without forward thrust.
            command=Command(y=self.command.y*0.5,z=500,r=self.command.r*0.5)
            self.command=command;return command

        command.y=clip(LATERAL_GAIN*observation.offset,LATERAL_LIMIT)
        command.r=clip(YAW_GAIN*observation.angle,YAW_LIMIT)
        if observation.spacing is not None:
            error=observation.spacing-TARGET_SPACING
            if abs(error)>SPACING_TOLERANCE/2:
                # Small spacing means too high: descend (z below 500).
                magnitude=min(HEAVE_LIMIT,HEAVE_DEADBAND+HEAVE_GAIN*(abs(error)-SPACING_TOLERANCE/2))
                command.z=500+math.copysign(magnitude,error)
        if observation.red_left and observation.red_right:
            command.z=min(command.z,500-HEAVE_DEADBAND-80)
        elif observation.red_left:command.y=clip(command.y+RED_PUSH,LATERAL_LIMIT)
        elif observation.red_right:command.y=clip(command.y-RED_PUSH,LATERAL_LIMIT)

        red=observation.red_left or observation.red_right
        if red:
            self.status=('Red and blue in view: holding position and descending' if observation.red_left and observation.red_right
                         else 'Red in view on the '+('left' if observation.red_left else 'right')+': holding position and centring')
        elif self.state=='align':self.status='Rails found: descending and centring'
        elif self.state=='track':self.status='Following the blue corridor'+(' (start marker passed)' if self.passed_start else '')

        aligned=(abs(observation.offset)<0.15 and abs(observation.angle)<0.12 and
                 observation.spacing is not None and abs(observation.spacing-TARGET_SPACING)<SPACING_TOLERANCE and
                 not (observation.red_left or observation.red_right))
        if self.state=='align':
            if observation.rails_end is not None and observation.rails_end<0.6:
                # The rails start ahead: creep forward until the ROV is above them. With red
                # in view, hold depth while creeping so the rails stay in the picture, and
                # descend only once above them (never forward and down together).
                command.x=APPROACH_COMMAND*0.8
                if red:
                    command.z=500;self.status='Red and blue in view: moving over the rails before descending'
            elif red:command.x=0
            self.aligned_since=(self.aligned_since or now) if aligned else None
            if self.aligned_since and now-self.aligned_since>=ALIGN_SECONDS:
                self.set_state('track','Following the blue corridor',now)
            elif now-self.state_since>25 and observation.rails==2:
                self.set_state('track','Following the blue corridor (alignment approximate)',now)
        if self.state=='track':
            self.track_frames+=1
            if observation.red_left or observation.red_right:self.red_frames+=1
            if observation.bar is not None:
                if observation.rails_ahead_of_bar and not observation.rails_behind_bar and not self.passed_start:
                    self.passed_start=True
                elif observation.rails_behind_bar and not observation.rails_ahead_of_bar and observation.bar>=0.45:
                    self.set_state('done','Task 1 complete: stopped above the end marker',now);return Command()
            quality=1-abs(observation.offset)/0.5-abs(observation.angle)/0.4
            # No forward movement while red is in view: descend and centre first.
            command.x=0 if red else FORWARD_COMMAND*max(0.2,min(1.0,quality))
        self.command=command
        return command
