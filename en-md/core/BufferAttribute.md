# BufferAttribute

This class stores data for an attribute (such as vertex positions, face
indices, normals, colors, UVs, and any custom attributes ) associated with a
[page:BufferGeometry], which allows for more efficient passing of data to the
GPU. See that page for details and a usage example. When working with vector-
like data, the _.fromBufferAttribute( attribute, index )_ helper methods on
[page:Vector2.fromBufferAttribute Vector2], [page:Vector3.fromBufferAttribute
Vector3], [page:Vector4.fromBufferAttribute Vector4], and
[page:Color.fromBufferAttribute Color] classes may be helpful.

## Constructor

###  function BufferAttribute( array: TypedArray, itemSize: Integer,
normalized: Boolean ): void;

[page:TypedArray array] -- Must be a
[link:https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/TypedArray
TypedArray]. Used to instantiate the buffer.  
This array should have  
```ts  
itemSize * numVertices  
```  
elements, where numVertices is the number of vertices in the associated
[page:BufferGemetry BufferGeometry].  
  
[page:Integer itemSize] -- the number of values of the array that should be
associated with a particular vertex. For instance, if this attribute is
storing a 3-component vector (such as a position, normal, or color), then
itemSize should be 3.  
  
[page:Boolean normalized] -- (optional) Applies to integer data only.
Indicates how the underlying data in the buffer maps to the values in the GLSL
code. For instance, if [page:TypedArray array] is an instance of UInt16Array,
and [page:Boolean normalized] is true, the values `0 - +65535` in the array
data will be mapped to 0.0f - +1.0f in the GLSL attribute. An Int16Array
(signed) would map from -32768 - +32767 to -1.0f - +1.0f. If [page:Boolean
normalized] is false, the values will be converted to floats unmodified, i.e.
32767 becomes 32767.0f.

## Properties

###  TypedArray array;

The [page:TypedArray array] holding data stored in the buffer.

###  Integer count;

Stores the [page:BufferAttribute.array array]'s length divided by the
[page:BufferAttribute.itemSize itemSize].  
  
If the buffer is storing a 3-component vector (such as a position, normal, or
color), then this will count the number of such vectors stored.

###  Number gpuType;

Configures the bound GPU type for use in shaders. Either [page:BufferAttribute
THREE.FloatType] or [page:BufferAttribute THREE.IntType], default is
[page:BufferAttribute THREE.FloatType]. Note: this only has an effect for
integer arrays and is not configurable for float arrays. For lower precision
float types, see [page:BufferAttributeTypes THREE.Float16BufferAttribute].

###  Boolean isBufferAttribute;

Read-only flag to check if a given object is of type BufferAttribute.

###  Integer itemSize;

The length of vectors that are being stored in the [page:BufferAttribute.array
array].

###  String name;

Optional name for this attribute instance. Default is an empty string.

###  Boolean needsUpdate;

Flag to indicate that this attribute has changed and should be re-sent to the
GPU. Set this to true when you modify the value of the array.  
  
Setting this to true also increments the [page:BufferAttribute.version
version].

###  Boolean normalized;

Indicates how the underlying data in the buffer maps to the values in the GLSL
shader code. See the constructor above for details.

###  Function onUploadCallback;

A callback function that is executed after the Renderer has transferred the
attribute array data to the GPU.

###  Object updateRange;

Object containing:  
[page:Integer offset]: Default is `0`. Position at which to start update.  
[page:Integer count]: Default is `-1`, which means don't use update ranges.  
  
This can be used to only update some components of stored vectors (for
example, just the component related to color).

###  Usage usage;

Defines the intended usage pattern of the data store for optimization
purposes. Corresponds to the `usage` parameter of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bufferData
WebGLRenderingContext.bufferData](). Default is [page:BufferAttributeUsage
StaticDrawUsage]. See usage [page:BufferAttributeUsage constants] for all
possible values.  
  
Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desired usage before the next render.

###  Integer version;

A version number, incremented every time the [page:BufferAttribute.needsUpdate
needsUpdate] property is set to true.

## Methods

###  function applyMatrix3( m: Matrix3 ): this;

Applies matrix [page:Matrix3 m] to every Vector3 element of this
BufferAttribute.

###  function applyMatrix4( m: Matrix4 ): this;

Applies matrix [page:Matrix4 m] to every Vector3 element of this
BufferAttribute.

###  function applyNormalMatrix( m: Matrix3 ): this;

Applies normal matrix [page:Matrix3 m] to every Vector3 element of this
BufferAttribute.

###  function transformDirection( m: Matrix4 ): this;

Applies matrix [page:Matrix4 m] to every Vector3 element of this
BufferAttribute, interpreting the elements as a direction vectors.

###  function clone( ): BufferAttribute;

Return a copy of this bufferAttribute.

###  function copy( bufferAttribute: BufferAttribute ): this;

Copies another BufferAttribute to this BufferAttribute.

###  function copyArray( ): this;

Copy the array given here (which can be a normal array or TypedArray) into
[page:BufferAttribute.array array].  
  
See [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set TypedArray.set]
for notes on requirements if copying a TypedArray.

###  function copyAt( index1: Integer, bufferAttribute: BufferAttribute,
index2: Integer ): this;

Copy a vector from bufferAttribute[index2] to [page:BufferAttribute.array
array][index1].

###  function getX( index: Integer ): Number;

Returns the x component of the vector at the given index.

###  function getY( index: Integer ): Number;

Returns the y component of the vector at the given index.

###  function getZ( index: Integer ): Number;

Returns the z component of the vector at the given index.

###  function getW( index: Integer ): Number;

Returns the w component of the vector at the given index.

###  function onUpload( callback: Function ): this;

Sets the value of the onUploadCallback property.  
  
In the [example:webgl_buffergeometry WebGL / Buffergeometry] this is used to
free memory after the buffer has been transferred to the GPU.

###  function set( value: Array, offset: Integer ): this;

value -- an [page:Array] or [page:TypedArray] from which to copy values.  
offset -- (optional) index of the [page:BufferAttribute.array array] at which
to start copying.  
  
Calls [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set
TypedArray.set]( [page:Array value], [page:Integer offset] ) on the
[page:BufferAttribute.array array].  
  
In particular, see that page for requirements on [page:Array value] being a
[page:TypedArray].

###  function setUsage( value: Usage ): this;

Set [page:BufferAttribute.usage usage] to value. See usage
[page:BufferAttributeUsage constants] for all possible input values.  
  
Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desired usage before the next render.

###  function setX( index: Integer, x: Float ): this;

Sets the x component of the vector at the given index.

###  function setY( index: Integer, y: Float ): this;

Sets the y component of the vector at the given index.

###  function setZ( index: Integer, z: Float ): this;

Sets the z component of the vector at the given index.

###  function setW( index: Integer, w: Float ): this;

Sets the w component of the vector at the given index.

###  function setXY( index: Integer, x: Float, y: Float ): this;

Sets the x and y components of the vector at the given index.

###  function setXYZ( index: Integer, x: Float, y: Float, z: Float ): this;

Sets the x, y and z components of the vector at the given index.

###  function setXYZW( index: Integer, x: Float, y: Float, z: Float, w: Float
): this;

Sets the x, y, z and w components of the vector at the given index.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

