[Object3D](en\core\Object3D.html) →

# Points

A class for displaying points. The points are rendered by the
[WebGLRenderer](en\renderers\WebGLRenderer.html) using <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements">gl.POINTS</a>.

## Constructor

### Points

  
  
```ts  
function Points( geometry: BufferGeometry, material: Material ): void;  
```  

[geometry](en\core\BufferGeometry.html) — (optional) an instance of
[BufferGeometry](en\core\BufferGeometry.html). Default is a new
[BufferGeometry](en\core\BufferGeometry.html).  
[material](en\materials\Material.html) — (optional) a
[Material](en\materials\Material.html). Default is a new
[PointsMaterial](en\materials\PointsMaterial.html).

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### geometry

  
  
```ts  
geometry: BufferGeometry;  
```  

An instance of [BufferGeometry](en\core\BufferGeometry.html) (or derived
classes), defining the object's structure.

### isPoints

  
  
```ts  
isPoints: Boolean;  
```  

Read-only flag to check if a given object is of type Points.

### material

  
  
```ts  
material: Material;  
```  

An instance of [Material](en\materials\Material.html), defining the object's
appearance. Default is a [PointsMaterial](en\materials\PointsMaterial.html).

### morphTargetInfluences

  
  
```ts  
morphTargetInfluences: Array;  
```  

An array of weights typically from 0-1 that specify how much of the morph is
applied. Undefined by default, but reset to a blank array by
[updateMorphTargets](#).

### morphTargetDictionary

  
  
```ts  
morphTargetDictionary: Object;  
```  

A dictionary of morphTargets based on the morphTarget.name property. Undefined
by default, but rebuilt [updateMorphTargets](#).

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### raycast

  
  
```ts  
function raycast( raycaster: Raycaster, intersects: Array ): undefined;  
```  

Get intersections between a casted ray and this Points.
[Raycaster.intersectObject](#) will call this method.

### clone

  
  
```ts  
function clone( ): Points;  
```  

Returns a clone of this Points object and its descendants.

### updateMorphTargets

  
  
```ts  
function updateMorphTargets( ): undefined;  
```  

Updates the morphTargets to have no influence on the object. Resets the
[morphTargetInfluences](#) and [morphTargetDictionary](#) properties.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/Points.js">src/objects/Points.js</a>

