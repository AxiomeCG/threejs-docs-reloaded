[page:Object3D] → [page:Line] → [page:LineSegments] →

# CameraHelper

This helps with visualizing what a camera contains in its frustum. It
visualizes the frustum of a camera using a [page:LineSegments].  
  
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

###  function CameraHelper( camera: Camera ): void;

[page:Camera camera] -- The camera to visualize.  
  
This create a new [Name] for the specified camera.

## Properties

See the base [page:LineSegments] class for common properties.

###  Camera camera;

The camera being visualized.

###  Object pointMap;

This contains the points used to visualize the camera.

###  Object matrix;

Reference to the [page:Object3D.matrixWorld camera.matrixWorld].

###  Object matrixAutoUpdate;

See [page:Object3D.matrixAutoUpdate]. Set to `false` here as the helper is
using the camera's [page:Object3D.matrixWorld matrixWorld].

## Methods

See the base [page:LineSegments] class for common methods.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function setColors( frustum: Color, cone: Color, up: Color, target:
Color, cross: Color ): this;

Defines the colors of the helper.

###  function update( ): undefined;

Updates the helper based on the projectionMatrix of the camera.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

