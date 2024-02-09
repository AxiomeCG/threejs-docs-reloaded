[page:Curve] →

# [name]

Create a smooth 2d [quadratic bezier
curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#mediaviewer/File:B%C3%A9zier_2_big.gif),
defined by a startpoint, endpoint and a single control point.

## Code Example

  
```ts  
const curve = new THREE.QuadraticBezierCurve(  
new THREE.Vector2( -10, 0 ),  
new THREE.Vector2( 20, 15 ),  
new THREE.Vector2( 10, 0 )  
);  
  
const points = curve.getPoints( 50 );  
const geometry = new THREE.BufferGeometry().setFromPoints( points );  
  
const material = new THREE.LineBasicMaterial( { color: 0xff0000 } );  
  
// Create the final object to add to the scene  
const curveObject = new THREE.Line( geometry, material );  
```  

## Constructor

###  [name]( [param:Vector2 v0], [param:Vector2 v1], [param:Vector2 v2] )

[page:Vector2 v0] – The startpoint.  
[page:Vector2 v1] – The control point.  
[page:Vector2 v2] – The endpoint.

## Properties

See the base [page:Curve] class for common properties.

### <br/> Vector2 v0; <br/>

The startpoint.

### <br/> Vector2 v1; <br/>

The control point.

### <br/> Vector2 v2; <br/>

The endpoint.

## Methods

See the base [page:Curve] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

