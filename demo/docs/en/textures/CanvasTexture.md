[Texture](en\textures\Texture.html) →

# CanvasTexture

Creates a texture from a canvas element.  
  
This is almost the same as the base [Texture](en\textures\Texture.html) class,
except that it sets [needsUpdate](#) to `true` immediately.

## Constructor

### CanvasTexture

  
  
```ts  
function CanvasTexture( canvas: HTMLElement, mapping: Constant, wrapS:
Constant, wrapT: Constant, magFilter: Constant, minFilter: Constant, format:
Constant, type: Constant, anisotropy: Number ): void;  
```  

[canvas](#) -- The HTML canvas element from which to load the texture.  
[mapping](#) -- How the image is applied to the object. An object type of
[THREE.UVMapping](en\constants\Textures.html). See [mapping
constants](en\constants\Textures.html) for other choices.  
[wrapS](#) -- The default is
[THREE.ClampToEdgeWrapping](en\constants\Textures.html). See [wrap mode
constants](en\constants\Textures.html) for other choices.  
[wrapT](#) -- The default is
[THREE.ClampToEdgeWrapping](en\constants\Textures.html). See [wrap mode
constants](en\constants\Textures.html) for other choices.  
[magFilter](#) -- How the texture is sampled when a texel covers more than one
pixel. The default is [THREE.LinearFilter](en\constants\Textures.html). See
[magnification filter constants](en\constants\Textures.html) for other
choices.  
[minFilter](#) -- How the texture is sampled when a texel covers less than one
pixel. The default is
[THREE.LinearMipmapLinearFilter](en\constants\Textures.html). See
[minification filter constants](en\constants\Textures.html) for other choices.  
[format](#) -- The format used in the texture. See [format
constants](en\constants\Textures.html) for other choices.  
[type](#) -- Default is [THREE.UnsignedByteType](en\constants\Textures.html).
See [type constants](en\constants\Textures.html) for other choices.  
[anisotropy](#) -- The number of samples taken along the axis through the
pixel that has the highest density of texels. By default, this value is `1`. A
higher value gives a less blurry result than a basic mipmap, at the cost of
more texture samples being used. Use [renderer.getMaxAnisotropy](#)() to find
the maximum valid anisotropy value for the GPU; this value is usually a power
of 2.  
  

## Properties

See the base [Texture](en\textures\Texture.html) class for common properties.

### isCanvasTexture

  
  
```ts  
isCanvasTexture: Boolean;  
```  

Read-only flag to check if a given object is of type CanvasTexture.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

True by default. This is required so that the canvas data is loaded.

## Methods

See the base [Texture](en\textures\Texture.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/CanvasTexture.js">src/textures/CanvasTexture.js</a>

