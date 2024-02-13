[page:Curve] →

# SplineCurve

Create a smooth 2d spline curve from a series of points. Internally this uses
[page:Interpolations.CatmullRom] to create the curve.

## Code Example

  
```ts  
// Create a sine-like wave const curve = new THREE.SplineCurve( [ new
THREE.Vector2( -10, 0 ), new THREE.Vector2( -5, 5 ), new THREE.Vector2( 0, 0
), new THREE.Vector2( 5, -5 ), new THREE.Vector2( 10, 0 ) ] ); const points =
curve.getPoints( 50 ); const geometry = new
THREE.BufferGeometry().setFromPoints( points ); const material = new
THREE.LineBasicMaterial( { color: 0xff0000 } ); // Create the final object to
add to the scene const splineObject = new THREE.Line( geometry, material );  
```  

## Constructor

###  function SplineCurve( points: Array ): void;

points – An array of [page:Vector2] points that define the curve.

## Properties

See the base [page:Curve] class for common properties.

###  Array points;

The array of [page:Vector2] points that define the curve.

## Methods

See the base [page:Curve] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

