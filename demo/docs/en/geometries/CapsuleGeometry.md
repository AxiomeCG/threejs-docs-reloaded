[BufferGeometry](en\core\BufferGeometry.html) →
[LatheGeometry](en\geometries\LatheGeometry.html) →

# CapsuleGeometry

CapsuleGeometry is a geometry class for a capsule with given radii and height.
It is constructed using a lathe.

## Code Example

  
```ts  
const geometry = new THREE.CapsuleGeometry( 1, 1, 4, 8 ); const material = new
THREE.MeshBasicMaterial( {color: 0x00ff00} ); const capsule = new THREE.Mesh(
geometry, material ); scene.add( capsule );  
```  

## Constructor

### CapsuleGeometry

  
  
```ts  
function CapsuleGeometry( radius: Float, length: Float, capSubdivisions:
Integer, radialSegments: Integer ): void;  
```  

radius — Radius of the capsule. Optional; defaults to `1`.  
length — Length of the middle section. Optional; defaults to `1`.  
capSegments — Number of curve segments used to build the caps. Optional;
defaults to `4`.  
radialSegments — Number of segmented faces around the circumference of the
capsule. Optional; defaults to `8`.  

## Properties

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
properties.

### parameters

  
  
```ts  
parameters: Object;  
```  

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/CapsuleGeometry.js">src/geometries/CapsuleGeometry.js</a>

