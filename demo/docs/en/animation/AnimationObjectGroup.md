# AnimationObjectGroup

A group of objects that receives a shared animation state.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Usage:

Add objects you would otherwise pass as 'root' to the constructor or the
[clipAction](#) method of [AnimationMixer](en\animation\AnimationMixer.html)
and instead pass this object as 'root'.  
  
Note that objects of this class appear as one object to the mixer, so cache
control of the individual objects must be done on the group.

## Limitations

The animated properties must be compatible among all objects in the group.  
  
A single property can either be controlled through a target group or directly,
but not both.

## Constructor

### AnimationObjectGroup

  
  
```ts  
function AnimationObjectGroup( obj1: Object, obj2: Object, obj3: Object ):
void;  
```  

[obj](#) - an arbitrary number of meshes that share the same animation state.

## Properties

### isAnimationObjectGroup

  
  
```ts  
isAnimationObjectGroup: Boolean;  
```  

Read-only flag to check if a given object is of type AnimationObjectGroup.

### stats

  
  
```ts  
stats: Object;  
```  

An object that contains some informations of this `AnimationObjectGroup`
(total number, number in use, number of bindings per object)

### uuid

  
  
```ts  
uuid: String;  
```  

The <a
href="http://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a> of
this `AnimationObjectGroup`. It gets automatically assigned and shouldn't be
edited.

## Methods

### add

  
  
```ts  
function add( obj1: Object, obj2: Object, obj3: Object ): undefined;  
```  

Adds an arbitrary number of objects to this `AnimationObjectGroup`.

### remove

  
  
```ts  
function remove( obj1: Object, obj2: Object, obj3: Object ): undefined;  
```  

Removes an arbitrary number of objects from this `AnimationObjectGroup`.

### uncache

  
  
```ts  
function uncache( obj1: Object, obj2: Object, obj3: Object ): undefined;  
```  

Deallocates all memory resources for the passed objects of this
`AnimationObjectGroup`.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/AnimationObjectGroup.js">src/animation/AnimationObjectGroup.js</a>

