[Material](en\materials\Material.html) →

# MeshBasicMaterial

A material for drawing geometries in a simple shaded (flat or wireframe) way.  
  
This material is not affected by lights.

## Constructor

### MeshBasicMaterial

  
  
```ts  
function MeshBasicMaterial( parameters: Object ): void;  
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

### envMap

  
  
```ts  
envMap: Texture;  
```  

The environment map. Default is null.

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

### reflectivity

  
  
```ts  
reflectivity: Float;  
```  

How much the environment map affects the surface; also see [.combine](#). The
default value is `1` and the valid range is between `0` (no reflections) and
`1` (full reflections).

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
href="https://github.com/mrdoob/three.js/blob/master/src/materials/MeshBasicMaterial.js">src/materials/MeshBasicMaterial.js</a>

