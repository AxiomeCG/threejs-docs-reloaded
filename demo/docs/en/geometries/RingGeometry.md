[BufferGeometry](en\core\BufferGeometry.html) →

# RingGeometry

A class for generating a two-dimensional ring geometry.

## Code Example

  
```ts  
const geometry = new THREE.RingGeometry( 1, 5, 32 ); const material = new
THREE.MeshBasicMaterial( { color: 0xffff00, side: THREE.DoubleSide } );const
mesh = new THREE.Mesh( geometry, material ); scene.add( mesh );  
```  

## Constructor

### RingGeometry

  
  
```ts  
function RingGeometry( innerRadius: Float, outerRadius: Float, thetaSegments:
Integer, phiSegments: Integer, thetaStart: Float, thetaLength: Float ): void;  
```  

innerRadius — Default is `0.5`.  
outerRadius — Default is `1`.  
thetaSegments — Number of segments. A higher number means the ring will be
more round. Minimum is `3`. Default is `32`.  
phiSegments — Minimum is `1`. Default is `1`.  
thetaStart — Starting angle. Default is `0`.  
thetaLength — Central angle. Default is Math.PI * 2.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/RingGeometry.js">src/geometries/RingGeometry.js</a>

