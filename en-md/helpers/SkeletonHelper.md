[page:Object3D] → [page:Line] → [page:LineSegments] →

# [name]

A helper object to assist with visualizing a [page:Skeleton Skeleton]. The
helper is rendered using a [page:LineBasicMaterial LineBasicMaterial].

## Code Example

  
```ts  
const helper = new THREE.SkeletonHelper( skinnedMesh );  
scene.add( helper );  
```  

## Examples

[example:webgl_animation_skinning_blending WebGL / animation / skinning /
blending]  
[example:webgl_animation_skinning_morph WebGL / animation / skinning / morph]  
[example:webgl_loader_bvh WebGL / loader / bvh ]

## Constructor

### [name]( [param:Object3D object] )

object -- Usually an instance of [page:SkinnedMesh]. However, any instance of
[page:Object3D] can be used if it represents a hierarchy of [page:Bone Bone]s
(via [page:Object3D.children]).

## Properties

### <br/> Array bones; <br/>

The list of bones that the helper renders as [page:Line Lines].

### <br/> Boolean isSkeletonHelper; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Object3D root; <br/>

The object passed in the constructor.

## Methods

See the base [page:LineSegments] class for common methods.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

