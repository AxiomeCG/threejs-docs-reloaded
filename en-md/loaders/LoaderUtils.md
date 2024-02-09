# [name]

An object with several loader utility functions.

## Functions

### [method:String decodeText]( [param:TypedArray array] )

[page:TypedArray array] — A stream of bytes as a typed array.

The function takes a stream of bytes as input and returns a string
representation.

### [method:String extractUrlBase]( [param:String url] )

[page:String url] — The url to extract the base url from.

Extract the base from the URL.

###  [method:String resolveURL]( [param:String url], [param:String path] )

[page:String url] — The absolute or relative url resolve. [page:String path] —
The base path for relative urls to be resolved against.

Resolves relative urls against the given path. Absolute paths, data urls, and
blob urls will be returned as is. Invalid urls will return an empty string.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]
