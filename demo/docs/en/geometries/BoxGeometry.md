[BufferGeometry](en\core\BufferGeometry.html) →

# BoxGeometry

BoxGeometry is a geometry class for a rectangular cuboid with a given 'width',
'height', and 'depth'. On creation, the cuboid is centred on the origin, with
each edge parallel to one of the axes.

## Code Example

  
```ts  
const geometry = new THREE.BoxGeometry( 1, 1, 1 ); const material = new
THREE.MeshBasicMaterial( {color: 0x00ff00} ); const cube = new THREE.Mesh(
geometry, material ); scene.add( cube );  
```  

## Constructor

### BoxGeometry

  
  
```ts  
function BoxGeometry( width: Float, height: Float, depth: Float,
widthSegments: Integer, heightSegments: Integer, depthSegments: Integer ):
void;  
```  

width — Width; that is, the length of the edges parallel to the X axis.
Optional; defaults to `1`.  
height — Height; that is, the length of the edges parallel to the Y axis.
Optional; defaults to `1`.  
depth — Depth; that is, the length of the edges parallel to the Z axis.
Optional; defaults to `1`.  
widthSegments — Number of segmented rectangular faces along the width of the
sides. Optional; defaults to `1`.  
heightSegments — Number of segmented rectangular faces along the height of the
sides. Optional; defaults to `1`.  
depthSegments — Number of segmented rectangular faces along the depth of the
sides. Optional; defaults to `1`.  

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/BoxGeometry.js">src/geometries/BoxGeometry.js</a>

