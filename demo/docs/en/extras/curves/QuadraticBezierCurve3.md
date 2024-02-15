[Curve](en\extras\core\Curve.html) →

# QuadraticBezierCurve3

Create a smooth 3d[quadratic bezier
curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#mediaviewer/File:B%C3%A9zier_2_big.gif),
defined by a startpoint, endpoint and a single control point.

## Code Example

  
```ts  
const curve = new THREE.QuadraticBezierCurve3( new THREE.Vector3( -10, 0, 0 ),
new THREE.Vector3( 20, 15, 0 ), new THREE.Vector3( 10, 0, 0 ) ); const points
= curve.getPoints( 50 ); const geometry = new
THREE.BufferGeometry().setFromPoints( points ); const material = new
THREE.LineBasicMaterial( { color: 0xff0000 } ); // Create the final object to
add to the scene const curveObject = new THREE.Line( geometry, material );  
```  

## Constructor

### QuadraticBezierCurve3

  
  
```ts  
function QuadraticBezierCurve3( v0: Vector3, v1: Vector3, v2: Vector3 ): void;  
```  

[v0](en\math\Vector3.html) – The starting point  
[v1](en\math\Vector3.html) – The middle control point  
[v2](en\math\Vector3.html) – The ending point  

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### v0

  
  
```ts  
v0: Vector3;  
```  

The startpoint.

### v1

  
  
```ts  
v1: Vector3;  
```  

The control point.

### v2

  
  
```ts  
v2: Vector3;  
```  

The endpoint.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/curves/QuadraticBezierCurve3.js">src/extras/curves/QuadraticBezierCurve3.js</a>

