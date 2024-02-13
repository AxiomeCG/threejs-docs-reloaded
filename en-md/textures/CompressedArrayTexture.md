[page:CompressedTexture] →

# CompressedArrayTexture

Creates an texture 2D array based on data in compressed form, for example from
a [link:https://en.wikipedia.org/wiki/DirectDraw_Surface DDS] file.  
  
For use with the [page:CompressedTextureLoader CompressedTextureLoader].

## Constructor

###  function CompressedArrayTexture( mipmaps: Array, width: Number, height:
Number, format: Constant, type: Constant ): void;

[page:Array mipmaps] -- The mipmaps array should contain objects with data,
width and height. The mipmaps should be of the correct format and type.  
[page:Number width] -- The width of the biggest mipmap.  
[page:Number height] -- The height of the biggest mipmap.  
[page:Number depth] -- The number of layers of the 2D array texture.  
[page:Constant format] -- The format used in the mipmaps. See [page:Textures
ST3C Compressed Texture Formats], [page:Textures PVRTC Compressed Texture
Formats] and [page:Textures ETC Compressed Texture Format] for other choices.  
[page:Constant type] -- Default is [page:Textures THREE.UnsignedByteType]. See
[page:Textures type constants] for other choices.  

## Properties

See the base [page:CompressedTexture CompressedTexture] class for common
properties.

###  number wrapR;

This defines how the texture is wrapped in the depth direction.  
The default is [page:Textures THREE.ClampToEdgeWrapping], where the edge is
clamped to the outer edge texels. The other two choices are [page:Textures
THREE.RepeatWrapping] and [page:Textures THREE.MirroredRepeatWrapping]. See
the [page:Textures texture constants] page for details.

###  Object image;

Overridden with a object containing width, height, and depth.

###  Boolean isCompressedArrayTexture;

Read-only flag to check if a given object is of type CompressedArrayTexture.

## Methods

See the base [page:CompressedTexture CompressedTexture] class for common
methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

