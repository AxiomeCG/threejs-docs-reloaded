# [name]

Class representing a 2D [link:https://en.wikipedia.org/wiki/Vector_space
vector]. A 2D vector is an ordered pair of numbers (labeled x and y), which
can be used to represent a number of things, such as:

  * A point in 2D space (i.e. a position on a plane).
  * A direction and length across a plane. In three.js the length will always be the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance] (straight-line distance) from `(0, 0)` to `(x, y)` and the direction is also measured from `(0, 0)` towards `(x, y)`. 
  * Any arbitrary ordered pair of numbers.

There are other things a 2D vector can be used to represent, such as momentum
vectors, complex numbers and so on, however these are the most common uses in
three.js.

Iterating through a [name] instance will yield its components `(x, y)` in the
corresponding order.

## Code Example

  
```ts  
const a = new THREE.Vector2( 0, 1 );  
  
//no arguments; will be initialised to (0, 0)  
const b = new THREE.Vector2( );  
  
const d = a.distanceTo( b );  
```  

## Constructor

### [name]( [param:Float x], [param:Float y] )

[page:Float x] - the x value of this vector. Default is `0`.  
[page:Float y] - the y value of this vector. Default is `0`.  
  
Creates a new [name].

## Properties

### <br/> Float height; <br/>

Alias for [page:.y y].

### <br/> Boolean isVector2; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Float width; <br/>

Alias for [page:.x x].

### <br/> Float x; <br/>

### <br/> Float y; <br/>

## Methods

### <br/> function add( v: Vector2 ): add; <br/>

Adds [page:Vector2 v] to this vector.

### <br/> function addScalar( s: Float ): addScalar; <br/>

Adds the scalar value [page:Float s] to this vector's [page:.x x] and [page:.y
y] values.

### <br/> function addScaledVector( v: Vector2, s: Float ): addScaledVector;
<br/>

Adds the multiple of [page:Vector2 v] and [page:Float s] to this vector.

### <br/> function addVectors( a: Vector2, b: Vector2 ): addVectors; <br/>

Sets this vector to [page:Vector2 a] + [page:Vector2 b].

### [method:Float angle]()

Computes the angle in radians of this vector with respect to the positive
x-axis.

### [method:Float angleTo]( [param:Vector2 v] )

Returns the angle between this vector and vector [page:Vector2 v] in radians.

### <br/> function applyMatrix3( m: Matrix3 ): applyMatrix3; <br/>

Multiplies this vector (with an implicit 1 as the 3rd component) by m.

### <br/> function ceil( ): ceil; <br/>

The [page:.x x] and [page:.y y] components of this vector are rounded up to
the nearest integer value.

### <br/> function clamp( min: Vector2, max: Vector2 ): clamp; <br/>

[page:Vector2 min] - the minimum x and y values.  
[page:Vector2 max] - the maximum x and y values in the desired range  
  
If this vector's x or y value is greater than the max vector's x or y value,
it is replaced by the corresponding value.  
  
If this vector's x or y value is less than the min vector's x or y value, it
is replaced by the corresponding value.

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
  
If this vector's x or y values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x or y values are less than the min value, they are replaced
by the min value.

### [method:Vector2 clone]()

Returns a new Vector2 with the same [page:.x x] and [page:.y y] values as this
one.

### <br/> function copy( v: Vector2 ): copy; <br/>

Copies the values of the passed Vector2's [page:.x x] and [page:.y y]
properties to this Vector2.

### [method:Float distanceTo]( [param:Vector2 v] )

Computes the distance from this vector to [page:Vector2 v].

### [method:Float manhattanDistanceTo]( [param:Vector2 v] )

Computes the [link:https://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
distance] from this vector to [page:Vector2 v].

### [method:Float distanceToSquared]( [param:Vector2 v] )

Computes the squared distance from this vector to [page:Vector2 v]. If you are
just comparing the distance with another distance, you should compare the
distance squared instead as it is slightly more efficient to calculate.

### <br/> function divide( v: Vector2 ): divide; <br/>

Divides this vector by [page:Vector2 v].

### <br/> function divideScalar( s: Float ): divideScalar; <br/>

Divides this vector by scalar [page:Float s].

### [method:Float dot]( [param:Vector2 v] )

Calculates the [link:https://en.wikipedia.org/wiki/Dot_product dot product] of
this vector and [page:Vector2 v].

### [method:Float cross]( [param:Vector2 v] )

Calculates the [link:https://en.wikipedia.org/wiki/Cross_product cross
product] of this vector and [page:Vector2 v]. Note that a 'cross-product' in
2D is not well-defined. This function computes a geometric cross-product often
used in 2D graphics

### [method:Boolean equals]( [param:Vector2 v] )

Returns `true` if the components of this vector and [page:Vector2 v] are
strictly equal; `false` otherwise.

### <br/> function floor( ): floor; <br/>

The components of this vector are rounded down to the nearest integer value.

### <br/> function fromArray( array: Array, offset: Integer ): fromArray;
<br/>

[page:Array array] - the source array.  
[page:Integer offset] - (optional) offset into the array. Default is `0`.  
  
Sets this vector's [page:.x x] value to be `array[ offset ]` and [page:.y y]
value to be `array[ offset + 1 ]`.

### <br/> function fromBufferAttribute( attribute: BufferAttribute, index:
Integer ): fromBufferAttribute; <br/>

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets this vector's [page:.x x] and [page:.y y] values from the
[page:BufferAttribute attribute].

