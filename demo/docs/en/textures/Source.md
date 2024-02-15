# Source

Represents the data source of a texture.

## Constructor

### Source

  
  
```ts  
function Source( data: Any ): void;  
```  

[data](#) -- The data definition of a texture. Default is `null`.

## Properties

### data

  
  
```ts  
data: Any;  
```  

The actual data of a texture. The type of this property depends on the texture
that uses this instance.

### isSource

  
  
```ts  
isSource: Boolean;  
```  

Read-only flag to check if a given object is of type Source.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

Set this to `true` to trigger a data upload to the GPU next time the source is
used.

### uuid

  
  
```ts  
uuid: String;  
```  

<a href="http://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a>
of this object instance. This gets automatically assigned, so this shouldn't
be edited.

### version

  
  
```ts  
version: Integer;  
```  

This starts at `0` and counts how many times [.needsUpdate](#) is set to
`true`.

## Methods

### toJSON

  
  
```ts  
function toJSON( meta: Object ): Object;  
```  

meta -- optional object containing metadata.  
Convert the data source to three.js <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/Source.js">src/textures/Source.js</a>

