[Object3D](en\core\Object3D.html) → [Camera](en\cameras\Camera.html) →

# OrthographicCamera

Camera that uses <a
href="https://en.wikipedia.org/wiki/Orthographic_projection">orthographic
projection</a>.  
  
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

### OrthographicCamera

  
  
```ts  
function OrthographicCamera( left: Number, right: Number, top: Number, bottom:
Number, near: Number, far: Number ): void;  
```  

left — Camera frustum left plane.  
right — Camera frustum right plane.  
top — Camera frustum top plane.  
bottom — Camera frustum bottom plane.  
near — Camera frustum near plane.  
far — Camera frustum far plane.  
  
Together these define the camera's <a
href="https://en.wikipedia.org/wiki/Viewing_frustum">viewing frustum</a>.

## Properties

See the base [Camera](en\cameras\Camera.html) class for common properties.  
Note that after making changes to most of these properties you will have to
call [.updateProjectionMatrix](#) for the changes to take effect.

### bottom

  
  
```ts  
bottom: Float;  
```  

Camera frustum bottom plane.

### far

  
  
```ts  
far: Float;  
```  

Camera frustum far plane. Default is `2000`.  
  
Must be greater than the current value of [.near](#near) plane.

### isOrthographicCamera

  
  
```ts  
isOrthographicCamera: Boolean;  
```  

Read-only flag to check if a given object is of type OrthographicCamera.

### left

  
  
```ts  
left: Float;  
```  

Camera frustum left plane.

### near

  
  
```ts  
near: Float;  
```  

Camera frustum near plane. Default is `0.1`.  
  
The valid range is between `0` and the current value of the [.far](#far)
plane. Note that, unlike for the
[PerspectiveCamera](en\cameras\PerspectiveCamera.html), `0` is a valid value
for an OrthographicCamera's near plane.

### right

  
  
```ts  
right: Float;  
```  

Camera frustum right plane.

### top

  
  
```ts  
top: Float;  
```  

Camera frustum top plane.

### view

  
  
```ts  
view: Object;  
```  

Set by [setViewOffset](#). Default is `null`.

### zoom

  
  
```ts  
zoom: number;  
```  

Gets or sets the zoom factor of the camera. Default is `1`.

## Methods

See the base [Camera](en\cameras\Camera.html) class for common methods.

### setViewOffset

  
  
```ts  
function setViewOffset( fullWidth: Float, fullHeight: Float, x: Float, y:
Float, width: Float, height: Float ): undefined;  
```  

fullWidth — full width of multiview setup  
fullHeight — full height of multiview setup  
x — horizontal offset of subcamera  
y — vertical offset of subcamera  
width — width of subcamera  
height — height of subcamera  
  
Sets an offset in a larger <a
href="https://en.wikipedia.org/wiki/Viewing_frustum">viewing frustum</a>. This
is useful for multi-window or multi-monitor/multi-machine setups. For an
example on how to use it see [PerspectiveCamera](#).

### clearViewOffset

  
  
```ts  
function clearViewOffset( ): undefined;  
```  

Removes any offset set by the .setViewOffset method.

### updateProjectionMatrix

  
  
```ts  
function updateProjectionMatrix( ): undefined;  
```  

Updates the camera projection matrix. Must be called after any change of
parameters.

### toJSON

  
  
```ts  
function toJSON( meta: Object ): Object;  
```  

meta -- object containing metadata such as textures or images in objects'
descendants.  
Convert the camera to three.js <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/cameras/OrthographicCamera.js">src/cameras/OrthographicCamera.js</a>

