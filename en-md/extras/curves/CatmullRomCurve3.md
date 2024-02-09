[page:Curve] →

# [name]

Create a smooth 3d spline curve from a series of points using the
[link:https://en.wikipedia.org/wiki/Centripetal_Catmull-Rom_spline Catmull-
Rom] algorithm.

## Code Example

  
```ts  
//Create a closed wavey loop  
const curve = new THREE.CatmullRomCurve3( [  
new THREE.Vector3( -10, 0, 10 ),  
new THREE.Vector3( -5, 5, 5 ),  
new THREE.Vector3( 0, 0, 0 ),  
new THREE.Vector3( 5, -5, 5 ),  
new THREE.Vector3( 10, 0, 10 )  
] );  
  
const points = curve.getPoints( 50 );  
const geometry = new THREE.BufferGeometry().setFromPoints( points );  
  
const material = new THREE.LineBasicMaterial( { color: 0xff0000 } );  
  
// Create the final object to add to the scene  
const curveObject = new THREE.Line( geometry, material );  
```  

## Examples

[example:webgl_geometry_extrude_splines WebGL / geometry / extrude / splines]

## Constructor

###  [name]( [param:Array points], [param:Boolean closed], [param:String
curveType], [param:Float tension] )

points – An array of [page:Vector3] points  
closed – Whether the curve is closed. Default is `false`.  
curveType – Type of the curve. Default is `centripetal`.  
tension – Tension of the curve. Default is `0.5`.

## Properties

See the base [page:Curve] class for common properties.

### <br/> Array points; <br/>

The array of [page:Vector3] points that define the curve. It needs at least
two entries.

### <br/> Boolean closed; <br/>

The curve will loop back onto itself when this is true.

### <br/> String curveType; <br/>

Possible values are `centripetal`, `chordal` and `catmullrom`.

### <br/> Float tension; <br/>

When [page:.curveType] is `catmullrom`, defines catmullrom's tension.

## Methods

See the base [page:Curve] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

