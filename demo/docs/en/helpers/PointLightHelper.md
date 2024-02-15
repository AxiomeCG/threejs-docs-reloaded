[Object3D](en\core\Object3D.html) → [Mesh](en\objects\Mesh.html) →

# PointLightHelper

This displays a helper object consisting of a spherical
[Mesh](en\objects\Mesh.html) for visualizing a
[PointLight](en\lights\PointLight.html).

## Code Example

  
```ts  
const pointLight = new THREE.PointLight( 0xff0000, 1, 100 );
pointLight.position.set( 10, 10, 10 ); scene.add( pointLight ); const
sphereSize = 1; const pointLightHelper = new THREE.PointLightHelper(
pointLight, sphereSize ); scene.add( pointLightHelper );  
```  

## Examples

[example:webgl_helpers WebGL / helpers]

## Constructor

### PointLightHelper

  
  
```ts  
function PointLightHelper( light: PointLight, sphereSize: Float, color: Hex ):
void;  
```  

[light](en\lights\PointLight.html) -- The light to be visualized.  
  
[sphereSize](#) -- (optional) The size of the sphere helper. Default is `1`.  
  
[color](#) -- (optional) if this is not the set the helper will take the color
of the light.

## Properties

See the base [Mesh](en\objects\Mesh.html) class for common properties.

### light

  
  
```ts  
light: PointLight;  
```  

The [PointLight](en\lights\PointLight.html) that is being visualized.

### matrix

  
  
```ts  
matrix: Object;  
```  

Reference to the pointLight's [matrixWorld](#).

### matrixAutoUpdate

  
  
```ts  
matrixAutoUpdate: Object;  
```  

See [Object3D.matrixAutoUpdate](#). Set to `false` here as the helper is using
the pointLight's [matrixWorld](#).

### color

  
  
```ts  
color: hex;  
```  

The color parameter passed in the constructor. Default is `undefined`. If this
is changed, the helper's color will update the next time [.update](#update) is
called.

## Methods

See the base [Mesh](en\objects\Mesh.html) class for common methods.

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

Updates the helper to match the position of the [.light](#).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/PointLightHelper.js">src/helpers/PointLightHelper.js</a>

