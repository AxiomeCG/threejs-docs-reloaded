# ShapeUtils

A class containing utility functions for shapes.  
  
Note that these are all linear functions so it is necessary to calculate
separately for x, y (and z, w if present) components of a vector.

## Methods

### area

  
  
```ts  
function area( ): Number;  
```  

contour -- 2D polygon. An array of THREE.Vector2()  
  
Calculate area of a ( 2D ) contour polygon.

### isClockWise

  
  
```ts  
function isClockWise( ): Boolean;  
```  

pts -- points defining a 2D polygon  
  
Note that this is a linear function so it is necessary to calculate separately
for x, y components of a polygon.  
  
Used internally by [Path](en\extras\core\Path.html),
[ExtrudeGeometry](en\geometries\ExtrudeGeometry.html) and
[ShapeGeometry](en\geometries\ShapeGeometry.html).

### triangulateShape

  
  
```ts  
function triangulateShape( ): Array;  
```  

contour -- 2D polygon. An array of [Vector2](en\math\Vector2.html).  
holes -- An array that holds arrays of [Vector2](en\math\Vector2.html)s. Each
array represents a single hole definition.  
  
Used internally by [ExtrudeGeometry](en\geometries\ExtrudeGeometry.html) and
[ShapeGeometry](en\geometries\ShapeGeometry.html) to calculate faces in shapes
with holes.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/ShapeUtils.js">src/extras/ShapeUtils.js</a>

