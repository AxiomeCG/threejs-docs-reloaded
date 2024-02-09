# [name]

Class representing a 4D [link:https://en.wikipedia.org/wiki/Vector_space
vector]. A 4D vector is an ordered quadruplet of numbers (labeled x, y, z, and
w), which can be used to represent a number of things, such as:

  * A point in 4D space.
  * A direction and length in 4D space. In three.js the length will always be the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance] (straight-line distance) from `(0, 0, 0, 0)` to `(x, y, z, w)` and the direction is also measured from `(0, 0, 0, 0)` towards `(x, y, z, w)`. 
  * Any arbitrary ordered quadruplet of numbers.

There are other things a 4D vector can be used to represent, however these are
the most common uses in *three.js*.

Iterating through a [name] instance will yield its components `(x, y, z, w)`
in the corresponding order.

## Code Example

  
```ts  
const a = new THREE.Vector4( 0, 1, 0, 0 );  
  
//no arguments; will be initialised to (0, 0, 0, 1)  
const b = new THREE.Vector4( );  
  
const d = a.dot( b );  
```  

## Constructor

###  [name]( [param:Float x], [param:Float y], [param:Float z], [param:Float
w] )

[page:Float x] - the x value of this vector. Default is `0`.  
[page:Float y] - the y value of this vector. Default is `0`.  
[page:Float z] - the z value of this vector. Default is `0`.  
[page:Float w] - the w value of this vector. Default is `1`.  
  
Creates a new [name].

## Properties

### <br/> Boolean isVector4; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Float x; <br/>

### <br/> Float y; <br/>

### <br/> Float z; <br/>

### <br/> Float w; <br/>

### <br/> Float width; <br/>

Alias for [page:.z z].

### <br/> Float height; <br/>

Alias for [page:.w w].

## Methods

### <br/> function add( v: Vector4 ): add; <br/>

Adds [page:Vector4 v] to this vector.

### <br/> function addScalar( s: Float ): addScalar; <br/>

Adds the scalar value s to this vector's [page:.x x], [page:.y y], [page:.z z]
and [page:.w w] values.

### <br/> function addScaledVector( v: Vector4, s: Float ): addScaledVector;
<br/>

Adds the multiple of [page:Vector4 v] and [page:Float s] to this vector.

### <br/> function addVectors( a: Vector4, b: Vector4 ): addVectors; <br/>

Sets this vector to [page:Vector4 a] + [page:Vector4 b].

### <br/> function applyMatrix4( m: Matrix4 ): applyMatrix4; <br/>

Multiplies this vector by 4 x 4 [page:Matrix4 m].

### <br/> function ceil( ): ceil; <br/>

The [page:.x x], [page:.y y], [page:.z z] and [page:.w w] components of this
vector are rounded up to the nearest integer value.

### <br/> function clamp( min: Vector4, max: Vector4 ): clamp; <br/>

[page:Vector4 min] - the minimum [page:.x x], [page:.y y], [page:.z z] and
[page:.w w] values.  
[page:Vector4 max] - the maximum [page:.x x], [page:.y y], [page:.z z] and
[page:.w w] values in the desired range  
  
If this vector's x, y, z or w value is greater than the max vector's x, y, z
or w value, it is replaced by the corresponding value.  
  
If this vector's x, y, z or w value is less than the min vector's x, y, z or w
value, it is replaced by the corresponding value.

### <br/> function clampLength( min: Float, max: Float ): clampLength; <br/>

[page:Float min] - the minimum value the length will be clamped to  
[page:Float max] - the maximum value the length will be clamped to  
  
If this vector's length is greater than the max value, it is replaced by the
max value.  
  
If this vector's length is less than the min value, it is replaced by the min
value.

### <br/> function clampScalar( min: Float, max: Float ): clampScalar; <br/>

[page:Float min] - the minimum value the components will be clamped to  
[page:Float max] - the maximum value the components will be clamped to  
  
