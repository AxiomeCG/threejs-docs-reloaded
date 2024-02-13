[page:Curve] →

# EllipseCurve

Creates a 2d curve in the shape of an ellipse. Setting the [page:Number
xRadius] equal to the [page:Number yRadius] will result in a circle.

## Code Example

  
```ts  
const curve = new THREE.EllipseCurve( 0, 0, // ax, aY 10, 10, // xRadius,
yRadius 0, 2 * Math.PI, // aStartAngle, aEndAngle false, // aClockwise 0 //
aRotation ); const points = curve.getPoints( 50 ); const geometry = new
THREE.BufferGeometry().setFromPoints( points ); const material = new
THREE.LineBasicMaterial( { color: 0xff0000 } ); // Create the final object to
add to the scene const ellipse = new THREE.Line( geometry, material );  
```  

## Constructor

###  function EllipseCurve( aX: Float, aY: Float, xRadius: Float, yRadius:
Float, aStartAngle: Radians, aEndAngle: Radians, aClockwise: Boolean,
aRotation: Radians ): void;

[page:Float aX] – The X center of the ellipse. Default is `0`.  
[page:Float aY] – The Y center of the ellipse. Default is `0`.  
[page:Float xRadius] – The radius of the ellipse in the x direction. Default
is `1`.  
[page:Float yRadius] – The radius of the ellipse in the y direction. Default
is `1`.  
[page:Radians aStartAngle] – The start angle of the curve in radians starting
from the positive X axis. Default is `0`.  
[page:Radians aEndAngle] – The end angle of the curve in radians starting from
the positive X axis. Default is `2 x Math.PI`.  
[page:Boolean aClockwise] – Whether the ellipse is drawn clockwise. Default is
`false`.  
[page:Radians aRotation] – The rotation angle of the ellipse in radians,
counterclockwise from the positive X axis (optional). Default is `0`.  
  

## Properties

See the base [page:Curve] class for common properties.

###  Float aX;

The X center of the ellipse.

###  Float aY;

The Y center of the ellipse.

###  Radians xRadius;

The radius of the ellipse in the x direction.

###  Radians yRadius;

The radius of the ellipse in the y direction.

###  Float aStartAngle;

The start angle of the curve in radians starting from the middle right side.

###  Float aEndAngle;

The end angle of the curve in radians starting from the middle right side.

###  Boolean aClockwise;

Whether the ellipse is drawn clockwise.

###  Float aRotation;

The rotation angle of the ellipse in radians, counterclockwise from the
positive X axis (optional). Default is `0`.

## Methods

See the base [page:Curve] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

