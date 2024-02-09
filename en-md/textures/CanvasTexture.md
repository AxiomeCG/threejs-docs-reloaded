[page:Texture] →

# [name]

Creates a texture from a canvas element.  
  
This is almost the same as the base [page:Texture Texture] class, except that
it sets [page:Texture.needsUpdate needsUpdate] to `true` immediately.

## Constructor

###  [name]( [param:HTMLElement canvas], [param:Constant mapping],
[param:Constant wrapS], [param:Constant wrapT], [param:Constant magFilter],
[param:Constant minFilter], [param:Constant format], [param:Constant type],
[param:Number anisotropy] )

[page:HTMLElement canvas] -- The HTML canvas element from which to load the
texture.  
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
[page:Constant format] -- The format used in the texture. See [page:Textures
format constants] for other choices.  
[page:Constant type] -- Default is [page:Textures THREE.UnsignedByteType]. See
[page:Textures type constants] for other choices.  
[page:Number anisotropy] -- The number of samples taken along the axis through
the pixel that has the highest density of texels. By default, this value is
`1`. A higher value gives a less blurry result than a basic mipmap, at the
cost of more texture samples being used. Use
[page:WebGLrenderer.getMaxAnisotropy renderer.getMaxAnisotropy]() to find the
maximum valid anisotropy value for the GPU; this value is usually a power of
2.  
  

## Properties

See the base [page:Texture Texture] class for common properties.

### <br/> Boolean isCanvasTexture; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Boolean needsUpdate; <br/>

True by default. This is required so that the canvas data is loaded.

## Methods

See the base [page:Texture Texture] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

