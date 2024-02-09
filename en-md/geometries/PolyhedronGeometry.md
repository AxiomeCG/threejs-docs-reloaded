[page:BufferGeometry] →

# [name]

A polyhedron is a solid in three dimensions with flat faces. This class will
take an array of vertices, project them onto a sphere, and then divide them up
to the desired level of detail. This class is used by
[page:DodecahedronGeometry], [page:IcosahedronGeometry],
[page:OctahedronGeometry], and [page:TetrahedronGeometry] to generate their
respective geometries.

## Code Example

  
```ts  
const verticesOfCube = [  
-1,-1,-1, 1,-1,-1, 1, 1,-1, -1, 1,-1,  
-1,-1, 1, 1,-1, 1, 1, 1, 1, -1, 1, 1,  
];  
  
const indicesOfFaces = [  
2,1,0, 0,3,2,  
0,4,7, 7,3,0,  
0,1,5, 5,4,0,  
1,2,6, 6,5,1,  
2,3,7, 7,6,2,  
4,5,6, 6,7,4  
];  
  
const geometry = new THREE.PolyhedronGeometry( verticesOfCube, indicesOfFaces,
6, 2 );  
```  

## Constructor

###  [name]([param:Array vertices], [param:Array indices], [param:Float
radius], [param:Integer detail])

vertices — [page:Array] of points of the form [1,1,1, -1,-1,-1, ... ]  
indices — [page:Array] of indices that make up the faces of the form [0,1,2,
2,3,0, ... ]  
radius — [page:Float] - The radius of the final shape  
detail — [page:Integer] - How many levels to subdivide the geometry. The more
detail, the smoother the shape.

## Properties

See the base [page:BufferGeometry] class for common properties.

### <br/> Object parameters; <br/>

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [page:BufferGeometry] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

