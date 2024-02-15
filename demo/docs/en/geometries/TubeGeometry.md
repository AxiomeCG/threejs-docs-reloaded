[BufferGeometry](en\core\BufferGeometry.html) →

# TubeGeometry

Creates a tube that extrudes along a 3d curve.

## Code Example

  
```ts  
class CustomSinCurve extends THREE.Curve { constructor( scale = 1 ) { super();
this.scale = scale; } getPoint( t, optionalTarget = new THREE.Vector3() ) {
const tx = t * 3 - 1.5; const ty = Math.sin( 2 * Math.PI * t ); const tz = 0;
return optionalTarget.set( tx, ty, tz ).multiplyScalar( this.scale ); } }
const path = new CustomSinCurve( 10 ); const geometry = new
THREE.TubeGeometry( path, 20, 2, 8, false ); const material = new
THREE.MeshBasicMaterial( { color: 0x00ff00 } ); const mesh = new THREE.Mesh(
geometry, material ); scene.add( mesh );  
```  

## Constructor

### TubeGeometry

  
  
```ts  
function TubeGeometry( path: Curve, tubularSegments: Integer, radius: Float,
radialSegments: Integer, closed: Boolean ): void;  
```  

path — [Curve](en\extras\core\Curve.html) - A 3D path that inherits from the
[Curve](en\extras\core\Curve.html) base class. Default is a quadratic bezier
curve.  
tubularSegments — [Integer](#) - The number of segments that make up the tube.
Default is `64`.  
radius — [Float](#) - The radius of the tube. Default is `1`.  
radialSegments — [Integer](#) - The number of segments that make up the cross-
section. Default is `8`.  
closed — [Boolean](#) Is the tube open or closed. Default is `false`.  

## Properties

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
properties.

### parameters

  
  
```ts  
parameters: Object;  
```  

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

### tangents

  
  
```ts  
tangents: Array;  
```  

An array of [Vector3](en\math\Vector3.html) tangents

### normals

  
  
```ts  
normals: Array;  
```  

An array of [Vector3](en\math\Vector3.html) normals

### binormals

  
  
```ts  
binormals: Array;  
```  

An array of [Vector3](en\math\Vector3.html) binormals

## Methods

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/TubeGeometry.js">src/geometries/TubeGeometry.js</a>

