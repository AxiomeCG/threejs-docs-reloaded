[page:Material] →

# MeshToonMaterial

A material implementing toon shading.

## Examples

[example:webgl_materials_toon materials / toon]

## Constructor

###  function MeshToonMaterial( parameters: Object ): void;

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.  
  
The exception is the property [page:Hexadecimal color], which can be passed in
as a hexadecimal string and is `0xffffff` (white) by default.
[page:Color.set]( color ) is called internally.

## Properties

See the base [page:Material] class for common properties.

###  Texture alphaMap;

The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Default is null.  
  
Only the color of the texture is used, ignoring the alpha channel if one
exists. For RGB and RGBA textures, the [page:WebGLRenderer WebGL] renderer
will use the green channel when sampling this texture due to the extra bit of
precision provided for green in DXT-compressed and uncompressed RGB 565
formats. Luminance-only and luminance/alpha textures will also still work as
expected.

###  Texture aoMap;

The red channel of this texture is used as the ambient occlusion map. Default
is null. The aoMap requires a second set of UVs.

###  Float aoMapIntensity;

Intensity of the ambient occlusion effect. Default is `1`. Zero is no
occlusion effect.

###  Texture bumpMap;

The texture to create a bump map. The black and white values map to the
perceived depth in relation to the lights. Bump doesn't actually affect the
geometry of the object, only the lighting. If a normal map is defined this
will be ignored.

###  Float bumpScale;

How much the bump map affects the material. Typical ranges are 0-1. Default is
`1`.

###  Color color;

[page:Color] of the material, by default set to white (0xffffff).

###  Texture displacementMap;

The displacement map affects the position of the mesh's vertices. Unlike other
maps which only affect the light and shade of the material the displaced
vertices can cast shadows, block other objects, and otherwise act as real
geometry. The displacement texture is an image where the value of each pixel
(white being the highest) is mapped against, and repositions, the vertices of
the mesh.

###  Float displacementScale;

How much the displacement map affects the mesh (where black is no
displacement, and white is maximum displacement). Without a displacement map
set, this value is not applied. Default is `1`.

###  Float displacementBias;

The offset of the displacement map's values on the mesh's vertices. Without a
displacement map set, this value is not applied. Default is `0`.

###  Color emissive;

Emissive (light) color of the material, essentially a solid color unaffected
by other lighting. Default is black.

###  Texture emissiveMap;

Set emissive (glow) map. Default is null. The emissive map color is modulated
by the emissive color and the emissive intensity. If you have an emissive map,
be sure to set the emissive color to something other than black.

###  Float emissiveIntensity;

Intensity of the emissive light. Modulates the emissive color. Default is 1.

###  Boolean fog;

Whether the material is affected by fog. Default is `true`.

###  Texture gradientMap;

Gradient map for toon shading. It's required to set [page:Texture.minFilter]
and [page:Texture.magFilter] to [page:Textures THREE.NearestFilter] when using
this type of texture. Default is `null`.

###  Texture lightMap;

The light map. Default is null. The lightMap requires a second set of UVs.

###  Float lightMapIntensity;

Intensity of the baked light. Default is `1`.

###  Texture map;

The color map. May optionally include an alpha channel, typically combined
with [page:Material.transparent .transparent] or [page:Material.alphaTest
.alphaTest]. Default is null. The texture map color is modulated by the
diffuse [page:.color].

###  Texture normalMap;

The texture to create a normal map. The RGB values affect the surface normal
for each pixel fragment and change the way the color is lit. Normal maps do
not change the actual shape of the surface, only the lighting. In case the
material has a normal map authored using the left handed convention, the y
component of normalScale should be negated to compensate for the different
handedness.

###  Integer normalMapType;

The type of normal map.  
  
Options are [page:constant THREE.TangentSpaceNormalMap] (default), and
[page:constant THREE.ObjectSpaceNormalMap].

###  Vector2 normalScale;

How much the normal map affects the material. Typical ranges are 0-1. Default
is a [page:Vector2] set to (1,1).

###  Boolean wireframe;

Render geometry as wireframe. Default is `false` (i.e. render as flat
polygons).

###  String wireframeLinecap;

Define appearance of line ends. Possible values are "butt", "round" and
"square". Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineCap
2D Canvas lineCap] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

###  String wireframeLinejoin;

Define appearance of line joints. Possible values are "round", "bevel" and
"miter". Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineJoin
2D Canvas lineJoin] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

###  Float wireframeLinewidth;

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

