[page:Texture] →

# [name]

This class can be used to automatically save the depth information of a
rendering into a texture. When using a WebGL 1 rendering context, [name]
requires support for the
[link:https://www.khronos.org/registry/webgl/extensions/WEBGL_depth_texture/
WEBGL_depth_texture] extension.

## Examples

[example:webgl_depth_texture depth / texture]

## Constructor

###  [name]( [param:Number width], [param:Number height], [param:Constant
type], [param:Constant mapping], [param:Constant wrapS], [param:Constant
wrapT], [param:Constant magFilter], [param:Constant minFilter], [param:Number
anisotropy], [param:Constant format] )

[page:Number width] -- width of the texture.  
[page:Number height] -- height of the texture.  
[page:Constant type] -- Default is [page:Textures THREE.UnsignedIntType] when
using [page:Textures DepthFormat] and [page:Textures THREE.UnsignedInt248Type]
when using [page:Textures DepthStencilFormat]. See [page:Textures type
constants] for other choices.  
[page:Constant mapping] -- See [page:Textures mapping mode constants] for
details.  
[page:Constant wrapS] -- The default is [page:Textures
THREE.ClampToEdgeWrapping]. See [page:Textures wrap mode constants] for other
choices.  
[page:Constant wrapT] -- The default is [page:Textures
THREE.ClampToEdgeWrapping]. See [page:Textures wrap mode constants] for other
choices.  
[page:Constant magFilter] -- How the texture is sampled when a texel covers
more than one pixel. The default is [page:Textures THREE.NearestFilter]. See
[page:Textures magnification filter constants] for other choices.  
[page:Constant minFilter] -- How the texture is sampled when a texel covers
less than one pixel. The default is [page:Textures THREE.NearestFilter]. See
[page:Textures minification filter constants] for other choices.  
[page:Number anisotropy] -- The number of samples taken along the axis through
the pixel that has the highest density of texels. By default, this value is
`1`. A higher value gives a less blurry result than a basic mipmap, at the
cost of more texture samples being used. Use
[page:WebGLrenderer.getMaxAnisotropy renderer.getMaxAnisotropy]() to find the
maximum valid anisotropy value for the GPU; this value is usually a power of
2.  
[page:Constant format] -- must be either [page:Textures DepthFormat] (default)
or [page:Textures DepthStencilFormat]. See [page:Textures format constants]
for details.  

## Properties

See the base [page:Texture Texture] class for common properties - the
following are also part of the texture class, but have different defaults
here.

### [page:Texture.format format]

Either [page:Textures DepthFormat] (default) or [page:Textures
DepthStencilFormat]. See [page:Textures format constants] for details.  

### [page:Texture.type type]

Default is [page:Textures THREE.UnsignedIntType] when using [page:Textures
DepthFormat] and [page:Textures THREE.UnsignedInt248Type] when using
[page:Textures DepthStencilFormat]. See [page:Textures format constants] for
details.  

### [page:Texture.magFilter magFilter]

How the texture is sampled when a texel covers more than one pixel. The
default is [page:Textures THREE.NearestFilter]. See [page:Textures
magnification filter constants] for other choices.

### [page:Texture.minFilter minFilter]

How the texture is sampled when a texel covers less than one pixel. The
default is [page:Textures THREE.NearestFilter]. See [page:Textures
magnification filter constants] for other choices.

### [page:Texture.flipY flipY]

Depth textures do not need to be flipped so this is `false` by default.

### [page:Texture.generateMipmaps .generateMipmaps]

Depth textures do not use mipmaps.

### <br/> Boolean isDepthTexture; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> number compareFunction; <br/>

This is used to define the comparison function used when comparing texels in
the depth texture to the value in the depth buffer. Default is `null` which
means comparison is disabled.  
  
See the [page:Textures texture constants] page for details of other functions.

## Methods

See the base [page:Texture Texture] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

