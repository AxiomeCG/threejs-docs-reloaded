[Loader](en\loaders\Loader.html) →

# CubeTextureLoader

CubeTextureLoader can be used to load cube maps. The loader returns an
instance of [CubeTexture](en\textures\CubeTexture.html) and expects the cube
map to be defined as six separate images representing the sides of a cube.
Other cube map definitions like vertical and horizontal cross, column and row
layouts are not supported.

The loaded [CubeTexture](en\textures\CubeTexture.html) is in sRGB color space.
Meaning the [colorSpace](#) property is set to `THREE.SRGBColorSpace` by
default.

## Code Example

  
```ts  
const scene = new THREE.Scene();scene.background = new
THREE.CubeTextureLoader() .setPath( 'textures/cubeMaps/' ) .load( [ 'px.png',
'nx.png', 'py.png', 'ny.png', 'pz.png', 'nz.png' ] );  
```  

## Examples

[example:webgl_materials_cubemap materials / cubemap]  
[example:webgl_materials_cubemap_dynamic materials / cubemap / dynamic]  
[example:webgl_materials_cubemap_refraction materials / cubemap / refraction]

## Constructor

### CubeTextureLoader

  
  
```ts  
function CubeTextureLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new CubeTextureLoader.

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

## Methods

See the base [Loader](en\loaders\Loader.html) class for common methods.

### load

  
  
```ts  
function load( urls: String, onLoad: Function, onProgress: Function, onError:
Function ): CubeTexture;  
```  

[urls](#) — array of 6 urls to images, one for each side of the CubeTexture.
The urls should be specified in the following order: pos-x, neg-x, pos-y,
neg-y, pos-z, neg-z. They can also be <a
href="https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs">Data URIs</a>.  
Note that, by convention, cube maps are specified in a coordinate system in
which positive-x is to the right when looking up the positive-z axis -- in
other words, using a left-handed coordinate system. Since three.js uses a
right-handed coordinate system, environment maps used in three.js will have
pos-x and neg-x swapped.  
[onLoad](#) (optional) — Will be called when load completes. The argument will
be the loaded [texture](en\textures\CubeTexture.html).  
[onProgress](#) (optional) — This callback function is currently not
supported.  
[onError](#) (optional) — Will be called when load errors.  

Begin loading from url and pass the loaded
[texture](en\textures\CubeTexture.html) to onLoad. The method also returns a
new texture object which can directly be used for material creation.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/CubeTextureLoader.js">src/loaders/CubeTextureLoader.js</a>

