[Loader](en\loaders\Loader.html) →

# AnimationLoader

Class for loading [AnimationClips](en\animation\AnimationClip.html) in JSON
format. This uses the [FileLoader](en\loaders\FileLoader.html) internally for
loading files.

## Code Example

  
```ts  
// instantiate a loader const loader = new THREE.AnimationLoader(); // load a
resource loader.load( // resource URL 'animations/animation.js', // onLoad
callback function ( animations ) { // animations is an array of AnimationClips
}, // onProgress callback function ( xhr ) { console.log( (xhr.loaded /
xhr.total * 100) + '% loaded' ); }, // onError callback function ( err ) {
console.log( 'An error happened' ); } );  
```  

## Constructor

### AnimationLoader

  
  
```ts  
function AnimationLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new AnimationLoader.

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
loaded [animation clips](en\animation\AnimationClip.html).  
[onProgress](#) (optional) — Will be called while load progresses. The
argument will be the ProgressEvent instance, which contains
.[lengthComputable](#), .[total](#) and .[loaded](#). If the server does not
set the Content-Length header; .[total](#) will be 0.  
[onError](#) (optional) — Will be called if load errors.  
  
Begin loading from url and pass the loaded animation to onLoad.

### parse

  
  
```ts  
function parse( json: JSON ): Array;  
```  

[json](#) — required  
  
Parse the JSON object and return an array of animation clips. Individual clips
in the object will be parsed with [AnimationClip.parse](#).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/AnimationLoader.js">src/loaders/AnimationLoader.js</a>

