[Object3D](en\core\Object3D.html) → [Light](en\lights\Light.html) →

# RectAreaLight

RectAreaLight emits light uniformly across the face a rectangular plane. This
light type can be used to simulate light sources such as bright windows or
strip lighting.  
  
Important Notes:

  * There is no shadow support.
  * Only [MeshStandardMaterial](en\materials\MeshStandardMaterial.html) and [MeshPhysicalMaterial](en\materials\MeshPhysicalMaterial.html) are supported.
  * You have to include <a href="https://threejs.org/examples/jsm/lights/RectAreaLightUniformsLib.js">RectAreaLightUniformsLib</a> into your scene and call `init()`.

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

### RectAreaLight

  
  
```ts  
function RectAreaLight( color: Integer, intensity: Float, width: Float,
height: Float ): void;  
```  

[color](#) - (optional) hexadecimal color of the light. Default is 0xffffff
(white).  
[intensity](#) - (optional) the light's intensity, or brightness. Default is
`1`.  
[width](#) - (optional) width of the light. Default is `10`.  
[height](#) - (optional) height of the light. Default is `10`.  
  
Creates a new RectAreaLight.

## Properties

See the base [Light](en\lights\Light.html) class for common properties.

### height

  
  
```ts  
height: Float;  
```  

The height of the light.

### intensity

  
  
```ts  
intensity: Float;  
```  

The light's intensity. Default is `1`.  
When [legacy lighting mode](#) is disabled, intensity is the luminance
(brightness) of the light measured in nits (cd/m^2).  
  
Changing the intensity will also change the light's power.

### isRectAreaLight

  
  
```ts  
isRectAreaLight: Boolean;  
```  

Read-only flag to check if a given object is of type RectAreaLight.

### power

  
  
```ts  
power: Float;  
```  

The light's power.  
When [legacy lighting mode](#) is disabled, power is the luminous power of the
light measured in lumens (lm).  
  
Changing the power will also change the light's intensity.

### width

  
  
```ts  
width: Float;  
```  

The width of the light.

## Methods

See the base [Light](en\lights\Light.html) class for common methods.

### copy

  
  
```ts  
function copy( source: RectAreaLight ): this;  
```  

Copies value of all the properties from the
[source](en\lights\RectAreaLight.html) to this RectAreaLight.

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/RectAreaLight.js">src/lights/RectAreaLight.js</a>

