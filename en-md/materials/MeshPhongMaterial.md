[page:Material] →

# [name]

A material for shiny surfaces with specular highlights.  
  
The material uses a non-physically based
[link:https://en.wikipedia.org/wiki/Blinn-Phong_shading_model Blinn-Phong]
model for calculating reflectance. Unlike the Lambertian model used in the
[page:MeshLambertMaterial] this can simulate shiny surfaces with specular
highlights (such as varnished wood). [name] uses per-fragment shading.  
  
Performance will generally be greater when using this material over the
[page:MeshStandardMaterial] or [page:MeshPhysicalMaterial], at the cost of
some graphical accuracy.

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.  
  
The exception is the property [page:Hexadecimal color], which can be passed in
as a hexadecimal string and is `0xffffff` (white) by default.
[page:Color.set]( color ) is called internally.

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

### <br/> Texture aoMap; <br/>

The red channel of this texture is used as the ambient occlusion map. Default
is null. The aoMap requires a second set of UVs.

### <br/> Float aoMapIntensity; <br/>

Intensity of the ambient occlusion effect. Default is `1`. Zero is no
occlusion effect.

### <br/> Texture bumpMap; <br/>

The texture to create a bump map. The black and white values map to the
perceived depth in relation to the lights. Bump doesn't actually affect the
geometry of the object, only the lighting. If a normal map is defined this
will be ignored.

### <br/> Float bumpScale; <br/>

How much the bump map affects the material. Typical ranges are 0-1. Default is
`1`.

### <br/> Color color; <br/>

[page:Color] of the material, by default set to white (0xffffff).

### <br/> Integer combine; <br/>

How to combine the result of the surface's color with the environment map, if
any.  
  
Options are [page:Materials THREE.MultiplyOperation] (default),
[page:Materials THREE.MixOperation], [page:Materials THREE.AddOperation]. If
mix is chosen, the [page:.reflectivity] is used to blend between the two
colors.

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

### <br/> Color emissive; <br/>

Emissive (light) color of the material, essentially a solid color unaffected
by other lighting. Default is black.

### <br/> Texture emissiveMap; <br/>

Set emissive (glow) map. Default is null. The emissive map color is modulated
by the emissive color and the emissive intensity. If you have an emissive map,
be sure to set the emissive color to something other than black.

### <br/> Float emissiveIntensity; <br/>

Intensity of the emissive light. Modulates the emissive color. Default is 1\.

### <br/> Texture envMap; <br/>

The environment map. Default is null.

### <br/> Boolean flatShading; <br/>

Define whether the material is rendered with flat shading. Default is false.

### <br/> Boolean fog; <br/>

Whether the material is affected by fog. Default is `true`.

### <br/> Texture lightMap; <br/>

The light map. Default is null. The lightMap requires a second set of UVs.

### <br/> Float lightMapIntensity; <br/>

Intensity of the baked light. Default is `1`.

### <br/> Texture map; <br/>

The color map. May optionally include an alpha channel, typically combined
with [page:Material.transparent .transparent] or [page:Material.alphaTest
.alphaTest]. Default is null. The texture map color is modulated by the
diffuse [page:.color].

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

### <br/> Float reflectivity; <br/>

How much the environment map affects the surface; also see [page:.combine].
The default value is `1` and the valid range is between `0` (no reflections)
and `1` (full reflections).

### <br/> Float refractionRatio; <br/>

The index of refraction (IOR) of air (approximately 1) divided by the index of
refraction of the material. It is used with environment mapping modes
[page:Textures THREE.CubeRefractionMapping] and [page:Textures
THREE.EquirectangularRefractionMapping]. The refraction ratio should not
exceed `1`. Default is `0.98`.

### <br/> Float shininess; <br/>

How shiny the [page:.specular] highlight is; a higher value gives a sharper
highlight. Default is `30`.

### <br/> Color specular; <br/>

Specular color of the material. Default is a [page:Color] set to `0x111111`
(very dark grey).  
  
This defines how shiny the material is and the color of its shine.

### <br/> Texture specularMap; <br/>

The specular map value affects both how much the specular surface highlight
contributes and how much of the environment map affects the surface. Default
is null.

### <br/> Boolean wireframe; <br/>

Render geometry as wireframe. Default is `false` (i.e. render as flat
polygons).

### <br/> String wireframeLinecap; <br/>

Define appearance of line ends. Possible values are "butt", "round" and
"square". Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineCap
2D Canvas lineCap] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

### <br/> String wireframeLinejoin; <br/>

Define appearance of line joints. Possible values are "round", "bevel" and
"miter". Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineJoin
2D Canvas lineJoin] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

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
