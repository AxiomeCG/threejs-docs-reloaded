# Vector4

Class representing a 4D <a
href="https://en.wikipedia.org/wiki/Vector_space">vector</a>. A 4D vector is
an ordered quadruplet of numbers (labeled x, y, z, and w), which can be used
to represent a number of things, such as:

  * A point in 4D space.
  * A direction and length in 4D space. In three.js the length will always be the <a href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a> (straight-line distance) from `(0, 0, 0, 0)` to `(x, y, z, w)` and the direction is also measured from `(0, 0, 0, 0)` towards `(x, y, z, w)`.
  * Any arbitrary ordered quadruplet of numbers.

There are other things a 4D vector can be used to represent, however these are
the most common uses in *three.js*.

Iterating through a Vector4 instance will yield its components `(x, y, z, w)`
in the corresponding order.

## Code Example

  
```ts  
const a = new THREE.Vector4( 0, 1, 0, 0 ); //no arguments; will be initialised
to (0, 0, 0, 1) const b = new THREE.Vector4( ); const d = a.dot( b );  
```  

## Constructor

### Vector4

  
  
```ts  
function Vector4( x: Float, y: Float, z: Float, w: Float ): void;  
```  

[x](#) - the x value of this vector. Default is `0`.  
[y](#) - the y value of this vector. Default is `0`.  
[z](#) - the z value of this vector. Default is `0`.  
[w](#) - the w value of this vector. Default is `1`.  
  
Creates a new Vector4.

## Properties

### isVector4

  
  
```ts  
isVector4: Boolean;  
```  

Read-only flag to check if a given object is of type Vector4.

### x

  
  
```ts  
x: Float;  
```  

### y

  
  
```ts  
y: Float;  
```  

### z

  
  
```ts  
z: Float;  
```  

### w

  
  
```ts  
w: Float;  
```  

### width

  
  
```ts  
width: Float;  
```  

Alias for [.z](#z).

### height

  
  
```ts  
height: Float;  
```  

Alias for [.w](#w).

## Methods

### add

  
  
```ts  
function add( v: Vector4 ): this;  
```  

Adds [v](en\math\Vector4.html) to this vector.

### addScalar

  
  
```ts  
function addScalar( s: Float ): this;  
```  

Adds the scalar value s to this vector's [.x](#x), [.y](#y), [.z](#z) and
[.w](#w) values.

### addScaledVector

  
  
```ts  
function addScaledVector( v: Vector4, s: Float ): this;  
```  

Adds the multiple of [v](en\math\Vector4.html) and [s](#) to this vector.

### addVectors

  
  
```ts  
function addVectors( a: Vector4, b: Vector4 ): this;  
```  

Sets this vector to [a](en\math\Vector4.html) + [b](en\math\Vector4.html).

### applyMatrix4

  
  
```ts  
function applyMatrix4( m: Matrix4 ): this;  
```  

Multiplies this vector by 4 x 4 [m](en\math\Matrix4.html).

### ceil

  
  
```ts  
function ceil( ): this;  
```  

The [.x](#x), [.y](#y), [.z](#z) and [.w](#w) components of this vector are
rounded up to the nearest integer value.

### clamp

  
  
```ts  
function clamp( min: Vector4, max: Vector4 ): this;  
```  

[.ector4](#ector4) - the minimum [.x](#x), [.y](#y), [.z](#z) and [.w](#w)
values.  
[.ector4](#ector4) - the maximum [.x](#x), [.y](#y), [.z](#z) and [.w](#w)
values in the desired range  
  
If this vector's x, y, z or w value is greater than the max vector's x, y, z
or w value, it is replaced by the corresponding value.  
  
If this vector's x, y, z or w value is less than the min vector's x, y, z or w
value, it is replaced by the corresponding value.

### clampLength

  
  
```ts  
function clampLength( min: Float, max: Float ): this;  
```  

[min](#) - the minimum value the length will be clamped to  
[max](#) - the maximum value the length will be clamped to  
  
If this vector's length is greater than the max value, it is replaced by the
max value.  
  
If this vector's length is less than the min value, it is replaced by the min
value.

### clampScalar

  
  
```ts  
function clampScalar( min: Float, max: Float ): this;  
```  

[min](#) - the minimum value the components will be clamped to  
[max](#) - the maximum value the components will be clamped to  
  
If this vector's x, y, z or w values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x, y, z or w values are less than the min value, they are
replaced by the min value.

### clone

  
  
```ts  
function clone( ): Vector4;  
```  

Returns a new Vector4 with the same [.x](#x), [.y](#y), [.z](#z) and [.w](#w)
values as this one.

### copy

  
  
```ts  
function copy( v: Vector4 ): this;  
```  

Copies the values of the passed Vector4's [.x](#x), [.y](#y), [.z](#z) and
[.w](#w) properties to this Vector4.

### divideScalar

  
  
```ts  
function divideScalar( s: Float ): this;  
```  

Divides this vector by scalar [s](#).

### dot

  
  
```ts  
function dot( v: Vector4 ): Float;  
```  

Calculates the <a href="https://en.wikipedia.org/wiki/Dot_product">dot
product</a> of this vector and [v](en\math\Vector4.html).

### equals

  
  
```ts  
function equals( v: Vector4 ): Boolean;  
```  

Returns `true` if the components of this vector and [v](en\math\Vector4.html)
are strictly equal; `false` otherwise.

### floor

  
  
```ts  
function floor( ): this;  
```  

The components of this vector are rounded down to the nearest integer value.

### fromArray

  
  
```ts  
function fromArray( array: Array, offset: Integer ): this;  
```  

[array](#) - the source array.  
[offset](#) - (optional) offset into the array. Default is `0`.  
  
Sets this vector's [.x](#x) value to be `array[ offset + 0 ]`, [.y](#y) value
to be `array[ offset + 1 ]` [.z](#z) value to be `array[ offset + 2 ]` and
[.w](#w) value to be `array[ offset + 3 ]`.

### fromBufferAttribute

  
  
```ts  
function fromBufferAttribute( attribute: BufferAttribute, index: Integer ):
this;  
```  

[attribute](en\core\BufferAttribute.html) - the source attribute.  
[index](#) - index in the attribute.  
  
Sets this vector's [.x](#x), [.y](#y), [.z](#z) and [.w](#w) values from the
[.ufferAttribute](#ufferAttribute).

### getComponent

  
  
```ts  
function getComponent( index: Integer ): Float;  
```  

[index](#) - `0`, `1`, `2` or `3`.  
  
If index equals `0` returns the [.x](#x) value.  
If index equals `1` returns the [.y](#y) value.  
If index equals `2` returns the [.z](#z) value.  
If index equals `3` returns the [.w](#w) value.

### length

  
  
```ts  
function length( ): Float;  
```  

Computes the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean length</a>
(straight-line length) from `(0, 0, 0, 0)` to `(x, y, z, w)`.

### manhattanLength

  
  
```ts  
function manhattanLength( ): Float;  
```  

Computes the <a href="http://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan
length</a> of this vector.

### lengthSq

  
  
```ts  
function lengthSq( ): Float;  
```  

Computes the square of the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean length</a>
(straight-line length) from `(0, 0, 0, 0)` to `(x, y, z, w)`. If you are
comparing the lengths of vectors, you should compare the length squared
instead as it is slightly more efficient to calculate.

### lerp

  
  
```ts  
function lerp( v: Vector4, alpha: Float ): this;  
```  

[v](en\math\Vector4.html) - [Vector4](en\math\Vector4.html) to interpolate
towards.  
[alpha](#) - interpolation factor, typically in the closed interval `[0, 1]`.  
  
Linearly interpolates between this vector and [v](en\math\Vector4.html), where
alpha is the percent distance along the line - `alpha = 0` will be this
vector, and `alpha = 1` will be [v](en\math\Vector4.html).

### lerpVectors

  
  
```ts  
function lerpVectors( v1: Vector4, v2: Vector4, alpha: Float ): this;  
```  

[v1](en\math\Vector4.html) - the starting [Vector4](en\math\Vector4.html).  
[v2](en\math\Vector4.html) - [Vector4](en\math\Vector4.html) to interpolate
towards.  
[alpha](#) - interpolation factor, typically in the closed interval `[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between
[v1](en\math\Vector4.html) and [v2](en\math\Vector4.html) where alpha is the
percent distance along the line connecting the two vectors - alpha = 0 will be
[v1](en\math\Vector4.html), and alpha = 1 will be [v2](en\math\Vector4.html).

### negate

  
  
```ts  
function negate( ): this;  
```  

Inverts this vector - i.e. sets x = -x, y = -y, z = -z and w = -w.

### normalize

  
  
```ts  
function normalize( ): this;  
```  

Converts this vector to a <a
href="https://en.wikipedia.org/wiki/Unit_vector">unit vector</a> \- that is,
sets it equal to a vector with the same direction as this one, but
[.length](#length) 1.

### max

  
  
```ts  
function max( v: Vector4 ): this;  
```  

If this vector's x, y, z or w value is less than [v](en\math\Vector4.html)'s
x, y, z or w value, replace that value with the corresponding max value.

### min

  
  
```ts  
function min( v: Vector4 ): this;  
```  

If this vector's x, y, z or w value is greater than
[v](en\math\Vector4.html)'s x, y, z or w value, replace that value with the
corresponding min value.

### multiply

  
  
```ts  
function multiply( v: Vector4 ): this;  
```  

Multiplies this vector by [v](en\math\Vector4.html).

### multiplyScalar

  
  
```ts  
function multiplyScalar( s: Float ): this;  
```  

Multiplies this vector by scalar [s](#).

### round

  
  
```ts  
function round( ): this;  
```  

The components of this vector are rounded to the nearest integer value.

### roundToZero

  
  
```ts  
function roundToZero( ): this;  
```  

The components of this vector are rounded towards zero (up if negative, down
if positive) to an integer value.

### set

  
  
```ts  
function set( x: Float, y: Float, z: Float, w: Float ): this;  
```  

Sets the [.x](#x), [.y](#y), [.z](#z) and [.w](#w) components of this vector.

### setAxisAngleFromQuaternion

  
  
```ts  
function setAxisAngleFromQuaternion( q: Quaternion ): this;  
```  

[q](en\math\Quaternion.html) - a normalized
[Quaternion](en\math\Quaternion.html)  
  
Sets the [.x](#x), [.y](#y) and [.z](#z) components of this vector to the
quaternion's axis and [.w](#w) to the angle.

### setAxisAngleFromRotationMatrix

  
  
```ts  
function setAxisAngleFromRotationMatrix( m: Matrix4 ): this;  
```  

[m](en\math\Matrix4.html) - a [Matrix4](en\math\Matrix4.html) of which the
upper left 3x3 matrix is a pure rotation matrix.  
  
Sets the [.x](#x), [.y](#y) and [.z](#z) to the axis of rotation and [.w](#w)
to the angle.

### setComponent

  
  
```ts  
function setComponent( index: Integer, value: Float ): this;  
```  

[index](#) - `0`, `1`, `2` or `3`.  
[value](#) - [Float](#)  
  
If index equals `0` set [.x](#x) to [.loat](#loat).  
If index equals `1` set [.y](#y) to [.loat](#loat).  
If index equals `2` set [.z](#z) to [.loat](#loat).  
If index equals `3` set [.w](#w) to [.loat](#loat).

### setLength

  
  
```ts  
function setLength( l: Float ): this;  
```  

Sets this vector to a vector with the same direction as this one, but
[.length](#length) [.loat](#loat).

### setScalar

  
  
```ts  
function setScalar( scalar: Float ): this;  
```  

Sets the [.x](#x), [.y](#y), [.z](#z) and [.w](#w) values of this vector both
equal to [.loat](#loat).

### setX

  
  
```ts  
function setX( x: Float ): this;  
```  

Replaces this vector's [.x](#x) value with [.loat](#loat).

### setY

  
  
```ts  
function setY( y: Float ): this;  
```  

Replaces this vector's [.y](#y) value with [.loat](#loat).

### setZ

  
  
```ts  
function setZ( z: Float ): this;  
```  

Replaces this vector's [.z](#z) value with [.loat](#loat).

### setW

  
  
```ts  
function setW( w: Float ): this;  
```  

Replaces this vector's [.w](#w) value with [.loat](#loat).

### sub

  
  
```ts  
function sub( v: Vector4 ): this;  
```  

Subtracts [v](en\math\Vector4.html) from this vector.

### subScalar

  
  
```ts  
function subScalar( s: Float ): this;  
```  

Subtracts [.loat](#loat) from this vector's [.x](#x), [.y](#y), [.z](#z) and
[.w](#w) components.

### subVectors

  
  
```ts  
function subVectors( a: Vector4, b: Vector4 ): this;  
```  

Sets this vector to [a](en\math\Vector4.html) - [b](en\math\Vector4.html).

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - (optional) array to store this vector to. If this is not
provided, a new array will be created.  
[offset](#) - (optional) optional offset into the array.  
  
Returns an array [x, y, z, w], or copies x, y, z and w into the provided
[array](#).

### random

  
  
```ts  
function random( ): this;  
```  

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Vector4.js">src/math/Vector4.js</a>

