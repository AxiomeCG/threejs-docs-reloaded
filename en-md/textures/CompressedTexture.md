[page:Texture] →

# [name]

Creates a texture based on data in compressed form, for example from a
[link:https://en.wikipedia.org/wiki/DirectDraw_Surface DDS] file.  
  
For use with the [page:CompressedTextureLoader CompressedTextureLoader].

## Constructor

###  [name]( [param:Array mipmaps], [param:Number width], [param:Number
height], [param:Constant format], [param:Constant type], [param:Constant
mapping], [param:Constant wrapS], [param:Constant wrapT], [param:Constant
magFilter], [param:Constant minFilter], [param:Number anisotropy],
[param:Constant colorSpace] )

[page:Array mipmaps] -- The mipmaps array should contain objects with data,
width and height. The mipmaps should be of the correct format and type.  
[page:Number width] -- The width of the biggest mipmap.  
[page:Number height] -- The height of the biggest mipmap.  
[page:Constant format] -- The format used in the mipmaps. See [page:Textures
ST3C Compressed Texture Formats], [page:Textures PVRTC Compressed Texture
Formats] and [page:Textures ETC Compressed Texture Format] for other choices.  
[page:Constant type] -- Default is [page:Textures THREE.UnsignedByteType]. See
[page:Textures type constants] for other choices.  
[page:Constant mapping] -- How the image is applied to the object. An object
type of [page:Textures THREE.UVMapping]. See [page:Textures mapping constants]
for other choices.  
[page:Constant wrapS] -- The default is [page:Textures
THREE.ClampToEdgeWrapping]. See [page:Textures wrap mode constants] for other
choices.  
[page:Constant wrapT] -- The default is [page:Textures
THREE.ClampToEdgeWrapping]. See [page:Textures wrap mode constants] for other
choices.  
[page:Constant magFilter] -- How the texture is sampled when a texel covers
more than one pixel. The default is [page:Textures THREE.LinearFilter]. See
[page:Textures magnification filter constants] for other choices.  
[page:Constant minFilter] -- How the texture is sampled when a texel covers
less than one pixel. The default is [page:Textures
THREE.LinearMipmapLinearFilter]. See [page:Textures minification filter
constants] for other choices.  
[page:Number anisotropy] -- The number of samples taken along the axis through
the pixel that has the highest density of texels. By default, this value is
`1`. A higher value gives a less blurry result than a basic mipmap, at the
cost of more texture samples being used. Use renderer.getMaxAnisotropy() to
find the maximum valid anisotropy value for the GPU; this value is usually a
power of 2.  
[page:Constant colorSpace] -- The default is [page:Textures
THREE.NoColorSpace]. See [page:Textures color space constants] for other
choices.  
  

## Properties

See the base [page:Texture Texture] class for common properties.

### <br/> Boolean flipY; <br/>

False by default. Flipping textures does not work for compressed textures.

### <br/> Boolean generateMipmaps; <br/>

False by default. Mipmaps can't be generated for compressed textures

### <br/> Object image; <br/>

Overridden with a object containing width and height.

### <br/> Boolean isCompressedTexture; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

See the base [page:Texture Texture] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]
