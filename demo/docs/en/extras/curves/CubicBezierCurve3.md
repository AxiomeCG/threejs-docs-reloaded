[Curve](en\extras\core\Curve.html) →

# CubicBezierCurve3

Create a smooth 3d[cubic bezier
curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#mediaviewer/File:Bezier_curve.svg),
defined by a start point, endpoint and two control points.

## Code Example

  
```ts  
const curve = new THREE.CubicBezierCurve3( new THREE.Vector3( -10, 0, 0 ), new
THREE.Vector3( -5, 15, 0 ), new THREE.Vector3( 20, 15, 0 ), new THREE.Vector3(
10, 0, 0 ) ); const points = curve.getPoints( 50 ); const geometry = new
THREE.BufferGeometry().setFromPoints( points ); const material = new
THREE.LineBasicMaterial( { color: 0xff0000 } ); // Create the final object to
add to the scene const curveObject = new THREE.Line( geometry, material );  
```  

## Constructor

### CubicBezierCurve3

  
  
```ts  
function CubicBezierCurve3( v0: Vector3, v1: Vector3, v2: Vector3, v3: Vector3
): void;  
```  

[v0](en\math\Vector3.html) – The starting point.  
[v1](en\math\Vector3.html) – The first control point.  
[v2](en\math\Vector3.html) – The second control point.  
[v3](en\math\Vector3.html) – The ending point.

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### v0

  
  
```ts  
v0: Vector3;  
```  

The starting point.

### v1

  
  
```ts  
v1: Vector3;  
```  

The first control point.

### v2

  
  
```ts  
v2: Vector3;  
```  

The second control point.

### v3

  
  
```ts  
v3: Vector3;  
```  

The ending point.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common Methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/curves/CubicBezierCurve3.js">src/extras/curves/CubicBezierCurve3.js</a>

