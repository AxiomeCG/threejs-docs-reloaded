[page:Object3D] →

# [name]

Helper object to assist with visualizing a [page:DirectionalLight]'s effect on
the scene. This consists of plane and a line representing the light's position
and direction.

## Code Example

  
```ts  
const light = new THREE.DirectionalLight( 0xFFFFFF );  
const helper = new THREE.DirectionalLightHelper( light, 5 );  
scene.add( helper );  
```  

## Constructor

###  [name]( [param:DirectionalLight light], [param:Number size], [param:Hex
color] )

[page:DirectionalLight light]-- The light to be visualized.  
  
[page:Number size] -- (optional) dimensions of the plane. Default is `1`.  
  
[page:Hex color] -- (optional) if this is not the set the helper will take the
color of the light.

## Properties

See the base [page:Object3D] class for common properties.

### <br/> Line lightPlane; <br/>

Contains the line mesh showing the location of the directional light.

### <br/> DirectionalLight light; <br/>

Reference to the [page:DirectionalLight directionalLight] being visualized.

### <br/> Object matrix; <br/>

Reference to the light's [page:Object3D.matrixWorld matrixWorld].

### <br/> Object matrixAutoUpdate; <br/>

See [page:Object3D.matrixAutoUpdate]. Set to `false` here as the helper is
using the light's [page:Object3D.matrixWorld matrixWorld].

### <br/> hex color; <br/>

The color parameter passed in the constructor. Default is `undefined`. If this
is changed, the helper's color will update the next time [page:.update update]
is called.

## Methods

See the base [page:Object3D] class for common properties.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### [method:undefined update]()

Updates the helper to match the position and direction of the [page:.light
directionalLight] being visualized.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

