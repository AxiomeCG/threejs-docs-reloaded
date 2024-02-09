[page:Object3D] →

# [name]

Creates a visual aid consisting of a spherical [page:Mesh] for a
[page:HemisphereLight HemisphereLight].

## Code Example

  
```ts  
const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1 );  
const helper = new THREE.HemisphereLightHelper( light, 5 );  
scene.add( helper );  
```  

## Constructor

###  [name]( [param:HemisphereLight light], [param:Number sphereSize],
[param:Hex color] )

[page:HemisphereLight light] -- The light being visualized.  
  
[page:Number size] -- The size of the mesh used to visualize the light.  
  
[page:Hex color] -- (optional) if this is not the set the helper will take the
color of the light.

## Properties

See the base [page:Object3D] class for common properties.

### <br/> HemisphereLight light; <br/>

Reference to the HemisphereLight being visualized.

### <br/> Object matrix; <br/>

Reference to the hemisphereLight's [page:Object3D.matrixWorld matrixWorld].

### <br/> Object matrixAutoUpdate; <br/>

See [page:Object3D.matrixAutoUpdate]. Set to `false` here as the helper is
using the hemisphereLight's [page:Object3D.matrixWorld matrixWorld].

### <br/> hex color; <br/>

The color parameter passed in the constructor. Default is `undefined`. If this
is changed, the helper's color will update the next time [page:.update update]
is called.

## Methods

See the base [page:Object3D] class for common methods.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### [method:undefined update]()

Updates the helper to match the position and direction of the [page:.light].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

