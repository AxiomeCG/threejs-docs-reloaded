# LoadingManager

Handles and keeps track of loaded and pending data. A default global instance
of this class is created and used by loaders if not supplied manually - see
[DefaultLoadingManager](en\loaders\managers\DefaultLoadingManager.html).  
  
In general that should be sufficient, however there are times when it can be
useful to have separate loaders - for example if you want to show separate
loading bars for objects and textures.

## Code Example

This example shows how to use LoadingManager to track the progress of
[OBJLoader](#).

  
```ts  
const manager = new THREE.LoadingManager(); manager.onStart = function ( url,
itemsLoaded, itemsTotal ) { console.log( 'Started loading file: ' + url +
'.\nLoaded ' + itemsLoaded + ' of ' + itemsTotal + ' files.' ); };
manager.onLoad = function ( ) { console.log( 'Loading complete!'); };
manager.onProgress = function ( url, itemsLoaded, itemsTotal ) { console.log(
'Loading file: ' + url + '.\nLoaded ' + itemsLoaded + ' of ' + itemsTotal + '
files.' ); }; manager.onError = function ( url ) { console.log( 'There was an
error loading ' + url ); }; const loader = new THREE.OBJLoader( manager );
loader.load( 'file.obj', function ( object ) { // } );  
```  

In addition to observing progress, a LoadingManager can be used to override
resource URLs during loading. This may be helpful for assets coming from drag-
and-drop events, WebSockets, WebRTC, or other APIs. An example showing how to
load an in-memory model using Blob URLs is below.

  
```ts  
// Blob or File objects created when dragging files into the webpage. const
blobs = {'fish.gltf': blob1, 'diffuse.png': blob2, 'normal.png': blob3}; const
manager = new THREE.LoadingManager(); // Initialize loading manager with URL
callback. const objectURLs = []; manager.setURLModifier( ( url ) => { url =
URL.createObjectURL( blobs[ url ] ); objectURLs.push( url ); return url; } );
// Load as usual, then revoke the blob URLs. const loader = new
THREE.GLTFLoader( manager ); loader.load( 'fish.gltf', (gltf) => { scene.add(
gltf.scene ); objectURLs.forEach( ( url ) => URL.revokeObjectURL( url ) ); });  
```  

## Examples

[example:webgl_loader_obj WebGL / loader / obj]  
[example:webgl_postprocessing_outline WebGL / postprocesing / outline]

## Constructor

### LoadingManager

  
  
```ts  
function LoadingManager( onLoad: Function, onProgress: Function, onError:
Function ): void;  
```  

[onLoad](#) — (optional) this function will be called when all loaders are
done.  
[onProgress](#) — (optional) this function will be called when an item is
complete.  
[onError](#) — (optional) this function will be called a loader encounters
errors.  
Creates a new LoadingManager.

## Properties

### onStart

  
  
```ts  
onStart: Function;  
```  

This function will be called when loading starts. The arguments are:  
[url](#) — The url of the item just loaded.  
[itemsLoaded](#) — the number of items already loaded so far.  
[itemsTotal](#) — the total amount of items to be loaded.  
  
By default this is undefined.

### onLoad

  
  
```ts  
onLoad: Function;  
```  

This function will be called when all loading is completed. By default this is
undefined, unless passed in the constructor.

### onProgress

  
  
```ts  
onProgress: Function;  
```  

This function will be called when an item is complete. The arguments are:  
[url](#) — The url of the item just loaded.  
[itemsLoaded](#) — the number of items already loaded so far.  
[itemsTotal](#) — the total amount of items to be loaded.  
  
By default this is undefined, unless passed in the constructor.

### onError

  
  
```ts  
onError: Function;  
```  

This function will be called when any item errors, with the argument:  
[url](#) — The url of the item that errored.  
  
By default this is undefined, unless passed in the constructor.

## Methods

### addHandler

  
  
```ts  
function addHandler( regex: Object, loader: Loader ): this;  
```  

[regex](#) — A regular expression.  
[loader](en\loaders\Loader.html) — The loader.

Registers a loader with the given regular expression. Can be used to define
what loader should be used in order to load specific files. A typical use case
is to overwrite the default loader for textures.

  
```ts  
// add handler for TGA textures manager.addHandler( /\\.tga$/i, new
TGALoader() );  
```  

### getHandler

  
  
```ts  
function getHandler( file: String ): Loader;  
```  

[file](#) — The file path.

Can be used to retrieve the registered loader for the given file path.

### removeHandler

  
  
```ts  
function removeHandler( regex: Object ): this;  
```  

[regex](#) — A regular expression.

Removes the loader for the given regular expression.

### resolveURL

  
  
```ts  
function resolveURL( url: String ): String;  
```  

[url](#) — the url to load  
  
Given a URL, uses the URL modifier callback (if any) and returns a resolved
URL. If no URL modifier is set, returns the original URL.

### setURLModifier

  
  
```ts  
function setURLModifier( callback: Function ): this;  
```  

[callback](#) — URL modifier callback. Called with [url](#) argument, and must
return [resolvedURL](#).  
  
If provided, the callback will be passed each resource URL before a request is
sent. The callback may return the original URL, or a new URL to override
loading behavior. This behavior can be used to load assets from .ZIP files,
drag-and-drop APIs, and Data URIs.

  

 _Note: The following methods are designed to be called internally by loaders.
You shouldn't call them directly._

### itemStart

  
  
```ts  
function itemStart( url: String ): undefined;  
```  

[url](#) — the url to load  
  
This should be called by any loader using the manager when the loader starts
loading an url.

### itemEnd

  
  
```ts  
function itemEnd( url: String ): undefined;  
```  

[url](#) — the loaded url  
  
This should be called by any loader using the manager when the loader ended
loading an url.

### itemError

  
  
```ts  
function itemError( url: String ): undefined;  
```  

[url](#) — the loaded url  
  
This should be called by any loader using the manager when the loader errors
loading an url.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/LoadingManager.js">src/loaders/LoadingManager.js</a>

