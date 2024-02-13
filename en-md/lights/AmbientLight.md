[page:Object3D] → [page:Light] →

# AmbientLight

This light globally illuminates all objects in the scene equally.  
  
This light cannot be used to cast shadows as it does not have a direction.

## Code Example

  
```ts  
const light = new THREE.AmbientLight( 0x404040 ); // soft white light
scene.add( light );  
```  

## Constructor

###  function AmbientLight( color: Integer, intensity: Float ): void;

[page:Integer color] - (optional) Numeric value of the RGB component of the
color. Default is 0xffffff.  
[page:Float intensity] - (optional) Numeric value of the light's
strength/intensity. Default is `1`.  
  
Creates a new AmbientLight.

## Properties

See the base [page:Light Light] class for common properties.

###  Boolean isAmbientLight;

Read-only flag to check if a given object is of type AmbientLight.

## Methods

See the base [page:Light Light] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

