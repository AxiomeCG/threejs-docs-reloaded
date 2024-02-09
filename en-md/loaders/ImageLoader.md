[page:Loader] →

# [name]

A loader for loading an [page:Image]. This is used internally by the
[page:CubeTextureLoader], [page:ObjectLoader] and [page:TextureLoader].

## Code Example

  
```ts  
// instantiate a loader  
const loader = new THREE.ImageLoader();  
  
// load a image resource  
loader.load(  
// resource URL  
'textures/skyboxsun25degtest.png',  
  
// onLoad callback  
function ( image ) {  
// use the image, e.g. draw part of it on a canvas  
const canvas = document.createElement( 'canvas' );  
const context = canvas.getContext( '2d' );  
context.drawImage( image, 100, 100 );  
},  
  
// onProgress callback currently not supported  
undefined,  
  
// onError callback  
function () {  
console.error( 'An error happened.' );  
}  
);  
```  

Please note three.js r84 dropped support for ImageLoader progress events. For
an ImageLoader that supports progress events, see
[link:https://github.com/mrdoob/three.js/issues/10439#issuecomment-275785639
this thread].

## Examples

[example:webgl_loader_obj WebGL / loader / obj]  
[example:webgl_shaders_ocean WebGL / shaders / ocean]

## Constructor

### [name]( [param:LoadingManager manager] )

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].  
  
Creates a new [name].

## Properties

See the base [page:Loader] class for common properties.

## Methods

See the base [page:Loader] class for common methods.

###  [method:HTMLImageElement load]( [param:String url], [param:Function
onLoad], [param:Function onProgress], [param:Function onError] )

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] — Will be called when load completes. The argument will
be the loaded [page:Image image].  
[page:Function onProgress] (optional) — This callback function is currently
not supported.  
[page:Function onError] (optional) — Will be called when load errors.  

Begin loading from url and return the [page:Image image] object that will
contain the data.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

