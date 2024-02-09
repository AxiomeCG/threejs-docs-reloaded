[page:Object3D] → [page:Camera] → [page:PerspectiveCamera] →

# [name]

[name] can be used in order to efficiently render a scene with a predefined
set of cameras. This is an important performance aspect for rendering VR
scenes.  
An instance of [name] always has an array of sub cameras. It's mandatory to
define for each sub camera the `viewport` property which determines the part
of the viewport that is rendered with this camera.

## Examples

[example:webgl_camera_array camera / array ]

## Constructor

### [name]( [param:Array array] )

An array of cameras.

## Properties

See the base [page:PerspectiveCamera] class for common properties.

### <br/> Array cameras; <br/>

An array of cameras.

### <br/> Boolean isArrayCamera; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

See the base [page:PerspectiveCamera] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

