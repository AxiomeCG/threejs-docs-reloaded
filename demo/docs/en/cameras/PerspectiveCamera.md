[Object3D](en\core\Object3D.html) → [Camera](en\cameras\Camera.html) →

# PerspectiveCamera

Camera that uses <a
href="https://en.wikipedia.org/wiki/Perspective_(graphical)">perspective
projection</a>.  
  
This projection mode is designed to mimic the way the human eye sees. It is
the most common projection mode used for rendering a 3D scene.

## Code Example

  
```ts  
const camera = new THREE.PerspectiveCamera( 45, width / height, 1, 1000 );
scene.add( camera );  
```  

## Examples

[example:webgl_animation_skinning_blending animation / skinning / blending]  
[example:webgl_animation_skinning_morph animation / skinning / morph ]  
[example:webgl_effects_stereo effects / stereo ]  
[example:webgl_interactive_cubes interactive / cubes ]  
[example:webgl_loader_collada_skinning loader / collada / skinning ]

## Constructor

### PerspectiveCamera

  
  
```ts  
function PerspectiveCamera( fov: Number, aspect: Number, near: Number, far:
Number ): void;  
```  

fov — Camera frustum vertical field of view.  
aspect — Camera frustum aspect ratio.  
near — Camera frustum near plane.  
far — Camera frustum far plane.  
  
Together these define the camera's <a
href="https://en.wikipedia.org/wiki/Viewing_frustum">viewing frustum</a>.

## Properties

See the base [Camera](en\cameras\Camera.html) class for common properties.  
Note that after making changes to most of these properties you will have to
call [.updateProjectionMatrix](#) for the changes to take effect.

### aspect

  
  
```ts  
aspect: Float;  
```  

Camera frustum aspect ratio, usually the canvas width / canvas height. Default
is `1` (square canvas).

### far

  
  
```ts  
far: Float;  
```  

Camera frustum far plane. Default is `2000`.  
  
Must be greater than the current value of [.near](#near) plane.

### filmGauge

  
  
```ts  
filmGauge: Float;  
```  

Film size used for the larger axis. Default is `35` (millimeters). This
parameter does not influence the projection matrix unless .filmOffset is set
to a nonzero value.

### filmOffset

  
  
```ts  
filmOffset: Float;  
```  

Horizontal off-center offset in the same unit as `.filmGauge`. Default is `0`.

### focus

  
  
```ts  
focus: Float;  
```  

Object distance used for stereoscopy and depth-of-field effects. This
parameter does not influence the projection matrix unless a
[StereoCamera](en\cameras\StereoCamera.html) is being used. Default is `10`.

### fov

  
  
```ts  
fov: Float;  
```  

Camera frustum vertical field of view, from bottom to top of view, in degrees.
Default is `50`.

### isPerspectiveCamera

  
  
```ts  
isPerspectiveCamera: Boolean;  
```  

Read-only flag to check if a given object is of type PerspectiveCamera.

### near

  
  
```ts  
near: Float;  
```  

Camera frustum near plane. Default is `0.1`.  
  
The valid range is greater than `0` and less than the current value of the
[.far](#far) plane. Note that, unlike for the
[OrthographicCamera](en\cameras\OrthographicCamera.html), `0` is _not_ a valid
value for a PerspectiveCamera's near plane.

### view

  
  
```ts  
view: Object;  
```  

Frustum window specification or null. This is set using the
[.setViewOffset](#) method and cleared using [.clearViewOffset](#).

### zoom

  
  
```ts  
zoom: number;  
```  

Gets or sets the zoom factor of the camera. Default is `1`.

## Methods

See the base [Camera](en\cameras\Camera.html) class for common methods.

### clearViewOffset

  
  
```ts  
function clearViewOffset( ): undefined;  
```  

Removes any offset set by the [.setViewOffset](#) method.

### getEffectiveFOV

  
  
```ts  
function getEffectiveFOV( ): Float;  
```  

Returns the current vertical field of view angle in degrees considering .zoom.

### getFilmHeight

  
  
```ts  
function getFilmHeight( ): Float;  
```  

Returns the height of the image on the film. If .aspect is less than or equal
to one (portrait format), the result equals .filmGauge.

### getFilmWidth

  
  
```ts  
function getFilmWidth( ): Float;  
```  

Returns the width of the image on the film. If .aspect is greater than or
equal to one (landscape format), the result equals .filmGauge.

### getFocalLength

  
  
```ts  
function getFocalLength( ): Float;  
```  

Returns the focal length of the current .fov in respect to .filmGauge.

### setFocalLength

  
  
```ts  
function setFocalLength( focalLength: Float ): undefined;  
```  

Sets the FOV by focal length in respect to the current [.filmGauge](#).  
  
By default, the focal length is specified for a 35mm (full frame) camera.

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

Sets an offset in a larger frustum. This is useful for multi-window or multi-
monitor/multi-machine setups.

For example, if you have 3x2 monitors and each monitor is 1920x1080 and the
monitors are in grid like this:  

    
    
    +---+---+---+| A | B | C |+---+---+---+| D | E | F |+---+---+---+

then for each monitor you would call it like this:  
  
```ts  
const w = 1920;const h = 1080;const fullWidth = w * 3;const fullHeight = h *
2;// Acamera.setViewOffset( fullWidth, fullHeight, w * 0, h * 0, w, h );//
Bcamera.setViewOffset( fullWidth, fullHeight, w * 1, h * 0, w, h );//
Ccamera.setViewOffset( fullWidth, fullHeight, w * 2, h * 0, w, h );//
Dcamera.setViewOffset( fullWidth, fullHeight, w * 0, h * 1, w, h );//
Ecamera.setViewOffset( fullWidth, fullHeight, w * 1, h * 1, w, h );//
Fcamera.setViewOffset( fullWidth, fullHeight, w * 2, h * 1, w, h );  
```  

Note there is no reason monitors have to be the same size or in a grid.

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
href="https://github.com/mrdoob/three.js/blob/master/src/cameras/PerspectiveCamera.js">src/cameras/PerspectiveCamera.js</a>

