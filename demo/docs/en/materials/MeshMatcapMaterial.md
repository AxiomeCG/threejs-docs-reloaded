[Material](en\materials\Material.html) →

# MeshMatcapMaterial

MeshMatcapMaterial is defined by a MatCap (or Lit Sphere) texture, which
encodes the material color and shading.  
  
MeshMatcapMaterial does not respond to lights since the matcap image file
encodes baked lighting. It will cast a shadow onto an object that receives
shadows (and shadow clipping works), but it will not self-shadow or receive
shadows.

## Constructor

### MeshMatcapMaterial

  
  
```ts  
function MeshMatcapMaterial( parameters: Object ): void;  
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
`1`.

### color

  
  
```ts  
color: Color;  
```  

[Color](en\math\Color.html) of the material, by default set to white
(0xffffff).

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

### map

  
  
```ts  
map: Texture;  
```  

The color map. May optionally include an alpha channel, typically combined
with [.transparent](#) or [.alphaTest](#). Default is null. The texture map
color is modulated by the diffuse [.color](#).

### matcap

  
  
```ts  
matcap: Texture;  
```  

The matcap map. Default is null.

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

## Methods

See the base [Material](en\materials\Material.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/MeshMatcapMaterial.js">src/materials/MeshMatcapMaterial.js</a>

