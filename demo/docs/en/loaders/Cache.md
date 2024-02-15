# Cache

A simple caching system, used internally by
[FileLoader](en\loaders\FileLoader.html).

## Code Example

To enable caching across all loaders that use
[FileLoader](en\loaders\FileLoader.html), set

  
```ts  
THREE.Cache.enabled = true.  
```  

## Examples

[example:webgl_geometry_text WebGL / geometry / text ]  
[example:webgl_interactive_instances_gpu WebGL / interactive / instances /
gpu]  
[example:webgl_loader_ttf WebGL / loader / ttf]

## Properties

### enabled

  
  
```ts  
enabled: Boolean;  
```  

Whether caching is enabled. Default is `false`.

### files

  
  
```ts  
files: Object;  
```  

An [object](#) that holds cached files.

## Methods

### add

  
  
```ts  
function add( key: String, file: Object ): undefined;  
```  

[key](#) — the [key](#) to reference the cached file by.  
[file](#) — The file to be cached.  
  
Adds a cache entry with a key to reference the file. If this key already holds
a file, it is overwritten.

### get

  
  
```ts  
function get( key: String ): Any;  
```  

[key](#) — A string key  
  
Get the value of [key](#). If the key does not exist `undefined` is returned.

### remove

  
  
```ts  
function remove( key: String ): undefined;  
```  

[key](#) — A string key that references a cached file.  
  
Remove the cached file associated with the key.

### clear

  
  
```ts  
function clear( ): undefined;  
```  

Remove all values from the cache.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/Cache.js">src/loaders/Cache.js</a>

