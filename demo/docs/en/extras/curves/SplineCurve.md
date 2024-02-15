[Curve](en\extras\core\Curve.html) →

# SplineCurve

Create a smooth 2d spline curve from a series of points. Internally this uses
[Interpolations.CatmullRom](#) to create the curve.

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

### SplineCurve

  
  
```ts  
function SplineCurve( points: Array ): void;  
```  

points – An array of [Vector2](en\math\Vector2.html) points that define the
curve.

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### points

  
  
```ts  
points: Array;  
```  

The array of [Vector2](en\math\Vector2.html) points that define the curve.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/curves/SplineCurve.js">src/extras/curves/SplineCurve.js</a>

