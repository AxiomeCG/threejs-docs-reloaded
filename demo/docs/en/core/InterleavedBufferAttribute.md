# InterleavedBufferAttribute

## Constructor

### InterleavedBufferAttribute

  
  
```ts  
function InterleavedBufferAttribute( interleavedBuffer: InterleavedBuffer,
itemSize: Integer, offset: Integer, normalized: Boolean ): void;  
```  

## Properties

### data

  
  
```ts  
data: InterleavedBuffer;  
```  

The [InterleavedBuffer](en\core\InterleavedBuffer.html) instance passed in the
constructor.

### array

  
  
```ts  
array: TypedArray;  
```  

The value of [data](#).array.

### count

  
  
```ts  
count: Integer;  
```  

The value of [data](#).count. If the buffer is storing a 3-component item
(such as a position, normal, or color), then this will count the number of
such items stored.

### isInterleavedBufferAttribute

  
  
```ts  
isInterleavedBufferAttribute: Boolean;  
```  

Read-only flag to check if a given object is of type
InterleavedBufferAttribute.

### itemSize

  
  
```ts  
itemSize: Integer;  
```  

How many values make up each item.

### name

  
  
```ts  
name: String;  
```  

Optional name for this attribute instance. Default is an empty string.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

Default is `false`. Setting this to `true` will send the entire interleaved
buffer (not just the specific attribute data) to the GPU again.

### normalized

  
  
```ts  
normalized: Boolean;  
```  

Default is `false`.

### offset

  
  
```ts  
offset: Integer;  
```  

The offset in the underlying array buffer where an item starts.

## Methods

### applyMatrix4

  
  
```ts  
function applyMatrix4( m: Matrix4 ): this;  
```  

Applies matrix [m](en\math\Matrix4.html) to every Vector3 element of this
InterleavedBufferAttribute.

### applyNormalMatrix

  
  
```ts  
function applyNormalMatrix( m: Matrix3 ): this;  
```  

Applies normal matrix [m](en\math\Matrix3.html) to every Vector3 element of
this InterleavedBufferAttribute.

### transformDirection

  
  
```ts  
function transformDirection( m: Matrix4 ): this;  
```  

Applies matrix [m](en\math\Matrix4.html) to every Vector3 element of this
InterleavedBufferAttribute, interpreting the elements as a direction vectors.

### getX

  
  
```ts  
function getX( index: Integer ): Number;  
```  

Returns the x component of the item at the given index.

### getY

  
  
```ts  
function getY( index: Integer ): Number;  
```  

Returns the y component of the item at the given index.

### getZ

  
  
```ts  
function getZ( index: Integer ): Number;  
```  

Returns the z component of the item at the given index.

### getW

  
  
```ts  
function getW( index: Integer ): Number;  
```  

Returns the w component of the item at the given index.

### setX

  
  
```ts  
function setX( index: Integer, x: Float ): this;  
```  

Sets the x component of the item at the given index.

### setY

  
  
```ts  
function setY( index: Integer, y: Float ): this;  
```  

Sets the y component of the item at the given index.

### setZ

  
  
```ts  
function setZ( index: Integer, z: Float ): this;  
```  

Sets the z component of the item at the given index.

### setW

  
  
```ts  
function setW( index: Integer, w: Float ): this;  
```  

Sets the w component of the item at the given index.

### setXY

  
  
```ts  
function setXY( index: Integer, x: Float, y: Float ): this;  
```  

Sets the x and y components of the item at the given index.

### setXYZ

  
  
```ts  
function setXYZ( index: Integer, x: Float, y: Float, z: Float ): this;  
```  

Sets the x, y and z components of the item at the given index.

### setXYZW

  
  
```ts  
function setXYZW( index: Integer, x: Float, y: Float, z: Float, w: Float ):
this;  
```  

Sets the x, y, z and w components of the item at the given index.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/InterleavedBufferAttribute.js">src/core/InterleavedBufferAttribute.js</a>

