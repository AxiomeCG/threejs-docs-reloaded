[page:Loader] →

# [name]

A loader for loading a [page:BufferGeometry]. This uses the [page:FileLoader]
internally for loading files.

## Code Example

  
```ts  
// instantiate a loader  
const loader = new THREE.BufferGeometryLoader();  
  
// load a resource  
loader.load(  
// resource URL  
'models/json/pressure.json',  
  
// onLoad callback  
function ( geometry ) {  
const material = new THREE.MeshLambertMaterial( { color: 0xF5F5F5 } );  
const object = new THREE.Mesh( geometry, material );  
scene.add( object );  
},  
  
// onProgress callback  
function ( xhr ) {  
console.log( (xhr.loaded / xhr.total * 100) + '% loaded' );  
},  
  
// onError callback  
function ( err ) {  
console.log( 'An error happened' );  
}  
);  
```  

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

###  [method:undefined load]( [param:String url], [param:Function onLoad],
[param:Function onProgress], [param:Function onError] )

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].d  
[page:Function onLoad] — Will be called when load completes. The argument will
be the loaded [page:BufferGeometry].  
[page:Function onProgress] (optional) — Will be called while load progresses.
The argument will be the ProgressEvent instance, which contains .[page:Boolean
lengthComputable], .[page:Integer total] and .[page:Integer loaded]. If the
server does not set the Content-Length header; .[page:Integer total] will be
0.  
[page:Function onError] (optional) — Will be called when load errors.  

Begin loading from url and call onLoad with the parsed response content.

### [method:BufferGeometry parse]( [param:Object json] )

[page:Object json] — The `JSON` structure to parse.  
  
Parse a `JSON` structure and return a [page:BufferGeometry].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

