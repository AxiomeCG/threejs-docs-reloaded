# ShapeUtils

A class containing utility functions for shapes.  
  
Note that these are all linear functions so it is necessary to calculate
separately for x, y (and z, w if present) components of a vector.

## Methods

###  function area( ): Number;

contour -- 2D polygon. An array of THREE.Vector2()  
  
Calculate area of a ( 2D ) contour polygon.

###  function isClockWise( ): Boolean;

pts -- points defining a 2D polygon  
  
Note that this is a linear function so it is necessary to calculate separately
for x, y components of a polygon.  
  
Used internally by [page:Path Path], [page:ExtrudeGeometry ExtrudeGeometry]
and [page:ShapeGeometry ShapeGeometry].

###  function triangulateShape( ): Array;

contour -- 2D polygon. An array of [page:Vector2].  
holes -- An array that holds arrays of [page:Vector2]s. Each array represents
a single hole definition.  
  
Used internally by [page:ExtrudeGeometry ExtrudeGeometry] and
[page:ShapeGeometry ShapeGeometry] to calculate faces in shapes with holes.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

