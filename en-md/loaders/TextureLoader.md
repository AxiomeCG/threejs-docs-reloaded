[page:Loader] →

# TextureLoader

Class for loading a [page:Texture texture]. This uses the [page:ImageLoader]
internally for loading files.

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
For a TextureLoader that supports progress events, see
[link:https://github.com/mrdoob/three.js/issues/10439#issuecomment-293260145
this thread].

## Examples

[example:webgl_geometry_cube geometry / cube]

## Constructor

###  function TextureLoader( manager: LoadingManager ): void;

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].  
  
Creates a new TextureLoader.

## Properties

See the base [page:Loader] class for common properties.

## Methods

See the base [page:Loader] class for common methods.

###  function load( url: String, onLoad: Function, onProgress: Function,
onError: Function ): Texture;

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] (optional) — Will be called when load completes. The
argument will be the loaded [page:Texture texture].  
[page:Function onProgress] (optional) — This callback function is currently
not supported.  
[page:Function onError] (optional) — Will be called when load errors.  
  
Begin loading from the given URL and pass the fully loaded [page:Texture
texture] to onLoad. The method also returns a new texture object which can
directly be used for material creation. If you do it this way, the texture may
pop up in your scene once the respective loading process is finished.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

