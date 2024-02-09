[page:Loader] →

# [name]

Class for loading an [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBuffer AudioBuffer]. This uses the [page:FileLoader]
internally for loading files.

## Code Example

  
```ts  
// instantiate a listener  
const audioListener = new THREE.AudioListener();  
  
// add the listener to the camera  
camera.add( audioListener );  
  
// instantiate audio object  
const oceanAmbientSound = new THREE.Audio( audioListener );  
  
// add the audio object to the scene  
scene.add( oceanAmbientSound );  
  
// instantiate a loader  
const loader = new THREE.AudioLoader();  
  
// load a resource  
loader.load(  
// resource URL  
'audio/ambient_ocean.ogg',  
  
// onLoad callback  
function ( audioBuffer ) {  
// set the audio object buffer to the loaded object  
oceanAmbientSound.setBuffer( audioBuffer );  
  
// play the audio  
oceanAmbientSound.play();  
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
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] — Will be called when load completes. The argument will
be the loaded text response.  
[page:Function onProgress] (optional) — Will be called while load progresses.
The argument will be the ProgressEvent instance, which contains .[page:Boolean
lengthComputable], .[page:Integer total] and .[page:Integer loaded]. If the
server does not set the Content-Length header; .[page:Integer total] will be
0.  
[page:Function onError] (optional) — Will be called when load errors.  

Begin loading from url and pass the loaded [page:String AudioBuffer] to
onLoad.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

