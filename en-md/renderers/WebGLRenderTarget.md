# WebGLRenderTarget

A [link:https://webglfundamentals.org/webgl/lessons/webgl-render-to-
texture.html render target] is a buffer where the video card draws pixels for
a scene that is being rendered in the background. It is used in different
effects, such as applying postprocessing to a rendered image before displaying
it on the screen.

## Constructor

###  function WebGLRenderTarget( width: Number, height: Number, options:
Object ): void;

[page:Float width] - The width of the renderTarget. Default is `1`.  
[page:Float height] - The height of the renderTarget. Default is `1`.  
options - optional object that holds texture parameters for an auto-generated
target texture and depthBuffer/stencilBuffer booleans. For an explanation of
the texture parameters see [page:Texture Texture]. The following are valid
options:  
  
[page:Constant wrapS] - default is [page:Textures ClampToEdgeWrapping].  
[page:Constant wrapT] - default is [page:Textures ClampToEdgeWrapping].  
[page:Constant magFilter] - default is [page:Textures LinearFilter].  
[page:Constant minFilter] - default is [page:Textures LinearFilter].  
[page:Boolean generateMipmaps] - default is `false`.  
[page:Constant format] - default is [page:Textures RGBAFormat].  
[page:Constant type] - default is [page:Textures UnsignedByteType].  
[page:Number anisotropy] - default is `1`. See [page:Texture.anisotropy]  
[page:Constant colorSpace] - default is [page:Textures NoColorSpace].  
[page:Boolean depthBuffer] - default is `true`.  
[page:Boolean stencilBuffer] - default is `false`.  
[page:Number samples] - default is `0`.  
  
Creates a new WebGLRenderTarget

## Properties

###  Boolean isWebGLRenderTarget;

Read-only flag to check if a given object is of type WebGLRenderTarget.

###  number width;

The width of the render target.

###  number height;

The height of the render target.

###  Vector4 scissor;

A rectangular area inside the render target's viewport. Fragments that are
outside the area will be discarded.

###  Boolean scissorTest;

Indicates whether the scissor test is active or not.

###  Vector4 viewport;

The viewport of this render target.

###  Texture texture;

This texture instance holds the rendered pixels. Use it as input for further
processing.

###  Boolean depthBuffer;

Renders to the depth buffer. Default is true.

###  Boolean stencilBuffer;

Renders to the stencil buffer. Default is false.

###  DepthTexture depthTexture;

If set, the scene depth will be rendered to this texture. Default is null.

###  Number samples;

Defines the count of MSAA samples. Can only be used with WebGL 2. Default is
`0`.

## Methods

###  function setSize( width: Number, height: Number ): undefined;

Sets the size of the render target.

###  function clone( ): WebGLRenderTarget;

Creates a copy of this render target.

###  function copy( source: WebGLRenderTarget ): this;

Adopts the settings of the given render target.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

[page:EventDispatcher EventDispatcher] methods are available on this class.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

