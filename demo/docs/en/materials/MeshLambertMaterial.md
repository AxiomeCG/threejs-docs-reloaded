[Material](en\materials\Material.html) →

# MeshLambertMaterial

A material for non-shiny surfaces, without specular highlights.  
  
The material uses a non-physically based <a
href="https://en.wikipedia.org/wiki/Lambertian_reflectance">Lambertian</a>
model for calculating reflectance. This can simulate some surfaces (such as
untreated wood or stone) well, but cannot simulate shiny surfaces with
specular highlights (such as varnished wood). MeshLambertMaterial uses per-
fragment shading.  
  
Due to the simplicity of the reflectance and illumination models, performance
will be greater when using this material over the
[MeshPhongMaterial](en\materials\MeshPhongMaterial.html),
[MeshStandardMaterial](en\materials\MeshStandardMaterial.html) or
[MeshPhysicalMaterial](en\materials\MeshPhysicalMaterial.html), at the cost of
some graphical accuracy.

## Constructor

### MeshLambertMaterial

  
  
```ts  
function MeshLambertMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.  
  
The exception is the property [color](#), which can be passed in as a
hexadecimal string and is `0xffffff` (white) by default. [Color.set](#)( color
) is called internally.

## Properties

See the base [Material](en\materials\Material.html) class for common
properties.

### alphaMap

  
  
```ts  
alphaMap: Texture;  
```  

The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Default is null.  
  
Only the color of the texture is used, ignoring the alpha channel if one
exists. For RGB and RGBA textures, the
[WebGL](en\renderers\WebGLRenderer.html) renderer will use the green channel
when sampling this texture due to the extra bit of precision provided for
green in DXT-compressed and uncompressed RGB 565 formats. Luminance-only and
luminance/alpha textures will also still work as expected.

### aoMap

  
  
```ts  
aoMap: Texture;  
```  

The red channel of this texture is used as the ambient occlusion map. Default
is null. The aoMap requires a second set of UVs.

### aoMapIntensity

  
  
```ts  
aoMapIntensity: Float;  
```  

Intensity of the ambient occlusion effect. Default is `1`. Zero is no
occlusion effect.

### bumpMap

  
  
```ts  
bumpMap: Texture;  
```  

The texture to create a bump map. The black and white values map to the
perceived depth in relation to the lights. Bump doesn't actually affect the
geometry of the object, only the lighting. If a normal map is defined this
will be ignored.

### bumpScale

  
  
```ts  
bumpScale: Float;  
```  

How much the bump map affects the material. Typical ranges are 0-1. Default is
1.

### color

  
  
```ts  
color: Color;  
```  

[Color](en\math\Color.html) of the material, by default set to white
(0xffffff).

### combine

  
  
```ts  
combine: Integer;  
```  

How to combine the result of the surface's color with the environment map, if
any.  
  
Options are [.aterials](#aterials) (default), [.aterials](#aterials),
[.aterials](#aterials). If mix is chosen, the [.reflectivity](#) is used to
blend between the two colors.

### displacementMap

  
  
```ts  
displacementMap: Texture;  
```  

The displacement map affects the position of the mesh's vertices. Unlike other
maps which only affect the light and shade of the material the displaced
vertices can cast shadows, block other objects, and otherwise act as real
geometry. The displacement texture is an image where the value of each pixel
(white being the highest) is mapped against, and repositions, the vertices of
the mesh.

### displacementScale

  
  
```ts  
displacementScale: Float;  
```  

How much the displacement map affects the mesh (where black is no
displacement, and white is maximum displacement). Without a displacement map
set, this value is not applied. Default is `1`.

### displacementBias

  
  
```ts  
displacementBias: Float;  
```  

The offset of the displacement map's values on the mesh's vertices. Without a
displacement map set, this value is not applied. Default is `0`.

### emissive

  
  
```ts  
emissive: Color;  
```  

Emissive (light) color of the material, essentially a solid color unaffected
by other lighting. Default is black.

### emissiveMap

  
  
```ts  
emissiveMap: Texture;  
```  

Set emissive (glow) map. Default is null. The emissive map color is modulated
by the emissive color and the emissive intensity. If you have an emissive map,
be sure to set the emissive color to something other than black.

### emissiveIntensity

  
  
```ts  
emissiveIntensity: Float;  
```  

Intensity of the emissive light. Modulates the emissive color. Default is 1.

### envMap

  
  
```ts  
envMap: Texture;  
```  

The environment map. Default is null.

### flatShading

  
  
```ts  
flatShading: Boolean;  
```  

Define whether the material is rendered with flat shading. Default is false.

### fog

  
  
```ts  
fog: Boolean;  
```  

Whether the material is affected by fog. Default is `true`.

### lightMap

  
  
```ts  
lightMap: Texture;  
```  

The light map. Default is null. The lightMap requires a second set of UVs.

### lightMapIntensity

  
  
```ts  
lightMapIntensity: Float;  
```  

Intensity of the baked light. Default is `1`.

### map

  
  
```ts  
map: Texture;  
```  

The color map. May optionally include an alpha channel, typically combined
with [.transparent](#) or [.alphaTest](#). Default is null.

### normalMap

  
  
```ts  
normalMap: Texture;  
```  

The texture to create a normal map. The RGB values affect the surface normal
for each pixel fragment and change the way the color is lit. Normal maps do
not change the actual shape of the surface, only the lighting. In case the
material has a normal map authored using the left handed convention, the y
component of normalScale should be negated to compensate for the different
handedness.

### normalMapType

  
  
```ts  
normalMapType: Integer;  
```  

The type of normal map.  
  
Options are [THREE.TangentSpaceNormalMap](#) (default), and
[THREE.ObjectSpaceNormalMap](#).

### normalScale

  
  
```ts  
normalScale: Vector2;  
```  

How much the normal map affects the material. Typical ranges are 0-1. Default
is a [Vector2](en\math\Vector2.html) set to (1,1).

### reflectivity

  
  
```ts  
reflectivity: Float;  
```  

How much the environment map affects the surface; also see [.combine](#).

### refractionRatio

  
  
```ts  
refractionRatio: Float;  
```  

The index of refraction (IOR) of air (approximately 1) divided by the index of
refraction of the material. It is used with environment mapping modes
[THREE.CubeRefractionMapping](en\constants\Textures.html) and
[THREE.EquirectangularRefractionMapping](en\constants\Textures.html). The
refraction ratio should not exceed `1`. Default is `0.98`.

### specularMap

  
  
```ts  
specularMap: Texture;  
```  

Specular map used by the material. Default is null.

### wireframe

  
  
```ts  
wireframe: Boolean;  
```  

Render geometry as wireframe. Default is `false` (i.e. render as flat
polygons).

### wireframeLinecap

  
  
```ts  
wireframeLinecap: String;  
```  

Define appearance of line ends. Possible values are "butt", "round" and
"square". Default is 'round'.  
  
This corresponds to the <a
href="https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineCap">2D
Canvas lineCap</a> property and it is ignored by the
[WebGL](en\renderers\WebGLRenderer.html) renderer.

### wireframeLinejoin

  
  
```ts  
wireframeLinejoin: String;  
```  

Define appearance of line joints. Possible values are "round", "bevel" and
"miter". Default is 'round'.  
  
This corresponds to the <a
href="https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineJoin">2D
Canvas lineJoin</a> property and it is ignored by the
[WebGL](en\renderers\WebGLRenderer.html) renderer.

### wireframeLinewidth

  
  
```ts  
wireframeLinewidth: Float;  
```  

Controls wireframe thickness. Default is `1`.  
  
Due to limitations of the <a
href="https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf">OpenGL
Core Profile</a> with the [WebGL](en\renderers\WebGLRenderer.html) renderer on
most platforms linewidth will always be `1` regardless of the set value.

## Methods

See the base [Material](en\materials\Material.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/MeshLambertMaterial.js">src/materials/MeshLambertMaterial.js</a>

