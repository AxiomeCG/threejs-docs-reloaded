# Loader

Base class for implementing loaders.

## Constructor

###  function Loader( manager: LoadingManager ): void;

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].

Creates a new Loader.

## Properties

###  String crossOrigin;

The crossOrigin string to implement CORS for loading the url from a different
domain that allows CORS. Default is `anonymous`.

###  Boolean withCredentials;

Whether the XMLHttpRequest uses credentials. See [page:.setWithCredentials].
Default is `false`.

###  LoadingManager manager;

The [page:LoadingManager loadingManager] the loader is using. Default is
[page:DefaultLoadingManager].

###  String path;

The base path from which the asset will be loaded. Default is the empty
string.

###  String resourcePath;

The base path from which additional resources like textures will be loaded.
Default is the empty string.

###  Object requestHeader;

The [link:https://developer.mozilla.org/en-US/docs/Glossary/Request_header
request header] used in HTTP request. See [page:.setRequestHeader]. Default is
empty object.

## Methods

###  function load( ): undefined;

This method needs to be implement by all concrete loaders. It holds the logic
for loading the asset from the backend.

###  function loadAsync( url: String, onProgress: Function ): Promise;

[page:String url] — A string containing the path/URL of the file to be loaded.  
[page:Function onProgress] (optional) — A function to be called while the
loading is in progress. The argument will be the ProgressEvent instance, which
contains .[page:Boolean lengthComputable], .[page:Integer total] and
.[page:Integer loaded]. If the server does not set the Content-Length header;
.[page:Integer total] will be 0.  

This method is equivalent to [page:.load], but returns a
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise Promise].

[page:Function onLoad] is handled by [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve
Promise.resolve] and [page:Function onError] is handled by
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject
Promise.reject].

###  function parse( ): undefined;

This method needs to be implement by all concrete loaders. It holds the logic
for parsing the asset into three.js entities.

###  function setCrossOrigin( crossOrigin: String ): this;

[page:String crossOrigin] — The crossOrigin string to implement CORS for
loading the url from a different domain that allows CORS.

###  function setWithCredentials( value: Boolean ): this;

Whether the XMLHttpRequest uses credentials such as cookies, authorization
headers or TLS client certificates. See
[link:https://developer.mozilla.org/en-
US/docs/Web/API/XMLHttpRequest/withCredentials
XMLHttpRequest.withCredentials].  
Note that this has no effect if you are loading files locally or from the same
domain.

###  function setPath( path: String ): this;

[page:String path] — Set the base path for the asset.

###  function setResourcePath( resourcePath: String ): this;

[page:String resourcePath] — Set the base path for dependent resources like
textures.

###  function setRequestHeader( requestHeader: Object ): this;

[page:Object requestHeader] - key: The name of the header whose value is to be
set. value: The value to set as the body of the header.  
  
Set the [link:https://developer.mozilla.org/en-US/docs/Glossary/Request_header
request header] used in HTTP request.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

