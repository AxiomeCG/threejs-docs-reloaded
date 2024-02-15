[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →
[LineSegments](en\objects\LineSegments.html) →

# PlaneHelper

Helper object to visualize a [Plane](en\math\Plane.html).

## Code Example

  
```ts  
const plane = new THREE.Plane( new THREE.Vector3( 1, 1, 0.2 ), 3 ); const
helper = new THREE.PlaneHelper( plane, 1, 0xffff00 ); scene.add( helper );  
```  

## Constructor

### PlaneHelper

  
  
```ts  
function PlaneHelper( plane: Plane, size: Float, hex: Color ): void;  
```  

[plane](en\math\Plane.html) -- the plane to visualize.  
[size](#) -- (optional) side length of plane helper. Default is 1.  
[color](en\math\Color.html) -- (optional) the color of the helper. Default is
0xffff00.  
  
Creates a new wireframe representation of the passed plane.

## Properties

See the base [Line](en\objects\Line.html) class for common properties.

### plane

  
  
```ts  
plane: Plane;  
```  

The [plane](en\math\Plane.html) being visualized.

### size

  
  
```ts  
size: Float;  
```  

The side lengths of plane helper.

## Methods

See the base [LineSegments](en\objects\LineSegments.html) class for common
methods.

### updateMatrixWorld

  
  
```ts  
function updateMatrixWorld( force: Boolean ): undefined;  
```  

This overrides the method in the base [Object3D](en\core\Object3D.html) class
so that it also updates the helper object according to the [.plane](#) and
[.size](#) properties.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/PlaneHelper.js">src/helpers/PlaneHelper.js</a>

