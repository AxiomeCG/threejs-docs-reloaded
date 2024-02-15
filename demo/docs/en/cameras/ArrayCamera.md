[Object3D](en\core\Object3D.html) → [Camera](en\cameras\Camera.html) →
[PerspectiveCamera](en\cameras\PerspectiveCamera.html) →

# ArrayCamera

ArrayCamera can be used in order to efficiently render a scene with a
predefined set of cameras. This is an important performance aspect for
rendering VR scenes.  
An instance of ArrayCamera always has an array of sub cameras. It's mandatory
to define for each sub camera the `viewport` property which determines the
part of the viewport that is rendered with this camera.

## Examples

[example:webgl_camera_array camera / array ]

## Constructor

### ArrayCamera

  
  
```ts  
function ArrayCamera( array: Array ): void;  
```  

An array of cameras.

## Properties

See the base [PerspectiveCamera](en\cameras\PerspectiveCamera.html) class for
common properties.

### cameras

  
  
```ts  
cameras: Array;  
```  

An array of cameras.

### isArrayCamera

  
  
```ts  
isArrayCamera: Boolean;  
```  

Read-only flag to check if a given object is of type ArrayCamera.

## Methods

See the base [PerspectiveCamera](en\cameras\PerspectiveCamera.html) class for
common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/cameras/ArrayCamera.js">src/cameras/ArrayCamera.js</a>

