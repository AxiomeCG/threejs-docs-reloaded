[Object3D](en\core\Object3D.html) →

# DirectionalLightHelper

Helper object to assist with visualizing a
[DirectionalLight](en\lights\DirectionalLight.html)'s effect on the scene.
This consists of plane and a line representing the light's position and
direction.

## Code Example

  
```ts  
const light = new THREE.DirectionalLight( 0xFFFFFF ); const helper = new
THREE.DirectionalLightHelper( light, 5 ); scene.add( helper );  
```  

## Constructor

### DirectionalLightHelper

  
  
```ts  
function DirectionalLightHelper( light: DirectionalLight, size: Number, color:
Hex ): void;  
```  

[light](en\lights\DirectionalLight.html)-- The light to be visualized.  
  
[size](#) -- (optional) dimensions of the plane. Default is `1`.  
  
[color](#) -- (optional) if this is not the set the helper will take the color
of the light.

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### lightPlane

  
  
```ts  
lightPlane: Line;  
```  

Contains the line mesh showing the location of the directional light.

### light

  
  
```ts  
light: DirectionalLight;  
```  

Reference to the [directionalLight](en\lights\DirectionalLight.html) being
visualized.

### matrix

  
  
```ts  
matrix: Object;  
```  

Reference to the light's [matrixWorld](#).

### matrixAutoUpdate

  
  
```ts  
matrixAutoUpdate: Object;  
```  

See [Object3D.matrixAutoUpdate](#). Set to `false` here as the helper is using
the light's [matrixWorld](#).

### color

  
  
```ts  
color: hex;  
```  

The color parameter passed in the constructor. Default is `undefined`. If this
is changed, the helper's color will update the next time [.update](#update) is
called.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common properties.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### update

  
  
```ts  
function update( ): undefined;  
```  

Updates the helper to match the position and direction of the [.light](#light)
being visualized.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/DirectionalLightHelper.js">src/helpers/DirectionalLightHelper.js</a>

