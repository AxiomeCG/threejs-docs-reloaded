[page:Curve] →

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

[page:Vector2 v0] – The starting point.  
[page:Vector2 v1] – The first control point.  
[page:Vector2 v2] – The second control point.  
[page:Vector2 v3] – The ending point.

## Properties

See the base [page:Curve] class for common properties.

###  Vector2 v0;

The starting point.

###  Vector2 v1;

The first control point.

###  Vector2 v2;

The second control point.

###  Vector2 v3;

The ending point.

## Methods

See the base [page:Curve] class for common Methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

