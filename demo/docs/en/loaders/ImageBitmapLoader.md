[Loader](en\loaders\Loader.html) →

# ImageBitmapLoader

A loader for loading an [Image](#) as an <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/ImageBitmap">ImageBitmap</a>. An ImageBitmap provides an
asynchronous and resource efficient pathway to prepare textures for rendering
in WebGL.  
Unlike [FileLoader](en\loaders\FileLoader.html), ImageBitmapLoader does not
avoid multiple concurrent requests to the same URL.

Note that [Texture.flipY](#) and [Texture.premultiplyAlpha](#) with <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/ImageBitmap">ImageBitmap</a> are ignored. <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/ImageBitmap">ImageBitmap</a> needs these configuration on
bitmap creation unlike regular images need them on uploading to GPU. You need
to set the equivalent options via [ImageBitmapLoader.setOptions](#) instead.
Refer to <a
href="https://www.khronos.org/registry/webgl/specs/latest/1.0/#6.10">WebGL
specification</a> for the detail.

## Code Example

  
```ts  
// instantiate a loader const loader = new THREE.ImageBitmapLoader(); // set
options if needed loader.setOptions( { imageOrientation: 'flipY' } ); // load
a image resource loader.load( // resource URL
'textures/skyboxsun25degtest.png', // onLoad callback function ( imageBitmap )
{ const texture = new THREE.CanvasTexture( imageBitmap ); const material = new
THREE.MeshBasicMaterial( { map: texture } ); }, // onProgress callback
currently not supported undefined, // onError callback function ( err ) {
console.log( 'An error happened' ); } );  
```  

## Examples

[example:webgl_loader_imagebitmap WebGL / loader / ImageBitmap]

## Constructor

### ImageBitmapLoader

  
  
```ts  
function ImageBitmapLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new ImageBitmapLoader.

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

### isImageBitmapLoader

  
  
```ts  
isImageBitmapLoader: Boolean;  
```  

Read-only flag to check if a given object is of type ImageBitmapLoader.

### options

  
  
```ts  
options: String;  
```  

An optional object that sets options for the internally used <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/createImageBitmap">createImageBitmap</a>
factory method. Default is `undefined`.

## Methods

See the base [Loader](en\loaders\Loader.html) class for common methods.

### load

  
  
```ts  
function load( url: String, onLoad: Function, onProgress: Function, onError:
Function ): undefined;  
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

### setOptions

  
  
```ts  
function setOptions( options: Object ): this;  
```  

Sets the options object for <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/createImageBitmap">createImageBitmap</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/ImageBitmapLoader.js">src/loaders/ImageBitmapLoader.js</a>

