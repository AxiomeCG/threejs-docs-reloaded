[page:Object3D] →

# SpotLightHelper

This displays a cone shaped helper object for a [page:SpotLight].

## Code Example

  
```ts  
const spotLight = new THREE.SpotLight( 0xffffff ); spotLight.position.set( 10,
10, 10 ); scene.add( spotLight ); const spotLightHelper = new
THREE.SpotLightHelper( spotLight ); scene.add( spotLightHelper );  
```  

## Examples

[example:webgl_lights_spotlights WebGL/ lights / spotlights ]

## Constructor

###  function SpotLightHelper( light: SpotLight, color: Hex ): void;

[page:SpotLight light] -- The [page:SpotLight] to be visualized.  
  
[page:Hex color] -- (optional) if this is not the set the helper will take the
color of the light.

## Properties

See the base [page:Object3D] class for common properties.

###  LineSegments cone;

[page:LineSegments] used to visualize the light.

###  SpotLight light;

Reference to the [page:SpotLight] being visualized.

###  Object matrix;

Reference to the spotLight's [page:Object3D.matrixWorld matrixWorld].

###  Object matrixAutoUpdate;

See [page:Object3D.matrixAutoUpdate]. Set to `false` here as the helper is
using the spotLight's [page:Object3D.matrixWorld matrixWorld].

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

Updates the light helper.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

