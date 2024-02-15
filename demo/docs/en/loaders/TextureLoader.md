[Loader](en\loaders\Loader.html) →

# TextureLoader

Class for loading a [texture](en\textures\Texture.html). This uses the
[ImageLoader](en\loaders\ImageLoader.html) internally for loading files.

## Code Example

  
```ts  
const texture = new
THREE.TextureLoader().load('textures/land_ocean_ice_cloud_2048.jpg' ); //
immediately use the texture for material creation const material = new
THREE.MeshBasicMaterial( { map:texture } );  
```  

## Code Example with Callbacks

  
```ts  
// instantiate a loader const loader = new THREE.TextureLoader(); // load a
resource loader.load( // resource URL
'textures/land_ocean_ice_cloud_2048.jpg', // onLoad callback function (
texture ) { // in this example we create the material when the texture is
loaded const material = new THREE.MeshBasicMaterial( { map: texture } ); }, //
onProgress callback currently not supported undefined, // onError callback
function ( err ) { console.error( 'An error happened.' ); } );  
```  

Please note three.js r84 dropped support for TextureLoader progress events.
For a TextureLoader that supports progress events, see <a
href="https://github.com/mrdoob/three.js/issues/10439#issuecomment-293260145">this
thread</a>.

## Examples

[example:webgl_geometry_cube geometry / cube]

## Constructor

### TextureLoader

  
  
```ts  
function TextureLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new TextureLoader.

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

## Methods

See the base [Loader](en\loaders\Loader.html) class for common methods.

### load

  
  
```ts  
function load( url: String, onLoad: Function, onProgress: Function, onError:
Function ): Texture;  
```  

[url](#) — the path or URL to the file. This can also be a <a
href="https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs">Data URI</a>.  
[onLoad](#) (optional) — Will be called when load completes. The argument will
be the loaded [texture](en\textures\Texture.html).  
[onProgress](#) (optional) — This callback function is currently not
supported.  
[onError](#) (optional) — Will be called when load errors.  
  
Begin loading from the given URL and pass the fully loaded
[texture](en\textures\Texture.html) to onLoad. The method also returns a new
texture object which can directly be used for material creation. If you do it
this way, the texture may pop up in your scene once the respective loading
process is finished.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/TextureLoader.js">src/loaders/TextureLoader.js</a>

