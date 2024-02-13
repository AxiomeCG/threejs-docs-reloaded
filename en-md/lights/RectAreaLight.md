[page:Object3D] → [page:Light] →

# RectAreaLight

RectAreaLight emits light uniformly across the face a rectangular plane. This
light type can be used to simulate light sources such as bright windows or
strip lighting.  
  
Important Notes:

  * There is no shadow support.
  * Only [page:MeshStandardMaterial MeshStandardMaterial] and [page:MeshPhysicalMaterial MeshPhysicalMaterial] are supported.
  * You have to include [link:https://threejs.org/examples/jsm/lights/RectAreaLightUniformsLib.js RectAreaLightUniformsLib] into your scene and call `init()`.

## Code Example

  
```ts  
const width = 10;const height = 10;const intensity = 1;const rectLight = new
THREE.RectAreaLight( 0xffffff, intensity, width, height
);rectLight.position.set( 5, 5, 0 );rectLight.lookAt( 0, 0, 0 );scene.add(
rectLight )const rectLightHelper = new RectAreaLightHelper( rectLight
);rectLight.add( rectLightHelper );  
```  

## Examples

[example:webgl_lights_rectarealight WebGL / rectarealight ]

## Constructor

###  function RectAreaLight( color: Integer, intensity: Float, width: Float,
height: Float ): void;

[page:Integer color] - (optional) hexadecimal color of the light. Default is
0xffffff (white).  
[page:Float intensity] - (optional) the light's intensity, or brightness.
Default is `1`.  
[page:Float width] - (optional) width of the light. Default is `10`.  
[page:Float height] - (optional) height of the light. Default is `10`.  
  
Creates a new RectAreaLight.

## Properties

See the base [page:Light Light] class for common properties.

###  Float height;

The height of the light.

###  Float intensity;

The light's intensity. Default is `1`.  
When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled,
intensity is the luminance (brightness) of the light measured in nits
(cd/m^2).  
  
Changing the intensity will also change the light's power.

###  Boolean isRectAreaLight;

Read-only flag to check if a given object is of type RectAreaLight.

###  Float power;

The light's power.  
When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled,
power is the luminous power of the light measured in lumens (lm).  
  
Changing the power will also change the light's intensity.

###  Float width;

The width of the light.

## Methods

See the base [page:Light Light] class for common methods.

###  function copy( source: RectAreaLight ): this;

Copies value of all the properties from the [page:RectAreaLight source] to
this RectAreaLight.

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

