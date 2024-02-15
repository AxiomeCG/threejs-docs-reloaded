[Texture](en\textures\Texture.html) →

# FramebufferTexture

This class can only be used in combination with
[WebGLRenderer.copyFramebufferToTexture](#)().

  
```ts  
const pixelRatio = window.devicePixelRatio;const textureSize = 128 *
pixelRatio;// instantiate a framebuffer textureconst frameTexture = new
FramebufferTexture( textureSize, textureSize );// calculate start position for
copying part of the frame dataconst vector = new Vector2();vector.x = (
window.innerWidth * pixelRatio / 2 ) - ( textureSize / 2 );vector.y = (
window.innerHeight * pixelRatio / 2 ) - ( textureSize / 2 );// render the
scenerenderer.clear();renderer.render( scene, camera );// copy part of the
rendered frame into the framebuffer texturerenderer.copyFramebufferToTexture(
vector, frameTexture );  
```  

## Examples

[example:webgl_framebuffer_texture]

## Constructor

### FramebufferTexture

  
  
```ts  
function FramebufferTexture( width: Number, height: Number ): void;  
```  

[width](#) -- The width of the texture.  
[height](#) -- The height of the texture.

## Properties

See the base [Texture](en\textures\Texture.html) class for common properties.

### generateMipmaps

  
  
```ts  
generateMipmaps: Boolean;  
```  

Whether to generate mipmaps for the FramebufferTexture. Default value is
`false`.

### isFramebufferTexture

  
  
```ts  
isFramebufferTexture: Boolean;  
```  

Read-only flag to check if a given object is of type FramebufferTexture.

### magFilter

  
  
```ts  
magFilter: number;  
```  

How the texture is sampled when a texel covers more than one pixel. The
default is [THREE.NearestFilter](en\constants\Textures.html), which uses the
value of the closest texel.  
  
See [texture constants](en\constants\Textures.html) for details.

### minFilter

  
  
```ts  
minFilter: number;  
```  

How the texture is sampled when a texel covers less than one pixel. The
default is [THREE.NearestFilter](en\constants\Textures.html), which uses the
value of the closest texel.  
  
See [texture constants](en\constants\Textures.html) for details.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

True by default. This is required so that the canvas data is loaded.

## Methods

See the base [Texture](en\textures\Texture.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/FramebufferTexture.js">src/textures/FramebufferTexture.js</a>

