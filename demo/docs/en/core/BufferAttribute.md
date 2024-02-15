# BufferAttribute

This class stores data for an attribute (such as vertex positions, face
indices, normals, colors, UVs, and any custom attributes ) associated with a
[BufferGeometry](en\core\BufferGeometry.html), which allows for more efficient
passing of data to the GPU. See that page for details and a usage example.
When working with vector-like data, the _.fromBufferAttribute( attribute,
index )_ helper methods on [Vector2](#), [Vector3](#), [Vector4](#), and
[Color](#) classes may be helpful.

## Constructor

### BufferAttribute

  
  
```ts  
function BufferAttribute( array: TypedArray, itemSize: Integer, normalized:
Boolean ): void;  
```  

[array](#) -- Must be a <a
href="https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/TypedArray">TypedArray</a>.
Used to instantiate the buffer.  
This array should have  
```ts  
itemSize * numVertices  
```  
elements, where numVertices is the number of vertices in the associated
[BufferGeometry](#).  
  
[itemSize](#) -- the number of values of the array that should be associated
with a particular vertex. For instance, if this attribute is storing a
3-component vector (such as a position, normal, or color), then itemSize
should be 3.  
  
[normalized](#) -- (optional) Applies to integer data only. Indicates how the
underlying data in the buffer maps to the values in the GLSL code. For
instance, if [array](#) is an instance of UInt16Array, and [normalized](#) is
true, the values `0 - +65535` in the array data will be mapped to 0.0f - +1.0f
in the GLSL attribute. An Int16Array (signed) would map from -32768 - +32767
to -1.0f - +1.0f. If [normalized](#) is false, the values will be converted to
floats unmodified, i.e. 32767 becomes 32767.0f.

## Properties

### array

  
  
```ts  
array: TypedArray;  
```  

The [array](#) holding data stored in the buffer.

### count

  
  
```ts  
count: Integer;  
```  

Stores the [array](#)'s length divided by the [itemSize](#).  
  
If the buffer is storing a 3-component vector (such as a position, normal, or
color), then this will count the number of such vectors stored.

### gpuType

  
  
```ts  
gpuType: Number;  
```  

Configures the bound GPU type for use in shaders. Either
[THREE.FloatType](en\core\BufferAttribute.html) or
[THREE.IntType](en\core\BufferAttribute.html), default is
[THREE.FloatType](en\core\BufferAttribute.html). Note: this only has an effect
for integer arrays and is not configurable for float arrays. For lower
precision float types, see
[THREE.Float16BufferAttribute](en\core\bufferAttributeTypes\BufferAttributeTypes.html).

### isBufferAttribute

  
  
```ts  
isBufferAttribute: Boolean;  
```  

Read-only flag to check if a given object is of type BufferAttribute.

### itemSize

  
  
```ts  
itemSize: Integer;  
```  

The length of vectors that are being stored in the [array](#).

### name

  
  
```ts  
name: String;  
```  

Optional name for this attribute instance. Default is an empty string.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

Flag to indicate that this attribute has changed and should be re-sent to the
GPU. Set this to true when you modify the value of the array.  
  
Setting this to true also increments the [version](#).

### normalized

  
  
```ts  
normalized: Boolean;  
```  

Indicates how the underlying data in the buffer maps to the values in the GLSL
shader code. See the constructor above for details.

### onUploadCallback

  
  
```ts  
onUploadCallback: Function;  
```  

A callback function that is executed after the Renderer has transferred the
attribute array data to the GPU.

### updateRange

  
  
```ts  
updateRange: Object;  
```  

Object containing:  
[offset](#): Default is `0`. Position at which to start update.  
[count](#): Default is `-1`, which means don't use update ranges.  
  
This can be used to only update some components of stored vectors (for
example, just the component related to color).

### usage

  
  
```ts  
usage: Usage;  
```  

Defines the intended usage pattern of the data store for optimization
purposes. Corresponds to the `usage` parameter of <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bufferData">WebGLRenderingContext.bufferData</a>().
Default is [StaticDrawUsage](en\constants\BufferAttributeUsage.html). See
usage [constants](en\constants\BufferAttributeUsage.html) for all possible
values.  
  
Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desired usage before the next render.

### version

  
  
```ts  
version: Integer;  
```  

A version number, incremented every time the [needsUpdate](#) property is set
to true.

## Methods

### applyMatrix3

  
  
```ts  
function applyMatrix3( m: Matrix3 ): this;  
```  

Applies matrix [m](en\math\Matrix3.html) to every Vector3 element of this
BufferAttribute.

### applyMatrix4

  
  
```ts  
function applyMatrix4( m: Matrix4 ): this;  
```  

Applies matrix [m](en\math\Matrix4.html) to every Vector3 element of this
BufferAttribute.

### applyNormalMatrix

  
  
```ts  
function applyNormalMatrix( m: Matrix3 ): this;  
```  

Applies normal matrix [m](en\math\Matrix3.html) to every Vector3 element of
this BufferAttribute.

### transformDirection

  
  
```ts  
function transformDirection( m: Matrix4 ): this;  
```  

Applies matrix [m](en\math\Matrix4.html) to every Vector3 element of this
BufferAttribute, interpreting the elements as a direction vectors.

### clone

  
  
```ts  
function clone( ): BufferAttribute;  
```  

Return a copy of this bufferAttribute.

### copy

  
  
```ts  
function copy( bufferAttribute: BufferAttribute ): this;  
```  

Copies another BufferAttribute to this BufferAttribute.

### copyArray

  
  
```ts  
function copyArray( ): this;  
```  

Copy the array given here (which can be a normal array or TypedArray) into
[array](#).  
  
See <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set">TypedArray.set</a>
for notes on requirements if copying a TypedArray.

### copyAt

  
  
```ts  
function copyAt( index1: Integer, bufferAttribute: BufferAttribute, index2:
Integer ): this;  
```  

Copy a vector from bufferAttribute[index2] to [array](#)[index1].

### getX

  
  
```ts  
function getX( index: Integer ): Number;  
```  

Returns the x component of the vector at the given index.

### getY

  
  
```ts  
function getY( index: Integer ): Number;  
```  

Returns the y component of the vector at the given index.

### getZ

  
  
```ts  
function getZ( index: Integer ): Number;  
```  

Returns the z component of the vector at the given index.

### getW

  
  
```ts  
function getW( index: Integer ): Number;  
```  

Returns the w component of the vector at the given index.

### onUpload

  
  
```ts  
function onUpload( callback: Function ): this;  
```  

Sets the value of the onUploadCallback property.  
  
In the [example:webgl_buffergeometry WebGL / Buffergeometry] this is used to
free memory after the buffer has been transferred to the GPU.

### set

  
  
```ts  
function set( value: Array, offset: Integer ): this;  
```  

value -- an [Array](#) or [TypedArray](#) from which to copy values.  
offset -- (optional) index of the [array](#) at which to start copying.  
  
Calls <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set">TypedArray.set</a>(
[value](#), [offset](#) ) on the [array](#).  
  
In particular, see that page for requirements on [value](#) being a
[TypedArray](#).

### setUsage

  
  
```ts  
function setUsage( value: Usage ): this;  
```  

Set [usage](#) to value. See usage
[constants](en\constants\BufferAttributeUsage.html) for all possible input
values.  
  
Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desired usage before the next render.

### setX

  
  
```ts  
function setX( index: Integer, x: Float ): this;  
```  

Sets the x component of the vector at the given index.

### setY

  
  
```ts  
function setY( index: Integer, y: Float ): this;  
```  

Sets the y component of the vector at the given index.

### setZ

  
  
```ts  
function setZ( index: Integer, z: Float ): this;  
```  

Sets the z component of the vector at the given index.

### setW

  
  
```ts  
function setW( index: Integer, w: Float ): this;  
```  

Sets the w component of the vector at the given index.

### setXY

  
  
```ts  
function setXY( index: Integer, x: Float, y: Float ): this;  
```  

Sets the x and y components of the vector at the given index.

### setXYZ

  
  
```ts  
function setXYZ( index: Integer, x: Float, y: Float, z: Float ): this;  
```  

Sets the x, y and z components of the vector at the given index.

### setXYZW

  
  
```ts  
function setXYZW( index: Integer, x: Float, y: Float, z: Float, w: Float ):
this;  
```  

Sets the x, y, z and w components of the vector at the given index.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/BufferAttribute.js">src/core/BufferAttribute.js</a>

