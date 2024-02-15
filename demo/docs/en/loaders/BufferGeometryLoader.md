[Loader](en\loaders\Loader.html) →

# BufferGeometryLoader

A loader for loading a [BufferGeometry](en\core\BufferGeometry.html). This
uses the [FileLoader](en\loaders\FileLoader.html) internally for loading
files.

## Code Example

  
```ts  
// instantiate a loader const loader = new THREE.BufferGeometryLoader(); //
load a resource loader.load( // resource URL 'models/json/pressure.json', //
onLoad callback function ( geometry ) { const material = new
THREE.MeshLambertMaterial( { color: 0xF5F5F5 } ); const object = new
THREE.Mesh( geometry, material ); scene.add( object ); }, // onProgress
callback function ( xhr ) { console.log( (xhr.loaded / xhr.total * 100) + '%
loaded' ); }, // onError callback function ( err ) { console.log( 'An error
happened' ); } );  
```  

## Constructor

### BufferGeometryLoader

  
  
```ts  
function BufferGeometryLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).

Creates a new BufferGeometryLoader.

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

## Methods

See the base [Loader](en\loaders\Loader.html) class for common methods.

### load

  
  
```ts  
function load( url: String, onLoad: Function, onProgress: Function, onError:
Function ): undefined;  
```  

[url](#) — the path or URL to the file. This can also be a <a
href="https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs">Data URI</a>.d  
[onLoad](#) — Will be called when load completes. The argument will be the
loaded [BufferGeometry](en\core\BufferGeometry.html).  
[onProgress](#) (optional) — Will be called while load progresses. The
argument will be the ProgressEvent instance, which contains
.[lengthComputable](#), .[total](#) and .[loaded](#). If the server does not
set the Content-Length header; .[total](#) will be 0.  
[onError](#) (optional) — Will be called when load errors.  

Begin loading from url and call onLoad with the parsed response content.

### parse

  
  
```ts  
function parse( json: Object ): BufferGeometry;  
```  

[json](#) — The `JSON` structure to parse.  
  
Parse a `JSON` structure and return a
[BufferGeometry](en\core\BufferGeometry.html).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/BufferGeometryLoader.js">src/loaders/BufferGeometryLoader.js</a>

