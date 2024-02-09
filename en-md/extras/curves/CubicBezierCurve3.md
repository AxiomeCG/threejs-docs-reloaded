[page:Curve] →

# [name]

Create a smooth 3d [cubic bezier
curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve#mediaviewer/File:Bezier_curve.svg),
defined by a start point, endpoint and two control points.

## Code Example

  
```ts  
const curve = new THREE.CubicBezierCurve3(  
new THREE.Vector3( -10, 0, 0 ),  
new THREE.Vector3( -5, 15, 0 ),  
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

###  [name]( [param:Vector3 v0], [param:Vector3 v1], [param:Vector3 v2],
[param:Vector3 v3] )

[page:Vector3 v0] – The starting point.  
[page:Vector3 v1] – The first control point.  
[page:Vector3 v2] – The second control point.  
[page:Vector3 v3] – The ending point.

## Properties

See the base [page:Curve] class for common properties.

### <br/> Vector3 v0; <br/>

The starting point.

### <br/> Vector3 v1; <br/>

The first control point.

### <br/> Vector3 v2; <br/>

The second control point.

### <br/> Vector3 v3; <br/>

The ending point.

## Methods

See the base [page:Curve] class for common Methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

