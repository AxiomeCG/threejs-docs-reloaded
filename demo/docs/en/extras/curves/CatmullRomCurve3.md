[Curve](en\extras\core\Curve.html) →

# CatmullRomCurve3

Create a smooth 3d spline curve from a series of points using the <a
href="https://en.wikipedia.org/wiki/Centripetal_Catmull-Rom_spline">Catmull-
Rom</a> algorithm.

## Code Example

  
```ts  
//Create a closed wavey loop const curve = new THREE.CatmullRomCurve3( [ new
THREE.Vector3( -10, 0, 10 ), new THREE.Vector3( -5, 5, 5 ), new THREE.Vector3(
0, 0, 0 ), new THREE.Vector3( 5, -5, 5 ), new THREE.Vector3( 10, 0, 10 ) ] );
const points = curve.getPoints( 50 ); const geometry = new
THREE.BufferGeometry().setFromPoints( points ); const material = new
THREE.LineBasicMaterial( { color: 0xff0000 } ); // Create the final object to
add to the scene const curveObject = new THREE.Line( geometry, material );  
```  

## Examples

[example:webgl_geometry_extrude_splines WebGL / geometry / extrude / splines]

## Constructor

### CatmullRomCurve3

  
  
```ts  
function CatmullRomCurve3( points: Array, closed: Boolean, curveType: String,
tension: Float ): void;  
```  

points – An array of [Vector3](en\math\Vector3.html) points  
closed – Whether the curve is closed. Default is `false`.  
curveType – Type of the curve. Default is `centripetal`.  
tension – Tension of the curve. Default is `0.5`.

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### points

  
  
```ts  
points: Array;  
```  

The array of [Vector3](en\math\Vector3.html) points that define the curve. It
needs at least two entries.

### closed

  
  
```ts  
closed: Boolean;  
```  

The curve will loop back onto itself when this is true.

### curveType

  
  
```ts  
curveType: String;  
```  

Possible values are `centripetal`, `chordal` and `catmullrom`.

### tension

  
  
```ts  
tension: Float;  
```  

When [.curveType](#) is `catmullrom`, defines catmullrom's tension.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/curves/CatmullRomCurve3.js">src/extras/curves/CatmullRomCurve3.js</a>

