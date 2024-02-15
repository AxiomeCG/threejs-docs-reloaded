[LightShadow](en\lights\shadows\LightShadow.html) →

# DirectionalLightShadow

This is used internally by
[DirectionalLights](en\lights\DirectionalLight.html) for calculating shadows.  
  
Unlike the other shadow classes, this uses an
[OrthographicCamera](en\cameras\OrthographicCamera.html) to calculate the
shadows, rather than a [PerspectiveCamera](en\cameras\PerspectiveCamera.html).
This is because light rays from a
[DirectionalLight](en\lights\DirectionalLight.html) are parallel.

## Code Example

  
```ts  
//Create a WebGLRenderer and turn on shadows in the renderer const renderer =
new THREE.WebGLRenderer(); renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // default
THREE.PCFShadowMap //Create a DirectionalLight and turn on shadows for the
light const light = new THREE.DirectionalLight( 0xffffff, 1 );
light.position.set( 0, 1, 0 ); //default; light shining from top
light.castShadow = true; // default false scene.add( light ); //Set up shadow
properties for the light light.shadow.mapSize.width = 512; // default
light.shadow.mapSize.height = 512; // default light.shadow.camera.near = 0.5;
// default light.shadow.camera.far = 500; // default //Create a sphere that
cast shadows (but does not receive them) const sphereGeometry = new
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

### DirectionalLightShadow

  
  
```ts  
function DirectionalLightShadow( ): void;  
```  

Creates a new DirectionalLightShadow. This is not intended to be called
directly - it is called internally by
[DirectionalLight](en\lights\DirectionalLight.html).

## Properties

See the base [LightShadow](en\lights\shadows\LightShadow.html) class for
common properties.

### camera

  
  
```ts  
camera: Camera;  
```  

The light's view of the world. This is used to generate a depth map of the
scene; objects behind other objects from the light's perspective will be in
shadow.  
  
The default is an [OrthographicCamera](en\cameras\OrthographicCamera.html)
with [left](#) and [bottom](#) set to -5, [right](#) and [top](#) set to `5`,
the [near](#) clipping plane at `0.5` and the [far](#) clipping plane at
`500`.

### isDirectionalLightShadow

  
  
```ts  
isDirectionalLightShadow: Boolean;  
```  

Read-only flag to check if a given object is of type DirectionalLightShadow.

## Methods

See the base [LightShadow](en\lights\shadows\LightShadow.html) class for
common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/DirectionalLightShadow.js">src/lights/DirectionalLightShadow.js</a>

