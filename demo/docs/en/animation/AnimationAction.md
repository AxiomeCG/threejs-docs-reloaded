# AnimationAction

AnimationActions schedule the performance of the animations which are stored
in [AnimationClips](en\animation\AnimationClip.html).  
  
Note: Most of AnimationAction's methods can be chained.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Constructor

### AnimationAction

  
  
```ts  
function AnimationAction( mixer: AnimationMixer, clip: AnimationClip,
localRoot: Object3D ): void;  
```  

[mixer](en\animation\AnimationMixer.html) - the `AnimationMixer` that is
controlled by this action.  
[clip](en\animation\AnimationClip.html) - the `AnimationClip` that holds the
animation data for this action.  
[localRoot](en\core\Object3D.html) - the root object on which this action is
performed.  
[blendMode](#) - defines how the animation is blended/combined when two or
more animations are simultaneously played.  
  
Note: Instead of calling this constructor directly you should instantiate an
AnimationAction with [AnimationMixer.clipAction](#) since this method provides
caching for better performance.

## Properties

### blendMode

  
  
```ts  
blendMode: Number;  
```  

Defines how the animation is blended/combined when two or more animations are
simultaneously played. Valid values are *NormalAnimationBlendMode* (default)
and *AdditiveAnimationBlendMode*.

### clampWhenFinished

  
  
```ts  
clampWhenFinished: Boolean;  
```  

If `clampWhenFinished` is set to true the animation will automatically be
[.paused](#paused) on its last frame.  
  
If `clampWhenFinished` is set to false, [.enabled](#enabled) will
automatically be switched to false when the last loop of the action has
finished, so that this action has no further impact.  
  
Default is `false`.  
  
Note: `clampWhenFinished` has no impact if the action is interrupted (it has
only an effect if its last loop has really finished).

### enabled

  
  
```ts  
enabled: Boolean;  
```  

Setting `enabled` to `false` disables this action, so that it has no impact.
Default is `true`.  
  
When the action is re-enabled, the animation continues from its current
[.time](#time) (setting `enabled` to `false` doesn't reset the action).  
  
Note: Setting `enabled` to `true` doesn’t automatically restart the animation.
Setting `enabled` to `true` will only restart the animation immediately if the
following condition is fulfilled: [.paused](#paused) is `false`, this action
has not been deactivated in the meantime (by executing a [.stop](#stop) or
[.reset](#reset) command), and neither [.weight](#weight) nor
[.timeScale](#timeScale) is `0`.

### loop

  
  
```ts  
loop: Number;  
```  

The looping mode (can be changed with [.setLoop](#setLoop)). Default is
[.nimation](#nimation) (with an infinite number of
[.repetitions](#repetitions))  
  
Must be one of these constants:  
  
[THREE.LoopOnce](en\constants\Animation.html) - playing the clip once,  
[THREE.LoopRepeat](en\constants\Animation.html) - playing the clip with the
chosen number of `repetitions`, each time jumping from the end of the clip
directly to its beginning,  
[THREE.LoopPingPong](en\constants\Animation.html) - playing the clip with the
chosen number of `repetitions`, alternately playing forward and backward.

### paused

  
  
```ts  
paused: Boolean;  
```  

Setting `paused` to `true` pauses the execution of the action by setting the
effective time scale to `0`. Default is `false`.  
  

### repetitions

  
  
```ts  
repetitions: Number;  
```  

The number of repetitions of the performed
[AnimationClip](en\animation\AnimationClip.html) over the course of this
action. Can be set via [.setLoop](#setLoop). Default is `Infinity`.  
  
Setting this number has no effect, if the [.loop](#loop) is set to
[.nimation](#nimation).

### time

  
  
```ts  
time: Number;  
```  

The local time of this action (in seconds, starting with `0`).  
  
The value gets clamped or wrapped to `0...clip.duration` (according to the
loop state). It can be scaled relatively to the global mixer time by changing
[.timeScale](#timeScale) (using
[.setEffectiveTimeScale](#setEffectiveTimeScale) or
[.setDuration](#setDuration)).  

### timeScale

  
  
```ts  
timeScale: Number;  
```  

Scaling factor for the [.time](#time). A value of `0` causes the animation to
pause. Negative values cause the animation to play backwards. Default is `1`.  
  
Properties/methods concerning `timeScale` (respectively `time`) are:
[.getEffectiveTimeScale](#getEffectiveTimeScale), [.halt](#halt),
[.paused](#paused), [.setDuration](#setDuration),
[.setEffectiveTimeScale](#setEffectiveTimeScale),
[.stopWarping](#stopWarping), [.syncWith](#syncWith), [.warp](#warp).

### weight

  
  
```ts  
weight: Number;  
```  

The degree of influence of this action (in the interval `[0, 1]`). Values
between `0` (no impact) and `1` (full impact) can be used to blend between
several actions. Default is `1`.  
  
Properties/methods concerning `weight` are: [.crossFadeFrom](#crossFadeFrom),
[.crossFadeTo](#crossFadeTo), [.enabled](#enabled), [.fadeIn](#fadeIn),
[.fadeOut](#fadeOut), [.getEffectiveWeight](#getEffectiveWeight),
[.setEffectiveWeight](#setEffectiveWeight), [.stopFading](#stopFading).

### zeroSlopeAtEnd

  
  
```ts  
zeroSlopeAtEnd: Boolean;  
```  

Enables smooth interpolation without separate clips for start, loop and end.
Default is `true`.

### zeroSlopeAtStart

  
  
```ts  
zeroSlopeAtStart: Boolean;  
```  

Enables smooth interpolation without separate clips for start, loop and end.
Default is `true`.

## Methods

### crossFadeFrom

  
  
```ts  
function crossFadeFrom( fadeOutAction: AnimationAction, durationInSeconds:
Number, warpBoolean: Boolean ): this;  
```  

Causes this action to [.fadeIn](#fadeIn), fading out another action
simultaneously, within the passed time interval. This method can be chained.  
  
If warpBoolean is true, additional [.warp](#warp) (gradually changes of the
time scales) will be applied.  
  
Note: Like with `fadeIn`/`fadeOut`, the fading starts/ends with a weight of
`1`.

### crossFadeTo

  
  
```ts  
function crossFadeTo( fadeInAction: AnimationAction, durationInSeconds:
Number, warpBoolean: Boolean ): this;  
```  

Causes this action to [.fadeOut](#fadeOut), fading in another action
simultaneously, within the passed time interval. This method can be chained.  
  
If warpBoolean is true, additional [.warp](#warp) (gradually changes of the
time scales) will be applied.  
  
Note: Like with `fadeIn`/`fadeOut`, the fading starts/ends with a weight of
`1`.

### fadeIn

  
  
```ts  
function fadeIn( durationInSeconds: Number ): this;  
```  

Increases the [.weight](#weight) of this action gradually from `0` to `1`,
within the passed time interval. This method can be chained.

### fadeOut

  
  
```ts  
function fadeOut( durationInSeconds: Number ): this;  
```  

Decreases the [.weight](#weight) of this action gradually from `1` to `0`,
within the passed time interval. This method can be chained.

### getEffectiveTimeScale

  
  
```ts  
function getEffectiveTimeScale( ): Number;  
```  

Returns the effective time scale (considering the current states of warping
and [.paused](#paused)).

### getEffectiveWeight

  
  
```ts  
function getEffectiveWeight( ): Number;  
```  

Returns the effective weight (considering the current states of fading and
[.enabled](#enabled)).

### getClip

  
  
```ts  
function getClip( ): AnimationClip;  
```  

Returns the clip which holds the animation data for this action.

### getMixer

  
  
```ts  
function getMixer( ): AnimationMixer;  
```  

Returns the mixer which is responsible for playing this action.

### getRoot

  
  
```ts  
function getRoot( ): Object3D;  
```  

Returns the root object on which this action is performed.

### halt

  
  
```ts  
function halt( durationInSeconds: Number ): this;  
```  

Decelerates this animation's speed to `0` by decreasing
[.timeScale](#timeScale) gradually (starting from its current value), within
the passed time interval. This method can be chained.

### isRunning

  
  
```ts  
function isRunning( ): Boolean;  
```  

Returns true if the action’s [.time](#time) is currently running.  
  
In addition to being activated in the mixer (see [.isScheduled](#isScheduled))
the following conditions must be fulfilled: [.paused](#paused) is equal to
false, [.enabled](#enabled) is equal to true, [.timeScale](#timeScale) is
different from `0`, and there is no scheduling for a delayed start
([.startAt](#startAt)).  
  
Note: `isRunning` being true doesn’t necessarily mean that the animation can
actually be seen. This is only the case, if [.weight](#weight) is additionally
set to a non-zero value.

### isScheduled

  
  
```ts  
function isScheduled( ): Boolean;  
```  

Returns true, if this action is activated in the mixer.  
  
Note: This doesn’t necessarily mean that the animation is actually running
(compare the additional conditions for [.isRunning](#isRunning)).

### play

  
  
```ts  
function play( ): this;  
```  

Tells the mixer to activate the action. This method can be chained.  
  
Note: Activating this action doesn’t necessarily mean that the animation
starts immediately: If the action had already finished before (by reaching the
end of its last loop), or if a time for a delayed start has been set (via
[.startAt](#startAt)), a [.reset](#reset) must be executed first. Some other
settings ([.paused](#paused)=true, [.enabled](#enabled)=false,
[.weight](#weight)=0, [.timeScale](#timeScale)=0) can prevent the animation
from playing, too.

### reset

  
  
```ts  
function reset( ): this;  
```  

Resets the action. This method can be chained.  
  
This method sets [.paused](#paused) to false, [.enabled](#enabled) to true,
[.time](#time) to `0`, interrupts any scheduled fading and warping, and
removes the internal loop count and scheduling for delayed starting.  
  
Note: .`reset` is always called by [.stop](#stop), but .`reset` doesn’t call
.`stop` itself. This means: If you want both, resetting and stopping, don’t
call .`reset`; call .`stop` instead.

### setDuration

  
  
```ts  
function setDuration( durationInSeconds: Number ): this;  
```  

Sets the duration for a single loop of this action (by adjusting
[.timeScale](#timeScale) and stopping any scheduled warping). This method can
be chained.

### setEffectiveTimeScale

  
  
```ts  
function setEffectiveTimeScale( timeScale: Number ): this;  
```  

Sets the [.timeScale](#timeScale) and stops any scheduled warping. This method
can be chained.  
  
If [.paused](#paused) is false, the effective time scale (an internal
property) will also be set to this value; otherwise the effective time scale
(directly affecting the animation at this moment) will be set to `0`.  
  
Note: .`paused` will not be switched to `true` automatically, if .`timeScale`
is set to `0` by this method.

### setEffectiveWeight

  
  
```ts  
function setEffectiveWeight( weight: Number ): this;  
```  

Sets the [.weight](#weight) and stops any scheduled fading. This method can be
chained.  
  
If [.enabled](#enabled) is true, the effective weight (an internal property)
will also be set to this value; otherwise the effective weight (directly
affecting the animation at this moment) will be set to `0`.  
  
Note: .`enabled` will not be switched to `false` automatically, if .`weight`
is set to `0` by this method.

### setLoop

  
  
```ts  
function setLoop( loopMode: Number, repetitions: Number ): this;  
```  

Sets the [.loop](#loop) and the number of [.repetitions](#repetitions). This
method can be chained.

### startAt

  
  
```ts  
function startAt( startTimeInSeconds: Number ): this;  
```  

Defines the time for a delayed start (usually passed as
[AnimationMixer.time](#) + deltaTimeInSeconds). This method can be chained.  
  
Note: The animation will only start at the given time, if .`startAt` is
chained with [.play](#play), or if the action has already been activated in
the mixer (by a previous call of .`play`, without stopping or resetting it in
the meantime).

### stop

  
  
```ts  
function stop( ): this;  
```  

Tells the mixer to deactivate this action. This method can be chained.  
  
The action will be immediately stopped and completely [.reset](#reset).  
  
Note: You can stop all active actions on the same mixer in one go via
[mixer.stopAllAction](#).

### stopFading

  
  
```ts  
function stopFading( ): this;  
```  

Stops any scheduled [.fadeIn](#fadeIn) which is applied to this action. This
method can be chained.

### stopWarping

  
  
```ts  
function stopWarping( ): this;  
```  

Stops any scheduled [.warp](#warp) which is applied to this action. This
method can be chained.

### syncWith

  
  
```ts  
function syncWith( otherAction: AnimationAction ): this;  
```  

Synchronizes this action with the passed other action. This method can be
chained.  
  
Synchronizing is done by setting this action’s [.time](#time) and
[.timeScale](#timeScale) values to the corresponding values of the other
action (stopping any scheduled warping).  
  
Note: Future changes of the other action's `time` and `timeScale` will not be
detected.

### warp

  
  
```ts  
function warp( startTimeScale: Number, endTimeScale: Number,
durationInSeconds: Number ): this;  
```  

Changes the playback speed, within the passed time interval, by modifying
[.timeScale](#timeScale) gradually from `startTimeScale` to `endTimeScale`.
This method can be chained.

## Events

There are two events indicating when a single loop of the action respectively
the entire action has finished. You can react to them with:

  
```ts  
mixer.addEventListener( 'loop', function( e ) { …} ); // properties of e:
type, action and loopDelta mixer.addEventListener( 'finished', function( e ) {
…} ); // properties of e: type, action and direction  
```  

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/AnimationAction.js">src/animation/AnimationAction.js</a>

