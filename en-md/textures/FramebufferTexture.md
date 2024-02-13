[page:Texture] →

# FramebufferTexture

This class can only be used in combination with
[page:WebGLRenderer.copyFramebufferToTexture]().

  
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

###  function FramebufferTexture( width: Number, height: Number ): void;

[page:Number width] -- The width of the texture.  
[page:Number height] -- The height of the texture.

## Properties

See the base [page:Texture Texture] class for common properties.

###  Boolean generateMipmaps;

Whether to generate mipmaps for the FramebufferTexture. Default value is
`false`.

###  Boolean isFramebufferTexture;

Read-only flag to check if a given object is of type FramebufferTexture.

###  number magFilter;

How the texture is sampled when a texel covers more than one pixel. The
default is [page:Textures THREE.NearestFilter], which uses the value of the
closest texel.  
  
See [page:Textures texture constants] for details.

###  number minFilter;

How the texture is sampled when a texel covers less than one pixel. The
default is [page:Textures THREE.NearestFilter], which uses the value of the
closest texel.  
  
See [page:Textures texture constants] for details.

###  Boolean needsUpdate;

True by default. This is required so that the canvas data is loaded.

## Methods

See the base [page:Texture Texture] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

