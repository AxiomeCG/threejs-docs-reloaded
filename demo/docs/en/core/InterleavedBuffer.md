# InterleavedBuffer

"Interleaved" means that multiple attributes, possibly of different types,
(e.g., position, normal, uv, color) are packed into a single array buffer.  
  
An introduction into interleaved arrays can be found here: <a
href="https://blog.tojicode.com/2011/05/interleaved-array-
basics.html">Interleaved array basics</a>

## Examples

[example:webgl_buffergeometry_points_interleaved webgl / buffergeometry /
points / interleaved]

## Constructor

### InterleavedBuffer

  
  
```ts  
function InterleavedBuffer( array: TypedArray, stride: Integer ): void;  
```  

[array](#) -- A typed array with a shared buffer. Stores the geometry data.  
[stride](#) -- The number of typed-array elements per vertex.

## Properties

### array

  
  
```ts  
array: Array;  
```  

A typed array with a shared buffer. Stores the geometry data.

### stride

  
  
```ts  
stride: Integer;  
```  

The number of typed-array elements per vertex.

### count

  
  
```ts  
count: Integer;  
```  

Gives the total number of elements in the array.

### updateRange

  
  
```ts  
updateRange: Object;  
```  

Object containing offset and count.  
\- [offset](#): Default is `0`.  
\- [count](#): Default is `-1`.  

### uuid

  
  
```ts  
uuid: String;  
```  

<a href="http://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a>
of this instance. This gets automatically assigned, so this shouldn't be
edited.

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

### usage

  
  
```ts  
usage: Usage;  
```  

Defines the intended usage pattern of the data store for optimization
purposes. Corresponds to the `usage` parameter of <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bufferData">WebGLRenderingContext.bufferData</a>().

## Methods

### copy

  
  
```ts  
function copy( source: InterleavedBuffer ): this;  
```  

Copies another InterleavedBuffer to this InterleavedBuffer.

### copyAt

  
  
```ts  
function copyAt( index1: Integer, attribute: InterleavedBuffer, index2:
Integer ): this;  
```  

Copies data from `attribute[index2]` to [array](#)[index1].

### set

  
  
```ts  
function set( value: TypedArray, offset: Integer ): this;  
```  

value - The source (typed) array.  
offset - The offset into the target array at which to begin writing values
from the source array. Default is `0`.  
  
Stores multiple values in the buffer, reading input values from a specified
array.

### clone

  
  
```ts  
function clone( data: Object ): InterleavedBuffer;  
```  

data - This object holds shared array buffers required for properly cloning
geometries with interleaved attributes.  
  
Creates a clone of this InterleavedBuffer.

### setUsage

  
  
```ts  
function setUsage( value: Usage ): this;  
```  

Set [usage](#) to value.

### toJSON

  
  
```ts  
function toJSON( data: Object ): Object;  
```  

data - This object holds shared array buffers required for properly
serializing geometries with interleaved attributes.  
  
Serializes this InterleavedBuffer.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/InterleavedBuffer.js">src/core/InterleavedBuffer.js</a>

