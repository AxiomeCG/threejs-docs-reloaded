[Object3D](en\core\Object3D.html) → [Light](en\lights\Light.html) →

# HemisphereLight

A light source positioned directly above the scene, with color fading from the
sky color to the ground color.  
  
This light cannot be used to cast shadows.

## Code Example

  
```ts  
const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1 ); scene.add(
light );  
```  

## Examples

[example:webgl_animation_skinning_blending animation / skinning / blending ]  
[example:webgl_lights_hemisphere lights / hemisphere ]  
[example:misc_controls_pointerlock controls / pointerlock ]  
[example:webgl_loader_collada_kinematics loader / collada / kinematics ]  
[example:webgl_loader_stl loader / stl ]

## Constructor

### HemisphereLight

  
  
```ts  
function HemisphereLight( skyColor: Integer, groundColor: Integer, intensity:
Float ): void;  
```  

[skyColor](#) - (optional) hexadecimal color of the sky. Default is 0xffffff.  
[groundColor](#) - (optional) hexadecimal color of the ground. Default is
0xffffff.  
[intensity](#) - (optional) numeric value of the light's strength/intensity.
Default is `1`.  
  
Creates a new HemisphereLight.

## Properties

See the base [Light](en\lights\Light.html) class for common properties.

### color

  
  
```ts  
color: Float;  
```  

The light's sky color, as passed in the constructor. Default is a new
[Color](en\math\Color.html) set to white (0xffffff).

### groundColor

  
  
```ts  
groundColor: Float;  
```  

The light's ground color, as passed in the constructor. Default is a new
[Color](en\math\Color.html) set to white (0xffffff).

### isHemisphereLight

  
  
```ts  
isHemisphereLight: Boolean;  
```  

Read-only flag to check if a given object is of type HemisphereLight.

### position

  
  
```ts  
position: Vector3;  
```  

This is set equal to [Object3D.DEFAULT_UP](#) (0, 1, 0), so that the light
shines from the top down.

## Methods

See the base [Light](en\lights\Light.html) class for common methods.

### copy

  
  
```ts  
function copy( source: HemisphereLight ): this;  
```  

Copies the value of [.color](#color), [.intensity](#intensity) and
[.groundColor](#groundColor) from the [.ight](#ight) light into this one.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/HemisphereLight.js">src/lights/HemisphereLight.js</a>

