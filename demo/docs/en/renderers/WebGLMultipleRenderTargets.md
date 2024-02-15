[WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) →

# WebGLMultipleRenderTargets

A special render target that enables a fragment shader to write to several
textures. This approach is useful for advanced rendering techniques like post-
processing or deferred rendering. Heads up: WebGLMultipleRenderTargets can
only be used with a WebGL 2 rendering context.

## Examples

[example:webgl2_multiple_rendertargets webgl2 / multiple / rendertargets ]

## Constructor

### WebGLMultipleRenderTargets

  
  
```ts  
function WebGLMultipleRenderTargets( width: Number, height: Number, count:
Number, options: Object ): void;  
```  

[width](#) - The width of the render target. Default is `1`.  
[height](#) - The height of the render target. Default is `1`.  
[count](#) - The number of render targets. Default is `1`.  
options - (optional object that holds texture parameters for an auto-generated
target texture and depthBuffer/stencilBuffer booleans. For an explanation of
the texture parameters see [Texture](en\textures\Texture.html). For a list of
valid options, see [WebGLRenderTarget](en\renderers\WebGLRenderTarget.html)).  
  

## Properties

### isWebGLMultipleRenderTargets

  
  
```ts  
isWebGLMultipleRenderTargets: Boolean;  
```  

Read-only flag to check if a given object is of type
WebGLMultipleRenderTargets.

### texture

  
  
```ts  
texture: Array;  
```  

The texture property is overwritten in WebGLMultipleRenderTargets and replaced
with an array. This array holds the [texture](#) references of the respective
render targets.

[WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) properties are
available on this class.

## Methods

[WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) methods are available
on this class.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/WebGLMultipleRenderTargets.js">src/renderers/WebGLMultipleRenderTargets.js</a>

