# Vector3

Class representing a 3D [link:https://en.wikipedia.org/wiki/Vector_space
vector]. A 3D vector is an ordered triplet of numbers (labeled x, y, and z),
which can be used to represent a number of things, such as:

  * A point in 3D space.
  * A direction and length in 3D space. In three.js the length will always be the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance] (straight-line distance) from `(0, 0, 0)` to `(x, y, z)` and the direction is also measured from `(0, 0, 0)` towards `(x, y, z)`.
  * Any arbitrary ordered triplet of numbers.

There are other things a 3D vector can be used to represent, such as momentum
vectors and so on, however these are the most common uses in three.js.

Iterating through a Vector3 instance will yield its components `(x, y, z)` in
the corresponding order.

## Code Example

  
```ts  
const a = new THREE.Vector3( 0, 1, 0 ); //no arguments; will be initialised to
(0, 0, 0) const b = new THREE.Vector3( ); const d = a.distanceTo( b );  
```  

## Constructor

###  function Vector3( x: Float, y: Float, z: Float ): void;

[page:Float x] - the x value of this vector. Default is `0`.  
[page:Float y] - the y value of this vector. Default is `0`.  
[page:Float z] - the z value of this vector. Default is `0`.  
  
Creates a new Vector3.

## Properties

###  Boolean isVector3;

Read-only flag to check if a given object is of type Vector3.

###  Float x;

###  Float y;

###  Float z;

## Methods

###  function add( v: Vector3 ): this;

Adds [page:Vector3 v] to this vector.

###  function addScalar( s: Float ): this;

Adds the scalar value s to this vector's [page:.x x], [page:.y y] and [page:.z
z] values.

###  function addScaledVector( v: Vector3, s: Float ): this;

Adds the multiple of [page:Vector3 v] and [page:Float s] to this vector.

###  function addVectors( a: Vector3, b: Vector3 ): this;

Sets this vector to [page:Vector3 a] + [page:Vector3 b].

###  function applyAxisAngle( axis: Vector3, angle: Float ): this;

[page:Vector3 axis] - A normalized [page:Vector3].  
[page:Float angle] - An angle in radians.  
  
Applies a rotation specified by an axis and an angle to this vector.

###  function applyEuler( euler: Euler ): this;

Applies euler transform to this vector by converting the [page:Euler] object
to a [page:Quaternion] and applying.

###  function applyMatrix3( m: Matrix3 ): this;

Multiplies this vector by [page:Matrix3 m]

###  function applyMatrix4( m: Matrix4 ): this;

Multiplies this vector (with an implicit 1 in the 4th dimension) by m, and
divides by perspective.

###  function applyNormalMatrix( m: Matrix3 ): this;

Multiplies this vector by normal matrix [page:Matrix3 m] and normalizes the
result.

###  function applyQuaternion( quaternion: Quaternion ): this;

Applies a [page:Quaternion] transform to this vector.

###  function angleTo( v: Vector3 ): Float;

Returns the angle between this vector and vector [page:Vector3 v] in radians.

###  function ceil( ): this;

The [page:.x x], [page:.y y] and [page:.z z] components of this vector are
rounded up to the nearest integer value.

###  function clamp( min: Vector3, max: Vector3 ): this;

[page:Vector3 min] - the minimum [page:.x x], [page:.y y] and [page:.z z]
values.  
[page:Vector3 max] - the maximum [page:.x x], [page:.y y] and [page:.z z]
values in the desired range  
  
If this vector's x, y or z value is greater than the max vector's x, y or z
value, it is replaced by the corresponding value.  
  
If this vector's x, y or z value is less than the min vector's x, y or z
value, it is replaced by the corresponding value.

###  function clampLength( min: Float, max: Float ): this;

[page:Float min] - the minimum value the length will be clamped to  
[page:Float max] - the maximum value the length will be clamped to  
  
If this vector's length is greater than the max value, the vector will be
scaled down so its length is the max value.  
  
If this vector's length is less than the min value, the vector will be scaled
up so its length is the min value.

###  function clampScalar( min: Float, max: Float ): this;

[page:Float min] - the minimum value the components will be clamped to  
[page:Float max] - the maximum value the components will be clamped to  
  
If this vector's x, y or z values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x, y or z values are less than the min value, they are
replaced by the min value.

###  function clone( ): Vector3;

Returns a new vector3 with the same [page:.x x], [page:.y y] and [page:.z z]
values as this one.

###  function copy( v: Vector3 ): this;

Copies the values of the passed vector3's [page:.x x], [page:.y y] and
[page:.z z] properties to this vector3.

###  function cross( v: Vector3 ): this;

Sets this vector to [link:https://en.wikipedia.org/wiki/Cross_product cross
product] of itself and [page:Vector3 v].

