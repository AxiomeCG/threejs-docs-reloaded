# [name]

A simple caching system, used internally by [page:FileLoader].

## Code Example

To enable caching across all loaders that use [page:FileLoader], set

  
```ts THREE.Cache.enabled = true. ```  

## Examples

[example:webgl_geometry_text WebGL / geometry / text ]  
[example:webgl_interactive_instances_gpu WebGL / interactive / instances /
gpu]  
[example:webgl_loader_ttf WebGL / loader / ttf]

## Properties

### <br/> Boolean enabled; <br/>

Whether caching is enabled. Default is `false`.

### <br/> Object files; <br/>

An [page:Object object] that holds cached files.

## Methods

### [method:undefined add]( [param:String key], [param:Object file] )

[page:String key] — the [page:String key] to reference the cached file by.  
[page:Object file] — The file to be cached.  
  
Adds a cache entry with a key to reference the file. If this key already holds
a file, it is overwritten.

### [method:Any get]( [param:String key] )

[page:String key] — A string key  
  
Get the value of [page:String key]. If the key does not exist `undefined` is
returned.

### [method:undefined remove]( [param:String key] )

[page:String key] — A string key that references a cached file.  
  
Remove the cached file associated with the key.

### [method:undefined clear]()

Remove all values from the cache.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

