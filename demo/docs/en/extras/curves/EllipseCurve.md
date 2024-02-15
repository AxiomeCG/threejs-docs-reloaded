[Curve](en\extras\core\Curve.html) →

# EllipseCurve

Creates a 2d curve in the shape of an ellipse. Setting the [xRadius](#) equal
to the [yRadius](#) will result in a circle.

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

### EllipseCurve

  
  
```ts  
function EllipseCurve( aX: Float, aY: Float, xRadius: Float, yRadius: Float,
aStartAngle: Radians, aEndAngle: Radians, aClockwise: Boolean, aRotation:
Radians ): void;  
```  

[aX](#) – The X center of the ellipse. Default is `0`.  
[aY](#) – The Y center of the ellipse. Default is `0`.  
[xRadius](#) – The radius of the ellipse in the x direction. Default is `1`.  
[yRadius](#) – The radius of the ellipse in the y direction. Default is `1`.  
[aStartAngle](#) – The start angle of the curve in radians starting from the
positive X axis. Default is `0`.  
[aEndAngle](#) – The end angle of the curve in radians starting from the
positive X axis. Default is `2 x Math.PI`.  
[aClockwise](#) – Whether the ellipse is drawn clockwise. Default is `false`.  
[aRotation](#) – The rotation angle of the ellipse in radians,
counterclockwise from the positive X axis (optional). Default is `0`.  
  

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### aX

  
  
```ts  
aX: Float;  
```  

The X center of the ellipse.

### aY

  
  
```ts  
aY: Float;  
```  

The Y center of the ellipse.

### xRadius

  
  
```ts  
xRadius: Radians;  
```  

The radius of the ellipse in the x direction.

### yRadius

  
  
```ts  
yRadius: Radians;  
```  

The radius of the ellipse in the y direction.

### aStartAngle

  
  
```ts  
aStartAngle: Float;  
```  

The start angle of the curve in radians starting from the middle right side.

### aEndAngle

  
  
```ts  
aEndAngle: Float;  
```  

The end angle of the curve in radians starting from the middle right side.

### aClockwise

  
  
```ts  
aClockwise: Boolean;  
```  

Whether the ellipse is drawn clockwise.

### aRotation

  
  
```ts  
aRotation: Float;  
```  

The rotation angle of the ellipse in radians, counterclockwise from the
positive X axis (optional). Default is `0`.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/curves/EllipseCurve.js">src/extras/curves/EllipseCurve.js</a>