###  function crossVectors( a: Vector3, b: Vector3 ): this;

Sets this vector to [link:https://en.wikipedia.org/wiki/Cross_product cross
product] of [page:Vector3 a] and [page:Vector3 b].

###  function distanceTo( v: Vector3 ): Float;

Computes the distance from this vector to [page:Vector3 v].

###  function manhattanDistanceTo( v: Vector3 ): Float;

Computes the [link:https://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
distance] from this vector to [page:Vector3 v].

###  function distanceToSquared( v: Vector3 ): Float;

Computes the squared distance from this vector to [page:Vector3 v]. If you are
just comparing the distance with another distance, you should compare the
distance squared instead as it is slightly more efficient to calculate.

###  function divide( v: Vector3 ): this;

Divides this vector by [page:Vector3 v].

###  function divideScalar( s: Float ): this;

Divides this vector by scalar [page:Float s].

###  function dot( v: Vector3 ): Float;

Calculate the [link:https://en.wikipedia.org/wiki/Dot_product dot product] of
this vector and [page:Vector3 v].

###  function equals( v: Vector3 ): Boolean;

Returns `true` if the components of this vector and [page:Vector3 v] are
strictly equal; `false` otherwise.

###  function floor( ): this;

The components of this vector are rounded down to the nearest integer value.

###  function fromArray( array: Array, offset: Integer ): this;

[page:Array array] - the source array.  
[page:Integer offset] - ( optional) offset into the array. Default is 0.  
  
Sets this vector's [page:.x x] value to be `array[ offset + 0 ]`, [page:.y y]
value to be `array[ offset + 1 ]` and [page:.z z] value to be `array[ offset +
2 ]`.

###  function fromBufferAttribute( attribute: BufferAttribute, index: Integer
): this;

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets this vector's [page:.x x], [page:.y y] and [page:.z z] values from the
[page:BufferAttribute attribute].

###  function getComponent( index: Integer ): Float;

[page:Integer index] - `0`, `1` or `2`.  
  
If index equals `0` returns the [page:.x x] value.  
If index equals `1` returns the [page:.y y] value.  
If index equals `2` returns the [page:.z z] value.

###  function length( ): Float;

Computes the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
length] (straight-line length) from (0, 0, 0) to (x, y, z).

###  function manhattanLength( ): Float;

Computes the [link:http://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
length] of this vector.

###  function lengthSq( ): Float;

Computes the square of the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean length]
(straight-line length) from (0, 0, 0) to (x, y, z). If you are comparing the
lengths of vectors, you should compare the length squared instead as it is
slightly more efficient to calculate.

###  function lerp( v: Vector3, alpha: Float ): this;

[page:Vector3 v] - [page:Vector3] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Linearly interpolate between this vector and [page:Vector3 v], where alpha is
the percent distance along the line - alpha = 0 will be this vector, and alpha
= 1 will be [page:Vector3 v].

###  function lerpVectors( v1: Vector3, v2: Vector3, alpha: Float ): this;

[page:Vector3 v1] - the starting [page:Vector3].  
[page:Vector3 v2] - [page:Vector3] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between [page:Vector3
v1] and [page:Vector3 v2] where alpha is the percent distance along the line
connecting the two vectors - alpha = 0 will be [page:Vector3 v1], and alpha =
1 will be [page:Vector3 v2].

###  function max( v: Vector3 ): this;

If this vector's x, y or z value is less than [page:Vector3 v]'s x, y or z
value, replace that value with the corresponding max value.

###  function min( v: Vector3 ): this;

If this vector's x, y or z value is greater than [page:Vector3 v]'s x, y or z
value, replace that value with the corresponding min value.

###  function multiply( v: Vector3 ): this;

Multiplies this vector by [page:Vector3 v].

###  function multiplyScalar( s: Float ): this;

Multiplies this vector by scalar [page:Float s].

###  function multiplyVectors( a: Vector3, b: Vector3 ): this;

Sets this vector equal to [page:Vector3 a] * [page:Vector3 b], component-wise.

###  function negate( ): this;

Inverts this vector - i.e. sets x = -x, y = -y and z = -z.

###  function normalize( ): this;

Convert this vector to a [link:https://en.wikipedia.org/wiki/Unit_vector unit
vector] - that is, sets it equal to a vector with the same direction as this
one, but [page:.length length] 1.

###  function project( camera: Camera ): this;

[page:Camera camera] — camera to use in the projection.  
  
Projects this vector from world space into the camera's normalized device
coordinate (NDC) space.

###  function projectOnPlane( planeNormal: Vector3 ): this;

[page:Vector3 planeNormal] - A vector representing a plane normal.  
  
