# [name]

This class stores data for an attribute (such as vertex positions, face
indices, normals, colors, UVs, and any custom attributes ) associated with a
[page:BufferGeometry], which allows for more efficient passing of data to the
GPU. See that page for details and a usage example. When working with vector-
like data, the _.fromBufferAttribute( attribute, index )_ helper methods on
[page:Vector2.fromBufferAttribute Vector2], [page:Vector3.fromBufferAttribute
Vector3], [page:Vector4.fromBufferAttribute Vector4], and
[page:Color.fromBufferAttribute Color] classes may be helpful.

## Constructor

### [name]( [param:TypedArray array], [param:Integer itemSize], [param:Boolean
normalized] )

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
(signed) would map from -32768 - +32767 to -1.0f \- +1.0f. If [page:Boolean
normalized] is false, the values will be converted to floats unmodified, i.e.
32767 becomes 32767.0f.

## Properties

### <br/> TypedArray array; <br/>

The [page:TypedArray array] holding data stored in the buffer.

### <br/> Integer count; <br/>

Stores the [page:BufferAttribute.array array]'s length divided by the
[page:BufferAttribute.itemSize itemSize].  
  
If the buffer is storing a 3-component vector (such as a position, normal, or
color), then this will count the number of such vectors stored.

### <br/> Number gpuType; <br/>

Configures the bound GPU type for use in shaders. Either [page:BufferAttribute
THREE.FloatType] or [page:BufferAttribute THREE.IntType], default is
[page:BufferAttribute THREE.FloatType]. Note: this only has an effect for
integer arrays and is not configurable for float arrays. For lower precision
float types, see [page:BufferAttributeTypes THREE.Float16BufferAttribute].

### <br/> Boolean isBufferAttribute; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Integer itemSize; <br/>

The length of vectors that are being stored in the [page:BufferAttribute.array
array].

### <br/> String name; <br/>

Optional name for this attribute instance. Default is an empty string.

### <br/> Boolean needsUpdate; <br/>

Flag to indicate that this attribute has changed and should be re-sent to the
GPU. Set this to true when you modify the value of the array.  
  
Setting this to true also increments the [page:BufferAttribute.version
version].

### <br/> Boolean normalized; <br/>

Indicates how the underlying data in the buffer maps to the values in the GLSL
shader code. See the constructor above for details.

### <br/> Function onUploadCallback; <br/>

A callback function that is executed after the Renderer has transferred the
attribute array data to the GPU.

### <br/> Object updateRange; <br/>

Object containing:  
[page:Integer offset]: Default is `0`. Position at which to start update.  
[page:Integer count]: Default is `-1`, which means don't use update ranges.  
  
This can be used to only update some components of stored vectors (for
example, just the component related to color).

### <br/> Usage usage; <br/>

Defines the intended usage pattern of the data store for optimization
purposes. Corresponds to the `usage` parameter of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bufferData
WebGLRenderingContext.bufferData](). Default is [page:BufferAttributeUsage
StaticDrawUsage]. See usage [page:BufferAttributeUsage constants] for all
possible values.  
  
Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desired usage before the next render.

### <br/> Integer version; <br/>

A version number, incremented every time the [page:BufferAttribute.needsUpdate
needsUpdate] property is set to true.

## Methods

### <br/> function applyMatrix3( m: Matrix3 ): applyMatrix3; <br/>

Applies matrix [page:Matrix3 m] to every Vector3 element of this
BufferAttribute.

### <br/> function applyMatrix4( m: Matrix4 ): applyMatrix4; <br/>

Applies matrix [page:Matrix4 m] to every Vector3 element of this
BufferAttribute.

### <br/> function applyNormalMatrix( m: Matrix3 ): applyNormalMatrix; <br/>

Applies normal matrix [page:Matrix3 m] to every Vector3 element of this
BufferAttribute.

### <br/> function transformDirection( m: Matrix4 ): transformDirection; <br/>

Applies matrix [page:Matrix4 m] to every Vector3 element of this
BufferAttribute, interpreting the elements as a direction vectors.

### [method:BufferAttribute clone]()

Return a copy of this bufferAttribute.

### <br/> function copy( bufferAttribute: BufferAttribute ): copy; <br/>

Copies another BufferAttribute to this BufferAttribute.

### <br/> function copyArray( ): copyArray; <br/>

Copy the array given here (which can be a normal array or TypedArray) into
[page:BufferAttribute.array array].  
  
See [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set TypedArray.set]
for notes on requirements if copying a TypedArray.

### <br/> function copyAt( index1: Integer, bufferAttribute: BufferAttribute,
index2: Integer ): copyAt; <br/>

Copy a vector from bufferAttribute[index2] to [page:BufferAttribute.array
array][index1].

### [method:Number getX]( [param:Integer index] )

Returns the x component of the vector at the given index.

### [method:Number getY]( [param:Integer index] )

Returns the y component of the vector at the given index.

### [method:Number getZ]( [param:Integer index] )

Returns the z component of the vector at the given index.

### [method:Number getW]( [param:Integer index] )

Returns the w component of the vector at the given index.

### <br/> function onUpload( callback: Function ): onUpload; <br/>

Sets the value of the onUploadCallback property.  
  
In the [example:webgl_buffergeometry WebGL / Buffergeometry] this is used to
free memory after the buffer has been transferred to the GPU.

### <br/> function set( value: Array, offset: Integer ): set; <br/>

value -- an [page:Array] or [page:TypedArray] from which to copy values.  
offset -- (optional) index of the [page:BufferAttribute.array array] at which
to start copying.  
  
Calls [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set
TypedArray.set]( [page:Array value], [page:Integer offset] ) on the
[page:BufferAttribute.array array].  
  
In particular, see that page for requirements on [page:Array value] being a
[page:TypedArray].

### <br/> function setUsage( value: Usage ): setUsage; <br/>

Set [page:BufferAttribute.usage usage] to value. See usage
[page:BufferAttributeUsage constants] for all possible input values.  
  
Note: After the initial use of a buffer, its usage cannot be changed. Instead,
instantiate a new one and set the desired usage before the next render.

### <br/> function setX( index: Integer, x: Float ): setX; <br/>

Sets the x component of the vector at the given index.

### <br/> function setY( index: Integer, y: Float ): setY; <br/>

Sets the y component of the vector at the given index.

### <br/> function setZ( index: Integer, z: Float ): setZ; <br/>

Sets the z component of the vector at the given index.

### <br/> function setW( index: Integer, w: Float ): setW; <br/>

Sets the w component of the vector at the given index.

### <br/> function setXY( index: Integer, x: Float, y: Float ): setXY; <br/>

Sets the x and y components of the vector at the given index.

### <br/> function setXYZ( index: Integer, x: Float, y: Float, z: Float ):
setXYZ; <br/>

Sets the x, y and z components of the vector at the given index.

### <br/> function setXYZW( index: Integer, x: Float, y: Float, z: Float, w:
Float ): setXYZW; <br/>

Sets the x, y, z and w components of the vector at the given index.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

