[page:Object3D] → [page:Mesh] →

# [name]

This displays a helper object consisting of a spherical [page:Mesh] for
visualizing a [page:PointLight].

## Code Example

  
```ts  
const pointLight = new THREE.PointLight( 0xff0000, 1, 100 );  
pointLight.position.set( 10, 10, 10 );  
scene.add( pointLight );  
  
const sphereSize = 1;  
const pointLightHelper = new THREE.PointLightHelper( pointLight, sphereSize );  
scene.add( pointLightHelper );  
```  

## Examples

[example:webgl_helpers WebGL / helpers]

## Constructor

###  [name]( [param:PointLight light], [param:Float sphereSize], [param:Hex
color] )

[page:PointLight light] -- The light to be visualized.  
  
[page:Float sphereSize] -- (optional) The size of the sphere helper. Default
is `1`.  
  
[page:Hex color] -- (optional) if this is not the set the helper will take the
color of the light.

## Properties

See the base [page:Mesh] class for common properties.

### <br/> PointLight light; <br/>

The [page:PointLight] that is being visualized.

### <br/> Object matrix; <br/>

Reference to the pointLight's [page:Object3D.matrixWorld matrixWorld].

### <br/> Object matrixAutoUpdate; <br/>

See [page:Object3D.matrixAutoUpdate]. Set to `false` here as the helper is
using the pointLight's [page:Object3D.matrixWorld matrixWorld].

### <br/> hex color; <br/>

The color parameter passed in the constructor. Default is `undefined`. If this
is changed, the helper's color will update the next time [page:.update update]
is called.

## Methods

See the base [page:Mesh] class for common methods.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### [method:undefined update]()

Updates the helper to match the position of the [page:.light].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

