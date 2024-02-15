# Loader

Base class for implementing loaders.

## Constructor

### Loader

  
  
```ts  
function Loader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).

Creates a new Loader.

## Properties

### crossOrigin

  
  
```ts  
crossOrigin: String;  
```  

The crossOrigin string to implement CORS for loading the url from a different
domain that allows CORS. Default is `anonymous`.

### withCredentials

  
  
```ts  
withCredentials: Boolean;  
```  

Whether the XMLHttpRequest uses credentials. See [.setWithCredentials](#).
Default is `false`.

### manager

  
  
```ts  
manager: LoadingManager;  
```  

The [loadingManager](en\loaders\managers\LoadingManager.html) the loader is
using. Default is
[DefaultLoadingManager](en\loaders\managers\DefaultLoadingManager.html).

### path

  
  
```ts  
path: String;  
```  

The base path from which the asset will be loaded. Default is the empty
string.

### resourcePath

  
  
```ts  
resourcePath: String;  
```  

The base path from which additional resources like textures will be loaded.
Default is the empty string.

### requestHeader

  
  
```ts  
requestHeader: Object;  
```  

The <a href="https://developer.mozilla.org/en-
US/docs/Glossary/Request_header">request header</a> used in HTTP request. See
[.setRequestHeader](#). Default is empty object.

## Methods

### load

  
  
```ts  
function load( ): undefined;  
```  

This method needs to be implement by all concrete loaders. It holds the logic
for loading the asset from the backend.

### loadAsync

  
  
```ts  
function loadAsync( url: String, onProgress: Function ): Promise;  
```  

[url](#) — A string containing the path/URL of the file to be loaded.  
[onProgress](#) (optional) — A function to be called while the loading is in
progress. The argument will be the ProgressEvent instance, which contains
.[lengthComputable](#), .[total](#) and .[loaded](#). If the server does not
set the Content-Length header; .[total](#) will be 0.  

This method is equivalent to [.load](#), but returns a <a
href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise">Promise</a>.

[onLoad](#) is handled by <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve">Promise.resolve</a>
and [onError](#) is handled by <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject">Promise.reject</a>.

### parse

  
  
```ts  
function parse( ): undefined;  
```  

This method needs to be implement by all concrete loaders. It holds the logic
for parsing the asset into three.js entities.

### setCrossOrigin

  
  
```ts  
function setCrossOrigin( crossOrigin: String ): this;  
```  

[crossOrigin](#) — The crossOrigin string to implement CORS for loading the
url from a different domain that allows CORS.

### setWithCredentials

  
  
```ts  
function setWithCredentials( value: Boolean ): this;  
```  

Whether the XMLHttpRequest uses credentials such as cookies, authorization
headers or TLS client certificates. See <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/XMLHttpRequest/withCredentials">XMLHttpRequest.withCredentials</a>.  
Note that this has no effect if you are loading files locally or from the same
domain.

### setPath

  
  
```ts  
function setPath( path: String ): this;  
```  

[path](#) — Set the base path for the asset.

### setResourcePath

  
  
```ts  
function setResourcePath( resourcePath: String ): this;  
```  

[resourcePath](#) — Set the base path for dependent resources like textures.

### setRequestHeader

  
  
```ts  
function setRequestHeader( requestHeader: Object ): this;  
```  

[requestHeader](#) - key: The name of the header whose value is to be set.
value: The value to set as the body of the header.  
  
Set the <a href="https://developer.mozilla.org/en-
US/docs/Glossary/Request_header">request header</a> used in HTTP request.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/Loader.js">src/loaders/Loader.js</a>

