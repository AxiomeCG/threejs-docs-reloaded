[page:Object3D] → [page:Light] →

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

###  function HemisphereLight( skyColor: Integer, groundColor: Integer,
intensity: Float ): void;

[page:Integer skyColor] - (optional) hexadecimal color of the sky. Default is
0xffffff.  
[page:Integer groundColor] - (optional) hexadecimal color of the ground.
Default is 0xffffff.  
[page:Float intensity] - (optional) numeric value of the light's
strength/intensity. Default is `1`.  
  
Creates a new HemisphereLight.

## Properties

See the base [page:Light Light] class for common properties.

###  Float color;

The light's sky color, as passed in the constructor. Default is a new
[page:Color] set to white (0xffffff).

###  Float groundColor;

The light's ground color, as passed in the constructor. Default is a new
[page:Color] set to white (0xffffff).

###  Boolean isHemisphereLight;

Read-only flag to check if a given object is of type HemisphereLight.

###  Vector3 position;

This is set equal to [page:Object3D.DEFAULT_UP] (0, 1, 0), so that the light
shines from the top down.

## Methods

See the base [page:Light Light] class for common methods.

###  function copy( source: HemisphereLight ): this;

Copies the value of [page:.color color], [page:.intensity intensity] and
[page:.groundColor groundColor] from the [page:Light source] light into this
one.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

