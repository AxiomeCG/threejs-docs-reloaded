[Loader](en\loaders\Loader.html) →

# ObjectLoader

A loader for loading a JSON resource in the <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.  
  
This uses the [FileLoader](en\loaders\FileLoader.html) internally for loading
files.

## Code Example

  
```ts  
const loader = new THREE.ObjectLoader(); loader.load( // resource URL
"models/json/example.json", // onLoad callback // Here the loaded data is
assumed to be an object function ( obj ) { // Add the loaded object to the
scene scene.add( obj ); }, // onProgress callback function ( xhr ) {
console.log( (xhr.loaded / xhr.total * 100) + '% loaded' ); }, // onError
callback function ( err ) { console.error( 'An error happened' ); } ); //
Alternatively, to parse a previously loaded JSON structure const object =
loader.parse( a_json_object ); scene.add( object );  
```  

## Examples

[example:webgl_materials_lightmap WebGL / materials / lightmap]

## Constructor

### ObjectLoader

  
  
```ts  
function ObjectLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new ObjectLoader.

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
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs">Data URI</a>.  
[onLoad](#) — Will be called when load completes. The argument will be the
loaded [object](en\core\Object3D.html).  
[onProgress](#) (optional) — Will be called while load progresses. The
argument will be the ProgressEvent instance, which contains
.[lengthComputable](#), .[total](#) and .[loaded](#). If the server does not
set the Content-Length header; .[total](#) will be 0.  
[onError](#) (optional) — Will be called when load errors.  

Begin loading from url and call onLoad with the parsed response content.

### parse

  
  
```ts  
function parse( json: Object, onLoad: Function ): Object3D;  
```  

[json](#) — required. The JSON source to parse.  
  
[onLoad](#) — Will be called when parsed completes. The argument will be the
parsed [object](en\core\Object3D.html).  
  
Parse a `JSON` structure and return a three.js object. This is used internally
by [.load](#)() but can also be used directly to parse a previously loaded
JSON structure.

### parseGeometries

  
  
```ts  
function parseGeometries( json: Object ): Object;  
```  

[json](#) — required. The JSON source to parse.  
  
This is used by [.parse](#)() to parse any [.ufferGeometry](#ufferGeometry) in
the JSON structure.

### parseMaterials

  
  
```ts  
function parseMaterials( json: Object ): Object;  
```  

[json](#) — required. The JSON source to parse.  
  
This is used by [.parse](#)() to parse any materials in the JSON structure
using [MaterialLoader](en\loaders\MaterialLoader.html).

### parseAnimations

  
  
```ts  
function parseAnimations( json: Object ): Object;  
```  

[json](#) — required. The JSON source to parse.  
  
This is used by [.parse](#)() to parse any animations in the JSON structure,
using [AnimationClip.parse](#)().

### parseImages

  
  
```ts  
function parseImages( json: Object ): Object;  
```  

[json](#) — required. The JSON source to parse.  
  
This is used by [.parse](#)() to parse any images in the JSON structure, using
[ImageLoader](en\loaders\ImageLoader.html).

### parseTextures

  
  
```ts  
function parseTextures( json: Object ): Object;  
```  

[json](#) — required. The JSON source to parse.  
  
This is used by [.parse](#)() to parse any textures in the JSON structure.

### parseObject

  
  
```ts  
function parseObject( json: Object, geometries: BufferGeometry, materials:
Material, animations: AnimationClip ): Object3D;  
```  

[json](#) — required. The JSON source to parse.  
[geometries](en\core\BufferGeometry.html) — required. The geometries of the
JSON.  
[materials](en\materials\Material.html) — required. The materials of the JSON.  
[animations](en\animation\AnimationClip.html) — required. The animations of
the JSON.  
  
This is used by [.parse](#)() to parse any 3D objects in the JSON structure.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/ObjectLoader.js">src/loaders/ObjectLoader.js</a>

