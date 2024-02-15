[Object3D](en\core\Object3D.html) →

# HemisphereLightHelper

Creates a visual aid consisting of a spherical [Mesh](en\objects\Mesh.html)
for a [HemisphereLight](en\lights\HemisphereLight.html).

## Code Example

  
```ts  
const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1 ); const helper
= new THREE.HemisphereLightHelper( light, 5 ); scene.add( helper );  
```  

## Constructor

### HemisphereLightHelper

  
  
```ts  
function HemisphereLightHelper( light: HemisphereLight, sphereSize: Number,
color: Hex ): void;  
```  

[light](en\lights\HemisphereLight.html) -- The light being visualized.  
  
[size](#) -- The size of the mesh used to visualize the light.  
  
[color](#) -- (optional) if this is not the set the helper will take the color
of the light.

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### light

  
  
```ts  
light: HemisphereLight;  
```  

Reference to the HemisphereLight being visualized.

### matrix

  
  
```ts  
matrix: Object;  
```  

Reference to the hemisphereLight's [matrixWorld](#).

### matrixAutoUpdate

  
  
```ts  
matrixAutoUpdate: Object;  
```  

See [Object3D.matrixAutoUpdate](#). Set to `false` here as the helper is using
the hemisphereLight's [matrixWorld](#).

### color

  
  
```ts  
color: hex;  
```  

The color parameter passed in the constructor. Default is `undefined`. If this
is changed, the helper's color will update the next time [.update](#update) is
called.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

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

Updates the helper to match the position and direction of the [.light](#).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/HemisphereLightHelper.js">src/helpers/HemisphereLightHelper.js</a>