### [method:Float getComponent]( [param:Integer index] )

[page:Integer index] - `0` or `1`.  
  
If index equals `0` returns the [page:.x x] value.  
If index equals `1` returns the [page:.y y] value.

### [method:Float length]()

Computes the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
length] (straight-line length) from (0, 0) to (x, y).

### [method:Float manhattanLength]()

Computes the [link:http://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
length] of this vector.

### [method:Float lengthSq]()

Computes the square of the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean length]
(straight-line length) from (0, 0) to (x, y). If you are comparing the lengths
of vectors, you should compare the length squared instead as it is slightly
more efficient to calculate.

### <br/> function lerp( v: Vector2, alpha: Float ): lerp; <br/>

[page:Vector2 v] - [page:Vector2] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Linearly interpolates between this vector and [page:Vector2 v], where alpha is
the percent distance along the line - alpha = 0 will be this vector, and alpha
= 1 will be [page:Vector2 v].

### <br/> function lerpVectors( v1: Vector2, v2: Vector2, alpha: Float ):
lerpVectors; <br/>

[page:Vector2 v1] - the starting [page:Vector2].  
[page:Vector2 v2] - [page:Vector2] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between [page:Vector2
v1] and [page:Vector2 v2] where alpha is the percent distance along the line
connecting the two vectors - alpha = 0 will be [page:Vector2 v1], and alpha =
1 will be [page:Vector2 v2].

### <br/> function negate( ): negate; <br/>

Inverts this vector - i.e. sets x = -x and y = -y.

### <br/> function normalize( ): normalize; <br/>

Converts this vector to a [link:https://en.wikipedia.org/wiki/Unit_vector unit
vector] - that is, sets it equal to a vector with the same direction as this
one, but [page:.length length] 1.

### <br/> function max( v: Vector2 ): max; <br/>

If this vector's x or y value is less than [page:Vector2 v]'s x or y value,
replace that value with the corresponding max value.

### <br/> function min( v: Vector2 ): min; <br/>

If this vector's x or y value is greater than [page:Vector2 v]'s x or y value,
replace that value with the corresponding min value.

### <br/> function multiply( v: Vector2 ): multiply; <br/>

Multiplies this vector by [page:Vector2 v].

### <br/> function multiplyScalar( s: Float ): multiplyScalar; <br/>

Multiplies this vector by scalar [page:Float s].

### <br/> function rotateAround( center: Vector2, angle: Float ):
rotateAround; <br/>

[page:Vector2 center] - the point around which to rotate.  
[page:Float angle] - the angle to rotate, in radians.  
  
Rotates this vector around [page:Vector2 center] by [page:Float angle]
radians.

### <br/> function round( ): round; <br/>

The components of this vector are rounded to the nearest integer value.

### <br/> function roundToZero( ): roundToZero; <br/>

The components of this vector are rounded towards zero (up if negative, down
if positive) to an integer value.

### <br/> function set( x: Float, y: Float ): set; <br/>

Sets the [page:.x x] and [page:.y y] components of this vector.

### <br/> function setComponent( index: Integer, value: Float ): setComponent;
<br/>

[page:Integer index] - `0` or `1`.  
[page:Float value] - [page:Float]  
  
If index equals `0` set [page:.x x] to [page:Float value].  
If index equals `1` set [page:.y y] to [page:Float value]

### <br/> function setLength( l: Float ): setLength; <br/>

Sets this vector to a vector with the same direction as this one, but
[page:.length length] [page:Float l].

### <br/> function setScalar( scalar: Float ): setScalar; <br/>

Sets the [page:.x x] and [page:.y y] values of this vector both equal to
[page:Float scalar].

### <br/> function setX( x: Float ): setX; <br/>

Replaces this vector's [page:.x x] value with [page:Float x].

### <br/> function setY( y: Float ): setY; <br/>

Replaces this vector's [page:.y y] value with [page:Float y].

### <br/> function sub( v: Vector2 ): sub; <br/>

Subtracts [page:Vector2 v] from this vector.

### <br/> function subScalar( s: Float ): subScalar; <br/>

Subtracts [page:Float s] from this vector's [page:.x x] and [page:.y y]
components.

### <br/> function subVectors( a: Vector2, b: Vector2 ): subVectors; <br/>

Sets this vector to [page:Vector2 a] - [page:Vector2 b].

###  [method:Array toArray]( [param:Array array], [param:Integer offset] )

[page:Array array] - (optional) array to store this vector to. If this is not
provided, a new array will be created.  
[page:Integer offset] - (optional) optional offset into the array.  
  
Returns an array [x, y], or copies x and y into the provided [page:Array
array].

### <br/> function random( ): random; <br/>

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

