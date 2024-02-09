[page:Object3D] →

# [name]

Creates 6 cameras that render to a [page:WebGLCubeRenderTarget].

## Code Example

  
```ts  
  
// Create cube render target  
const cubeRenderTarget = new THREE.WebGLCubeRenderTarget( 128, {
generateMipmaps: true, minFilter: THREE.LinearMipmapLinearFilter } );  
  
// Create cube camera  
const cubeCamera = new THREE.CubeCamera( 1, 100000, cubeRenderTarget );  
scene.add( cubeCamera );  
  
// Create car  
const chromeMaterial = new THREE.MeshLambertMaterial( { color: 0xffffff,
envMap: cubeRenderTarget.texture } );  
const car = new THREE.Mesh( carGeometry, chromeMaterial );  
scene.add( car );  
  
// Update the render target cube  
car.visible = false;  
cubeCamera.position.copy( car.position );  
cubeCamera.update( renderer, scene );  
  
// Render the scene  
car.visible = true;  
renderer.render( scene, camera );  
  
```  

## Examples

[example:webgl_materials_cubemap_dynamic materials / cubemap / dynamic ]

## Constructor

### [name]( [param:Number near], [param:Number far],
[param:WebGLCubeRenderTarget renderTarget] )

near -- The near clipping distance.  
far -- The far clipping distance.  
renderTarget -- The destination cube render target.

Constructs a CubeCamera that contains 6 [page:PerspectiveCamera
PerspectiveCameras] that render to a [page:WebGLCubeRenderTarget].

## Properties

See the base [page:Object3D] class for common properties.

### <br/> WebGLCubeRenderTarget renderTarget; <br/>

The destination cube render target.

## Methods

See the base [page:Object3D] class for common methods.

### [method:undefined update]( [param:WebGLRenderer renderer], [param:Scene
scene] )

renderer -- The current WebGL renderer  
scene -- The current scene

Call this to update the [page:CubeCamera.renderTarget renderTarget].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

