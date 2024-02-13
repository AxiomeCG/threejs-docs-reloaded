[page:Loader] →

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
loaders that use FileLoader internally. [page:Cache Cache] is a cache module
that holds the response from each request made through this loader, so each
file is requested once.

## Constructor

### FileLoader ( [param:LoadingManager manager] )

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:DefaultLoadingManager].

## Properties

See the base [page:Loader] class for common properties.

###  String mimeType;

The expected [link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/MIME_types mimeType]. See [page:.setMimeType].
Default is `undefined`.

###  String responseType;

The expected response type. See [page:.setResponseType]. Default is
`undefined`.

## Methods

See the base [page:Loader] class for common methods.

###  function load( url: String, onLoad: Function, onProgress: Function,
onError: Function ): undefined;

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] (optional) — Will be called when loading completes. The
argument will be the loaded response.  
[page:Function onProgress] (optional) — Will be called while load progresses.
The argument will be the ProgressEvent instance, which contains .[page:Boolean
lengthComputable], .[page:Integer total] and .[page:Integer loaded]. If the
server does not set the Content-Length header; .[page:Integer total] will be
0.  
[page:Function onError] (optional) — Will be called if an error occurs.  
  
Load the URL and pass the response to the onLoad function.

###  function setMimeType( mimeType: String ): this;

Set the expected [link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/MIME_types mimeType] of the file being loaded.
Note that in many cases this will be determined automatically, so by default
it is `undefined`.

###  function setResponseType( responseType: String ): this;

Change the response type. Valid values are:  
[page:String text] or empty string (default) - returns the data as
[page:String String].  
[page:String arraybuffer] - loads the data into a
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer ArrayBuffer] and
returns that.  
[page:String blob] - returns the data as a
[link:https://developer.mozilla.org/en/docs/Web/API/Blob Blob].  
[page:String document] - parses the file using the
[link:https://developer.mozilla.org/en-US/docs/Web/API/DOMParser DOMParser].  
[page:String json] - parses the file using
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse JSON.parse].  

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

