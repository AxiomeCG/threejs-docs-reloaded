[Curve](en\extras\core\Curve.html) →

# QuadraticBezierCurve

Create a smooth 2d[quadratic bezier
curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#mediaviewer/File:B%C3%A9zier_2_big.gif),
defined by a startpoint, endpoint and a single control point.

## Code Example

  
```ts  
const curve = new THREE.QuadraticBezierCurve( new THREE.Vector2( -10, 0 ), new
THREE.Vector2( 20, 15 ), new THREE.Vector2( 10, 0 ) ); const points =
curve.getPoints( 50 ); const geometry = new
THREE.BufferGeometry().setFromPoints( points ); const material = new
THREE.LineBasicMaterial( { color: 0xff0000 } ); // Create the final object to
add to the scene const curveObject = new THREE.Line( geometry, material );  
```  

## Constructor

### QuadraticBezierCurve

  
  
```ts  
function QuadraticBezierCurve( v0: Vector2, v1: Vector2, v2: Vector2 ): void;  
```  

[v0](en\math\Vector2.html) – The startpoint.  
[v1](en\math\Vector2.html) – The control point.  
[v2](en\math\Vector2.html) – The endpoint.

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### v0

  
  
```ts  
v0: Vector2;  
```  

The startpoint.

### v1

  
  
```ts  
v1: Vector2;  
```  

The control point.

### v2

  
  
```ts  
v2: Vector2;  
```  

The endpoint.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/curves/QuadraticBezierCurve.js">src/extras/curves/QuadraticBezierCurve.js</a>

