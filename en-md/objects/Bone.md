[page:Object3D] →

# [name]

A bone which is part of a [page:Skeleton]. The skeleton in turn is used by the
[page:SkinnedMesh]. Bones are almost identical to a blank [page:Object3D].

## Code Example

  
```ts  
const root = new THREE.Bone();  
const child = new THREE.Bone();  
  
root.add( child );  
child.position.y = 5;  
```  

## Constructor

### [name]( )

Creates a new [name].

## Properties

See the base [page:Object3D] class for common properties.

### <br/> Boolean isBone; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> String type; <br/>

Set to 'Bone', this can be used to find all Bones in a scene.

## Methods

See the base [page:Object3D] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

