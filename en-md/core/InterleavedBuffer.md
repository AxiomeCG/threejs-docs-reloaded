# InterleavedBuffer

"Interleaved" means that multiple attributes, possibly of different types,
(e.g., position, normal, uv, color) are packed into a single array buffer.  
  
An introduction into interleaved arrays can be found here:
[link:https://blog.tojicode.com/2011/05/interleaved-array-basics.html
Interleaved array basics]

## Examples

[example:webgl_buffergeometry_points_interleaved webgl / buffergeometry /
points / interleaved]

## Constructor

###  function InterleavedBuffer( array: TypedArray, stride: Integer ): void;

[page:TypedArray array] -- A typed array with a shared buffer. Stores the
geometry data.  
[page:Integer stride] -- The number of typed-array elements per vertex.

## Properties

###  Array array;

A typed array with a shared buffer. Stores the geometry data.

###  Integer stride;

The number of typed-array elements per vertex.

###  Integer count;

Gives the total number of elements in the array.

###  Object updateRange;

Object containing offset and count.  
\- [page:Number offset]: Default is `0`.  
\- [page:Number count]: Default is `-1`.  

###  String uuid;

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
instance. This gets automatically assigned, so this shouldn't be edited.

###  Integer version;

A version number, incremented every time the needsUpdate property is set to
true.

###  Boolean needsUpdate;

Default is `false`. Setting this to true increments
[page:InterleavedBuffer.version version].

###  Usage usage;

Defines the intended usage pattern of the data store for optimization
purposes. Corresponds to the `usage` parameter of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bufferData
WebGLRenderingContext.bufferData]().

## Methods

###  function copy( source: InterleavedBuffer ): this;

Copies another InterleavedBuffer to this InterleavedBuffer.

###  function copyAt( index1: Integer, attribute: InterleavedBuffer, index2:
Integer ): this;

Copies data from `attribute[index2]` to [page:InterleavedBuffer.array
array][index1].

###  function set( value: TypedArray, offset: Integer ): this;

value - The source (typed) array.  
offset - The offset into the target array at which to begin writing values
from the source array. Default is `0`.  
  
Stores multiple values in the buffer, reading input values from a specified
array.

###  function clone( data: Object ): InterleavedBuffer;

data - This object holds shared array buffers required for properly cloning
geometries with interleaved attributes.  
  
Creates a clone of this InterleavedBuffer.

###  function setUsage( value: Usage ): this;

Set [page:InterleavedBuffer.usage usage] to value.

###  function toJSON( data: Object ): Object;

data - This object holds shared array buffers required for properly
serializing geometries with interleaved attributes.  
  
Serializes this InterleavedBuffer.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

