[page:Object3D] → [page:Camera] → [page:PerspectiveCamera] →

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

###  function ArrayCamera( array: Array ): void;

An array of cameras.

## Properties

See the base [page:PerspectiveCamera] class for common properties.

###  Array cameras;

An array of cameras.

###  Boolean isArrayCamera;

Read-only flag to check if a given object is of type ArrayCamera.

## Methods

See the base [page:PerspectiveCamera] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