[link:https://en.wikipedia.org/wiki/Vector_projection Projects] this vector
onto a plane by subtracting this vector projected onto the plane's normal from
this vector.

###  function projectOnVector( v: Vector3 ): this;

[link:https://en.wikipedia.org/wiki/Vector_projection Projects] this vector
onto [page:Vector3 v].

###  function reflect( normal: Vector3 ): this;

[page:Vector3 normal] - the normal to the reflecting plane  
  
Reflect this vector off of plane orthogonal to [page:Vector3 normal]. Normal
is assumed to have unit length.

###  function round( ): this;

The components of this vector are rounded to the nearest integer value.

###  function roundToZero( ): this;

The components of this vector are rounded towards zero (up if negative, down
if positive) to an integer value.

###  function set( x: Float, y: Float, z: Float ): this;

Sets the [page:.x x], [page:.y y] and [page:.z z] components of this vector.

###  function setComponent( index: Integer, value: Float ): this;

[page:Integer index] - `0`, `1` or `2`.  
[page:Float value] - [page:Float]  
  
If index equals `0` set [page:.x x] to [page:Float value].  
If index equals `1` set [page:.y y] to [page:Float value].  
If index equals `2` set [page:.z z] to [page:Float value]

###  function setFromColor( color: Color ): this;

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
the r, g, and b components of the specified [page:Color color].

###  function setFromCylindrical( c: Cylindrical ): this;

Sets this vector from the cylindrical coordinates [page:Cylindrical c].

###  function setFromCylindricalCoords( radius: Float, theta: Float, y: Float
): this;

Sets this vector from the cylindrical coordinates [page:Cylindrical radius],
[page:Cylindrical theta] and [page:Cylindrical y].

###  function setFromEuler( euler: Euler ): this;

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
the x, y, and z components of the specified [page:Euler Euler Angle].

###  function setFromMatrixColumn( matrix: Matrix4, index: Integer ): this;

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
[page:Integer index] column of [page:Matrix4 matrix].

###  function setFromMatrix3Column( matrix: Matrix3, index: Integer ): this;

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
[page:Integer index] column of [page:Matrix3 matrix].

###  function setFromMatrixPosition( m: Matrix4 ): this;

Sets this vector to the position elements of the
[link:https://en.wikipedia.org/wiki/Transformation_matrix transformation
matrix] [page:Matrix4 m].

###  function setFromMatrixScale( m: Matrix4 ): this;

Sets this vector to the scale elements of the
[link:https://en.wikipedia.org/wiki/Transformation_matrix transformation
matrix] [page:Matrix4 m].

###  function setFromSpherical( s: Spherical ): this;

Sets this vector from the spherical coordinates [page:Spherical s].

###  function setFromSphericalCoords( radius: Float, phi: Float, theta: Float
): this;

Sets this vector from the spherical coordinates [page:Spherical radius],
[page:Spherical phi] and [page:Spherical theta].

###  function setLength( l: Float ): this;

Set this vector to a vector with the same direction as this one, but
[page:.length length] [page:Float l].

###  function setScalar( scalar: Float ): this;

Set the [page:.x x], [page:.y y] and [page:.z z] values of this vector both
equal to [page:Float scalar].

###  function setX( x: Float ): this;

Replace this vector's [page:.x x] value with [page:Float x].

###  function setY( y: Float ): this;

Replace this vector's [page:.y y] value with [page:Float y].

###  function setZ( z: Float ): this;

Replace this vector's [page:.z z] value with [page:Float z].

###  function sub( v: Vector3 ): this;

Subtracts [page:Vector3 v] from this vector.

###  function subScalar( s: Float ): this;

Subtracts [page:Float s] from this vector's [page:.x x], [page:.y y] and
[page:.z z] components.

###  function subVectors( a: Vector3, b: Vector3 ): this;

Sets this vector to [page:Vector3 a] - [page:Vector3 b].

###  function toArray( array: Array, offset: Integer ): Array;

[page:Array array] - (optional) array to store this vector to. If this is not
provided a new array will be created.  
[page:Integer offset] - (optional) optional offset into the array.  
  
Returns an array [x, y, z], or copies x, y and z into the provided [page:Array
array].

###  function transformDirection( m: Matrix4 ): this;

Transforms the direction of this vector by a matrix (the upper left 3 x 3
subset of a [page:Matrix4 m]) and then [page:.normalize normalizes] the
result.

###  function unproject( camera: Camera ): this;

[page:Camera camera] — camera to use in the projection.  
  
Projects this vector from the camera's normalized device coordinate (NDC)
space into world space.

###  function random( ): this;

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

###  function randomDirection( ): this;

Sets this vector to a uniformly random point on a unit sphere.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

