[Object3D](en\core\Object3D.html) →

# CubeCamera

Creates 6 cameras that render to a
[WebGLCubeRenderTarget](en\renderers\WebGLCubeRenderTarget.html).

## Code Example

  
```ts  
// Create cube render target const cubeRenderTarget = new
THREE.WebGLCubeRenderTarget( 128, { generateMipmaps: true, minFilter:
THREE.LinearMipmapLinearFilter } ); // Create cube camera const cubeCamera =
new THREE.CubeCamera( 1, 100000, cubeRenderTarget ); scene.add( cubeCamera );
// Create car const chromeMaterial = new THREE.MeshLambertMaterial( { color:
0xffffff, envMap: cubeRenderTarget.texture } ); const car = new THREE.Mesh(
carGeometry, chromeMaterial ); scene.add( car ); // Update the render target
cube car.visible = false; cubeCamera.position.copy( car.position );
cubeCamera.update( renderer, scene ); // Render the scene car.visible = true;
renderer.render( scene, camera );  
```  

## Examples

[example:webgl_materials_cubemap_dynamic materials / cubemap / dynamic ]

## Constructor

### CubeCamera

  
  
```ts  
function CubeCamera( near: Number, far: Number, renderTarget:
WebGLCubeRenderTarget ): void;  
```  

near -- The near clipping distance.  
far -- The far clipping distance.  
renderTarget -- The destination cube render target.

Constructs a CubeCamera that contains 6
[PerspectiveCameras](en\cameras\PerspectiveCamera.html) that render to a
[WebGLCubeRenderTarget](en\renderers\WebGLCubeRenderTarget.html).

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### renderTarget

  
  
```ts  
renderTarget: WebGLCubeRenderTarget;  
```  

The destination cube render target.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### update

  
  
```ts  
function update( renderer: WebGLRenderer, scene: Scene ): undefined;  
```  

renderer -- The current WebGL renderer  
scene -- The current scene

Call this to update the [renderTarget](#).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/cameras/CubeCamera.js">src/cameras/CubeCamera.js</a>

