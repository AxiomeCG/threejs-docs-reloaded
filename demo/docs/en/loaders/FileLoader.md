[Loader](en\loaders\Loader.html) →

# FileLoader

A low level class for loading resources with Fetch, used internally by most
loaders. It can also be used directly to load any file type that does not have
a loader.

## Code Example

  
```ts  
const loader = new THREE.FileLoader(); //load a text file and output the
result to the console loader.load( // resource URL 'example.txt', // onLoad
callback function ( data ) { // output the text to the console console.log(
data ) }, // onProgress callback function ( xhr ) { console.log( (xhr.loaded /
xhr.total * 100) + '% loaded' ); }, // onError callback function ( err ) {
console.error( 'An error happened' ); } );  
```  

*Note:* The cache must be enabled using  
```ts  
THREE.Cache.enabled = true;  
```  
This is a global property and only needs to be set once to be used by all
loaders that use FileLoader internally. [Cache](en\loaders\Cache.html) is a
cache module that holds the response from each request made through this
loader, so each file is requested once.

## Constructor

### FileLoader ( [param:LoadingManager manager] )

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[DefaultLoadingManager](en\loaders\managers\DefaultLoadingManager.html).

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

### mimeType

  
  
```ts  
mimeType: String;  
```  

The expected <a href="https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/MIME_types">mimeType</a>. See
[.setMimeType](#). Default is `undefined`.

### responseType

  
  
```ts  
responseType: String;  
```  

The expected response type. See [.setResponseType](#). Default is `undefined`.

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
[onLoad](#) (optional) — Will be called when loading completes. The argument
will be the loaded response.  
[onProgress](#) (optional) — Will be called while load progresses. The
argument will be the ProgressEvent instance, which contains
.[lengthComputable](#), .[total](#) and .[loaded](#). If the server does not
set the Content-Length header; .[total](#) will be 0.  
[onError](#) (optional) — Will be called if an error occurs.  
  
Load the URL and pass the response to the onLoad function.

### setMimeType

  
  
```ts  
function setMimeType( mimeType: String ): this;  
```  

Set the expected <a href="https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/MIME_types">mimeType</a> of the file being
loaded. Note that in many cases this will be determined automatically, so by
default it is `undefined`.

### setResponseType

  
  
```ts  
function setResponseType( responseType: String ): this;  
```  

Change the response type. Valid values are:  
[text](#) or empty string (default) - returns the data as [String](#).  
[arraybuffer](#) - loads the data into a <a
href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer">ArrayBuffer</a>
and returns that.  
[blob](#) - returns the data as a <a
href="https://developer.mozilla.org/en/docs/Web/API/Blob">Blob</a>.  
[document](#) - parses the file using the <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/DOMParser">DOMParser</a>.  
[json](#) - parses the file using <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse">JSON.parse</a>.  

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/FileLoader.js">src/loaders/FileLoader.js</a>

