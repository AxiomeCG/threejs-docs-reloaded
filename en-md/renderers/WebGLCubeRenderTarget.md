[page:WebGLRenderTarget] →

# WebGLCubeRenderTarget

Used by the [page:CubeCamera] as its [page:WebGLRenderTarget].

## Examples

See [page:CubeCamera] for examples.

## Constructor

###  function WebGLCubeRenderTarget( size: Number, options: Object ): void;

[page:Float size] - the size, in pixels. Default is `1`.  
options - (optional) object that holds texture parameters for an auto-
generated target texture and depthBuffer/stencilBuffer booleans. For an
explanation of the texture parameters see [page:Texture Texture]. The
following are valid options:  
  
[page:Constant wrapS] - default is [page:Textures ClampToEdgeWrapping].  
[page:Constant wrapT] - default is [page:Textures ClampToEdgeWrapping].  
[page:Constant magFilter] - default is [page:Textures .LinearFilter].  
[page:Constant minFilter] - default is [page:Textures LinearFilter].  
[page:Boolean generateMipmaps] - default is `false`.  
[page:Constant format] - default is [page:Textures RGBAFormat].  
[page:Constant type] - default is [page:Textures UnsignedByteType].  
[page:Number anisotropy] - default is `1`. See [page:Texture.anisotropy]  
[page:Constant colorSpace] - default is [page:Textures NoColorSpace].  
[page:Boolean depthBuffer] - default is `true`.  
[page:Boolean stencilBuffer] - default is `false`.  
  
Creates a new WebGLCubeRenderTarget

## Properties

### See [page:WebGLRenderTarget] for inherited properties

## Methods

### See [page:WebGLRenderTarget] for inherited methods

###  function fromEquirectangularTexture( renderer: WebGLRenderer, texture:
Texture ): this;

[page:WebGLRenderer renderer] — the renderer.  
[page:Texture texture] — the equirectangular texture.

Use this method if you want to convert an equirectangular panorama to the
cubemap format.

###  function clear( renderer: WebGLRenderer, color: Boolean, depth: Boolean,
stencil: Boolean ): undefined;

Call this to clear the renderTarget's color, depth, and/or stencil buffers.
The color buffer is set to the renderer's current clear color. Arguments
default to `true`.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

