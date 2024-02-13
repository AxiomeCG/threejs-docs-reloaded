# Cache

A simple caching system, used internally by [page:FileLoader].

## Code Example

To enable caching across all loaders that use [page:FileLoader], set

  
```ts  
THREE.Cache.enabled = true.  
```  

## Examples

[example:webgl_geometry_text WebGL / geometry / text ]  
[example:webgl_interactive_instances_gpu WebGL / interactive / instances /
gpu]  
[example:webgl_loader_ttf WebGL / loader / ttf]

## Properties

###  Boolean enabled;

Whether caching is enabled. Default is `false`.

###  Object files;

An [page:Object object] that holds cached files.

## Methods

###  function add( key: String, file: Object ): undefined;

[page:String key] — the [page:String key] to reference the cached file by.  
[page:Object file] — The file to be cached.  
  
Adds a cache entry with a key to reference the file. If this key already holds
a file, it is overwritten.

###  function get( key: String ): Any;

[page:String key] — A string key  
  
Get the value of [page:String key]. If the key does not exist `undefined` is
returned.

###  function remove( key: String ): undefined;

[page:String key] — A string key that references a cached file.  
  
Remove the cached file associated with the key.

###  function clear( ): undefined;

Remove all values from the cache.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

