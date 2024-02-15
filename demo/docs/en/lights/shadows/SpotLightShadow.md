[LightShadow](en\lights\shadows\LightShadow.html) →

# SpotLightShadow

This is used internally by [SpotLights](en\lights\SpotLight.html) for
calculating shadows.

## Code Example

  
```ts  
//Create a WebGLRenderer and turn on shadows in the renderer const renderer =
new THREE.WebGLRenderer(); renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // default
THREE.PCFShadowMap //Create a SpotLight and turn on shadows for the light
const light = new THREE.SpotLight( 0xffffff ); light.castShadow = true; //
default false scene.add( light ); //Set up shadow properties for the light
light.shadow.mapSize.width = 512; // default light.shadow.mapSize.height =
512; // default light.shadow.camera.near = 0.5; // default
light.shadow.camera.far = 500; // default light.shadow.focus = 1; // default
//Create a sphere that cast shadows (but does not receive them) const
sphereGeometry = new THREE.SphereGeometry( 5, 32, 32 ); const sphereMaterial =
new THREE.MeshStandardMaterial( { color: 0xff0000 } ); const sphere = new
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

The constructor creates a [param:PerspectiveCamera PerspectiveCamera] to
manage the shadow's view of the world.

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
  
The default is a [PerspectiveCamera](en\cameras\PerspectiveCamera.html) with
[near](#) clipping plane at `0.5`. The [fov](#) will track the [angle](#)
property of the owning [SpotLight](en\lights\SpotLight.html) via the
[update](#) method. Similarly, the [aspect](#) property will track the aspect
of the [mapSize](#). If the [distance](#) property of the light is set, the
[far](#) clipping plane will track that, otherwise it defaults to `500`.

### focus

  
  
```ts  
focus: Number;  
```  

Used to focus the shadow camera. The camera's field of view is set as a
percentage of the spotlight's field-of-view. Range is `[0, 1]`. Default is
`1.0`.  

### isSpotLightShadow

  
  
```ts  
isSpotLightShadow: Boolean;  
```  

Read-only flag to check if a given object is of type SpotLightShadow.

## Methods

See the base [LightShadow](en\lights\shadows\LightShadow.html) class for
common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/SpotLightShadow.js">src/lights/SpotLightShadow.js</a>

