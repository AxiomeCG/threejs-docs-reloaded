[page:Loader] →

# MaterialLoader

A loader for loading a [page:Material] in JSON format. This uses the
[page:FileLoader] internally for loading files.

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

###  function MaterialLoader( manager: LoadingManager ): void;

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].  
  
Creates a new MaterialLoader.

## Properties

See the base [page:Loader] class for common properties.

###  Object textures;

Object holding any textures used by the material. See [page:.setTextures].

## Methods

See the base [page:Loader] class for common methods.

###  function load( url: String, onLoad: Function, onProgress: Function,
onError: Function ): undefined;

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] — Will be called when load completes. The argument will
be the loaded [page:Material].  
[page:Function onProgress] (optional) — Will be called while load progresses.
The argument will be the ProgressEvent instance, which contains .[page:Boolean
lengthComputable], .[page:Integer total] and .[page:Integer loaded]. If the
server does not set the Content-Length header; .[page:Integer total] will be
0.  
[page:Function onError] (optional) — Will be called when load errors.  
  
Begin loading from url.

###  function parse( json: Object ): Material;

[page:Object json] — The json object containing the parameters of the
Material.  
  
Parse a `JSON` structure and create a new [page:Material] of the type
[page:String json.type] with parameters defined in the json object.

###  function setTextures( textures: Object ): this;

[page:Object textures] — object containing any textures used by the material.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

