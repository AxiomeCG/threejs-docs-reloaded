[Material](en\materials\Material.html) →
[MeshStandardMaterial](en\materials\MeshStandardMaterial.html) →

# MeshPhysicalMaterial

An extension of the
[MeshStandardMaterial](en\materials\MeshStandardMaterial.html), providing more
advanced physically-based rendering properties:

  *  **Clearcoat:** Some materials — like car paints, carbon fiber, and wet surfaces — require a clear, reflective layer on top of another layer that may be irregular or rough. Clearcoat approximates this effect, without the need for a separate transparent surface.
  *  **Physically-based transparency:** One limitation of [.opacity](#) is that highly transparent materials are less reflective. Physically-based [.transmission](#) provides a more realistic option for thin, transparent surfaces like glass.
  *  **Advanced reflectivity:** More flexible reflectivity for non-metallic materials.
  *  **Sheen:** Can be used for representing cloth and fabric materials.

As a result of these complex shading features, MeshPhysicalMaterial has a
higher performance cost, per pixel, than other three.js materials. Most
effects are disabled by default, and add cost as they are enabled. For best
results, always specify an [.envMap](#envMap) when using this material.

## Examples

[example:webgl_materials_physical_clearcoat materials / physical / clearcoat]  
[example:webgl_loader_gltf_sheen loader / gltf / sheen]  
[example:webgl_materials_physical_transmission materials / physical /
transmission]

## Constructor

### MeshPhysicalMaterial

  
  
```ts  
function MeshPhysicalMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html) and
[MeshStandardMaterial](en\materials\MeshStandardMaterial.html)) can be passed
in here.  
  
The exception is the property [color](#), which can be passed in as a
hexadecimal string and is `0xffffff` (white) by default. [Color.set](#)( color
) is called internally.

## Properties

See the base [Material](en\materials\Material.html) and
[MeshStandardMaterial](en\materials\MeshStandardMaterial.html) classes for
common properties.

### attenuationColor

  
  
```ts  
attenuationColor: Color;  
```  

The color that white light turns into due to absorption when reaching the
attenuation distance. Default is `white` (0xffffff).

### attenuationDistance

  
  
```ts  
attenuationDistance: Float;  
```  

Density of the medium given as the average distance that light travels in the
medium before interacting with a particle. The value is given in world space
units, and must be greater than zero. Default is `Infinity`.

### clearcoat

  
  
```ts  
clearcoat: Float;  
```  

Represents the intensity of the clear coat layer, from `0.0` to `1.0`. Use
clear coat related properties to enable multilayer materials that have a thin
translucent layer over the base layer. Default is `0.0`.

### clearcoatMap

  
  
```ts  
clearcoatMap: Texture;  
```  

The red channel of this texture is multiplied against [.clearcoat](#), for
per-pixel control over a coating's intensity. Default is `null`.

### clearcoatNormalMap

  
  
```ts  
clearcoatNormalMap: Texture;  
```  

Can be used to enable independent normals for the clear coat layer. Default is
`null`.

### clearcoatNormalScale

  
  
```ts  
clearcoatNormalScale: Vector2;  
```  

How much [.clearcoatNormalMap](#) affects the clear coat layer, from `(0,0)`
to `(1,1)`. Default is `(1,1)`.

### clearcoatRoughness

  
  
```ts  
clearcoatRoughness: Float;  
```  

Roughness of the clear coat layer, from `0.0` to `1.0`. Default is `0.0`.

### clearcoatRoughnessMap

  
  
```ts  
clearcoatRoughnessMap: Texture;  
```  

The green channel of this texture is multiplied against
[.clearcoatRoughness](#), for per-pixel control over a coating's roughness.
Default is `null`.

### defines

  
  
```ts  
defines: Object;  
```  

An object of the form:  
```ts  
{ 'STANDARD': '', 'PHYSICAL': '', };  
```  
This is used by the [WebGLRenderer](en\renderers\WebGLRenderer.html) for
selecting shaders.

### ior

  
  
```ts  
ior: Float;  
```  

Index-of-refraction for non-metallic materials, from `1.0` to `2.333`. Default
is `1.5`.  

### reflectivity

  
  
```ts  
reflectivity: Float;  
```  

Degree of reflectivity, from `0.0` to `1.0`. Default is `0.5`, which
corresponds to an index-of-refraction of 1.5.  
This models the reflectivity of non-metallic materials. It has no effect when
[metalness](#) is `1.0`

### sheen

  
  
```ts  
sheen: Float;  
```  

The intensity of the sheen layer, from `0.0` to `1.0`. Default is `0.0`.

### sheenRoughness

  
  
```ts  
sheenRoughness: Float;  
```  

Roughness of the sheen layer, from `0.0` to `1.0`. Default is `1.0`.

### sheenRoughnessMap

  
  
```ts  
sheenRoughnessMap: Texture;  
```  

The alpha channel of this texture is multiplied against [.sheenRoughness](#),
for per-pixel control over sheen roughness. Default is `null`.

### sheenColor

  
  
```ts  
sheenColor: Color;  
```  

The sheen tint. Default is `0xffffff`, white.

### sheenColorMap

  
  
```ts  
sheenColorMap: Texture;  
```  

The RGB channels of this texture are multiplied against [.sheenColor](#), for
per-pixel control over sheen tint. Default is `null`.

### specularIntensity

  
  
```ts  
specularIntensity: Float;  
```  

A float that scales the amount of specular reflection for non-metals only.
When set to zero, the model is effectively Lambertian. From `0.0` to `1.0`.
Default is `0.0`.

### specularIntensityMap

  
  
```ts  
specularIntensityMap: Texture;  
```  

The alpha channel of this texture is multiplied against
[.specularIntensity](#), for per-pixel control over specular intensity.
Default is `null`.

### specularColor

  
  
```ts  
specularColor: Color;  
```  

A [Color](en\math\Color.html) that tints the specular reflection at normal
incidence for non-metals only. Default is `0xffffff`, white.

### specularColorMap

  
  
```ts  
specularColorMap: Texture;  
```  

The RGB channels of this texture are multiplied against [.specularColor](#),
for per-pixel control over specular color. Default is `null`.

### thickness

  
  
```ts  
thickness: Float;  
```  

The thickness of the volume beneath the surface. The value is given in the
coordinate space of the mesh. If the value is `0` the material is thin-walled.
Otherwise the material is a volume boundary. Default is `0`.

### thicknessMap

  
  
```ts  
thicknessMap: Texture;  
```  

A texture that defines the thickness, stored in the G channel. This will be
multiplied by [.thickness](#). Default is `null`.

### transmission

  
  
```ts  
transmission: Float;  
```  

Degree of transmission (or optical transparency), from `0.0` to `1.0`. Default
is `0.0`.  
Thin, transparent or semitransparent, plastic or glass materials remain
largely reflective even if they are fully transmissive. The transmission
property can be used to model these materials.  
When transmission is non-zero, [opacity](#) should be set to `0`.

### transmissionMap

  
  
```ts  
transmissionMap: Texture;  
```  

The red channel of this texture is multiplied against [.transmission](#), for
per-pixel control over optical transparency. Default is `null`.

## Methods

See the base [Material](en\materials\Material.html) and
[MeshStandardMaterial](en\materials\MeshStandardMaterial.html) classes for
common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/MeshPhysicalMaterial.js">src/materials/MeshPhysicalMaterial.js</a>

