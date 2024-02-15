[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →
[LineSegments](en\objects\LineSegments.html) →

# CameraHelper

This helps with visualizing what a camera contains in its frustum. It
visualizes the frustum of a camera using a
[LineSegments](en\objects\LineSegments.html).  
  
CameraHelper must be a child of the scene.

## Code Example

  
```ts  
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth /
window.innerHeight, 0.1, 1000 );const helper = new THREE.CameraHelper( camera
);scene.add( helper );  
```  

## Examples

[example:webgl_camera WebGL / camera]  
[example:webgl_geometry_extrude_splines WebGL / extrude / splines]

## Constructor

### CameraHelper

  
  
```ts  
function CameraHelper( camera: Camera ): void;  
```  

[camera](en\cameras\Camera.html) -- The camera to visualize.  
  
This create a new [Name] for the specified camera.

## Properties

See the base [LineSegments](en\objects\LineSegments.html) class for common
properties.

### camera

  
  
```ts  
camera: Camera;  
```  

The camera being visualized.

### pointMap

  
  
```ts  
pointMap: Object;  
```  

This contains the points used to visualize the camera.

### matrix

  
  
```ts  
matrix: Object;  
```  

Reference to the [camera.matrixWorld](#).

### matrixAutoUpdate

  
  
```ts  
matrixAutoUpdate: Object;  
```  

See [Object3D.matrixAutoUpdate](#). Set to `false` here as the helper is using
the camera's [matrixWorld](#).

## Methods

See the base [LineSegments](en\objects\LineSegments.html) class for common
methods.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### setColors

  
  
```ts  
function setColors( frustum: Color, cone: Color, up: Color, target: Color,
cross: Color ): this;  
```  

Defines the colors of the helper.

### update

  
  
```ts  
function update( ): undefined;  
```  

Updates the helper based on the projectionMatrix of the camera.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/CameraHelper.js">src/helpers/CameraHelper.js</a>

