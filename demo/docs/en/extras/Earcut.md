# Earcut

An implementation of the earcut polygon triangulation algorithm. The code is a
port of <a href="https://github.com/mapbox/earcut">mapbox/earcut</a>.

## Methods

### triangulate

  
  
```ts  
function triangulate( ): Array;  
```  

data -- A flat array of vertex coordinates.  
holeIndices -- An array of hole indices if any.  
dim -- The number of coordinates per vertex in the input array.  
  
Triangulates the given shape definition by returning an array of triangles. A
triangle is defined by three consecutive integers representing vertex indices.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/Earcut.js">src/extras/Earcut.js</a>

