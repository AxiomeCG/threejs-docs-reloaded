[page:Curve] → [page:CurvePath] → [page:Path] →

# Shape

Defines an arbitrary 2d shape plane using paths with optional holes. It can be
used with [page:ExtrudeGeometry], [page:ShapeGeometry], to get points, or to
get triangulated faces.

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

###  function Shape( points: Array ): void;

points -- (optional) array of [page:Vector2 Vector2s].  
  
Creates a Shape from the points. The first point defines the offset, then
successive points are added to the [page:CurvePath.curves curves] array as
[page:LineCurve LineCurves].  
  
If no points are specified, an empty shape is created and the
[page:.currentPoint] is set to the origin.

## Properties

See the base [page:Path] class for common properties.

###  String uuid;

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
instance. This gets automatically assigned, so this shouldn't be edited.

###  Array holes;

An array of [page:Path paths] that define the holes in the shape.

## Methods

See the base [page:Path] class for common methods.

###  function extractPoints( divisions: Integer ): Array;

divisions -- The fineness of the result.  
  
Call [page:Curve.getPoints getPoints] on the shape and the [page:.holes]
array, and return an object of the form:  
```ts  
{ shape holes }  
```  
where shape and holes are arrays of [page:Vector2 Vector2s].

###  function getPointsHoles( divisions: Integer ): Array;

divisions -- The fineness of the result.  
  
Get an array of [page:Vector2 Vector2s] that represent the holes in the shape.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

