[BufferGeometry](en\core\BufferGeometry.html) →

# LatheGeometry

Creates meshes with axial symmetry like vases. The lathe rotates around the Y
axis.

## Code Example

  
```ts  
const points = []; for ( let i = 0; i < 10; i ++ ) { points.push( new
THREE.Vector2( Math.sin( i * 0.2 ) * 10 + 5, ( i - 5 ) * 2 ) ); } const
geometry = new THREE.LatheGeometry( points ); const material = new
THREE.MeshBasicMaterial( { color: 0xffff00 } ); const lathe = new THREE.Mesh(
geometry, material ); scene.add( lathe );  
```  

## Constructor

### LatheGeometry

  
  
```ts  
function LatheGeometry( points: Array, segments: Integer, phiLength: Float ):
void;  
```  

points — Array of Vector2s. The x-coordinate of each point must be greater
than zero. Default is an array with (0,-0.5), (0.5,0) and (0,0.5) which
creates a simple diamond shape.  
segments — the number of circumference segments to generate. Default is 12.  
phiStart — the starting angle in radians. Default is `0`.  
phiLength — the radian (0 to 2PI) range of the lathed section 2PI is a closed
lathe, less than 2PI is a portion. Default is 2PI.

This creates a LatheGeometry based on the parameters.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/LatheGeometry.js">src/geometries/LatheGeometry.js</a>

