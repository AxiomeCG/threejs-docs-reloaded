# [name]

A group of objects that receives a shared animation state.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Usage:

Add objects you would otherwise pass as 'root' to the constructor or the
[page:AnimationMixer.clipAction clipAction] method of [page:AnimationMixer
AnimationMixer] and instead pass this object as 'root'.  
  
Note that objects of this class appear as one object to the mixer, so cache
control of the individual objects must be done on the group.

## Limitations

The animated properties must be compatible among all objects in the group.  
  
A single property can either be controlled through a target group or directly,
but not both.

## Constructor

###  [name]( [param:Object obj1], [param:Object obj2], [param:Object obj3],
...)

[page:Object obj] - an arbitrary number of meshes that share the same
animation state.

## Properties

### <br/> Boolean isAnimationObjectGroup; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Object stats; <br/>

An object that contains some informations of this `AnimationObjectGroup`
(total number, number in use, number of bindings per object)

### <br/> String uuid; <br/>

The [link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of
this `AnimationObjectGroup`. It gets automatically assigned and shouldn't be
edited.

## Methods

### [method:undefined add]( [param:Object obj1], [param:Object obj2],
[param:Object obj3], ... )

Adds an arbitrary number of objects to this `AnimationObjectGroup`.

### [method:undefined remove]( [param:Object obj1], [param:Object obj2],
[param:Object obj3], ... )

Removes an arbitrary number of objects from this `AnimationObjectGroup`.

### [method:undefined uncache]( [param:Object obj1], [param:Object obj2],
[param:Object obj3], ... )

Deallocates all memory resources for the passed objects of this
`AnimationObjectGroup`.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

