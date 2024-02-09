[page:Material] →

# [name]

A material that maps the normal vectors to RGB colors.

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.

## Properties

See the base [page:Material] class for common properties.

### <br/> Texture bumpMap; <br/>

The texture to create a bump map. The black and white values map to the
perceived depth in relation to the lights. Bump doesn't actually affect the
geometry of the object, only the lighting. If a normal map is defined this
will be ignored.

### <br/> Float bumpScale; <br/>

How much the bump map affects the material. Typical ranges are 0-1. Default is
`1`.

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

### <br/> Boolean flatShading; <br/>

Define whether the material is rendered with flat shading. Default is false.

### <br/> Boolean fog; <br/>

Whether the material is affected by fog. Default is `false`.

### <br/> Texture normalMap; <br/>

The texture to create a normal map. The RGB values affect the surface normal
for each pixel fragment and change the way the color is lit. Normal maps do
not change the actual shape of the surface, only the lighting. In case the
material has a normal map authored using the left handed convention, the y
component of normalScale should be negated to compensate for the different
handedness.

### <br/> Integer normalMapType; <br/>

The type of normal map.  
  
Options are [page:constant THREE.TangentSpaceNormalMap] (default), and
[page:constant THREE.ObjectSpaceNormalMap].

### <br/> Vector2 normalScale; <br/>

How much the normal map affects the material. Typical ranges are 0-1. Default
is a [page:Vector2] set to (1,1).

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

