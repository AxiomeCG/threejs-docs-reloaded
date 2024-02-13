# Vector2

Class representing a 2D [link:https://en.wikipedia.org/wiki/Vector_space
vector]. A 2D vector is an ordered pair of numbers (labeled x and y), which
can be used to represent a number of things, such as:

  * A point in 2D space (i.e. a position on a plane).
  * A direction and length across a plane. In three.js the length will always be the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance] (straight-line distance) from `(0, 0)` to `(x, y)` and the direction is also measured from `(0, 0)` towards `(x, y)`.
  * Any arbitrary ordered pair of numbers.

There are other things a 2D vector can be used to represent, such as momentum
vectors, complex numbers and so on, however these are the most common uses in
three.js.

Iterating through a Vector2 instance will yield its components `(x, y)` in the
corresponding order.

## Code Example

  
```ts  
const a = new THREE.Vector2( 0, 1 ); //no arguments; will be initialised to
(0, 0) const b = new THREE.Vector2( ); const d = a.distanceTo( b );  
```  

## Constructor

###  function Vector2( x: Float, y: Float ): void;

[page:Float x] - the x value of this vector. Default is `0`.  
[page:Float y] - the y value of this vector. Default is `0`.  
  
Creates a new Vector2.

## Properties

###  Float height;

Alias for [page:.y y].

###  Boolean isVector2;

Read-only flag to check if a given object is of type Vector2.

###  Float width;

Alias for [page:.x x].

###  Float x;

###  Float y;

## Methods

###  function add( v: Vector2 ): this;

Adds [page:Vector2 v] to this vector.

###  function addScalar( s: Float ): this;

Adds the scalar value [page:Float s] to this vector's [page:.x x] and [page:.y
y] values.

###  function addScaledVector( v: Vector2, s: Float ): this;

Adds the multiple of [page:Vector2 v] and [page:Float s] to this vector.

###  function addVectors( a: Vector2, b: Vector2 ): this;

Sets this vector to [page:Vector2 a] + [page:Vector2 b].

###  function angle( ): Float;

Computes the angle in radians of this vector with respect to the positive
x-axis.

###  function angleTo( v: Vector2 ): Float;

Returns the angle between this vector and vector [page:Vector2 v] in radians.

###  function applyMatrix3( m: Matrix3 ): this;

Multiplies this vector (with an implicit 1 as the 3rd component) by m.

###  function ceil( ): this;

The [page:.x x] and [page:.y y] components of this vector are rounded up to
the nearest integer value.

###  function clamp( min: Vector2, max: Vector2 ): this;

[page:Vector2 min] - the minimum x and y values.  
[page:Vector2 max] - the maximum x and y values in the desired range  
  
If this vector's x or y value is greater than the max vector's x or y value,
it is replaced by the corresponding value.  
  
If this vector's x or y value is less than the min vector's x or y value, it
is replaced by the corresponding value.

###  function clampLength( min: Float, max: Float ): this;

[page:Float min] - the minimum value the length will be clamped to  
[page:Float max] - the maximum value the length will be clamped to  
  
If this vector's length is greater than the max value, it is replaced by the
max value.  
  
If this vector's length is less than the min value, it is replaced by the min
value.

###  function clampScalar( min: Float, max: Float ): this;

[page:Float min] - the minimum value the components will be clamped to  
[page:Float max] - the maximum value the components will be clamped to  
  
If this vector's x or y values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x or y values are less than the min value, they are replaced
by the min value.

###  function clone( ): Vector2;

Returns a new Vector2 with the same [page:.x x] and [page:.y y] values as this
one.

###  function copy( v: Vector2 ): this;

Copies the values of the passed Vector2's [page:.x x] and [page:.y y]
properties to this Vector2.

###  function distanceTo( v: Vector2 ): Float;

Computes the distance from this vector to [page:Vector2 v].

###  function manhattanDistanceTo( v: Vector2 ): Float;

Computes the [link:https://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
distance] from this vector to [page:Vector2 v].

###  function distanceToSquared( v: Vector2 ): Float;

Computes the squared distance from this vector to [page:Vector2 v]. If you are
just comparing the distance with another distance, you should compare the
distance squared instead as it is slightly more efficient to calculate.

###  function divide( v: Vector2 ): this;

Divides this vector by [page:Vector2 v].

###  function divideScalar( s: Float ): this;

Divides this vector by scalar [page:Float s].

###  function dot( v: Vector2 ): Float;

