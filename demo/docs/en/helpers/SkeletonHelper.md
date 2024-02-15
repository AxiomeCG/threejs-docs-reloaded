[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →
[LineSegments](en\objects\LineSegments.html) →

# SkeletonHelper

A helper object to assist with visualizing a
[Skeleton](en\objects\Skeleton.html). The helper is rendered using a
[LineBasicMaterial](en\materials\LineBasicMaterial.html).

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

### SkeletonHelper

  
  
```ts  
function SkeletonHelper( object: Object3D ): void;  
```  

object -- Usually an instance of [SkinnedMesh](en\objects\SkinnedMesh.html).
However, any instance of [Object3D](en\core\Object3D.html) can be used if it
represents a hierarchy of [Bone](en\objects\Bone.html)s (via
[Object3D.children](#)).

## Properties

### bones

  
  
```ts  
bones: Array;  
```  

The list of bones that the helper renders as [Lines](en\objects\Line.html).

### isSkeletonHelper

  
  
```ts  
isSkeletonHelper: Boolean;  
```  

Read-only flag to check if a given object is of type SkeletonHelper.

### root

  
  
```ts  
root: Object3D;  
```  

The object passed in the constructor.

## Methods

See the base [LineSegments](en\objects\LineSegments.html) class for common
methods.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/SkeletonHelper.js">src/helpers/SkeletonHelper.js</a>

