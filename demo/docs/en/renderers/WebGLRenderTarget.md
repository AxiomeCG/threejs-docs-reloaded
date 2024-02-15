# WebGLRenderTarget

A <a href="https://webglfundamentals.org/webgl/lessons/webgl-render-to-
texture.html">render target</a> is a buffer where the video card draws pixels
for a scene that is being rendered in the background. It is used in different
effects, such as applying postprocessing to a rendered image before displaying
it on the screen.

## Constructor

### WebGLRenderTarget

  
  
```ts  
function WebGLRenderTarget( width: Number, height: Number, options: Object ):
void;  
```  

[width](#) - The width of the renderTarget. Default is `1`.  
[height](#) - The height of the renderTarget. Default is `1`.  
options - optional object that holds texture parameters for an auto-generated
target texture and depthBuffer/stencilBuffer booleans. For an explanation of
the texture parameters see [Texture](en\textures\Texture.html). The following
are valid options:  
  
[wrapS](#) - default is [ClampToEdgeWrapping](en\constants\Textures.html).  
[wrapT](#) - default is [ClampToEdgeWrapping](en\constants\Textures.html).  
[magFilter](#) - default is [LinearFilter](en\constants\Textures.html).  
[minFilter](#) - default is [LinearFilter](en\constants\Textures.html).  
[generateMipmaps](#) - default is `false`.  
[format](#) - default is [RGBAFormat](en\constants\Textures.html).  
[type](#) - default is [UnsignedByteType](en\constants\Textures.html).  
[anisotropy](#) - default is `1`. See [Texture.anisotropy](#)  
[colorSpace](#) - default is [NoColorSpace](en\constants\Textures.html).  
[depthBuffer](#) - default is `true`.  
[stencilBuffer](#) - default is `false`.  
[samples](#) - default is `0`.  
  
Creates a new WebGLRenderTarget

## Properties

### isWebGLRenderTarget

  
  
```ts  
isWebGLRenderTarget: Boolean;  
```  

Read-only flag to check if a given object is of type WebGLRenderTarget.

### width

  
  
```ts  
width: number;  
```  

The width of the render target.

### height

  
  
```ts  
height: number;  
```  

The height of the render target.

### scissor

  
  
```ts  
scissor: Vector4;  
```  

A rectangular area inside the render target's viewport. Fragments that are
outside the area will be discarded.

### scissorTest

  
  
```ts  
scissorTest: Boolean;  
```  

Indicates whether the scissor test is active or not.

### viewport

  
  
```ts  
viewport: Vector4;  
```  

The viewport of this render target.

### texture

  
  
```ts  
texture: Texture;  
```  

This texture instance holds the rendered pixels. Use it as input for further
processing.

### depthBuffer

  
  
```ts  
depthBuffer: Boolean;  
```  

Renders to the depth buffer. Default is true.

### stencilBuffer

  
  
```ts  
stencilBuffer: Boolean;  
```  

Renders to the stencil buffer. Default is false.

### depthTexture

  
  
```ts  
depthTexture: DepthTexture;  
```  

If set, the scene depth will be rendered to this texture. Default is null.

### samples

  
  
```ts  
samples: Number;  
```  

Defines the count of MSAA samples. Can only be used with WebGL 2. Default is
`0`.

## Methods

### setSize

  
  
```ts  
function setSize( width: Number, height: Number ): undefined;  
```  

Sets the size of the render target.

### clone

  
  
```ts  
function clone( ): WebGLRenderTarget;  
```  

Creates a copy of this render target.

### copy

  
  
```ts  
function copy( source: WebGLRenderTarget ): this;  
```  

Adopts the settings of the given render target.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

[EventDispatcher](en\core\EventDispatcher.html) methods are available on this
class.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/WebGLRenderTarget.js">src/renderers/WebGLRenderTarget.js</a>