If this vector's x, y, z or w values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x, y, z or w values are less than the min value, they are
replaced by the min value.

### [method:Vector4 clone]()

Returns a new Vector4 with the same [page:.x x], [page:.y y], [page:.z z] and
[page:.w w] values as this one.

### <br/> function copy( v: Vector4 ): copy; <br/>

Copies the values of the passed Vector4's [page:.x x], [page:.y y], [page:.z
z] and [page:.w w] properties to this Vector4.

### <br/> function divideScalar( s: Float ): divideScalar; <br/>

Divides this vector by scalar [page:Float s].

### [method:Float dot]( [param:Vector4 v] )

Calculates the [link:https://en.wikipedia.org/wiki/Dot_product dot product] of
this vector and [page:Vector4 v].

### [method:Boolean equals]( [param:Vector4 v] )

Returns `true` if the components of this vector and [page:Vector4 v] are
strictly equal; `false` otherwise.

### <br/> function floor( ): floor; <br/>

The components of this vector are rounded down to the nearest integer value.

### <br/> function fromArray( array: Array, offset: Integer ): fromArray;
<br/>

[page:Array array] - the source array.  
[page:Integer offset] - (optional) offset into the array. Default is `0`.  
  
Sets this vector's [page:.x x] value to be `array[ offset + 0 ]`, [page:.y y]
value to be `array[ offset + 1 ]` [page:.z z] value to be `array[ offset + 2
]` and [page:.w w ] value to be `array[ offset + 3 ]`.

### <br/> function fromBufferAttribute( attribute: BufferAttribute, index:
Integer ): fromBufferAttribute; <br/>

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets this vector's [page:.x x], [page:.y y], [page:.z z] and [page:.w w]
values from the [page:BufferAttribute attribute].

### [method:Float getComponent]( [param:Integer index] )

[page:Integer index] - `0`, `1`, `2` or `3`.  
  
If index equals `0` returns the [page:.x x] value.  
If index equals `1` returns the [page:.y y] value.  
If index equals `2` returns the [page:.z z] value.  
If index equals `3` returns the [page:.w w] value.

### [method:Float length]()

Computes the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
length] (straight-line length) from `(0, 0, 0, 0)` to `(x, y, z, w)`.

### [method:Float manhattanLength]()

Computes the [link:http://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
length] of this vector.

### [method:Float lengthSq]()

Computes the square of the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean length]
(straight-line length) from `(0, 0, 0, 0)` to `(x, y, z, w)`. If you are
comparing the lengths of vectors, you should compare the length squared
instead as it is slightly more efficient to calculate.

### <br/> function lerp( v: Vector4, alpha: Float ): lerp; <br/>

[page:Vector4 v] - [page:Vector4] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Linearly interpolates between this vector and [page:Vector4 v], where alpha is
the percent distance along the line - `alpha = 0` will be this vector, and
`alpha = 1` will be [page:Vector4 v].

### <br/> function lerpVectors( v1: Vector4, v2: Vector4, alpha: Float ):
lerpVectors; <br/>

[page:Vector4 v1] - the starting [page:Vector4].  
[page:Vector4 v2] - [page:Vector4] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between [page:Vector4
v1] and [page:Vector4 v2] where alpha is the percent distance along the line
connecting the two vectors - alpha = 0 will be [page:Vector4 v1], and alpha =
1 will be [page:Vector4 v2].

### <br/> function negate( ): negate; <br/>

Inverts this vector - i.e. sets x = -x, y = -y, z = -z and w = -w.

### <br/> function normalize( ): normalize; <br/>

Converts this vector to a [link:https://en.wikipedia.org/wiki/Unit_vector unit
vector] \- that is, sets it equal to a vector with the same direction as this
one, but [page:.length length] 1.

### <br/> function max( v: Vector4 ): max; <br/>

