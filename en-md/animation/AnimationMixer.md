# [name]

The AnimationMixer is a player for animations on a particular object in the
scene. When multiple objects in the scene are animated independently, one
AnimationMixer may be used for each object.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Constructor

### [name]( [param:Object3D rootObject] )

[page:Object3D rootObject] - the object whose animations shall be played by
this mixer.  

## Properties

### <br/> Number time; <br/>

The global mixer time (in seconds; starting with `0` on the mixer's creation).

### <br/> Number timeScale; <br/>

A scaling factor for the global [page:.time mixer time].  
  
Note: Setting the mixer's timeScale to `0` and later back to `1` is a
possibility to pause/unpause all actions that are controlled by this mixer.

## Methods

### [method:AnimationAction clipAction]([param:AnimationClip clip],
[param:Object3D optionalRoot])

Returns an [page:AnimationAction] for the passed clip, optionally using a root
object different from the mixer's default root. The first parameter can be
either an [page:AnimationClip] object or the name of an AnimationClip.  
  
If an action fitting the clip and root parameters doesn't yet exist, it will
be created by this method. Calling this method several times with the same
clip and root parameters always returns the same clip instance.

### [method:AnimationAction existingAction]([param:AnimationClip clip],
[param:Object3D optionalRoot])

Returns an existing [page:AnimationAction] for the passed clip, optionally
using a root object different from the mixer's default root.  
  
The first parameter can be either an [page:AnimationClip] object or the name
of an AnimationClip.

### [method:Object3D getRoot]()

Returns this mixer's root object.

### <br/> function stopAllAction( ): stopAllAction; <br/>

Deactivates all previously scheduled actions on this mixer.

### <br/> function update( deltaTimeInSeconds: Number ): update; <br/>

Advances the global mixer time and updates the animation.  
  
This is usually done in the render loop, passing [page:Clock.getDelta
clock.getDelta] scaled by the mixer's [page:.timeScale timeScale].

### <br/> function setTime( timeInSeconds: Number ): setTime; <br/>

Sets the global mixer to a specific time and updates the animation
accordingly.  
  
This is useful when you need to jump to an exact time in an animation. The
input parameter will be scaled by the mixer's [page:.timeScale timeScale].

### [method:undefined uncacheClip]([param:AnimationClip clip])

Deallocates all memory resources for a clip. Before using this method make
sure to call [page:AnimationAction.stop]() for all related actions.

### [method:undefined uncacheRoot]([param:Object3D root])

Deallocates all memory resources for a root object. Before using this method
make sure to call [page:AnimationAction.stop]() for all related actions.

### [method:undefined uncacheAction]([param:AnimationClip clip],
[param:Object3D optionalRoot])

Deallocates all memory resources for an action. Before using this method make
sure to call [page:AnimationAction.stop]() to deactivate the action.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

