# Vector2

Class representing a 2D <a
href="https://en.wikipedia.org/wiki/Vector_space">vector</a>. A 2D vector is
an ordered pair of numbers (labeled x and y), which can be used to represent a
number of things, such as:

  * A point in 2D space (i.e. a position on a plane).
  * A direction and length across a plane. In three.js the length will always be the <a href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a> (straight-line distance) from `(0, 0)` to `(x, y)` and the direction is also measured from `(0, 0)` towards `(x, y)`.
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

### Vector2

  
  
```ts  
function Vector2( x: Float, y: Float ): void;  
```  

[x](#) - the x value of this vector. Default is `0`.  
[y](#) - the y value of this vector. Default is `0`.  
  
Creates a new Vector2.

## Properties

### height

  
  
```ts  
height: Float;  
```  

Alias for [.y](#y).

### isVector2

  
  
```ts  
isVector2: Boolean;  
```  

Read-only flag to check if a given object is of type Vector2.

### width

  
  
```ts  
width: Float;  
```  

Alias for [.x](#x).

### x

  
  
```ts  
x: Float;  
```  

### y

  
  
```ts  
y: Float;  
```  

## Methods

### add

  
  
```ts  
function add( v: Vector2 ): this;  
```  

Adds [v](en\math\Vector2.html) to this vector.

### addScalar

  
  
```ts  
function addScalar( s: Float ): this;  
```  

Adds the scalar value [.loat](#loat) to this vector's [.x](#x) and [.y](#y)
values.

### addScaledVector

  
  
```ts  
function addScaledVector( v: Vector2, s: Float ): this;  
```  

Adds the multiple of [v](en\math\Vector2.html) and [s](#) to this vector.

### addVectors

  
  
```ts  
function addVectors( a: Vector2, b: Vector2 ): this;  
```  

Sets this vector to [a](en\math\Vector2.html) + [b](en\math\Vector2.html).

### angle

  
  
```ts  
function angle( ): Float;  
```  

Computes the angle in radians of this vector with respect to the positive
x-axis.

### angleTo

  
  
```ts  
function angleTo( v: Vector2 ): Float;  
```  

Returns the angle between this vector and vector [v](en\math\Vector2.html) in
radians.

### applyMatrix3

  
  
```ts  
function applyMatrix3( m: Matrix3 ): this;  
```  

Multiplies this vector (with an implicit 1 as the 3rd component) by m.

### ceil

  
  
```ts  
function ceil( ): this;  
```  

The [.x](#x) and [.y](#y) components of this vector are rounded up to the
nearest integer value.

### clamp

  
  
```ts  
function clamp( min: Vector2, max: Vector2 ): this;  
```  

[min](en\math\Vector2.html) - the minimum x and y values.  
[max](en\math\Vector2.html) - the maximum x and y values in the desired range  
  
If this vector's x or y value is greater than the max vector's x or y value,
it is replaced by the corresponding value.  
  
If this vector's x or y value is less than the min vector's x or y value, it
is replaced by the corresponding value.

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
  
If this vector's x or y values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x or y values are less than the min value, they are replaced
by the min value.

### clone

  
  
```ts  
function clone( ): Vector2;  
```  

Returns a new Vector2 with the same [.x](#x) and [.y](#y) values as this one.

### copy

  
  
```ts  
function copy( v: Vector2 ): this;  
```  

Copies the values of the passed Vector2's [.x](#x) and [.y](#y) properties to
this Vector2.

### distanceTo

  
  
```ts  
function distanceTo( v: Vector2 ): Float;  
```  

Computes the distance from this vector to [v](en\math\Vector2.html).

### manhattanDistanceTo

  
  
```ts  
function manhattanDistanceTo( v: Vector2 ): Float;  
```  

Computes the <a
href="https://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan distance</a>
from this vector to [v](en\math\Vector2.html).

### distanceToSquared

  
  
```ts  
function distanceToSquared( v: Vector2 ): Float;  
```  

Computes the squared distance from this vector to [v](en\math\Vector2.html).
If you are just comparing the distance with another distance, you should
compare the distance squared instead as it is slightly more efficient to
calculate.

### divide

  
  
```ts  
function divide( v: Vector2 ): this;  
```  

Divides this vector by [v](en\math\Vector2.html).

### divideScalar

  
  
```ts  
function divideScalar( s: Float ): this;  
```  

Divides this vector by scalar [s](#).

### dot

  
  
```ts  
function dot( v: Vector2 ): Float;  
```  

Calculates the <a href="https://en.wikipedia.org/wiki/Dot_product">dot
product</a> of this vector and [v](en\math\Vector2.html).

### cross

  
  
```ts  
function cross( v: Vector2 ): Float;  
```  

Calculates the <a href="https://en.wikipedia.org/wiki/Cross_product">cross
product</a> of this vector and [v](en\math\Vector2.html). Note that a 'cross-
product' in 2D is not well-defined. This function computes a geometric cross-
product often used in 2D graphics

### equals

  
  
```ts  
function equals( v: Vector2 ): Boolean;  
```  

Returns `true` if the components of this vector and [v](en\math\Vector2.html)
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
  
Sets this vector's [.x](#x) value to be `array[ offset ]` and [.y](#y) value
to be `array[ offset + 1 ]`.

### fromBufferAttribute

  
  
```ts  
function fromBufferAttribute( attribute: BufferAttribute, index: Integer ):
this;  
```  

[attribute](en\core\BufferAttribute.html) - the source attribute.  
[index](#) - index in the attribute.  
  
Sets this vector's [.x](#x) and [.y](#y) values from the
[.ufferAttribute](#ufferAttribute).

### getComponent

  
  
```ts  
function getComponent( index: Integer ): Float;  
```  

[index](#) - `0` or `1`.  
  
If index equals `0` returns the [.x](#x) value.  
If index equals `1` returns the [.y](#y) value.

### length

  
  
```ts  
function length( ): Float;  
```  

Computes the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean length</a>
(straight-line length) from (0, 0) to (x, y).

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
(straight-line length) from (0, 0) to (x, y). If you are comparing the lengths
of vectors, you should compare the length squared instead as it is slightly
more efficient to calculate.

### lerp

  
  
```ts  
function lerp( v: Vector2, alpha: Float ): this;  
```  

[v](en\math\Vector2.html) - [Vector2](en\math\Vector2.html) to interpolate
towards.  
[alpha](#) - interpolation factor, typically in the closed interval `[0, 1]`.  
  
Linearly interpolates between this vector and [v](en\math\Vector2.html), where
alpha is the percent distance along the line - alpha = 0 will be this vector,
and alpha = 1 will be [v](en\math\Vector2.html).

### lerpVectors

  
  
```ts  
function lerpVectors( v1: Vector2, v2: Vector2, alpha: Float ): this;  
```  

[v1](en\math\Vector2.html) - the starting [Vector2](en\math\Vector2.html).  
[v2](en\math\Vector2.html) - [Vector2](en\math\Vector2.html) to interpolate
towards.  
[alpha](#) - interpolation factor, typically in the closed interval `[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between
[v1](en\math\Vector2.html) and [v2](en\math\Vector2.html) where alpha is the
percent distance along the line connecting the two vectors - alpha = 0 will be
[v1](en\math\Vector2.html), and alpha = 1 will be [v2](en\math\Vector2.html).

### negate

  
  
```ts  
function negate( ): this;  
```  

Inverts this vector - i.e. sets x = -x and y = -y.

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
function max( v: Vector2 ): this;  
```  

If this vector's x or y value is less than [v](en\math\Vector2.html)'s x or y
value, replace that value with the corresponding max value.

### min

  
  
```ts  
function min( v: Vector2 ): this;  
```  

If this vector's x or y value is greater than [v](en\math\Vector2.html)'s x or
y value, replace that value with the corresponding min value.

### multiply

  
  
```ts  
function multiply( v: Vector2 ): this;  
```  

Multiplies this vector by [v](en\math\Vector2.html).

### multiplyScalar

  
  
```ts  
function multiplyScalar( s: Float ): this;  
```  

Multiplies this vector by scalar [s](#).

### rotateAround

  
  
```ts  
function rotateAround( center: Vector2, angle: Float ): this;  
```  

[center](en\math\Vector2.html) - the point around which to rotate.  
[angle](#) - the angle to rotate, in radians.  
  
Rotates this vector around [center](en\math\Vector2.html) by [angle](#)
radians.

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
function set( x: Float, y: Float ): this;  
```  

Sets the [.x](#x) and [.y](#y) components of this vector.

### setComponent

  
  
```ts  
function setComponent( index: Integer, value: Float ): this;  
```  

[index](#) - `0` or `1`.  
[value](#) - [Float](#)  
  
If index equals `0` set [.x](#x) to [.loat](#loat).  
If index equals `1` set [.y](#y) to [.loat](#loat)

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

Sets the [.x](#x) and [.y](#y) values of this vector both equal to
[.loat](#loat).

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

### sub

  
  
```ts  
function sub( v: Vector2 ): this;  
```  

Subtracts [v](en\math\Vector2.html) from this vector.

### subScalar

  
  
```ts  
function subScalar( s: Float ): this;  
```  

Subtracts [.loat](#loat) from this vector's [.x](#x) and [.y](#y) components.

### subVectors

  
  
```ts  
function subVectors( a: Vector2, b: Vector2 ): this;  
```  

Sets this vector to [a](en\math\Vector2.html) - [b](en\math\Vector2.html).

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - (optional) array to store this vector to. If this is not
provided, a new array will be created.  
[offset](#) - (optional) optional offset into the array.  
  
Returns an array [x, y], or copies x and y into the provided [array](#).

### random

  
  
```ts  
function random( ): this;  
```  

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Vector2.js">src/math/Vector2.js</a>

