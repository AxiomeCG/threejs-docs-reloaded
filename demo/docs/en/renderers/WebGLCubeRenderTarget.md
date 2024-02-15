[WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) →

# WebGLCubeRenderTarget

Used by the [CubeCamera](en\cameras\CubeCamera.html) as its
[WebGLRenderTarget](en\renderers\WebGLRenderTarget.html).

## Examples

See [CubeCamera](en\cameras\CubeCamera.html) for examples.

## Constructor

### WebGLCubeRenderTarget

  
  
```ts  
function WebGLCubeRenderTarget( size: Number, options: Object ): void;  
```  

[size](#) - the size, in pixels. Default is `1`.  
options - (optional) object that holds texture parameters for an auto-
generated target texture and depthBuffer/stencilBuffer booleans. For an
explanation of the texture parameters see [Texture](en\textures\Texture.html).
The following are valid options:  
  
[wrapS](#) - default is [ClampToEdgeWrapping](en\constants\Textures.html).  
[wrapT](#) - default is [ClampToEdgeWrapping](en\constants\Textures.html).  
[magFilter](#) - default is [.LinearFilter](en\constants\Textures.html).  
[minFilter](#) - default is [LinearFilter](en\constants\Textures.html).  
[generateMipmaps](#) - default is `false`.  
[format](#) - default is [RGBAFormat](en\constants\Textures.html).  
[type](#) - default is [UnsignedByteType](en\constants\Textures.html).  
[anisotropy](#) - default is `1`. See [Texture.anisotropy](#)  
[colorSpace](#) - default is [NoColorSpace](en\constants\Textures.html).  
[depthBuffer](#) - default is `true`.  
[stencilBuffer](#) - default is `false`.  
  
Creates a new WebGLCubeRenderTarget

## Properties

### See [WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) for inherited
properties

## Methods

### See [WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) for inherited
methods

### fromEquirectangularTexture

  
  
```ts  
function fromEquirectangularTexture( renderer: WebGLRenderer, texture: Texture
): this;  
```  

[renderer](en\renderers\WebGLRenderer.html) — the renderer.  
[texture](en\textures\Texture.html) — the equirectangular texture.

Use this method if you want to convert an equirectangular panorama to the
cubemap format.

### clear

  
  
```ts  
function clear( renderer: WebGLRenderer, color: Boolean, depth: Boolean,
stencil: Boolean ): undefined;  
```  

Call this to clear the renderTarget's color, depth, and/or stencil buffers.
The color buffer is set to the renderer's current clear color. Arguments
default to `true`.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/WebGLCubeRenderTarget.js">src/renderers/WebGLCubeRenderTarget.js</a>

