# [name]

Handles and keeps track of loaded and pending data. A default global instance
of this class is created and used by loaders if not supplied manually - see
[page:DefaultLoadingManager].  
  
In general that should be sufficient, however there are times when it can be
useful to have separate loaders - for example if you want to show separate
loading bars for objects and textures.

## Code Example

This example shows how to use LoadingManager to track the progress of
[page:OBJLoader].

  
```ts  
const manager = new THREE.LoadingManager();  
manager.onStart = function ( url, itemsLoaded, itemsTotal ) {  
console.log( 'Started loading file: ' + url + '.\nLoaded ' + itemsLoaded + '
of ' + itemsTotal + ' files.' );  
};  
  
manager.onLoad = function ( ) {  
console.log( 'Loading complete!');  
};  
  
manager.onProgress = function ( url, itemsLoaded, itemsTotal ) {  
console.log( 'Loading file: ' + url + '.\nLoaded ' + itemsLoaded + ' of ' +
itemsTotal + ' files.' );  
};  
  
manager.onError = function ( url ) {  
console.log( 'There was an error loading ' + url );  
};  
  
const loader = new THREE.OBJLoader( manager );  
loader.load( 'file.obj', function ( object ) {  
//  
} );  
```  

In addition to observing progress, a LoadingManager can be used to override
resource URLs during loading. This may be helpful for assets coming from drag-
and-drop events, WebSockets, WebRTC, or other APIs. An example showing how to
load an in-memory model using Blob URLs is below.

  
```ts  
// Blob or File objects created when dragging files into the webpage.  
const blobs = {'fish.gltf': blob1, 'diffuse.png': blob2, 'normal.png': blob3};  
  
const manager = new THREE.LoadingManager();  
  
// Initialize loading manager with URL callback.  
const objectURLs = [];  
manager.setURLModifier( ( url ) => {  
  
url = URL.createObjectURL( blobs[ url ] );  
objectURLs.push( url );  
return url;  
  
} );  
  
// Load as usual, then revoke the blob URLs.  
const loader = new THREE.GLTFLoader( manager );  
loader.load( 'fish.gltf', (gltf) => {  
  
scene.add( gltf.scene );  
objectURLs.forEach( ( url ) => URL.revokeObjectURL( url ) );  
  
});  
```  

## Examples

[example:webgl_loader_obj WebGL / loader / obj]  
[example:webgl_postprocessing_outline WebGL / postprocesing / outline]

## Constructor

###  [name]( [param:Function onLoad], [param:Function onProgress],
[param:Function onError] )

[page:Function onLoad] — (optional) this function will be called when all
loaders are done.  
[page:Function onProgress] — (optional) this function will be called when an
item is complete.  
[page:Function onError] — (optional) this function will be called a loader
encounters errors.  
Creates a new [name].

## Properties

### <br/> Function onStart; <br/>

This function will be called when loading starts. The arguments are:  
[page:String url] — The url of the item just loaded.  
[page:Integer itemsLoaded] — the number of items already loaded so far.  
[page:Integer itemsTotal] — the total amount of items to be loaded.  
  
By default this is undefined.

### <br/> Function onLoad; <br/>

This function will be called when all loading is completed. By default this is
undefined, unless passed in the constructor.

### <br/> Function onProgress; <br/>

This function will be called when an item is complete. The arguments are:  
[page:String url] — The url of the item just loaded.  
[page:Integer itemsLoaded] — the number of items already loaded so far.  
[page:Integer itemsTotal] — the total amount of items to be loaded.  
  
By default this is undefined, unless passed in the constructor.

### <br/> Function onError; <br/>

This function will be called when any item errors, with the argument:  
[page:String url] — The url of the item that errored.  
  
By default this is undefined, unless passed in the constructor.

## Methods

### <br/> function addHandler( regex: Object, loader: Loader ): addHandler;
<br/>

[page:Object regex] — A regular expression.  
[page:Loader loader] — The loader.

Registers a loader with the given regular expression. Can be used to define
what loader should be used in order to load specific files. A typical use case
is to overwrite the default loader for textures.

  
```ts  
// add handler for TGA textures  
manager.addHandler( /\\.tga$/i, new TGALoader() );  
```  

### [method:Loader getHandler]( [param:String file] )

[page:String file] — The file path.

Can be used to retrieve the registered loader for the given file path.

### <br/> function removeHandler( regex: Object ): removeHandler; <br/>

[page:Object regex] — A regular expression.

Removes the loader for the given regular expression.

### [method:String resolveURL]( [param:String url] )

[page:String url] — the url to load  
  
Given a URL, uses the URL modifier callback (if any) and returns a resolved
URL. If no URL modifier is set, returns the original URL.

### <br/> function setURLModifier( callback: Function ): setURLModifier; <br/>

[page:Function callback] — URL modifier callback. Called with [page:String
url] argument, and must return [page:String resolvedURL].  
  
If provided, the callback will be passed each resource URL before a request is
sent. The callback may return the original URL, or a new URL to override
loading behavior. This behavior can be used to load assets from .ZIP files,
drag-and-drop APIs, and Data URIs.

  

_Note: The following methods are designed to be called internally by loaders.
You shouldn't call them directly._

### [method:undefined itemStart]( [param:String url] )

[page:String url] — the url to load  
  
This should be called by any loader using the manager when the loader starts
loading an url.

### [method:undefined itemEnd]( [param:String url] )

[page:String url] — the loaded url  
  
This should be called by any loader using the manager when the loader ended
loading an url.

### [method:undefined itemError]( [param:String url] )

[page:String url] — the loaded url  
  
This should be called by any loader using the manager when the loader errors
loading an url.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/loaders/LoadingManager.js
src/loaders/LoadingManager.js]

