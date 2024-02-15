# StereoCamera

Dual [PerspectiveCamera](en\cameras\PerspectiveCamera.html)s used for effects
such as <a href="https://en.wikipedia.org/wiki/Anaglyph_3D">3D Anaglyph</a> or
<a href="https://en.wikipedia.org/wiki/parallax_barrier">Parallax Barrier</a>.

## Examples

[example:webgl_effects_anaglyph effects / anaglyph ]  
[example:webgl_effects_parallaxbarrier effects / parallaxbarrier ]  
[example:webgl_effects_stereo effects / stereo ]

## Constructor

### StereoCamera

  
  
```ts  
function StereoCamera( ): void;  
```  

## Properties

### aspect

  
  
```ts  
aspect: Float;  
```  

Default is `1`.

### eyeSep

  
  
```ts  
eyeSep: Float;  
```  

Default is `0.064`.

### cameraL

  
  
```ts  
cameraL: PerspectiveCamera;  
```  

Left camera. This is added to [layer 1](en\core\Layers.html) - objects to be
rendered by the left camera must also be added to this layer.

### cameraR

  
  
```ts  
cameraR: PerspectiveCamera;  
```  

Right camera.This is added to [layer 2](en\core\Layers.html) - objects to be
rendered by the right camera must also be added to this layer.

## Methods

### update

  
  
```ts  
function update( camera: PerspectiveCamera ): undefined;  
```  

Update the stereo cameras based on the camera passed in.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/cameras/StereoCamera.js">src/cameras/StereoCamera.js</a>

