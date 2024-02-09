# [name]

An implementation of the earcut polygon triangulation algorithm. The code is a
port of [link:https://github.com/mapbox/earcut mapbox/earcut].

## Methods

### [method:Array triangulate]( data, holeIndices, dim )

data -- A flat array of vertex coordinates.  
holeIndices -- An array of hole indices if any.  
dim -- The number of coordinates per vertex in the input array.  
  
Triangulates the given shape definition by returning an array of triangles. A
triangle is defined by three consecutive integers representing vertex indices.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

