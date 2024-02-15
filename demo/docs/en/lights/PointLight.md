[Object3D](en\core\Object3D.html) → [Light](en\lights\Light.html) →

# PointLight

A light that gets emitted from a single point in all directions. A common use
case for this is to replicate the light emitted from a bare lightbulb.  
  
This light can cast shadows - see
[PointLightShadow](en\lights\shadows\PointLightShadow.html) page for details.

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

### PointLight

  
  
```ts  
function PointLight( color: Integer, intensity: Float, distance: Number,
decay: Float ): void;  
```  

[color](#) - (optional) hexadecimal color of the light. Default is 0xffffff
(white).  
[intensity](#) - (optional) numeric value of the light's strength/intensity.
Default is `1`.  
[distance](#) - Maximum range of the light. Default is `0` (no limit).  
[decay](#) - The amount the light dims along the distance of the light.
Default is `2`.  
  
Creates a new PointLight.

## Properties

See the base [Light](en\lights\Light.html) class for common properties.

### castShadow

  
  
```ts  
castShadow: Boolean;  
```  

If set to `true` light will cast dynamic shadows. *Warning*: This is expensive
and requires tweaking to get shadows looking right. See the
[PointLightShadow](en\lights\shadows\PointLightShadow.html) for details. The
default is `false`.

### decay

  
  
```ts  
decay: Float;  
```  

The amount the light dims along the distance of the light. Default is `2`.  
In context of physically-correct rendering the default value should not be
changed.

### distance

  
  
```ts  
distance: Float;  
```  

`Default mode` — When distance is zero, light does not attenuate. When
distance is non-zero, light will attenuate linearly from maximum intensity at
the light's position down to zero at this distance from the light.

When [legacy lighting mode](#) is disabled — When distance is zero, light will
attenuate according to inverse-square law to infinite distance. When distance
is non-zero, light will attenuate according to inverse-square law until near
the distance cutoff, where it will then attenuate quickly and smoothly to 0.
Inherently, cutoffs are not physically correct.

Default is `0.0`.

### intensity

  
  
```ts  
intensity: Float;  
```  

The light's intensity. Default is `1`.  
When [legacy lighting mode](#) is disabled, intensity is the luminous
intensity of the light measured in candela (cd).  
  
Changing the intensity will also change the light's power.

### power

  
  
```ts  
power: Float;  
```  

The light's power.  
When [legacy lighting mode](#) is disabled, power is the luminous power of the
light measured in lumens (lm).  
  
Changing the power will also change the light's intensity.

### shadow

  
  
```ts  
shadow: PointLightShadow;  
```  

A [PointLightShadow](en\lights\shadows\PointLightShadow.html) used to
calculate shadows for this light.  
  
The lightShadow's [camera](#) is set to a
[PerspectiveCamera](en\cameras\PerspectiveCamera.html) with [fov](#) of `90`,
[aspect](#) of `1`, [near](#) clipping plane at `0.5` and [far](#) clipping
plane at `500`.

## Methods

See the base [Light](en\lights\Light.html) class for common methods.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### copy

  
  
```ts  
function copy( source: PointLight ): this;  
```  

Copies value of all the properties from the
[source](en\lights\PointLight.html) to this PointLight.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/PointLight.js">src/lights/PointLight.js</a>

