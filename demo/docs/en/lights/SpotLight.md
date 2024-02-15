[Object3D](en\core\Object3D.html) → [Light](en\lights\Light.html) →

# SpotLight

This light gets emitted from a single point in one direction, along a cone
that increases in size the further from the light it gets.  
  
This light can cast shadows - see the
[SpotLightShadow](en\lights\shadows\SpotLightShadow.html) page for details.

## Code Example

  
```ts  
// white spotlight shining from the side, modulated by a texture, casting a
shadow const spotLight = new THREE.SpotLight( 0xffffff );
spotLight.position.set( 100, 1000, 100 ); spotLight.map = new
THREE.TextureLoader().load( url ); spotLight.castShadow = true;
spotLight.shadow.mapSize.width = 1024; spotLight.shadow.mapSize.height = 1024;
spotLight.shadow.camera.near = 500; spotLight.shadow.camera.far = 4000;
spotLight.shadow.camera.fov = 30; scene.add( spotLight );  
```  

## Examples

[example:webgl_lights_spotlight lights / spotlight ]  
[example:webgl_lights_spotlights lights / spotlights ]

## Constructor

### SpotLight

  
  
```ts  
function SpotLight( color: Integer, intensity: Float, distance: Float, angle:
Radians, penumbra: Float, decay: Float ): void;  
```  

[color](#) - (optional) hexadecimal color of the light. Default is 0xffffff
(white).  
[intensity](#) - (optional) numeric value of the light's strength/intensity.
Default is `1`.  
[distance](#) - Maximum range of the light. Default is `0` (no limit).  
[angle](#) - Maximum angle of light dispersion from its direction whose upper
bound is Math.PI/2.  
[penumbra](#) - Percent of the spotlight cone that is attenuated due to
penumbra. Takes values between zero and `1`. Default is zero.  
[decay](#) - The amount the light dims along the distance of the light.  
  
Creates a new SpotLight.

## Properties

See the base [Light](en\lights\Light.html) class for common properties.

### angle

  
  
```ts  
angle: Float;  
```  

Maximum extent of the spotlight, in radians, from its direction. Should be no
more than `Math.PI/2`. The default is `Math.PI/3`.

### castShadow

  
  
```ts  
castShadow: Boolean;  
```  

If set to `true` light will cast dynamic shadows. *Warning*: This is expensive
and requires tweaking to get shadows looking right. See the
[SpotLightShadow](en\lights\shadows\SpotLightShadow.html) for details. The
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
the distance cutoff, where it will then attenuate quickly and smoothly to `0`.
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

### isSpotLight

  
  
```ts  
isSpotLight: Boolean;  
```  

Read-only flag to check if a given object is of type SpotLight.

### penumbra

  
  
```ts  
penumbra: Float;  
```  

Percent of the spotlight cone that is attenuated due to penumbra. Takes values
between zero and `1`. The default is `0.0`.

### position

  
  
```ts  
position: Vector3;  
```  

This is set equal to [Object3D.DEFAULT_UP](#) (0, 1, 0), so that the light
shines from the top down.

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
shadow: SpotLightShadow;  
```  

A [SpotLightShadow](en\lights\shadows\SpotLightShadow.html) used to calculate
shadows for this light.

### target

  
  
```ts  
target: Object3D;  
```  

The Spotlight points from its [.position](#position) to target.position. The
default position of the target is `(0, 0, 0)`.  
*Note*: For the target's position to be changed to anything other than the default, it must be added to the [scene](en\scenes\Scene.html) using  
```ts  
scene.add( light.target );  
```  
This is so that the target's [matrixWorld](#) gets automatically updated each
frame.  
  
It is also possible to set the target to be another object in the scene
(anything with a [position](#) property), like so:  
```ts  
const targetObject = new THREE.Object3D();
scene.add(targetObject);light.target = targetObject;  
```  
The spotlight will now track the target object.

### map

  
  
```ts  
map: Texture;  
```  

A [Texture](en\textures\Texture.html) used to modulate the color of the light.
The spot light color is mixed with the RGB value of this texture, with a ratio
corresponding to its alpha value. The cookie-like masking effect is reproduced
using pixel values (0, 0, 0, 1-cookie_value). *Warning*: [param:SpotLight map]
is disabled if [param:SpotLight castShadow] is *false*.

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
function copy( source: SpotLight ): this;  
```  

Copies value of all the properties from the [source](en\lights\SpotLight.html)
to this SpotLight.

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/SpotLight.js">src/lights/SpotLight.js</a>

