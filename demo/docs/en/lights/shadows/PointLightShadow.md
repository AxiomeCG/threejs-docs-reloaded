[LightShadow](en\lights\shadows\LightShadow.html) →

# PointLightShadow

This is used internally by [PointLights](en\lights\PointLight.html) for
calculating shadows.

## Code Example

  
```ts  
//Create a WebGLRenderer and turn on shadows in the renderer const renderer =
new THREE.WebGLRenderer(); renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // default
THREE.PCFShadowMap //Create a PointLight and turn on shadows for the light
const light = new THREE.PointLight( 0xffffff, 1, 100 ); light.position.set( 0,
10, 4 ); light.castShadow = true; // default false scene.add( light ); //Set
up shadow properties for the light light.shadow.mapSize.width = 512; //
default light.shadow.mapSize.height = 512; // default light.shadow.camera.near
= 0.5; // default light.shadow.camera.far = 500; // default //Create a sphere
that cast shadows (but does not receive them) const sphereGeometry = new
THREE.SphereGeometry( 5, 32, 32 ); const sphereMaterial = new
THREE.MeshStandardMaterial( { color: 0xff0000 } ); const sphere = new
THREE.Mesh( sphereGeometry, sphereMaterial ); sphere.castShadow = true;
//default is false sphere.receiveShadow = false; //default scene.add( sphere
); //Create a plane that receives shadows (but does not cast them) const
planeGeometry = new THREE.PlaneGeometry( 20, 20, 32, 32 ); const planeMaterial
= new THREE.MeshStandardMaterial( { color: 0x00ff00 } ) const plane = new
THREE.Mesh( planeGeometry, planeMaterial ); plane.receiveShadow = true;
scene.add( plane ); //Create a helper for the shadow camera (optional) const
helper = new THREE.CameraHelper( light.shadow.camera ); scene.add( helper );  
```  

## Constructor

### PointLightShadow

  
  
```ts  
function PointLightShadow( ): void;  
```  

Creates a new PointLightShadow. This is not intended to be called directly -
it is called internally by [PointLight](en\lights\PointLight.html).

## Properties

See the base [LightShadow](en\lights\shadows\LightShadow.html) class for
common properties.

### isPointLightShadow

  
  
```ts  
isPointLightShadow: Boolean;  
```  

Read-only flag to check if a given object is of type PointLightShadow.

## Methods

See the base [LightShadow](en\lights\shadows\LightShadow.html) class for
common methods.

### updateMatrices

  
  
```ts  
function updateMatrices( light: Light, viewportIndex: number ): undefined;  
```  

Update the matrices for the camera and shadow, used internally by the
renderer.  
  
light -- the light for which the shadow is being rendered.  
viewportIndex -- calculates the matrix for this viewport

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/PointLightShadow.js">src/lights/PointLightShadow.js</a>