If this vector's x, y, z or w value is less than [page:Vector4 v]'s x, y, z or
w value, replace that value with the corresponding max value.

### <br/> function min( v: Vector4 ): min; <br/>

If this vector's x, y, z or w value is greater than [page:Vector4 v]'s x, y, z
or w value, replace that value with the corresponding min value.

### <br/> function multiply( v: Vector4 ): multiply; <br/>

Multiplies this vector by [page:Vector4 v].

### <br/> function multiplyScalar( s: Float ): multiplyScalar; <br/>

Multiplies this vector by scalar [page:Float s].

### <br/> function round( ): round; <br/>

The components of this vector are rounded to the nearest integer value.

### <br/> function roundToZero( ): roundToZero; <br/>

The components of this vector are rounded towards zero (up if negative, down
if positive) to an integer value.

### <br/> function set( x: Float, y: Float, z: Float, w: Float ): set; <br/>

Sets the [page:.x x], [page:.y y], [page:.z z] and [page:.w w] components of
this vector.

### <br/> function setAxisAngleFromQuaternion( q: Quaternion ):
setAxisAngleFromQuaternion; <br/>

[page:Quaternion q] - a normalized [page:Quaternion]  
  
Sets the [page:.x x], [page:.y y] and [page:.z z] components of this vector to
the quaternion's axis and [page:.w w] to the angle.

### <br/> function setAxisAngleFromRotationMatrix( m: Matrix4 ):
setAxisAngleFromRotationMatrix; <br/>

[page:Matrix4 m] - a [page:Matrix4] of which the upper left 3x3 matrix is a
pure rotation matrix.  
  
Sets the [page:.x x], [page:.y y] and [page:.z z] to the axis of rotation and
[page:.w w] to the angle.

### <br/> function setComponent( index: Integer, value: Float ): setComponent;
<br/>

[page:Integer index] - `0`, `1`, `2` or `3`.  
[page:Float value] - [page:Float]  
  
If index equals `0` set [page:.x x] to [page:Float value].  
If index equals `1` set [page:.y y] to [page:Float value].  
If index equals `2` set [page:.z z] to [page:Float value].  
If index equals `3` set [page:.w w] to [page:Float value].

### <br/> function setLength( l: Float ): setLength; <br/>

Sets this vector to a vector with the same direction as this one, but
[page:.length length] [page:Float l].

### <br/> function setScalar( scalar: Float ): setScalar; <br/>

Sets the [page:.x x], [page:.y y], [page:.z z] and [page:.w w] values of this
vector both equal to [page:Float scalar].

### <br/> function setX( x: Float ): setX; <br/>

Replaces this vector's [page:.x x] value with [page:Float x].

### <br/> function setY( y: Float ): setY; <br/>

Replaces this vector's [page:.y y] value with [page:Float y].

### <br/> function setZ( z: Float ): setZ; <br/>

Replaces this vector's [page:.z z] value with [page:Float z].

### <br/> function setW( w: Float ): setW; <br/>

Replaces this vector's [page:.w w] value with [page:Float w].

### <br/> function sub( v: Vector4 ): sub; <br/>

Subtracts [page:Vector4 v] from this vector.

### <br/> function subScalar( s: Float ): subScalar; <br/>

Subtracts [page:Float s] from this vector's [page:.x x], [page:.y y], [page:.z
z] and [page:.w w] components.

### <br/> function subVectors( a: Vector4, b: Vector4 ): subVectors; <br/>

Sets this vector to [page:Vector4 a] - [page:Vector4 b].

###  [method:Array toArray]( [param:Array array], [param:Integer offset] )

[page:Array array] - (optional) array to store this vector to. If this is not
provided, a new array will be created.  
[page:Integer offset] - (optional) optional offset into the array.  
  
Returns an array [x, y, z, w], or copies x, y, z and w into the provided
[page:Array array].

### <br/> function random( ): random; <br/>

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

