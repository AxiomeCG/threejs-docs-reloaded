[Texture](en\textures\Texture.html) →

# CompressedTexture

Creates a texture based on data in compressed form, for example from a <a
href="https://en.wikipedia.org/wiki/DirectDraw_Surface">DDS</a> file.  
  
For use with the
[CompressedTextureLoader](en\loaders\CompressedTextureLoader.html).

## Constructor

### CompressedTexture

  
  
```ts  
function CompressedTexture( mipmaps: Array, width: Number, height: Number,
format: Constant, type: Constant, mapping: Constant, wrapS: Constant, wrapT:
Constant, magFilter: Constant, minFilter: Constant, anisotropy: Number,
colorSpace: Constant ): void;  
```  

[mipmaps](#) -- The mipmaps array should contain objects with data, width and
height. The mipmaps should be of the correct format and type.  
[width](#) -- The width of the biggest mipmap.  
[height](#) -- The height of the biggest mipmap.  
[format](#) -- The format used in the mipmaps. See [ST3C Compressed Texture
Formats](en\constants\Textures.html), [PVRTC Compressed Texture
Formats](en\constants\Textures.html) and [ETC Compressed Texture
Format](en\constants\Textures.html) for other choices.  
[type](#) -- Default is [THREE.UnsignedByteType](en\constants\Textures.html).
See [type constants](en\constants\Textures.html) for other choices.  
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
[anisotropy](#) -- The number of samples taken along the axis through the
pixel that has the highest density of texels. By default, this value is `1`. A
higher value gives a less blurry result than a basic mipmap, at the cost of
more texture samples being used. Use renderer.getMaxAnisotropy() to find the
maximum valid anisotropy value for the GPU; this value is usually a power of
2.  
[colorSpace](#) -- The default is
[THREE.NoColorSpace](en\constants\Textures.html). See [color space
constants](en\constants\Textures.html) for other choices.  
  

## Properties

See the base [Texture](en\textures\Texture.html) class for common properties.

### flipY

  
  
```ts  
flipY: Boolean;  
```  

False by default. Flipping textures does not work for compressed textures.

### generateMipmaps

  
  
```ts  
generateMipmaps: Boolean;  
```  

False by default. Mipmaps can't be generated for compressed textures

### image

  
  
```ts  
image: Object;  
```  

Overridden with a object containing width and height.

### isCompressedTexture

  
  
```ts  
isCompressedTexture: Boolean;  
```  

Read-only flag to check if a given object is of type CompressedTexture.

## Methods

See the base [Texture](en\textures\Texture.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/CompressedTexture.js">src/textures/CompressedTexture.js</a>

