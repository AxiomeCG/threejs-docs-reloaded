[page:Texture] →

# CubeTexture

Creates a cube texture made up of six images.

## Code Example

  
```ts  
const loader = new THREE.CubeTextureLoader(); loader.setPath(
'textures/cube/pisa/' ); const textureCube = loader.load( [ 'px.png',
'nx.png', 'py.png', 'ny.png', 'pz.png', 'nz.png' ] ); const material = new
THREE.MeshBasicMaterial( { color: 0xffffff, envMap: textureCube } );  
```  

## Constructor

###  function CubeTexture( ): void;

CubeTexture is almost equivalent in functionality and usage to [page:Texture].
The only differences are that the images are an array of 6 images as opposed
to a single image, and the mapping options are [page:Textures
THREE.CubeReflectionMapping] (default) or [page:Textures
THREE.CubeRefractionMapping]

## Properties

See the base [page:Texture Texture] class for common properties.

###  Boolean flipY;

If set to `true`, the texture is flipped along the vertical axis when uploaded
to the GPU. Default is `false`.

###  Boolean isCubeTexture;

Read-only flag to check if a given object is of type CubeTexture.

## Methods

See the base [page:Texture Texture] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

