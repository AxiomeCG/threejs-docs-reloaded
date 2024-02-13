# StereoCamera

Dual [page:PerspectiveCamera PerspectiveCamera]s used for effects such as
[link:https://en.wikipedia.org/wiki/Anaglyph_3D 3D Anaglyph] or
[link:https://en.wikipedia.org/wiki/parallax_barrier Parallax Barrier].

## Examples

[example:webgl_effects_anaglyph effects / anaglyph ]  
[example:webgl_effects_parallaxbarrier effects / parallaxbarrier ]  
[example:webgl_effects_stereo effects / stereo ]

## Constructor

###  function StereoCamera( ): void;

## Properties

###  Float aspect;

Default is `1`.

###  Float eyeSep;

Default is `0.064`.

###  PerspectiveCamera cameraL;

Left camera. This is added to [page:Layers layer 1] - objects to be rendered
by the left camera must also be added to this layer.

###  PerspectiveCamera cameraR;

Right camera.This is added to [page:Layers layer 2] - objects to be rendered
by the right camera must also be added to this layer.

## Methods

###  function update( camera: PerspectiveCamera ): undefined;

Update the stereo cameras based on the camera passed in.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

