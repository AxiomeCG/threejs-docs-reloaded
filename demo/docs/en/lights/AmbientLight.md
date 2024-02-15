[Object3D](en\core\Object3D.html) → [Light](en\lights\Light.html) →

# AmbientLight

This light globally illuminates all objects in the scene equally.  
  
This light cannot be used to cast shadows as it does not have a direction.

## Code Example

  
```ts  
const light = new THREE.AmbientLight( 0x404040 ); // soft white light
scene.add( light );  
```  

## Constructor

### AmbientLight

  
  
```ts  
function AmbientLight( color: Integer, intensity: Float ): void;  
```  

[color](#) - (optional) Numeric value of the RGB component of the color.
Default is 0xffffff.  
[intensity](#) - (optional) Numeric value of the light's strength/intensity.
Default is `1`.  
  
Creates a new AmbientLight.

## Properties

See the base [Light](en\lights\Light.html) class for common properties.

### isAmbientLight

  
  
```ts  
isAmbientLight: Boolean;  
```  

Read-only flag to check if a given object is of type AmbientLight.

## Methods

See the base [Light](en\lights\Light.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/AmbientLight.js">src/lights/AmbientLight.js</a>

