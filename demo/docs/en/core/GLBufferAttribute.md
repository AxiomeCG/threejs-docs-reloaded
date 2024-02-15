# GLBufferAttribute

This buffer attribute class does not construct a VBO. Instead, it uses
whatever VBO is passed in constructor and can later be altered via the
`buffer` property.  
  
It is required to pass additional params alongside the VBO. Those are: the GL
context, the GL data type, the number of components per vertex, the number of
bytes per component, and the number of vertices.  
  
The most common use case for this class is when some kind of GPGPU calculation
interferes or even produces the VBOs in question.

## Constructor

### GLBufferAttribute

  
  
```ts  
function GLBufferAttribute( buffer: WebGLBuffer, type: GLenum, itemSize:
Integer, elementSize: Integer, count: Integer ): void;  
```  

`buffer` — Must be a <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLBuffer">WebGLBuffer</a>.  
`type` — One of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGL_API/Constants#Data_types">WebGL Data Types</a>.  
`itemSize` — The number of values of the array that should be associated with
a particular vertex. For instance, if this attribute is storing a 3-component
vector (such as a position, normal, or color), then itemSize should be 3.  
`elementSize` — 1, 2 or 4. The corresponding size (in bytes) for the given
"type" param.

  * gl.FLOAT: 4
  * gl.UNSIGNED_SHORT: 2
  * gl.SHORT: 2
  * gl.UNSIGNED_INT: 4
  * gl.INT: 4
  * gl.BYTE: 1
  * gl.UNSIGNED_BYTE: 1

`count` — The expected number of vertices in VBO.

## Properties

### buffer

  
  
```ts  
buffer: WebGLBuffer;  
```  

The current <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLBuffer">WebGLBuffer</a> instance.

### count

  
  
```ts  
count: Integer;  
```  

The expected number of vertices in VBO.

### isGLBufferAttribute

  
  
```ts  
isGLBufferAttribute: Boolean;  
```  

Read-only. Always `true`.

### itemSize

  
  
```ts  
itemSize: Integer;  
```  

How many values make up each item (vertex).

### elementSize

  
  
```ts  
elementSize: Integer;  
```  

Stores the corresponding size in bytes for the current `type` property value.

See above (constructor) for a list of known type sizes.

### name

  
  
```ts  
name: String;  
```  

Optional name for this attribute instance. Default is an empty string.

### type

  
  
```ts  
type: GLenum;  
```  

A <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGL_API/Constants#Data_types">WebGL Data Type</a> describing
the underlying VBO contents.

Set this property together with `elementSize`. The recommended way is using
the `setType` method.

## Methods

### setBuffer

  
  
```ts  
function setBuffer( ): this;  
```  

Sets the `buffer` property.

### setType

  
  
```ts  
function setType( ): this;  
```  

Sets the both `type` and `elementSize` properties.

### setItemSize

  
  
```ts  
function setItemSize( ): this;  
```  

Sets the `itemSize` property.

### setCount

  
  
```ts  
function setCount( ): this;  
```  

Sets the `count` property.

### version

  
  
```ts  
version: Integer;  
```  

A version number, incremented every time the needsUpdate property is set to
true.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

Default is `false`. Setting this to true increments [version](#).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/GLBufferAttribute.js">src/core/GLBufferAttribute.js</a>

