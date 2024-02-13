# AnimationMixer

The AnimationMixer is a player for animations on a particular object in the
scene. When multiple objects in the scene are animated independently, one
AnimationMixer may be used for each object.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Constructor

###  function AnimationMixer( rootObject: Object3D ): void;

[page:Object3D rootObject] - the object whose animations shall be played by
this mixer.  

## Properties

###  Number time;

The global mixer time (in seconds; starting with `0` on the mixer's creation).

###  Number timeScale;

A scaling factor for the global [page:.time mixer time].  
  
Note: Setting the mixer's timeScale to `0` and later back to `1` is a
possibility to pause/unpause all actions that are controlled by this mixer.

## Methods

###  function clipAction( clip: AnimationClip, optionalRoot: Object3D ):
AnimationAction;

Returns an [page:AnimationAction] for the passed clip, optionally using a root
object different from the mixer's default root. The first parameter can be
either an [page:AnimationClip] object or the name of an AnimationClip.  
  
If an action fitting the clip and root parameters doesn't yet exist, it will
be created by this method. Calling this method several times with the same
clip and root parameters always returns the same clip instance.

###  function existingAction( clip: AnimationClip, optionalRoot: Object3D ):
AnimationAction;

Returns an existing [page:AnimationAction] for the passed clip, optionally
using a root object different from the mixer's default root.  
  
The first parameter can be either an [page:AnimationClip] object or the name
of an AnimationClip.

###  function getRoot( ): Object3D;

Returns this mixer's root object.

###  function stopAllAction( ): this;

Deactivates all previously scheduled actions on this mixer.

###  function update( deltaTimeInSeconds: Number ): this;

Advances the global mixer time and updates the animation.  
  
This is usually done in the render loop, passing [page:Clock.getDelta
clock.getDelta] scaled by the mixer's [page:.timeScale timeScale].

###  function setTime( timeInSeconds: Number ): this;

Sets the global mixer to a specific time and updates the animation
accordingly.  
  
This is useful when you need to jump to an exact time in an animation. The
input parameter will be scaled by the mixer's [page:.timeScale timeScale].

###  function uncacheClip( clip: AnimationClip ): undefined;

Deallocates all memory resources for a clip. Before using this method make
sure to call [page:AnimationAction.stop]() for all related actions.

###  function uncacheRoot( root: Object3D ): undefined;

Deallocates all memory resources for a root object. Before using this method
make sure to call [page:AnimationAction.stop]() for all related actions.

###  function uncacheAction( clip: AnimationClip, optionalRoot: Object3D ):
undefined;

Deallocates all memory resources for an action. Before using this method make
sure to call [page:AnimationAction.stop]() to deactivate the action.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

