[CompressedTexture](en\textures\CompressedTexture.html) →

# CompressedArrayTexture

Creates an texture 2D array based on data in compressed form, for example from
a <a href="https://en.wikipedia.org/wiki/DirectDraw_Surface">DDS</a> file.  
  
For use with the
[CompressedTextureLoader](en\loaders\CompressedTextureLoader.html).

## Constructor

### CompressedArrayTexture

  
  
```ts  
function CompressedArrayTexture( mipmaps: Array, width: Number, height:
Number, format: Constant, type: Constant ): void;  
```  

[mipmaps](#) -- The mipmaps array should contain objects with data, width and
height. The mipmaps should be of the correct format and type.  
[width](#) -- The width of the biggest mipmap.  
[height](#) -- The height of the biggest mipmap.  
[depth](#) -- The number of layers of the 2D array texture.  
[format](#) -- The format used in the mipmaps. See [ST3C Compressed Texture
Formats](en\constants\Textures.html), [PVRTC Compressed Texture
Formats](en\constants\Textures.html) and [ETC Compressed Texture
Format](en\constants\Textures.html) for other choices.  
[type](#) -- Default is [THREE.UnsignedByteType](en\constants\Textures.html).
See [type constants](en\constants\Textures.html) for other choices.  

## Properties

See the base [CompressedTexture](en\textures\CompressedTexture.html) class for
common properties.

### wrapR

  
  
```ts  
wrapR: number;  
```  

This defines how the texture is wrapped in the depth direction.  
The default is [THREE.ClampToEdgeWrapping](en\constants\Textures.html), where
the edge is clamped to the outer edge texels. The other two choices are
[THREE.RepeatWrapping](en\constants\Textures.html) and
[THREE.MirroredRepeatWrapping](en\constants\Textures.html). See the [texture
constants](en\constants\Textures.html) page for details.

### image

  
  
```ts  
image: Object;  
```  

Overridden with a object containing width, height, and depth.

### isCompressedArrayTexture

  
  
```ts  
isCompressedArrayTexture: Boolean;  
```  

Read-only flag to check if a given object is of type CompressedArrayTexture.

## Methods

See the base [CompressedTexture](en\textures\CompressedTexture.html) class for
common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/CompressedArrayTexture.js">src/textures/CompressedArrayTexture.js</a>

