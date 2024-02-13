[page:LightShadow] →

# SpotLightShadow

This is used internally by [page:SpotLight SpotLights] for calculating
shadows.

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

See the base [page:LightShadow LightShadow] class for common properties.

###  Camera camera;

The light's view of the world. This is used to generate a depth map of the
scene; objects behind other objects from the light's perspective will be in
shadow.  
  
The default is a [page:PerspectiveCamera] with [page:PerspectiveCamera.near
near] clipping plane at `0.5`. The [page:PerspectiveCamera.fov fov] will track
the [page:SpotLight.angle angle] property of the owning [page:SpotLight
SpotLight] via the [page:SpotLightShadow.update update] method. Similarly, the
[page:PerspectiveCamera.aspect aspect] property will track the aspect of the
[page:LightShadow.mapSize mapSize]. If the [page:SpotLight.distance distance]
property of the light is set, the [page:PerspectiveCamera.far far] clipping
plane will track that, otherwise it defaults to `500`.

###  Number focus;

Used to focus the shadow camera. The camera's field of view is set as a
percentage of the spotlight's field-of-view. Range is `[0, 1]`. Default is
`1.0`.  

###  Boolean isSpotLightShadow;

Read-only flag to check if a given object is of type SpotLightShadow.

## Methods

See the base [page:LightShadow LightShadow] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/lights/SpotLightShadow.js
src/lights/SpotLightShadow.js]

