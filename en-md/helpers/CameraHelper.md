[page:Object3D] → [page:Line] → [page:LineSegments] →

# [name]

This helps with visualizing what a camera contains in its frustum. It
visualizes the frustum of a camera using a [page:LineSegments].  
  
[name] must be a child of the scene.

## Code Example

  
```ts  
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth /
window.innerHeight, 0.1, 1000 );  
const helper = new THREE.CameraHelper( camera );  
scene.add( helper );  
```  

## Examples

[example:webgl_camera WebGL / camera]  
[example:webgl_geometry_extrude_splines WebGL / extrude / splines]

## Constructor

### [name]( [param:Camera camera] )

[page:Camera camera] -- The camera to visualize.  
  
This create a new [Name] for the specified camera.

## Properties

See the base [page:LineSegments] class for common properties.

### <br/> Camera camera; <br/>

The camera being visualized.

### <br/> Object pointMap; <br/>

This contains the points used to visualize the camera.

### <br/> Object matrix; <br/>

Reference to the [page:Object3D.matrixWorld camera.matrixWorld].

### <br/> Object matrixAutoUpdate; <br/>

See [page:Object3D.matrixAutoUpdate]. Set to `false` here as the helper is
using the camera's [page:Object3D.matrixWorld matrixWorld].

## Methods

See the base [page:LineSegments] class for common methods.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### <br/> function setColors( frustum: Color, cone: Color, up: Color, target:
Color, cross: Color ): setColors; <br/>

Defines the colors of the helper.

### [method:undefined update]()

Updates the helper based on the projectionMatrix of the camera.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

