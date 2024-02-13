[page:WebGLRenderTarget] →

# WebGLMultipleRenderTargets

A special render target that enables a fragment shader to write to several
textures. This approach is useful for advanced rendering techniques like post-
processing or deferred rendering. Heads up: WebGLMultipleRenderTargets can
only be used with a WebGL 2 rendering context.

## Examples

[example:webgl2_multiple_rendertargets webgl2 / multiple / rendertargets ]

## Constructor

###  function WebGLMultipleRenderTargets( width: Number, height: Number,
count: Number, options: Object ): void;

[page:Number width] - The width of the render target. Default is `1`.  
[page:Number height] - The height of the render target. Default is `1`.  
[page:Number count] - The number of render targets. Default is `1`.  
options - (optional object that holds texture parameters for an auto-generated
target texture and depthBuffer/stencilBuffer booleans. For an explanation of
the texture parameters see [page:Texture Texture]. For a list of valid
options, see [page:WebGLRenderTarget WebGLRenderTarget]).  
  

## Properties

###  Boolean isWebGLMultipleRenderTargets;

Read-only flag to check if a given object is of type
WebGLMultipleRenderTargets.

###  Array texture;

The texture property is overwritten in WebGLMultipleRenderTargets and replaced
with an array. This array holds the [page:WebGLRenderTarget.texture texture]
references of the respective render targets.

[page:WebGLRenderTarget WebGLRenderTarget] properties are available on this
class.

## Methods

[page:WebGLRenderTarget WebGLRenderTarget] methods are available on this
class.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

