[page:Material] →

# [name]

A material for drawing geometry by depth. Depth is based off of the camera
near and far plane. White is nearest, black is farthest.

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.

## Properties

See the base [page:Material] class for common properties.

### <br/> Texture alphaMap; <br/>

The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Default is null.  
  
Only the color of the texture is used, ignoring the alpha channel if one
exists. For RGB and RGBA textures, the [page:WebGLRenderer WebGL] renderer
will use the green channel when sampling this texture due to the extra bit of
precision provided for green in DXT-compressed and uncompressed RGB 565
formats. Luminance-only and luminance/alpha textures will also still work as
expected.

### <br/> Constant depthPacking; <br/>

Type for depth packing. Default is [page:Textures BasicDepthPacking].

### <br/> Texture displacementMap; <br/>

The displacement map affects the position of the mesh's vertices. Unlike other
maps which only affect the light and shade of the material the displaced
vertices can cast shadows, block other objects, and otherwise act as real
geometry. The displacement texture is an image where the value of each pixel
(white being the highest) is mapped against, and repositions, the vertices of
the mesh.

### <br/> Float displacementScale; <br/>

How much the displacement map affects the mesh (where black is no
displacement, and white is maximum displacement). Without a displacement map
set, this value is not applied. Default is `1`.

### <br/> Float displacementBias; <br/>

The offset of the displacement map's values on the mesh's vertices. Without a
displacement map set, this value is not applied. Default is `0`.

### <br/> Boolean fog; <br/>

Whether the material is affected by fog. Default is `false`.

### <br/> Texture map; <br/>

The color map. May optionally include an alpha channel, typically combined
with [page:Material.transparent .transparent] or [page:Material.alphaTest
.alphaTest]. Default is null.

### <br/> Boolean wireframe; <br/>

Render geometry as wireframe. Default is false (i.e. render as smooth shaded).

### <br/> Float wireframeLinewidth; <br/>

Controls wireframe thickness. Default is `1`.  
  
Due to limitations of the
[link:https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf
OpenGL Core Profile] with the [page:WebGLRenderer WebGL] renderer on most
platforms linewidth will always be `1` regardless of the set value.

## Methods

See the base [page:Material] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]
