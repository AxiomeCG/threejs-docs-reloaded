[page:Curve] →

# [name]

Create a smooth 3d [quadratic bezier
curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#mediaviewer/File:B%C3%A9zier_2_big.gif),
defined by a startpoint, endpoint and a single control point.

## Code Example

  
```ts  
const curve = new THREE.QuadraticBezierCurve3(  
new THREE.Vector3( -10, 0, 0 ),  
new THREE.Vector3( 20, 15, 0 ),  
new THREE.Vector3( 10, 0, 0 )  
);  
  
const points = curve.getPoints( 50 );  
const geometry = new THREE.BufferGeometry().setFromPoints( points );  
  
const material = new THREE.LineBasicMaterial( { color: 0xff0000 } );  
  
// Create the final object to add to the scene  
const curveObject = new THREE.Line( geometry, material );  
```  

## Constructor

###  [name]( [param:Vector3 v0], [param:Vector3 v1], [param:Vector3 v2] )

[page:Vector3 v0] – The starting point  
[page:Vector3 v1] – The middle control point  
[page:Vector3 v2] – The ending point  

## Properties

See the base [page:Curve] class for common properties.

### <br/> Vector3 v0; <br/>

The startpoint.

### <br/> Vector3 v1; <br/>

The control point.

### <br/> Vector3 v2; <br/>

The endpoint.

## Methods

See the base [page:Curve] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

