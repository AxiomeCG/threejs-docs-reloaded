[page:Loader] →

# [name]

A loader for loading a JSON resource in the
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].  
  
This uses the [page:FileLoader] internally for loading files.

## Code Example

  
```ts  
const loader = new THREE.ObjectLoader();  
  
loader.load(  
// resource URL  
"models/json/example.json",  
  
// onLoad callback  
// Here the loaded data is assumed to be an object  
function ( obj ) {  
// Add the loaded object to the scene  
scene.add( obj );  
},  
  
// onProgress callback  
function ( xhr ) {  
console.log( (xhr.loaded / xhr.total * 100) + '% loaded' );  
},  
  
// onError callback  
function ( err ) {  
console.error( 'An error happened' );  
}  
);  
  
  
// Alternatively, to parse a previously loaded JSON structure  
const object = loader.parse( a_json_object );  
  
scene.add( object );  
```  

## Examples

[example:webgl_materials_lightmap WebGL / materials / lightmap]

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
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] — Will be called when load completes. The argument will
be the loaded [page:Object3D object].  
[page:Function onProgress] (optional) — Will be called while load progresses.
The argument will be the ProgressEvent instance, which contains .[page:Boolean
lengthComputable], .[page:Integer total] and .[page:Integer loaded]. If the
server does not set the Content-Length header; .[page:Integer total] will be
0.  
[page:Function onError] (optional) — Will be called when load errors.  

Begin loading from url and call onLoad with the parsed response content.

###  [method:Object3D parse]( [param:Object json], [param:Function onLoad] )

[page:Object json] — required. The JSON source to parse.  
  
[page:Function onLoad] — Will be called when parsed completes. The argument
will be the parsed [page:Object3D object].  
  
Parse a `JSON` structure and return a three.js object. This is used internally
by [page:.load]() but can also be used directly to parse a previously loaded
JSON structure.

### [method:Object parseGeometries]( [param:Object json] )

[page:Object json] — required. The JSON source to parse.  
  
This is used by [page:.parse]() to parse any [page:BufferGeometry geometries]
in the JSON structure.

### [method:Object parseMaterials]( [param:Object json] )

[page:Object json] — required. The JSON source to parse.  
  
This is used by [page:.parse]() to parse any materials in the JSON structure
using [page:MaterialLoader].

### [method:Object parseAnimations]( [param:Object json] )

[page:Object json] — required. The JSON source to parse.  
  
This is used by [page:.parse]() to parse any animations in the JSON structure,
using [page:AnimationClip.parse]().

### [method:Object parseImages]( [param:Object json] )

[page:Object json] — required. The JSON source to parse.  
  
This is used by [page:.parse]() to parse any images in the JSON structure,
using [page:ImageLoader].

### [method:Object parseTextures]( [param:Object json] )

[page:Object json] — required. The JSON source to parse.  
  
This is used by [page:.parse]() to parse any textures in the JSON structure.

###  [method:Object3D parseObject]( [param:Object json], [param:BufferGeometry
geometries], [param:Material materials], [param:AnimationClip animations] )

[page:Object json] — required. The JSON source to parse.  
[page:BufferGeometry geometries] — required. The geometries of the JSON.  
[page:Material materials] — required. The materials of the JSON.  
[page:AnimationClip animations] — required. The animations of the JSON.  
  
This is used by [page:.parse]() to parse any 3D objects in the JSON structure.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

