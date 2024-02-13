[page:Object3D] → [page:Line] → [page:LineSegments] →

# SkeletonHelper

A helper object to assist with visualizing a [page:Skeleton Skeleton]. The
helper is rendered using a [page:LineBasicMaterial LineBasicMaterial].

## Code Example

  
```ts  
const helper = new THREE.SkeletonHelper( skinnedMesh ); scene.add( helper );  
```  

## Examples

[example:webgl_animation_skinning_blending WebGL / animation / skinning /
blending]  
[example:webgl_animation_skinning_morph WebGL / animation / skinning / morph]  
[example:webgl_loader_bvh WebGL / loader / bvh ]

## Constructor

###  function SkeletonHelper( object: Object3D ): void;

object -- Usually an instance of [page:SkinnedMesh]. However, any instance of
[page:Object3D] can be used if it represents a hierarchy of [page:Bone Bone]s
(via [page:Object3D.children]).

## Properties

###  Array bones;

The list of bones that the helper renders as [page:Line Lines].

###  Boolean isSkeletonHelper;

Read-only flag to check if a given object is of type SkeletonHelper.

###  Object3D root;

The object passed in the constructor.

## Methods

See the base [page:LineSegments] class for common methods.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

