# InterleavedBufferAttribute

## Constructor

###  function InterleavedBufferAttribute( interleavedBuffer:
InterleavedBuffer, itemSize: Integer, offset: Integer, normalized: Boolean ):
void;

## Properties

###  InterleavedBuffer data;

The [page:InterleavedBuffer InterleavedBuffer] instance passed in the
constructor.

###  TypedArray array;

The value of [page:InterleavedBufferAttribute.data data].array.

###  Integer count;

The value of [page:InterleavedBufferAttribute.data data].count. If the buffer
is storing a 3-component item (such as a position, normal, or color), then
this will count the number of such items stored.

###  Boolean isInterleavedBufferAttribute;

Read-only flag to check if a given object is of type
InterleavedBufferAttribute.

###  Integer itemSize;

How many values make up each item.

###  String name;

Optional name for this attribute instance. Default is an empty string.

###  Boolean needsUpdate;

Default is `false`. Setting this to `true` will send the entire interleaved
buffer (not just the specific attribute data) to the GPU again.

###  Boolean normalized;

Default is `false`.

###  Integer offset;

The offset in the underlying array buffer where an item starts.

## Methods

###  function applyMatrix4( m: Matrix4 ): this;

Applies matrix [page:Matrix4 m] to every Vector3 element of this
InterleavedBufferAttribute.

###  function applyNormalMatrix( m: Matrix3 ): this;

Applies normal matrix [page:Matrix3 m] to every Vector3 element of this
InterleavedBufferAttribute.

###  function transformDirection( m: Matrix4 ): this;

Applies matrix [page:Matrix4 m] to every Vector3 element of this
InterleavedBufferAttribute, interpreting the elements as a direction vectors.

###  function getX( index: Integer ): Number;

Returns the x component of the item at the given index.

###  function getY( index: Integer ): Number;

Returns the y component of the item at the given index.

###  function getZ( index: Integer ): Number;

Returns the z component of the item at the given index.

###  function getW( index: Integer ): Number;

Returns the w component of the item at the given index.

###  function setX( index: Integer, x: Float ): this;

Sets the x component of the item at the given index.

###  function setY( index: Integer, y: Float ): this;

Sets the y component of the item at the given index.

###  function setZ( index: Integer, z: Float ): this;

Sets the z component of the item at the given index.

###  function setW( index: Integer, w: Float ): this;

Sets the w component of the item at the given index.

###  function setXY( index: Integer, x: Float, y: Float ): this;

Sets the x and y components of the item at the given index.

###  function setXYZ( index: Integer, x: Float, y: Float, z: Float ): this;

Sets the x, y and z components of the item at the given index.

###  function setXYZW( index: Integer, x: Float, y: Float, z: Float, w: Float
): this;

Sets the x, y, z and w components of the item at the given index.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

