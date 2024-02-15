[Material](en\materials\Material.html) →

# MeshNormalMaterial

A material that maps the normal vectors to RGB colors.

## Constructor

### MeshNormalMaterial

  
  
```ts  
function MeshNormalMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.

## Properties

See the base [Material](en\materials\Material.html) class for common
properties.

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

Whether the material is affected by fog. Default is `false`.

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
href="https://github.com/mrdoob/three.js/blob/master/src/materials/MeshNormalMaterial.js">src/materials/MeshNormalMaterial.js</a>

