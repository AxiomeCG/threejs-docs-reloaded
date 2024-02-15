[WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) →

# WebGL3DRenderTarget

Represents a three-dimensional render target.

## Constructor

### WebGL3DRenderTarget

  
  
```ts  
function WebGL3DRenderTarget( width: Number, height: Number, depth: Number ):
void;  
```  

[width](#) - the width of the render target, in pixels. Default is `1`.  
[height](#) - the height of the render target, in pixels. Default is `1`.  
[depth](#) - the depth of the render target. Default is `1`.  
  
Creates a new WebGL3DRenderTarget.

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
texture: Data3DTexture;  
```  

The texture property is overwritten with an instance of
[Data3DTexture](en\textures\Data3DTexture.html).

## Methods

### See [WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) for inherited
methods

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/WebGL3DRenderTarget.js">src/renderers/WebGL3DRenderTarget.js</a>

