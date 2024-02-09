# [name]

## Constructor

### [name]( [param:InterleavedBuffer interleavedBuffer], [param:Integer
itemSize], [param:Integer offset], [param:Boolean normalized] )

## Properties

### <br/> InterleavedBuffer data; <br/>

The [page:InterleavedBuffer InterleavedBuffer] instance passed in the
constructor.

### <br/> TypedArray array; <br/>

The value of [page:InterleavedBufferAttribute.data data].array.

### <br/> Integer count; <br/>

The value of [page:InterleavedBufferAttribute.data data].count. If the buffer
is storing a 3-component item (such as a position, normal, or color), then
this will count the number of such items stored.

### <br/> Boolean isInterleavedBufferAttribute; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Integer itemSize; <br/>

How many values make up each item.

### <br/> String name; <br/>

Optional name for this attribute instance. Default is an empty string.

### <br/> Boolean needsUpdate; <br/>

Default is `false`. Setting this to `true` will send the entire interleaved
buffer (not just the specific attribute data) to the GPU again.

### <br/> Boolean normalized; <br/>

Default is `false`.

### <br/> Integer offset; <br/>

The offset in the underlying array buffer where an item starts.

## Methods

### <br/> function applyMatrix4( m: Matrix4 ): applyMatrix4; <br/>

Applies matrix [page:Matrix4 m] to every Vector3 element of this
InterleavedBufferAttribute.

### <br/> function applyNormalMatrix( m: Matrix3 ): applyNormalMatrix; <br/>

Applies normal matrix [page:Matrix3 m] to every Vector3 element of this
InterleavedBufferAttribute.

### <br/> function transformDirection( m: Matrix4 ): transformDirection; <br/>

Applies matrix [page:Matrix4 m] to every Vector3 element of this
InterleavedBufferAttribute, interpreting the elements as a direction vectors.

### [method:Number getX]( [param:Integer index] )

Returns the x component of the item at the given index.

### [method:Number getY]( [param:Integer index] )

Returns the y component of the item at the given index.

### [method:Number getZ]( [param:Integer index] )

Returns the z component of the item at the given index.

### [method:Number getW]( [param:Integer index] )

Returns the w component of the item at the given index.

### <br/> function setX( index: Integer, x: Float ): setX; <br/>

Sets the x component of the item at the given index.

### <br/> function setY( index: Integer, y: Float ): setY; <br/>

Sets the y component of the item at the given index.

### <br/> function setZ( index: Integer, z: Float ): setZ; <br/>

Sets the z component of the item at the given index.

### <br/> function setW( index: Integer, w: Float ): setW; <br/>

Sets the w component of the item at the given index.

### <br/> function setXY( index: Integer, x: Float, y: Float ): setXY; <br/>

Sets the x and y components of the item at the given index.

### <br/> function setXYZ( index: Integer, x: Float, y: Float, z: Float ):
setXYZ; <br/>

Sets the x, y and z components of the item at the given index.

### <br/> function setXYZW( index: Integer, x: Float, y: Float, z: Float, w:
Float ): setXYZW; <br/>

Sets the x, y, z and w components of the item at the given index.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

