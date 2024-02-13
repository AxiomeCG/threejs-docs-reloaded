[page:Object3D] →

# Line

A continuous line.  
  
This is nearly the same as [page:LineSegments]; the only difference is that it
is rendered using [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements gl.LINE_STRIP] instead of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements gl.LINES]

## Code Example

  
```ts  
const material = new THREE.LineBasicMaterial({ color: 0x0000ff }); const
points = []; points.push( new THREE.Vector3( - 10, 0, 0 ) ); points.push( new
THREE.Vector3( 0, 10, 0 ) ); points.push( new THREE.Vector3( 10, 0, 0 ) );
const geometry = new THREE.BufferGeometry().setFromPoints( points ); const
line = new THREE.Line( geometry, material ); scene.add( line );  
```  

## Constructor

###  function Line( geometry: BufferGeometry, material: Material ): void;

[page:BufferGeometry geometry] — vertices representing the line segment(s).
Default is a new [page:BufferGeometry].  
[page:Material material] — material for the line. Default is a new
[page:LineBasicMaterial].  

## Properties

See the base [page:Object3D] class for common properties.

###  BufferGeometry geometry;

Vertices representing the line segment(s).

###  Boolean isLine;

Read-only flag to check if a given object is of type Line.

###  Material material;

Material for the line.

###  Array morphTargetInfluences;

An array of weights typically from 0-1 that specify how much of the morph is
applied. Undefined by default, but reset to a blank array by
[page:.updateMorphTargets]().

###  Object morphTargetDictionary;

A dictionary of morphTargets based on the morphTarget.name property. Undefined
by default, but rebuilt [page:.updateMorphTargets]().

## Methods

See the base [page:Object3D] class for common methods.

###  function computeLineDistances( ): this;

Computes an array of distance values which are necessary for
[page:LineDashedMaterial]. For each vertex in the geometry, the method
calculates the cumulative length from the current point to the very beginning
of the line.

###  function raycast( raycaster: Raycaster, intersects: Array ): undefined;

Get intersections between a casted [page:Ray] and this Line.
[page:Raycaster.intersectObject] will call this method.

###  function clone( ): Line;

Returns a clone of this Line object and its descendants.

###  function updateMorphTargets( ): undefined;

Updates the morphTargets to have no influence on the object. Resets the
[page:.morphTargetInfluences] and [page:.morphTargetDictionary] properties.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

