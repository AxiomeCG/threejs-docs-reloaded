[Object3D](en\core\Object3D.html) →

# Line

A continuous line.  
  
This is nearly the same as [LineSegments](en\objects\LineSegments.html); the
only difference is that it is rendered using <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements">gl.LINE_STRIP</a> instead
of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements">gl.LINES</a>

## Code Example

  
```ts  
const material = new THREE.LineBasicMaterial({ color: 0x0000ff }); const
points = []; points.push( new THREE.Vector3( - 10, 0, 0 ) ); points.push( new
THREE.Vector3( 0, 10, 0 ) ); points.push( new THREE.Vector3( 10, 0, 0 ) );
const geometry = new THREE.BufferGeometry().setFromPoints( points ); const
line = new THREE.Line( geometry, material ); scene.add( line );  
```  

## Constructor

### Line

  
  
```ts  
function Line( geometry: BufferGeometry, material: Material ): void;  
```  

[geometry](en\core\BufferGeometry.html) — vertices representing the line
segment(s). Default is a new [BufferGeometry](en\core\BufferGeometry.html).  
[material](en\materials\Material.html) — material for the line. Default is a
new [LineBasicMaterial](en\materials\LineBasicMaterial.html).  

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### geometry

  
  
```ts  
geometry: BufferGeometry;  
```  

Vertices representing the line segment(s).

### isLine

  
  
```ts  
isLine: Boolean;  
```  

Read-only flag to check if a given object is of type Line.

### material

  
  
```ts  
material: Material;  
```  

Material for the line.

### morphTargetInfluences

  
  
```ts  
morphTargetInfluences: Array;  
```  

An array of weights typically from 0-1 that specify how much of the morph is
applied. Undefined by default, but reset to a blank array by
[.updateMorphTargets](#)().

### morphTargetDictionary

  
  
```ts  
morphTargetDictionary: Object;  
```  

A dictionary of morphTargets based on the morphTarget.name property. Undefined
by default, but rebuilt [.updateMorphTargets](#)().

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### computeLineDistances

  
  
```ts  
function computeLineDistances( ): this;  
```  

Computes an array of distance values which are necessary for
[LineDashedMaterial](en\materials\LineDashedMaterial.html). For each vertex in
the geometry, the method calculates the cumulative length from the current
point to the very beginning of the line.

### raycast

  
  
```ts  
function raycast( raycaster: Raycaster, intersects: Array ): undefined;  
```  

Get intersections between a casted [Ray](en\math\Ray.html) and this Line.
[Raycaster.intersectObject](#) will call this method.

### clone

  
  
```ts  
function clone( ): Line;  
```  

Returns a clone of this Line object and its descendants.

### updateMorphTargets

  
  
```ts  
function updateMorphTargets( ): undefined;  
```  

Updates the morphTargets to have no influence on the object. Resets the
[.morphTargetInfluences](#) and [.morphTargetDictionary](#) properties.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/Line.js">src/objects/Line.js</a>

