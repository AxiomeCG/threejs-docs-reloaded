[page:Object3D] → [page:Light] →

# PointLight

A light that gets emitted from a single point in all directions. A common use
case for this is to replicate the light emitted from a bare lightbulb.  
  
This light can cast shadows - see [page:PointLightShadow] page for details.

## Code Example

  
```ts  
const light = new THREE.PointLight( 0xff0000, 1, 100 );light.position.set( 50,
50, 50 );scene.add( light );  
```  

## Examples

[example:webgl_lights_pointlights lights / pointlights ]  
[example:webgl_effects_anaglyph effects / anaglyph ]  
[example:webgl_geometry_text geometry / text ]  
[example:webgl_lensflares lensflares ]

## Constructor

###  function PointLight( color: Integer, intensity: Float, distance: Number,
decay: Float ): void;

[page:Integer color] - (optional) hexadecimal color of the light. Default is
0xffffff (white).  
[page:Float intensity] - (optional) numeric value of the light's
strength/intensity. Default is `1`.  
[page:Number distance] - Maximum range of the light. Default is `0` (no
limit).  
[page:Float decay] - The amount the light dims along the distance of the
light. Default is `2`.  
  
Creates a new PointLight.

## Properties

See the base [page:Light Light] class for common properties.

###  Boolean castShadow;

If set to `true` light will cast dynamic shadows. *Warning*: This is expensive
and requires tweaking to get shadows looking right. See the
[page:PointLightShadow] for details. The default is `false`.

###  Float decay;

The amount the light dims along the distance of the light. Default is `2`.  
In context of physically-correct rendering the default value should not be
changed.

###  Float distance;

`Default mode` — When distance is zero, light does not attenuate. When
distance is non-zero, light will attenuate linearly from maximum intensity at
the light's position down to zero at this distance from the light.

When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled —
When distance is zero, light will attenuate according to inverse-square law to
infinite distance. When distance is non-zero, light will attenuate according
to inverse-square law until near the distance cutoff, where it will then
attenuate quickly and smoothly to 0. Inherently, cutoffs are not physically
correct.

Default is `0.0`.

###  Float intensity;

The light's intensity. Default is `1`.  
When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled,
intensity is the luminous intensity of the light measured in candela (cd).  
  
Changing the intensity will also change the light's power.

###  Float power;

The light's power.  
When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled,
power is the luminous power of the light measured in lumens (lm).  
  
Changing the power will also change the light's intensity.

###  PointLightShadow shadow;

A [page:PointLightShadow] used to calculate shadows for this light.  
  
The lightShadow's [page:LightShadow.camera camera] is set to a
[page:PerspectiveCamera] with [page:PerspectiveCamera.fov fov] of `90`,
[page:PerspectiveCamera.aspect aspect] of `1`, [page:PerspectiveCamera.near
near] clipping plane at `0.5` and [page:PerspectiveCamera.far far] clipping
plane at `500`.

## Methods

See the base [page:Light Light] class for common methods.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function copy( source: PointLight ): this;

Copies value of all the properties from the [page:PointLight source] to this
PointLight.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

