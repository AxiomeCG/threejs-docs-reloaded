# AnimationMixer

The AnimationMixer is a player for animations on a particular object in the
scene. When multiple objects in the scene are animated independently, one
AnimationMixer may be used for each object.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Constructor

### AnimationMixer

  
  
```ts  
function AnimationMixer( rootObject: Object3D ): void;  
```  

[rootObject](en\core\Object3D.html) - the object whose animations shall be
played by this mixer.  

## Properties

### time

  
  
```ts  
time: Number;  
```  

The global mixer time (in seconds; starting with `0` on the mixer's creation).

### timeScale

  
  
```ts  
timeScale: Number;  
```  

A scaling factor for the global [.time](#time).  
  
Note: Setting the mixer's timeScale to `0` and later back to `1` is a
possibility to pause/unpause all actions that are controlled by this mixer.

## Methods

### clipAction

  
  
```ts  
function clipAction( clip: AnimationClip, optionalRoot: Object3D ):
AnimationAction;  
```  

Returns an [AnimationAction](en\animation\AnimationAction.html) for the passed
clip, optionally using a root object different from the mixer's default root.
The first parameter can be either an
[AnimationClip](en\animation\AnimationClip.html) object or the name of an
AnimationClip.  
  
If an action fitting the clip and root parameters doesn't yet exist, it will
be created by this method. Calling this method several times with the same
clip and root parameters always returns the same clip instance.

### existingAction

  
  
```ts  
function existingAction( clip: AnimationClip, optionalRoot: Object3D ):
AnimationAction;  
```  

Returns an existing [AnimationAction](en\animation\AnimationAction.html) for
the passed clip, optionally using a root object different from the mixer's
default root.  
  
The first parameter can be either an
[AnimationClip](en\animation\AnimationClip.html) object or the name of an
AnimationClip.

### getRoot

  
  
```ts  
function getRoot( ): Object3D;  
```  

Returns this mixer's root object.

### stopAllAction

  
  
```ts  
function stopAllAction( ): this;  
```  

Deactivates all previously scheduled actions on this mixer.

### update

  
  
```ts  
function update( deltaTimeInSeconds: Number ): this;  
```  

Advances the global mixer time and updates the animation.  
  
This is usually done in the render loop, passing [clock.getDelta](#) scaled by
the mixer's [.timeScale](#timeScale).

### setTime

  
  
```ts  
function setTime( timeInSeconds: Number ): this;  
```  

Sets the global mixer to a specific time and updates the animation
accordingly.  
  
This is useful when you need to jump to an exact time in an animation. The
input parameter will be scaled by the mixer's [.timeScale](#timeScale).

### uncacheClip

  
  
```ts  
function uncacheClip( clip: AnimationClip ): undefined;  
```  

Deallocates all memory resources for a clip. Before using this method make
sure to call [AnimationAction.stop](#)() for all related actions.

### uncacheRoot

  
  
```ts  
function uncacheRoot( root: Object3D ): undefined;  
```  

Deallocates all memory resources for a root object. Before using this method
make sure to call [AnimationAction.stop](#)() for all related actions.

### uncacheAction

  
  
```ts  
function uncacheAction( clip: AnimationClip, optionalRoot: Object3D ):
undefined;  
```  

Deallocates all memory resources for an action. Before using this method make
sure to call [AnimationAction.stop](#)() to deactivate the action.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/AnimationMixer.js">src/animation/AnimationMixer.js</a>

