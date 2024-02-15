[Curve](en\extras\core\Curve.html) →

# CubicBezierCurve

Create a smooth 2d[cubic bezier
curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#mediaviewer/File:Bezier_curve.svg),
defined by a start point, endpoint and two control points.

## Code Example

  
```ts  
const curve = new THREE.CubicBezierCurve( new THREE.Vector2( -10, 0 ), new
THREE.Vector2( -5, 15 ), new THREE.Vector2( 20, 15 ), new THREE.Vector2( 10, 0
) ); const points = curve.getPoints( 50 ); const geometry = new
THREE.BufferGeometry().setFromPoints( points ); const material = new
THREE.LineBasicMaterial( { color: 0xff0000 } ); // Create the final object to
add to the scene const curveObject = new THREE.Line( geometry, material );  
```  

## Constructor

### CubicBezierCurve ( [param:Vector2 v0], [param:Vector2 v1], [param:Vector2
v2], [param:Vector2 v3] )

[v0](en\math\Vector2.html) – The starting point.  
[v1](en\math\Vector2.html) – The first control point.  
[v2](en\math\Vector2.html) – The second control point.  
[v3](en\math\Vector2.html) – The ending point.

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### v0

  
  
```ts  
v0: Vector2;  
```  

The starting point.

### v1

  
  
```ts  
v1: Vector2;  
```  

The first control point.

### v2

  
  
```ts  
v2: Vector2;  
```  

The second control point.

### v3

  
  
```ts  
v3: Vector2;  
```  

The ending point.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common Methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/curves/CubicBezierCurve.js">src/extras/curves/CubicBezierCurve.js</a>

