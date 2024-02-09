[page:WebGLRenderTarget] →

# [name]

This type of render target represents an array of textures.

## Examples

[example:webgl2_rendertarget_texture2darray WebGL 2 / render target / array]  

## Constructor

###  [name]( [param:Number width], [param:Number height], [param:Number depth]
)

[page:Number width] - the width of the render target, in pixels. Default is
`1`.  
[page:Number height] - the height of the render target, in pixels. Default is
`1`.  
[page:Number depth] - the depth/layer count of the render target. Default is
`1`.  
  
Creates a new [name].

## Properties

### See [page:WebGLRenderTarget] for inherited properties

### <br/> number depth; <br/>

The depth of the render target.

### <br/> DataArrayTexture texture; <br/>

The texture property is overwritten with an instance of
[page:DataArrayTexture].

## Methods

### See [page:WebGLRenderTarget] for inherited methods

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