Calculates the [link:https://en.wikipedia.org/wiki/Dot_product dot product] of
this vector and [page:Vector2 v].

###  function cross( v: Vector2 ): Float;

Calculates the [link:https://en.wikipedia.org/wiki/Cross_product cross
product] of this vector and [page:Vector2 v]. Note that a 'cross-product' in
2D is not well-defined. This function computes a geometric cross-product often
used in 2D graphics

###  function equals( v: Vector2 ): Boolean;

Returns `true` if the components of this vector and [page:Vector2 v] are
strictly equal; `false` otherwise.

###  function floor( ): this;

The components of this vector are rounded down to the nearest integer value.

###  function fromArray( array: Array, offset: Integer ): this;

[page:Array array] - the source array.  
[page:Integer offset] - (optional) offset into the array. Default is `0`.  
  
Sets this vector's [page:.x x] value to be `array[ offset ]` and [page:.y y]
value to be `array[ offset + 1 ]`.

###  function fromBufferAttribute( attribute: BufferAttribute, index: Integer
): this;

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets this vector's [page:.x x] and [page:.y y] values from the
[page:BufferAttribute attribute].

###  function getComponent( index: Integer ): Float;

[page:Integer index] - `0` or `1`.  
  
If index equals `0` returns the [page:.x x] value.  
If index equals `1` returns the [page:.y y] value.

###  function length( ): Float;

Computes the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
length] (straight-line length) from (0, 0) to (x, y).

###  function manhattanLength( ): Float;

Computes the [link:http://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
length] of this vector.

###  function lengthSq( ): Float;

Computes the square of the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean length]
(straight-line length) from (0, 0) to (x, y). If you are comparing the lengths
of vectors, you should compare the length squared instead as it is slightly
more efficient to calculate.

###  function lerp( v: Vector2, alpha: Float ): this;

[page:Vector2 v] - [page:Vector2] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Linearly interpolates between this vector and [page:Vector2 v], where alpha is
the percent distance along the line - alpha = 0 will be this vector, and alpha
= 1 will be [page:Vector2 v].

###  function lerpVectors( v1: Vector2, v2: Vector2, alpha: Float ): this;

[page:Vector2 v1] - the starting [page:Vector2].  
[page:Vector2 v2] - [page:Vector2] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between [page:Vector2
v1] and [page:Vector2 v2] where alpha is the percent distance along the line
connecting the two vectors - alpha = 0 will be [page:Vector2 v1], and alpha =
1 will be [page:Vector2 v2].

###  function negate( ): this;

Inverts this vector - i.e. sets x = -x and y = -y.

###  function normalize( ): this;

Converts this vector to a [link:https://en.wikipedia.org/wiki/Unit_vector unit
vector] - that is, sets it equal to a vector with the same direction as this
one, but [page:.length length] 1.

###  function max( v: Vector2 ): this;

If this vector's x or y value is less than [page:Vector2 v]'s x or y value,
replace that value with the corresponding max value.

###  function min( v: Vector2 ): this;

If this vector's x or y value is greater than [page:Vector2 v]'s x or y value,
replace that value with the corresponding min value.

###  function multiply( v: Vector2 ): this;

Multiplies this vector by [page:Vector2 v].

###  function multiplyScalar( s: Float ): this;

Multiplies this vector by scalar [page:Float s].

###  function rotateAround( center: Vector2, angle: Float ): this;

[page:Vector2 center] - the point around which to rotate.  
[page:Float angle] - the angle to rotate, in radians.  
  
Rotates this vector around [page:Vector2 center] by [page:Float angle]
radians.

###  function round( ): this;

The components of this vector are rounded to the nearest integer value.

###  function roundToZero( ): this;

The components of this vector are rounded towards zero (up if negative, down
if positive) to an integer value.

###  function set( x: Float, y: Float ): this;

Sets the [page:.x x] and [page:.y y] components of this vector.

###  function setComponent( index: Integer, value: Float ): this;

[page:Integer index] - `0` or `1`.  
[page:Float value] - [page:Float]  
  
If index equals `0` set [page:.x x] to [page:Float value].  
If index equals `1` set [page:.y y] to [page:Float value]

###  function setLength( l: Float ): this;

Sets this vector to a vector with the same direction as this one, but
[page:.length length] [page:Float l].

###  function setScalar( scalar: Float ): this;

Sets the [page:.x x] and [page:.y y] values of this vector both equal to
[page:Float scalar].

###  function setX( x: Float ): this;

Replaces this vector's [page:.x x] value with [page:Float x].

###  function setY( y: Float ): this;

Replaces this vector's [page:.y y] value with [page:Float y].

###  function sub( v: Vector2 ): this;

Subtracts [page:Vector2 v] from this vector.

###  function subScalar( s: Float ): this;

Subtracts [page:Float s] from this vector's [page:.x x] and [page:.y y]
components.

###  function subVectors( a: Vector2, b: Vector2 ): this;

Sets this vector to [page:Vector2 a] - [page:Vector2 b].

###  function toArray( array: Array, offset: Integer ): Array;

[page:Array array] - (optional) array to store this vector to. If this is not
provided, a new array will be created.  
[page:Integer offset] - (optional) optional offset into the array.  
  
Returns an array [x, y], or copies x and y into the provided [page:Array
array].

###  function random( ): this;

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

