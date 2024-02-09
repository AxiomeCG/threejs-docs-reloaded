[page:Loader] →

# [name]

A loader for loading an [page:Image] as an
[link:https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap
ImageBitmap]. An ImageBitmap provides an asynchronous and resource efficient
pathway to prepare textures for rendering in WebGL.  
Unlike [page:FileLoader], [name] does not avoid multiple concurrent requests
to the same URL.

Note that [page:Texture.flipY] and [page:Texture.premultiplyAlpha] with
[link:https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap
ImageBitmap] are ignored. [link:https://developer.mozilla.org/en-
US/docs/Web/API/ImageBitmap ImageBitmap] needs these configuration on bitmap
creation unlike regular images need them on uploading to GPU. You need to set
the equivalent options via [page:ImageBitmapLoader.setOptions] instead. Refer
to [link:https://www.khronos.org/registry/webgl/specs/latest/1.0/#6.10 WebGL
specification] for the detail.

## Code Example

  
```ts  
// instantiate a loader  
const loader = new THREE.ImageBitmapLoader();  
  
// set options if needed  
loader.setOptions( { imageOrientation: 'flipY' } );  
  
// load a image resource  
loader.load(  
// resource URL  
'textures/skyboxsun25degtest.png',  
  
// onLoad callback  
function ( imageBitmap ) {  
const texture = new THREE.CanvasTexture( imageBitmap );  
const material = new THREE.MeshBasicMaterial( { map: texture } );  
},  
  
// onProgress callback currently not supported  
undefined,  
  
// onError callback  
function ( err ) {  
console.log( 'An error happened' );  
}  
);  
```  

## Examples

[example:webgl_loader_imagebitmap WebGL / loader / ImageBitmap]

## Constructor

### [name]( [param:LoadingManager manager] )

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].  
  
Creates a new [name].

## Properties

See the base [page:Loader] class for common properties.

### <br/> Boolean isImageBitmapLoader; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> String options; <br/>

An optional object that sets options for the internally used
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/createImageBitmap createImageBitmap]
factory method. Default is `undefined`.

## Methods

See the base [page:Loader] class for common methods.

###  [method:undefined load]( [param:String url], [param:Function onLoad],
[param:Function onProgress], [param:Function onError] )

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] — Will be called when load completes. The argument will
be the loaded [page:Image image].  
[page:Function onProgress] (optional) — This callback function is currently
not supported.  
[page:Function onError] (optional) — Will be called when load errors.  

Begin loading from url and return the [page:ImageBitmap image] object that
will contain the data.

### <br/> function setOptions( options: Object ): setOptions; <br/>

Sets the options object for [link:https://developer.mozilla.org/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/createImageBitmap
createImageBitmap].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

