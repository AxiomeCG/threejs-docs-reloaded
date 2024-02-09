[page:Curve] → [page:CurvePath] →

# [name]

A 2D path representation. The class provides methods for creating paths and
contours of 2D shapes similar to the 2D Canvas API.

## Code Example

  
```ts  
const path = new THREE.Path();  
  
path.lineTo( 0, 0.8 );  
path.quadraticCurveTo( 0, 1, 0.2, 1 );  
path.lineTo( 1, 1 );  
  
const points = path.getPoints();  
  
const geometry = new THREE.BufferGeometry().setFromPoints( points );  
const material = new THREE.LineBasicMaterial( { color: 0xffffff } );  
  
const line = new THREE.Line( geometry, material );  
scene.add( line );  
```  

## Constructor

### [name]( [param:Array points] )

points -- (optional) array of [page:Vector2 Vector2s].  
  
Creates a Path from the points. The first point defines the offset, then
successive points are added to the [page:CurvePath.curves curves] array as
[page:LineCurve LineCurves].  
  
If no points are specified, an empty path is created and the
[page:.currentPoint] is set to the origin.

## Properties

See the base [page:CurvePath] class for common properties.

### <br/> Vector2 currentPoint; <br/>

The current offset of the path. Any new [page:Curve] added will start here.

## Methods

See the base [page:CurvePath] class for common methods.

### <br/> function absarc( x: Float, y: Float, radius: Float, startAngle:
Float, endAngle: Float, clockwise: Boolean? ): absarc; <br/>

x, y -- The absolute center of the arc.  
radius -- The radius of the arc.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the arc clockwise. Defaults to `false`.  
  
Adds an absolutely positioned [page:EllipseCurve EllipseCurve] to the path.

### <br/> function absellipse( x: Float, y: Float, xRadius: Float, yRadius:
Float, startAngle: Float, endAngle: Float, clockwise: Boolean?, rotation:
Float ): absellipse; <br/>

x, y -- The absolute center of the ellipse.  
xRadius -- The radius of the ellipse in the x axis.  
yRadius -- The radius of the ellipse in the y axis.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the ellipse clockwise. Defaults to false.  
rotation -- The rotation angle of the ellipse in radians, counterclockwise
from the positive X axis. Optional, defaults to `0`.  
  
Adds an absolutely positioned [page:EllipseCurve EllipseCurve] to the path.

### <br/> function arc( x: Float, y: Float, radius: Float, startAngle: Float,
endAngle: Float, clockwise: Boolean? ): arc; <br/>

x, y -- The center of the arc offset from the last call.  
radius -- The radius of the arc.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the arc clockwise. Defaults to `false`.  
  
Adds an [page:EllipseCurve EllipseCurve] to the path, positioned relative to
[page:.currentPoint].

### <br/> function bezierCurveTo( cp1X: Float, cp1Y: Float, cp2X: Float, cp2Y:
Float, x: Float, y: Float ): bezierCurveTo; <br/>

This creates a bezier curve from [page:.currentPoint] with (cp1X, cp1Y) and
(cp2X, cp2Y) as control points and updates [page:.currentPoint] to x and y.

### <br/> function ellipse( x: Float, y: Float, xRadius: Float, yRadius:
Float, startAngle: Float, endAngle: Float, clockwise: Boolean?, rotation:
Float ): ellipse; <br/>

x, y -- The center of the ellipse offset from the last call.  
xRadius -- The radius of the ellipse in the x axis.  
yRadius -- The radius of the ellipse in the y axis.  
startAngle -- The start angle in radians.  
endAngle -- The end angle in radians.  
clockwise -- Sweep the ellipse clockwise. Defaults to `false`.  
rotation -- The rotation angle of the ellipse in radians, counterclockwise
from the positive X axis. Optional, defaults to `0`.  
  
Adds an [page:EllipseCurve EllipseCurve] to the path, positioned relative to
[page:.currentPoint].

### <br/> function lineTo( x: Float, y: Float ): lineTo; <br/>

Connects a [page:LineCurve] from [page:.currentPoint] to x, y onto the path.

### <br/> function moveTo( x: Float, y: Float ): moveTo; <br/>

Move the [page:.currentPoint] to x, y.

### <br/> function quadraticCurveTo( cpX: Float, cpY: Float, x: Float, y:
Float ): quadraticCurveTo; <br/>

Creates a quadratic curve from [page:.currentPoint] with cpX and cpY as
control point and updates [page:.currentPoint] to x and y.

### <br/> function setFromPoints( vector2s: Array ): setFromPoints; <br/>

points -- array of [page:Vector2 Vector2s].  
  
Points are added to the [page:CurvePath.curves curves] array as
[page:LineCurve LineCurves].

### <br/> function splineThru( points: Array ): splineThru; <br/>

points - An array of [page:Vector2 Vector2s]  
  
Connects a new [page:SplineCurve] onto the path.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

