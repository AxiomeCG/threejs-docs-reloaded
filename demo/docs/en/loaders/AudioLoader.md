[Loader](en\loaders\Loader.html) →

# AudioLoader

Class for loading an <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBuffer">AudioBuffer</a>. This uses the
[FileLoader](en\loaders\FileLoader.html) internally for loading files.

## Code Example

  
```ts  
// instantiate a listener const audioListener = new THREE.AudioListener(); //
add the listener to the camera camera.add( audioListener ); // instantiate
audio object const oceanAmbientSound = new THREE.Audio( audioListener ); //
add the audio object to the scene scene.add( oceanAmbientSound ); //
instantiate a loader const loader = new THREE.AudioLoader(); // load a
resource loader.load( // resource URL 'audio/ambient_ocean.ogg', // onLoad
callback function ( audioBuffer ) { // set the audio object buffer to the
loaded object oceanAmbientSound.setBuffer( audioBuffer ); // play the audio
oceanAmbientSound.play(); }, // onProgress callback function ( xhr ) {
console.log( (xhr.loaded / xhr.total * 100) + '% loaded' ); }, // onError
callback function ( err ) { console.log( 'An error happened' ); } );  
```  

## Constructor

### AudioLoader

  
  
```ts  
function AudioLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new AudioLoader.

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
loaded text response.  
[onProgress](#) (optional) — Will be called while load progresses. The
argument will be the ProgressEvent instance, which contains
.[lengthComputable](#), .[total](#) and .[loaded](#). If the server does not
set the Content-Length header; .[total](#) will be 0.  
[onError](#) (optional) — Will be called when load errors.  

Begin loading from url and pass the loaded [AudioBuffer](#) to onLoad.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/AudioLoader.js">src/loaders/AudioLoader.js</a>

