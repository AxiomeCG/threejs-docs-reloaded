[Loader](en\loaders\Loader.html) →

# MaterialLoader

A loader for loading a [Material](en\materials\Material.html) in JSON format.
This uses the [FileLoader](en\loaders\FileLoader.html) internally for loading
files.

## Code Example

  
```ts  
// instantiate a loader const loader = new THREE.MaterialLoader(); // load a
resource loader.load( // resource URL 'path/to/material.json', // onLoad
callback function ( material ) { object.material = material; }, // onProgress
callback function ( xhr ) { console.log( (xhr.loaded / xhr.total * 100) + '%
loaded' ); }, // onError callback function ( err ) { console.log( 'An error
happened' ); } );  
```  

## Constructor

### MaterialLoader

  
  
```ts  
function MaterialLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new MaterialLoader.

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

### textures

  
  
```ts  
textures: Object;  
```  

Object holding any textures used by the material. See [.setTextures](#).

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
loaded [Material](en\materials\Material.html).  
[onProgress](#) (optional) — Will be called while load progresses. The
argument will be the ProgressEvent instance, which contains
.[lengthComputable](#), .[total](#) and .[loaded](#). If the server does not
set the Content-Length header; .[total](#) will be 0.  
[onError](#) (optional) — Will be called when load errors.  
  
Begin loading from url.

### parse

  
  
```ts  
function parse( json: Object ): Material;  
```  

[json](#) — The json object containing the parameters of the Material.  
  
Parse a `JSON` structure and create a new
[Material](en\materials\Material.html) of the type [json.type](#) with
parameters defined in the json object.

### setTextures

  
  
```ts  
function setTextures( textures: Object ): this;  
```  

[textures](#) — object containing any textures used by the material.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/MaterialLoader.js">src/loaders/MaterialLoader.js</a>

