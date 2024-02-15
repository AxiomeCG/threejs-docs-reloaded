[Object3D](en\core\Object3D.html) →

# Bone

A bone which is part of a [Skeleton](en\objects\Skeleton.html). The skeleton
in turn is used by the [SkinnedMesh](en\objects\SkinnedMesh.html). Bones are
almost identical to a blank [Object3D](en\core\Object3D.html).

## Code Example

  
```ts  
const root = new THREE.Bone(); const child = new THREE.Bone(); root.add( child
); child.position.y = 5;  
```  

## Constructor

### Bone

  
  
```ts  
function Bone( ): void;  
```  

Creates a new Bone.

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### isBone

  
  
```ts  
isBone: Boolean;  
```  

Read-only flag to check if a given object is of type Bone.

### type

  
  
```ts  
type: String;  
```  

Set to 'Bone', this can be used to find all Bones in a scene.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/Bone.js">src/objects/Bone.js</a>

