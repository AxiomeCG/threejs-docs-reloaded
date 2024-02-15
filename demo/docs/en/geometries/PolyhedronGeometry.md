[BufferGeometry](en\core\BufferGeometry.html) →

# PolyhedronGeometry

A polyhedron is a solid in three dimensions with flat faces. This class will
take an array of vertices, project them onto a sphere, and then divide them up
to the desired level of detail. This class is used by
[DodecahedronGeometry](en\geometries\DodecahedronGeometry.html),
[IcosahedronGeometry](en\geometries\IcosahedronGeometry.html),
[OctahedronGeometry](en\geometries\OctahedronGeometry.html), and
[TetrahedronGeometry](en\geometries\TetrahedronGeometry.html) to generate
their respective geometries.

## Code Example

  
```ts  
const verticesOfCube = [ -1,-1,-1, 1,-1,-1, 1, 1,-1, -1, 1,-1, -1,-1, 1, 1,-1,
1, 1, 1, 1, -1, 1, 1,];const indicesOfFaces = [ 2,1,0, 0,3,2, 0,4,7, 7,3,0,
0,1,5, 5,4,0, 1,2,6, 6,5,1, 2,3,7, 7,6,2, 4,5,6, 6,7,4];const geometry = new
THREE.PolyhedronGeometry( verticesOfCube, indicesOfFaces, 6, 2 );  
```  

## Constructor

### PolyhedronGeometry

  
  
```ts  
function PolyhedronGeometry( vertices: Array, indices: Array, radius: Float,
detail: Integer ): void;  
```  

vertices — [Array](#) of points of the form [1,1,1, -1,-1,-1, ... ]  
indices — [Array](#) of indices that make up the faces of the form [0,1,2,
2,3,0, ... ]  
radius — [Float](#) - The radius of the final shape  
detail — [Integer](#) - How many levels to subdivide the geometry. The more
detail, the smoother the shape.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/PolyhedronGeometry.js">src/geometries/PolyhedronGeometry.js</a>

