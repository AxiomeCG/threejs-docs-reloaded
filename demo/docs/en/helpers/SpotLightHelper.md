[Object3D](en\core\Object3D.html) →

# SpotLightHelper

This displays a cone shaped helper object for a
[SpotLight](en\lights\SpotLight.html).

## Code Example

  
```ts  
const spotLight = new THREE.SpotLight( 0xffffff ); spotLight.position.set( 10,
10, 10 ); scene.add( spotLight ); const spotLightHelper = new
THREE.SpotLightHelper( spotLight ); scene.add( spotLightHelper );  
```  

## Examples

[example:webgl_lights_spotlights WebGL/ lights / spotlights ]

## Constructor

### SpotLightHelper

  
  
```ts  
function SpotLightHelper( light: SpotLight, color: Hex ): void;  
```  

[light](en\lights\SpotLight.html) -- The [SpotLight](en\lights\SpotLight.html)
to be visualized.  
  
[color](#) -- (optional) if this is not the set the helper will take the color
of the light.

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### cone

  
  
```ts  
cone: LineSegments;  
```  

[LineSegments](en\objects\LineSegments.html) used to visualize the light.

### light

  
  
```ts  
light: SpotLight;  
```  

Reference to the [SpotLight](en\lights\SpotLight.html) being visualized.

### matrix

  
  
```ts  
matrix: Object;  
```  

Reference to the spotLight's [matrixWorld](#).

### matrixAutoUpdate

  
  
```ts  
matrixAutoUpdate: Object;  
```  

See [Object3D.matrixAutoUpdate](#). Set to `false` here as the helper is using
the spotLight's [matrixWorld](#).

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

Updates the light helper.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/SpotLightHelper.js">src/helpers/SpotLightHelper.js</a>

