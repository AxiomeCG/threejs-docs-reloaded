[Loader](en\loaders\Loader.html) →

# ImageLoader

A loader for loading an [Image](#). This is used internally by the
[CubeTextureLoader](en\loaders\CubeTextureLoader.html),
[ObjectLoader](en\loaders\ObjectLoader.html) and
[TextureLoader](en\loaders\TextureLoader.html).

## Code Example

  
```ts  
// instantiate a loader const loader = new THREE.ImageLoader(); // load a
image resource loader.load( // resource URL 'textures/skyboxsun25degtest.png',
// onLoad callback function ( image ) { // use the image, e.g. draw part of it
on a canvas const canvas = document.createElement( 'canvas' ); const context =
canvas.getContext( '2d' ); context.drawImage( image, 100, 100 ); }, //
onProgress callback currently not supported undefined, // onError callback
function () { console.error( 'An error happened.' ); } );  
```  

Please note three.js r84 dropped support for ImageLoader progress events. For
an ImageLoader that supports progress events, see <a
href="https://github.com/mrdoob/three.js/issues/10439#issuecomment-275785639">this
thread</a>.

## Examples

[example:webgl_loader_obj WebGL / loader / obj]  
[example:webgl_shaders_ocean WebGL / shaders / ocean]

## Constructor

### ImageLoader

  
  
```ts  
function ImageLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new ImageLoader.

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

## Methods

See the base [Loader](en\loaders\Loader.html) class for common methods.

### load

  
  
```ts  
function load( url: String, onLoad: Function, onProgress: Function, onError:
Function ): HTMLImageElement;  
```  

[url](#) — the path or URL to the file. This can also be a <a
href="https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs">Data URI</a>.  
[onLoad](#) — Will be called when load completes. The argument will be the
loaded [image](#).  
[onProgress](#) (optional) — This callback function is currently not
supported.  
[onError](#) (optional) — Will be called when load errors.  

Begin loading from url and return the [image](#) object that will contain the
data.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/ImageLoader.js">src/loaders/ImageLoader.js</a>

