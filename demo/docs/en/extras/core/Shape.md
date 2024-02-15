[Curve](en\extras\core\Curve.html) →
[CurvePath](en\extras\core\CurvePath.html) → [Path](en\extras\core\Path.html)
→

# Shape

Defines an arbitrary 2d shape plane using paths with optional holes. It can be
used with [ExtrudeGeometry](en\geometries\ExtrudeGeometry.html),
[ShapeGeometry](en\geometries\ShapeGeometry.html), to get points, or to get
triangulated faces.

## Code Example

  
```ts  
const heartShape = new THREE.Shape(); heartShape.moveTo( 25, 25 );
heartShape.bezierCurveTo( 25, 25, 20, 0, 0, 0 ); heartShape.bezierCurveTo( -
30, 0, - 30, 35, - 30, 35 ); heartShape.bezierCurveTo( - 30, 55, - 10, 77, 25,
95 ); heartShape.bezierCurveTo( 60, 77, 80, 55, 80, 35 );
heartShape.bezierCurveTo( 80, 35, 80, 0, 50, 0 ); heartShape.bezierCurveTo(
35, 0, 25, 25, 25, 25 ); const extrudeSettings = { depth: 8, bevelEnabled:
true, bevelSegments: 2, steps: 2, bevelSize: 1, bevelThickness: 1 }; const
geometry = new THREE.ExtrudeGeometry( heartShape, extrudeSettings ); const
mesh = new THREE.Mesh( geometry, new THREE.MeshPhongMaterial() );  
```  

## Examples

[example:webgl_geometry_shapes geometry / shapes ]  
[example:webgl_geometry_extrude_shapes geometry / extrude / shapes ]

## Constructor

### Shape

  
  
```ts  
function Shape( points: Array ): void;  
```  

points -- (optional) array of [Vector2s](en\math\Vector2.html).  
  
Creates a Shape from the points. The first point defines the offset, then
successive points are added to the [curves](#) array as
[LineCurves](en\extras\curves\LineCurve.html).  
  
If no points are specified, an empty shape is created and the
[.currentPoint](#) is set to the origin.

## Properties

See the base [Path](en\extras\core\Path.html) class for common properties.

### uuid

  
  
```ts  
uuid: String;  
```  

<a href="http://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a>
of this instance. This gets automatically assigned, so this shouldn't be
edited.

### holes

  
  
```ts  
holes: Array;  
```  

An array of [paths](en\extras\core\Path.html) that define the holes in the
shape.

## Methods

See the base [Path](en\extras\core\Path.html) class for common methods.

### extractPoints

  
  
```ts  
function extractPoints( divisions: Integer ): Array;  
```  

divisions -- The fineness of the result.  
  
Call [getPoints](#) on the shape and the [.holes](#) array, and return an
object of the form:  
```ts  
{ shape holes }  
```  
where shape and holes are arrays of [Vector2s](en\math\Vector2.html).

### getPointsHoles

  
  
```ts  
function getPointsHoles( divisions: Integer ): Array;  
```  

divisions -- The fineness of the result.  
  
Get an array of [Vector2s](en\math\Vector2.html) that represent the holes in
the shape.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/core/Shape.js">src/extras/core/Shape.js</a>

