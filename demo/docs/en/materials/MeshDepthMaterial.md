[Material](en\materials\Material.html) →

# MeshDepthMaterial

A material for drawing geometry by depth. Depth is based off of the camera
near and far plane. White is nearest, black is farthest.

## Constructor

### MeshDepthMaterial

  
  
```ts  
function MeshDepthMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.

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

### depthPacking

  
  
```ts  
depthPacking: Constant;  
```  

Type for depth packing. Default is
[BasicDepthPacking](en\constants\Textures.html).

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

### fog

  
  
```ts  
fog: Boolean;  
```  

Whether the material is affected by fog. Default is `false`.

### map

  
  
```ts  
map: Texture;  
```  

The color map. May optionally include an alpha channel, typically combined
with [.transparent](#) or [.alphaTest](#). Default is null.

### wireframe

  
  
```ts  
wireframe: Boolean;  
```  

Render geometry as wireframe. Default is false (i.e. render as smooth shaded).

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
href="https://github.com/mrdoob/three.js/blob/master/src/materials/MeshDepthMaterial.js">src/materials/MeshDepthMaterial.js</a>

