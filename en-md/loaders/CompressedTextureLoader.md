[page:Loader] →

# CompressedTextureLoader

Abstract base class for block based textures loader (dds, pvr, ...). This uses
the [page:FileLoader] internally for loading files.

## Examples

See the
[link:https://github.com/mrdoob/three.js/blob/master/examples/jsm/loaders/DDSLoader.js
DDSLoader] and
[link:https://github.com/mrdoob/three.js/blob/master/examples/jsm/loaders/PVRLoader.js
PVRLoader] for examples of derived classes.

## Constructor

###  function CompressedTextureLoader( manager: LoadingManager ): void;

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].  
  
Creates a new CompressedTextureLoader.

## Properties

See the base [page:Loader] class for common properties.

## Methods

See the base [page:Loader] class for common methods.

###  function load( url: String, onLoad: Function, onProgress: Function,
onError: Function ): CompressedTexture;

[page:String url] — the path or URL to the file. This can also be a
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URI].  
[page:Function onLoad] (optional) — Will be called when load completes. The
argument will be the loaded texture.  
[page:Function onProgress] (optional) — Will be called while load progresses.
The argument will be the ProgressEvent instance, which contains .[page:Boolean
lengthComputable], .[page:Integer total] and .[page:Integer loaded]. If the
server does not set the Content-Length header; .[page:Integer total] will be
0.  
[page:Function onError] (optional) — Will be called when load errors.  

Begin loading from url and pass the loaded texture to onLoad. The method also
returns a new texture object which can directly be used for material creation.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

