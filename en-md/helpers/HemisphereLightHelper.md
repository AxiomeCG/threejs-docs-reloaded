[page:Object3D] →

# HemisphereLightHelper

Creates a visual aid consisting of a spherical [page:Mesh] for a
[page:HemisphereLight HemisphereLight].

## Code Example

  
```ts  
const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1 ); const helper
= new THREE.HemisphereLightHelper( light, 5 ); scene.add( helper );  
```  

## Constructor

###  function HemisphereLightHelper( light: HemisphereLight, sphereSize:
Number, color: Hex ): void;

[page:HemisphereLight light] -- The light being visualized.  
  
[page:Number size] -- The size of the mesh used to visualize the light.  
  
[page:Hex color] -- (optional) if this is not the set the helper will take the
color of the light.

## Properties

See the base [page:Object3D] class for common properties.

###  HemisphereLight light;

Reference to the HemisphereLight being visualized.

###  Object matrix;

Reference to the hemisphereLight's [page:Object3D.matrixWorld matrixWorld].

###  Object matrixAutoUpdate;

See [page:Object3D.matrixAutoUpdate]. Set to `false` here as the helper is
using the hemisphereLight's [page:Object3D.matrixWorld matrixWorld].

###  hex color;

The color parameter passed in the constructor. Default is `undefined`. If this
is changed, the helper's color will update the next time [page:.update update]
is called.

## Methods

See the base [page:Object3D] class for common methods.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function update( ): undefined;

Updates the helper to match the position and direction of the [page:.light].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

