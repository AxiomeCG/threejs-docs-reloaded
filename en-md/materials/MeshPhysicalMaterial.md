[page:Material] → [page:MeshStandardMaterial] →

# MeshPhysicalMaterial

An extension of the [page:MeshStandardMaterial], providing more advanced
physically-based rendering properties:

  *  **Clearcoat:** Some materials — like car paints, carbon fiber, and wet surfaces — require a clear, reflective layer on top of another layer that may be irregular or rough. Clearcoat approximates this effect, without the need for a separate transparent surface.
  *  **Physically-based transparency:** One limitation of [page:Material.opacity .opacity] is that highly transparent materials are less reflective. Physically-based [page:.transmission] provides a more realistic option for thin, transparent surfaces like glass.
  *  **Advanced reflectivity:** More flexible reflectivity for non-metallic materials.
  *  **Sheen:** Can be used for representing cloth and fabric materials.

As a result of these complex shading features, MeshPhysicalMaterial has a
higher performance cost, per pixel, than other three.js materials. Most
effects are disabled by default, and add cost as they are enabled. For best
results, always specify an [page:.envMap environment map] when using this
material.

## Examples

[example:webgl_materials_physical_clearcoat materials / physical / clearcoat]  
[example:webgl_loader_gltf_sheen loader / gltf / sheen]  
[example:webgl_materials_physical_transmission materials / physical /
transmission]

## Constructor

###  function MeshPhysicalMaterial( parameters: Object ): void;

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material] and [page:MeshStandardMaterial])
can be passed in here.  
  
The exception is the property [page:Hexadecimal color], which can be passed in
as a hexadecimal string and is `0xffffff` (white) by default.
[page:Color.set]( color ) is called internally.

## Properties

See the base [page:Material] and [page:MeshStandardMaterial] classes for
common properties.

###  Color attenuationColor;

The color that white light turns into due to absorption when reaching the
attenuation distance. Default is `white` (0xffffff).

###  Float attenuationDistance;

Density of the medium given as the average distance that light travels in the
medium before interacting with a particle. The value is given in world space
units, and must be greater than zero. Default is `Infinity`.

###  Float clearcoat;

Represents the intensity of the clear coat layer, from `0.0` to `1.0`. Use
clear coat related properties to enable multilayer materials that have a thin
translucent layer over the base layer. Default is `0.0`.

###  Texture clearcoatMap;

The red channel of this texture is multiplied against [page:.clearcoat], for
per-pixel control over a coating's intensity. Default is `null`.

###  Texture clearcoatNormalMap;

Can be used to enable independent normals for the clear coat layer. Default is
`null`.

###  Vector2 clearcoatNormalScale;

How much [page:.clearcoatNormalMap] affects the clear coat layer, from `(0,0)`
to `(1,1)`. Default is `(1,1)`.

###  Float clearcoatRoughness;

Roughness of the clear coat layer, from `0.0` to `1.0`. Default is `0.0`.

###  Texture clearcoatRoughnessMap;

The green channel of this texture is multiplied against
[page:.clearcoatRoughness], for per-pixel control over a coating's roughness.
Default is `null`.

###  Object defines;

An object of the form:  
```ts  
{ 'STANDARD': '', 'PHYSICAL': '', };  
```  
This is used by the [page:WebGLRenderer] for selecting shaders.

###  Float ior;

Index-of-refraction for non-metallic materials, from `1.0` to `2.333`. Default
is `1.5`.  

###  Float reflectivity;

Degree of reflectivity, from `0.0` to `1.0`. Default is `0.5`, which
corresponds to an index-of-refraction of 1.5.  
This models the reflectivity of non-metallic materials. It has no effect when
[page:MeshStandardMaterial.metalness metalness] is `1.0`

###  Float sheen;

The intensity of the sheen layer, from `0.0` to `1.0`. Default is `0.0`.

###  Float sheenRoughness;

Roughness of the sheen layer, from `0.0` to `1.0`. Default is `1.0`.

###  Texture sheenRoughnessMap;

The alpha channel of this texture is multiplied against
[page:.sheenRoughness], for per-pixel control over sheen roughness. Default is
`null`.

###  Color sheenColor;

The sheen tint. Default is `0xffffff`, white.

###  Texture sheenColorMap;

The RGB channels of this texture are multiplied against [page:.sheenColor],
for per-pixel control over sheen tint. Default is `null`.

###  Float specularIntensity;

A float that scales the amount of specular reflection for non-metals only.
When set to zero, the model is effectively Lambertian. From `0.0` to `1.0`.
Default is `0.0`.

###  Texture specularIntensityMap;

The alpha channel of this texture is multiplied against
[page:.specularIntensity], for per-pixel control over specular intensity.
Default is `null`.

###  Color specularColor;

A [page:Color] that tints the specular reflection at normal incidence for non-
metals only. Default is `0xffffff`, white.

###  Texture specularColorMap;

The RGB channels of this texture are multiplied against [page:.specularColor],
for per-pixel control over specular color. Default is `null`.

###  Float thickness;

The thickness of the volume beneath the surface. The value is given in the
coordinate space of the mesh. If the value is `0` the material is thin-walled.
Otherwise the material is a volume boundary. Default is `0`.

###  Texture thicknessMap;

A texture that defines the thickness, stored in the G channel. This will be
multiplied by [page:.thickness]. Default is `null`.

###  Float transmission;

Degree of transmission (or optical transparency), from `0.0` to `1.0`. Default
is `0.0`.  
Thin, transparent or semitransparent, plastic or glass materials remain
largely reflective even if they are fully transmissive. The transmission
property can be used to model these materials.  
When transmission is non-zero, [page:Material.opacity opacity] should be set
to `0`.

###  Texture transmissionMap;

The red channel of this texture is multiplied against [page:.transmission],
for per-pixel control over optical transparency. Default is `null`.

## Methods

See the base [page:Material] and [page:MeshStandardMaterial] classes for
common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

