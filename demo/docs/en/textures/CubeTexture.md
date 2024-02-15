[Texture](en\textures\Texture.html) →

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

### CubeTexture

  
  
```ts  
function CubeTexture( ): void;  
```  

CubeTexture is almost equivalent in functionality and usage to
[Texture](en\textures\Texture.html). The only differences are that the images
are an array of 6 images as opposed to a single image, and the mapping options
are [THREE.CubeReflectionMapping](en\constants\Textures.html) (default) or
[THREE.CubeRefractionMapping](en\constants\Textures.html)

## Properties

See the base [Texture](en\textures\Texture.html) class for common properties.

### flipY

  
  
```ts  
flipY: Boolean;  
```  

If set to `true`, the texture is flipped along the vertical axis when uploaded
to the GPU. Default is `false`.

### isCubeTexture

  
  
```ts  
isCubeTexture: Boolean;  
```  

Read-only flag to check if a given object is of type CubeTexture.

## Methods

See the base [Texture](en\textures\Texture.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/CubeTexture.js">src/textures/CubeTexture.js</a>

