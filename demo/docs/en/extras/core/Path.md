[Curve](en\extras\core\Curve.html) →
[CurvePath](en\extras\core\CurvePath.html) →

# Path

A 2D path representation. The class provides methods for creating paths and
contours of 2D shapes similar to the 2D Canvas API.

## Code Example

  
```ts  
const path = new THREE.Path(); path.lineTo( 0, 0.8 ); path.quadraticCurveTo(
0, 1, 0.2, 1 ); path.lineTo( 1, 1 ); const points = path.getPoints(); const
geometry = new THREE.BufferGeometry().setFromPoints( points ); const material
= new THREE.LineBasicMaterial( { color: 0xffffff } ); const line = new
THREE.Line( geometry, material ); scene.add( line );  
```  

## Constructor

### Path

  
  
```ts  
function Path( points: Array ): void;  
```  

points -- (optional) array of [Vector2s](en\math\Vector2.html).  
  
Creates a Path from the points. The first point defines the offset, then
successive points are added to the [curves](#) array as
[LineCurves](en\extras\curves\LineCurve.html).  
  
If no points are specified, an empty path is created and the
[.currentPoint](#) is set to the origin.

## Properties

See the base [CurvePath](en\extras\core\CurvePath.html) class for common
properties.

### currentPoint

  
  
```ts  
currentPoint: Vector2;  
```  

The current offset of the path. Any new [Curve](en\extras\core\Curve.html)
added will start here.

## Methods

See the base [CurvePath](en\extras\core\CurvePath.html) class for common
methods.

### absarc

  
  
```ts  
function absarc( x: Float, y: Float, radius: Float, startAngle: Float,
endAngle: Float, clockwise: Boolean ): this;  
```  

x, y -- The absolute center of the arc.  
radius -- The radius of the arc.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the arc clockwise. Defaults to `false`.  
  
Adds an absolutely positioned
[EllipseCurve](en\extras\curves\EllipseCurve.html) to the path.

### absellipse

  
  
```ts  
function absellipse( x: Float, y: Float, xRadius: Float, yRadius: Float,
startAngle: Float, endAngle: Float, clockwise: Boolean, rotation: Float ):
this;  
```  

x, y -- The absolute center of the ellipse.  
xRadius -- The radius of the ellipse in the x axis.  
yRadius -- The radius of the ellipse in the y axis.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the ellipse clockwise. Defaults to false.  
rotation -- The rotation angle of the ellipse in radians, counterclockwise
from the positive X axis. Optional, defaults to `0`.  
  
Adds an absolutely positioned
[EllipseCurve](en\extras\curves\EllipseCurve.html) to the path.

### arc

  
  
```ts  
function arc( x: Float, y: Float, radius: Float, startAngle: Float, endAngle:
Float, clockwise: Boolean ): this;  
```  

x, y -- The center of the arc offset from the last call.  
radius -- The radius of the arc.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the arc clockwise. Defaults to `false`.  
  
Adds an [.llipseCurve](#llipseCurve) to the path, positioned relative to
[.currentPoint](#).

### bezierCurveTo

  
  
```ts  
function bezierCurveTo( cp1X: Float, cp1Y: Float, cp2X: Float, cp2Y: Float, x:
Float, y: Float ): this;  
```  

This creates a bezier curve from [.currentPoint](#) with (cp1X, cp1Y) and
(cp2X, cp2Y) as control points and updates [.currentPoint](#) to x and y.

### ellipse

  
  
```ts  
function ellipse( x: Float, y: Float, xRadius: Float, yRadius: Float,
startAngle: Float, endAngle: Float, clockwise: Boolean, rotation: Float ):
this;  
```  

x, y -- The center of the ellipse offset from the last call.  
xRadius -- The radius of the ellipse in the x axis.  
yRadius -- The radius of the ellipse in the y axis.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the ellipse clockwise. Defaults to `false`.  
rotation -- The rotation angle of the ellipse in radians, counterclockwise
from the positive X axis. Optional, defaults to `0`.  
  
Adds an [.llipseCurve](#llipseCurve) to the path, positioned relative to
[.currentPoint](#).

### lineTo

  
  
```ts  
function lineTo( x: Float, y: Float ): this;  
```  

Connects a [LineCurve](en\extras\curves\LineCurve.html) from
[.currentPoint](#) to x, y onto the path.

### moveTo

  
  
```ts  
function moveTo( x: Float, y: Float ): this;  
```  

Move the [.currentPoint](#) to x, y.

### quadraticCurveTo

  
  
```ts  
function quadraticCurveTo( cpX: Float, cpY: Float, x: Float, y: Float ): this;  
```  

Creates a quadratic curve from [.currentPoint](#) with cpX and cpY as control
point and updates [.currentPoint](#) to x and y.

### setFromPoints

  
  
```ts  
function setFromPoints( vector2s: Array ): this;  
```  

points -- array of [Vector2s](en\math\Vector2.html).  
  
Points are added to the [curves](#) array as
[LineCurves](en\extras\curves\LineCurve.html).

### splineThru

  
  
```ts  
function splineThru( points: Array ): this;  
```  

points - An array of [Vector2s](en\math\Vector2.html)  
  
Connects a new [SplineCurve](en\extras\curves\SplineCurve.html) onto the path.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/core/Path.js">src/extras/core/Path.js</a>

