[Loader](en\loaders\Loader.html) →

# DataTextureLoader

Abstract base class to load generic binary textures formats (rgbe, hdr, ...).
This uses the [FileLoader](en\loaders\FileLoader.html) internally for loading
files, and creates a new [DataTexture](en\textures\DataTexture.html).

## Examples

See the <a
href="https://github.com/mrdoob/three.js/blob/master/examples/jsm/loaders/RGBELoader.js">RGBELoader</a>
for an example of a derived class.

## Constructor

### DataTextureLoader

  
  
```ts  
function DataTextureLoader( manager: LoadingManager ): void;  
```  

[manager](en\loaders\managers\LoadingManager.html) — The
[loadingManager](en\loaders\managers\LoadingManager.html) for the loader to
use. Default is
[THREE.DefaultLoadingManager](en\loaders\managers\LoadingManager.html).  
  
Creates a new DataTextureLoader.

## Properties

See the base [Loader](en\loaders\Loader.html) class for common properties.

## Methods

See the base [Loader](en\loaders\Loader.html) class for common methods.

### load

  
  
```ts  
function load( url: String, onLoad: Function, onProgress: Function, onError:
Function ): DataTexture;  
```  

[url](#) — the path or URL to the file. This can also be a <a
href="https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs">Data URI</a>.  
[onLoad](#) (optional) — Will be called when load completes. The argument will
be the loaded texture.  
[onProgress](#) (optional) — Will be called while load progresses.The argument
will be the ProgressEvent instance, which contains .[lengthComputable](#),
.[total](#) and .[ loaded](#). If the server does not set the Content-Length
header; .[total](#) will be 0.  
[onError](#) (optional) — Will be called when load errors.  

Begin loading from url and pass the loaded texture to onLoad. The method also
returns a new texture object which can directly be used for material creation.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/DataTextureLoader.js">src/loaders/DataTextureLoader.js</a>

