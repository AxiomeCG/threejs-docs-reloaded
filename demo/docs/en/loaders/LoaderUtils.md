# LoaderUtils

An object with several loader utility functions.

## Functions

### decodeText

  
  
```ts  
function decodeText( array: TypedArray ): String;  
```  

[array](#) — A stream of bytes as a typed array.

The function takes a stream of bytes as input and returns a string
representation.

### extractUrlBase

  
  
```ts  
function extractUrlBase( url: String ): String;  
```  

[url](#) — The url to extract the base url from.

Extract the base from the URL.

### resolveURL

  
  
```ts  
function resolveURL( url: String, path: String ): String;  
```  

[url](#) — The absolute or relative url resolve. [path](#) — The base path for
relative urls to be resolved against.

Resolves relative urls against the given path. Absolute paths, data urls, and
blob urls will be returned as is. Invalid urls will return an empty string.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/LoaderUtils.js">src/loaders/LoaderUtils.js</a>

