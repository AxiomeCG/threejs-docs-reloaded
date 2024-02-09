[page:Object3D] → [page:Light] →

# [name]

RectAreaLight emits light uniformly across the face a rectangular plane. This
light type can be used to simulate light sources such as bright windows or
strip lighting.  
  
Important Notes:

  * There is no shadow support.
  * Only [page:MeshStandardMaterial MeshStandardMaterial] and [page:MeshPhysicalMaterial MeshPhysicalMaterial] are supported. 
  * You have to include [link:https://threejs.org/examples/jsm/lights/RectAreaLightUniformsLib.js RectAreaLightUniformsLib] into your scene and call `init()`. 

## Code Example

  
```ts  
const width = 10;  
const height = 10;  
const intensity = 1;  
const rectLight = new THREE.RectAreaLight( 0xffffff, intensity, width, height
);  
rectLight.position.set( 5, 5, 0 );  
rectLight.lookAt( 0, 0, 0 );  
scene.add( rectLight )  
  
const rectLightHelper = new RectAreaLightHelper( rectLight );  
rectLight.add( rectLightHelper );  
```  

## Examples

[example:webgl_lights_rectarealight WebGL / rectarealight ]

## Constructor

###  [name]( [param:Integer color], [param:Float intensity], [param:Float
width], [param:Float height] )

[page:Integer color] - (optional) hexadecimal color of the light. Default is
0xffffff (white).  
[page:Float intensity] - (optional) the light's intensity, or brightness.
Default is `1`.  
[page:Float width] - (optional) width of the light. Default is `10`.  
[page:Float height] - (optional) height of the light. Default is `10`.  
  
Creates a new [name].

## Properties

See the base [page:Light Light] class for common properties.

### <br/> Float height; <br/>

The height of the light.

### <br/> Float intensity; <br/>

The light's intensity. Default is `1`.  
When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled,
intensity is the luminance (brightness) of the light measured in nits
(cd/m^2).  
  
Changing the intensity will also change the light's power.

### <br/> Boolean isRectAreaLight; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Float power; <br/>

The light's power.  
When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled,
power is the luminous power of the light measured in lumens (lm).  
  
Changing the power will also change the light's intensity.

### <br/> Float width; <br/>

The width of the light.

## Methods

See the base [page:Light Light] class for common methods.

### <br/> function copy( source: RectAreaLight ): copy; <br/>

Copies value of all the properties from the [page:RectAreaLight source] to
this RectAreaLight.

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

