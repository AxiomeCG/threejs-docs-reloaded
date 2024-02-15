[WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) →

# WebGLArrayRenderTarget

This type of render target represents an array of textures.

## Examples

[example:webgl2_rendertarget_texture2darray WebGL 2 / render target / array]  

## Constructor

### WebGLArrayRenderTarget

  
  
```ts  
function WebGLArrayRenderTarget( width: Number, height: Number, depth: Number
): void;  
```  

[width](#) - the width of the render target, in pixels. Default is `1`.  
[height](#) - the height of the render target, in pixels. Default is `1`.  
[depth](#) - the depth/layer count of the render target. Default is `1`.  
  
Creates a new WebGLArrayRenderTarget.

## Properties

### See [WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) for inherited
properties

### depth

  
  
```ts  
depth: number;  
```  

The depth of the render target.

### texture

  
  
```ts  
texture: DataArrayTexture;  
```  

The texture property is overwritten with an instance of
[DataArrayTexture](en\textures\DataArrayTexture.html).

## Methods

### See [WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) for inherited
methods

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/WebGLArrayRenderTarget.js">src/renderers/WebGLArrayRenderTarget.js</a>

