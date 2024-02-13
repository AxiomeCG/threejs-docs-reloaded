[page:Object3D] → [page:Camera] →

# OrthographicCamera

Camera that uses [link:https://en.wikipedia.org/wiki/Orthographic_projection
orthographic projection].  
  
In this projection mode, an object's size in the rendered image stays constant
regardless of its distance from the camera.  
  
This can be useful for rendering 2D scenes and UI elements, amongst other
things.

## Code Example

  
```ts  
const camera = new THREE.OrthographicCamera( width / - 2, width / 2, height /
2, height / - 2, 1, 1000 ); scene.add( camera );  
```  

## Examples

[example:webgl_camera camera ]  
[example:webgl_interactive_cubes_ortho interactive / cubes / ortho ]  
[example:webgl_materials_cubemap_dynamic materials / cubemap / dynamic]  
[example:webgl_postprocessing_advanced postprocessing / advanced ]  
[example:webgl_postprocessing_dof2 postprocessing / dof2 ]  
[example:webgl_postprocessing_godrays postprocessing / godrays ]  
[example:webgl_rtt rtt ]  
[example:webgl_shadowmap shadowmap ]

## Constructor

###  function OrthographicCamera( left: Number, right: Number, top: Number,
bottom: Number, near: Number, far: Number ): void;

left — Camera frustum left plane.  
right — Camera frustum right plane.  
top — Camera frustum top plane.  
bottom — Camera frustum bottom plane.  
near — Camera frustum near plane.  
far — Camera frustum far plane.  
  
Together these define the camera's
[link:https://en.wikipedia.org/wiki/Viewing_frustum viewing frustum].

## Properties

See the base [page:Camera] class for common properties.  
Note that after making changes to most of these properties you will have to
call [page:OrthographicCamera.updateProjectionMatrix .updateProjectionMatrix]
for the changes to take effect.

###  Float bottom;

Camera frustum bottom plane.

###  Float far;

Camera frustum far plane. Default is `2000`.  
  
Must be greater than the current value of [page:.near near] plane.

###  Boolean isOrthographicCamera;

Read-only flag to check if a given object is of type OrthographicCamera.

###  Float left;

Camera frustum left plane.

###  Float near;

Camera frustum near plane. Default is `0.1`.  
  
The valid range is between `0` and the current value of the [page:.far far]
plane. Note that, unlike for the [page:PerspectiveCamera], `0` is a valid
value for an OrthographicCamera's near plane.

###  Float right;

Camera frustum right plane.

###  Float top;

Camera frustum top plane.

###  Object view;

Set by [page:OrthographicCamera.setViewOffset setViewOffset]. Default is
`null`.

###  number zoom;

Gets or sets the zoom factor of the camera. Default is `1`.

## Methods

See the base [page:Camera] class for common methods.

###  function setViewOffset( fullWidth: Float, fullHeight: Float, x: Float, y:
Float, width: Float, height: Float ): undefined;

fullWidth — full width of multiview setup  
fullHeight — full height of multiview setup  
x — horizontal offset of subcamera  
y — vertical offset of subcamera  
width — width of subcamera  
height — height of subcamera  
  
Sets an offset in a larger [link:https://en.wikipedia.org/wiki/Viewing_frustum
viewing frustum]. This is useful for multi-window or multi-monitor/multi-
machine setups. For an example on how to use it see
[page:PerspectiveCamera.setViewOffset PerspectiveCamera].

###  function clearViewOffset( ): undefined;

Removes any offset set by the .setViewOffset method.

###  function updateProjectionMatrix( ): undefined;

Updates the camera projection matrix. Must be called after any change of
parameters.

###  function toJSON( meta: Object ): Object;

meta -- object containing metadata such as textures or images in objects'
descendants.  
Convert the camera to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

