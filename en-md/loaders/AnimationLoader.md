[page:Loader] →

# AnimationLoader

Class for loading [page:AnimationClip AnimationClips] in JSON format. This
uses the [page:FileLoader] internally for loading files.

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

###  function AnimationLoader( manager: LoadingManager ): void;

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].  
  
Creates a new AnimationLoader.

## Properties

See the base [page:Loader] class for common properties.

## Methods

See the base [page:Loader] class for common methods.

###  function load( url: String, onLoad: Function, onProgress: Function,
onError: Function ): undefined;

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] — Will be called when load completes. The argument will
be the loaded [page:AnimationClip animation clips].  
[page:Function onProgress] (optional) — Will be called while load progresses.
The argument will be the ProgressEvent instance, which contains .[page:Boolean
lengthComputable], .[page:Integer total] and .[page:Integer loaded]. If the
server does not set the Content-Length header; .[page:Integer total] will be
0.  
[page:Function onError] (optional) — Will be called if load errors.  
  
Begin loading from url and pass the loaded animation to onLoad.

###  function parse( json: JSON ): Array;

[page:JSON json] — required  
  
Parse the JSON object and return an array of animation clips. Individual clips
in the object will be parsed with [page:AnimationClip.parse].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

