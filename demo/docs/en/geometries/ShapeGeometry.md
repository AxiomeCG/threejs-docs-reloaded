[BufferGeometry](en\core\BufferGeometry.html) →

# ShapeGeometry

Creates an one-sided polygonal geometry from one or more path shapes.

## Code Example

  
```ts  
const x = 0, y = 0; const heartShape = new THREE.Shape(); heartShape.moveTo( x
+ 5, y + 5 ); heartShape.bezierCurveTo( x + 5, y + 5, x + 4, y, x, y );
heartShape.bezierCurveTo( x - 6, y, x - 6, y + 7,x - 6, y + 7 );
heartShape.bezierCurveTo( x - 6, y + 11, x - 3, y + 15.4, x + 5, y + 19 );
heartShape.bezierCurveTo( x + 12, y + 15.4, x + 16, y + 11, x + 16, y + 7 );
heartShape.bezierCurveTo( x + 16, y + 7, x + 16, y, x + 10, y );
heartShape.bezierCurveTo( x + 7, y, x + 5, y + 5, x + 5, y + 5 ); const
geometry = new THREE.ShapeGeometry( heartShape ); const material = new
THREE.MeshBasicMaterial( { color: 0x00ff00 } ); const mesh = new THREE.Mesh(
geometry, material ) ; scene.add( mesh );  
```  

## Constructor

### ShapeGeometry

  
  
```ts  
function ShapeGeometry( shapes: Array, curveSegments: Integer ): void;  
```  

shapes — [Array](#) of shapes or a single [shape](en\extras\core\Shape.html).
Default is a single triangle shape.  
curveSegments - [Integer](#) - Number of segments per shape. Default is 12.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/ShapeGeometry.js">src/geometries/ShapeGeometry.js</a>

