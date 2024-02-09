# [name]

"Interleaved" means that multiple attributes, possibly of different types,
(e.g., position, normal, uv, color) are packed into a single array buffer.  
  
An introduction into interleaved arrays can be found here:
[link:https://blog.tojicode.com/2011/05/interleaved-array-basics.html
Interleaved array basics]

## Examples

[example:webgl_buffergeometry_points_interleaved webgl / buffergeometry /
points / interleaved]

## Constructor

### [name]( [param:TypedArray array], [param:Integer stride] )

[page:TypedArray array] -- A typed array with a shared buffer. Stores the
geometry data.  
[page:Integer stride] -- The number of typed-array elements per vertex.

## Properties

### <br/> Array array; <br/>

A typed array with a shared buffer. Stores the geometry data.

### <br/> Integer stride; <br/>

The number of typed-array elements per vertex.

### <br/> Integer count; <br/>

Gives the total number of elements in the array.

### <br/> Object updateRange; <br/>

Object containing offset and count.  
\- [page:Number offset]: Default is `0`.  
\- [page:Number count]: Default is `-1`.  

### <br/> String uuid; <br/>

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
instance. This gets automatically assigned, so this shouldn't be edited.

### <br/> Integer version; <br/>

A version number, incremented every time the needsUpdate property is set to
true.

### <br/> Boolean needsUpdate; <br/>

Default is `false`. Setting this to true increments
[page:InterleavedBuffer.version version].

### <br/> Usage usage; <br/>

Defines the intended usage pattern of the data store for optimization
purposes. Corresponds to the `usage` parameter of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bufferData
WebGLRenderingContext.bufferData]().

## Methods

### <br/> function copy( source: InterleavedBuffer ): copy; <br/>

Copies another [name] to this [name].

### <br/> function copyAt( index1: Integer, attribute: InterleavedBuffer,
index2: Integer ): copyAt; <br/>

Copies data from `attribute[index2]` to [page:InterleavedBuffer.array
array][index1].

### <br/> function set( value: TypedArray, offset: Integer ): set; <br/>

value - The source (typed) array.  
offset - The offset into the target array at which to begin writing values
from the source array. Default is `0`.  
  
Stores multiple values in the buffer, reading input values from a specified
array.

### [method:InterleavedBuffer clone]( [param:Object data] )

data - This object holds shared array buffers required for properly cloning
geometries with interleaved attributes.  
  
Creates a clone of this [name].

### <br/> function setUsage( value: Usage ): setUsage; <br/>

Set [page:InterleavedBuffer.usage usage] to value.

### [method:Object toJSON]( [param:Object data] )

data - This object holds shared array buffers required for properly
serializing geometries with interleaved attributes.  
  
Serializes this [name].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

