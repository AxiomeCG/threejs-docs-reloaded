[BufferGeometry](en\core\BufferGeometry.html) →

# EdgesGeometry

This can be used as a helper object to view the edges of a
[geometry](en\core\BufferGeometry.html).

## Code Example

  
```ts  
const geometry = new THREE.BoxGeometry( 100, 100, 100 ); const edges = new
THREE.EdgesGeometry( geometry ); const line = new THREE.LineSegments(edges,
new THREE.LineBasicMaterial( { color: 0xffffff } ) ); scene.add( line );  
```  

## Examples

[example:webgl_helpers helpers]

## Constructor

### EdgesGeometry

  
  
```ts  
function EdgesGeometry( geometry: BufferGeometry, thresholdAngle: Integer ):
void;  
```  

geometry — Any geometry object.  
thresholdAngle — An edge is only rendered if the angle (in degrees) between
the face normals of the adjoining faces exceeds this value. default = 1
degree.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/EdgesGeometry.js">src/geometries/EdgesGeometry.js</a>

