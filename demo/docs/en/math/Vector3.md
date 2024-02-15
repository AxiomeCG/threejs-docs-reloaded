# Vector3

Class representing a 3D <a
href="https://en.wikipedia.org/wiki/Vector_space">vector</a>. A 3D vector is
an ordered triplet of numbers (labeled x, y, and z), which can be used to
represent a number of things, such as:

  * A point in 3D space.
  * A direction and length in 3D space. In three.js the length will always be the <a href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a> (straight-line distance) from `(0, 0, 0)` to `(x, y, z)` and the direction is also measured from `(0, 0, 0)` towards `(x, y, z)`.
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

### Vector3

  
  
```ts  
function Vector3( x: Float, y: Float, z: Float ): void;  
```  

[x](#) - the x value of this vector. Default is `0`.  
[y](#) - the y value of this vector. Default is `0`.  
[z](#) - the z value of this vector. Default is `0`.  
  
Creates a new Vector3.

## Properties

### isVector3

  
  
```ts  
isVector3: Boolean;  
```  

Read-only flag to check if a given object is of type Vector3.

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

## Methods

### add

  
  
```ts  
function add( v: Vector3 ): this;  
```  

Adds [v](en\math\Vector3.html) to this vector.

### addScalar

  
  
```ts  
function addScalar( s: Float ): this;  
```  

Adds the scalar value s to this vector's [.x](#x), [.y](#y) and [.z](#z)
values.

### addScaledVector

  
  
```ts  
function addScaledVector( v: Vector3, s: Float ): this;  
```  

Adds the multiple of [v](en\math\Vector3.html) and [s](#) to this vector.

### addVectors

  
  
```ts  
function addVectors( a: Vector3, b: Vector3 ): this;  
```  

Sets this vector to [a](en\math\Vector3.html) + [b](en\math\Vector3.html).

### applyAxisAngle

  
  
```ts  
function applyAxisAngle( axis: Vector3, angle: Float ): this;  
```  

[axis](en\math\Vector3.html) - A normalized [Vector3](en\math\Vector3.html).  
[angle](#) - An angle in radians.  
  
Applies a rotation specified by an axis and an angle to this vector.

### applyEuler

  
  
```ts  
function applyEuler( euler: Euler ): this;  
```  

Applies euler transform to this vector by converting the
[Euler](en\math\Euler.html) object to a [Quaternion](en\math\Quaternion.html)
and applying.

### applyMatrix3

  
  
```ts  
function applyMatrix3( m: Matrix3 ): this;  
```  

Multiplies this vector by [m](en\math\Matrix3.html)

### applyMatrix4

  
  
```ts  
function applyMatrix4( m: Matrix4 ): this;  
```  

Multiplies this vector (with an implicit 1 in the 4th dimension) by m, and
divides by perspective.

### applyNormalMatrix

  
  
```ts  
function applyNormalMatrix( m: Matrix3 ): this;  
```  

Multiplies this vector by normal matrix [m](en\math\Matrix3.html) and
normalizes the result.

### applyQuaternion

  
  
```ts  
function applyQuaternion( quaternion: Quaternion ): this;  
```  

Applies a [Quaternion](en\math\Quaternion.html) transform to this vector.

### angleTo

  
  
```ts  
function angleTo( v: Vector3 ): Float;  
```  

Returns the angle between this vector and vector [v](en\math\Vector3.html) in
radians.

### ceil

  
  
```ts  
function ceil( ): this;  
```  

The [.x](#x), [.y](#y) and [.z](#z) components of this vector are rounded up
to the nearest integer value.

### clamp

  
  
```ts  
function clamp( min: Vector3, max: Vector3 ): this;  
```  

[.ector3](#ector3) - the minimum [.x](#x), [.y](#y) and [.z](#z) values.  
[.ector3](#ector3) - the maximum [.x](#x), [.y](#y) and [.z](#z) values in the
desired range  
  
If this vector's x, y or z value is greater than the max vector's x, y or z
value, it is replaced by the corresponding value.  
  
If this vector's x, y or z value is less than the min vector's x, y or z
value, it is replaced by the corresponding value.

### clampLength

  
  
```ts  
function clampLength( min: Float, max: Float ): this;  
```  

[min](#) - the minimum value the length will be clamped to  
[max](#) - the maximum value the length will be clamped to  
  
If this vector's length is greater than the max value, the vector will be
scaled down so its length is the max value.  
  
If this vector's length is less than the min value, the vector will be scaled
up so its length is the min value.

### clampScalar

  
  
```ts  
function clampScalar( min: Float, max: Float ): this;  
```  

[min](#) - the minimum value the components will be clamped to  
[max](#) - the maximum value the components will be clamped to  
  
If this vector's x, y or z values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x, y or z values are less than the min value, they are
replaced by the min value.

### clone

  
  
```ts  
function clone( ): Vector3;  
```  

Returns a new vector3 with the same [.x](#x), [.y](#y) and [.z](#z) values as
this one.

### copy

  
  
```ts  
function copy( v: Vector3 ): this;  
```  

Copies the values of the passed vector3's [.x](#x), [.y](#y) and [.z](#z)
properties to this vector3.

### cross

  
  
```ts  
function cross( v: Vector3 ): this;  
```  

Sets this vector to <a
href="https://en.wikipedia.org/wiki/Cross_product">cross product</a> of itself
and [v](en\math\Vector3.html).

### crossVectors

  
  
```ts  
function crossVectors( a: Vector3, b: Vector3 ): this;  
```  

Sets this vector to <a
href="https://en.wikipedia.org/wiki/Cross_product">cross product</a> of
[a](en\math\Vector3.html) and [b](en\math\Vector3.html).

### distanceTo

  
  
```ts  
function distanceTo( v: Vector3 ): Float;  
```  

Computes the distance from this vector to [v](en\math\Vector3.html).

### manhattanDistanceTo

  
  
```ts  
function manhattanDistanceTo( v: Vector3 ): Float;  
```  

Computes the <a
href="https://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan distance</a>
from this vector to [v](en\math\Vector3.html).

### distanceToSquared

  
  
```ts  
function distanceToSquared( v: Vector3 ): Float;  
```  

Computes the squared distance from this vector to [v](en\math\Vector3.html).
If you are just comparing the distance with another distance, you should
compare the distance squared instead as it is slightly more efficient to
calculate.

### divide

  
  
```ts  
function divide( v: Vector3 ): this;  
```  

Divides this vector by [v](en\math\Vector3.html).

### divideScalar

  
  
```ts  
function divideScalar( s: Float ): this;  
```  

Divides this vector by scalar [s](#).

### dot

  
  
```ts  
function dot( v: Vector3 ): Float;  
```  

Calculate the <a href="https://en.wikipedia.org/wiki/Dot_product">dot
product</a> of this vector and [v](en\math\Vector3.html).

### equals

  
  
```ts  
function equals( v: Vector3 ): Boolean;  
```  

Returns `true` if the components of this vector and [v](en\math\Vector3.html)
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
[offset](#) - ( optional) offset into the array. Default is 0.  
  
Sets this vector's [.x](#x) value to be `array[ offset + 0 ]`, [.y](#y) value
to be `array[ offset + 1 ]` and [.z](#z) value to be `array[ offset + 2 ]`.

### fromBufferAttribute

  
  
```ts  
function fromBufferAttribute( attribute: BufferAttribute, index: Integer ):
this;  
```  

[attribute](en\core\BufferAttribute.html) - the source attribute.  
[index](#) - index in the attribute.  
  
Sets this vector's [.x](#x), [.y](#y) and [.z](#z) values from the
[.ufferAttribute](#ufferAttribute).

### getComponent

  
  
```ts  
function getComponent( index: Integer ): Float;  
```  

[index](#) - `0`, `1` or `2`.  
  
If index equals `0` returns the [.x](#x) value.  
If index equals `1` returns the [.y](#y) value.  
If index equals `2` returns the [.z](#z) value.

### length

  
  
```ts  
function length( ): Float;  
```  

Computes the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean length</a>
(straight-line length) from (0, 0, 0) to (x, y, z).

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
(straight-line length) from (0, 0, 0) to (x, y, z). If you are comparing the
lengths of vectors, you should compare the length squared instead as it is
slightly more efficient to calculate.

### lerp

  
  
```ts  
function lerp( v: Vector3, alpha: Float ): this;  
```  

[v](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to interpolate
towards.  
[alpha](#) - interpolation factor, typically in the closed interval `[0, 1]`.  
  
Linearly interpolate between this vector and [v](en\math\Vector3.html), where
alpha is the percent distance along the line - alpha = 0 will be this vector,
and alpha = 1 will be [v](en\math\Vector3.html).

### lerpVectors

  
  
```ts  
function lerpVectors( v1: Vector3, v2: Vector3, alpha: Float ): this;  
```  

[v1](en\math\Vector3.html) - the starting [Vector3](en\math\Vector3.html).  
[v2](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to interpolate
towards.  
[alpha](#) - interpolation factor, typically in the closed interval `[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between
[v1](en\math\Vector3.html) and [v2](en\math\Vector3.html) where alpha is the
percent distance along the line connecting the two vectors - alpha = 0 will be
[v1](en\math\Vector3.html), and alpha = 1 will be [v2](en\math\Vector3.html).

### max

  
  
```ts  
function max( v: Vector3 ): this;  
```  

If this vector's x, y or z value is less than [v](en\math\Vector3.html)'s x, y
or z value, replace that value with the corresponding max value.

### min

  
  
```ts  
function min( v: Vector3 ): this;  
```  

If this vector's x, y or z value is greater than [v](en\math\Vector3.html)'s
x, y or z value, replace that value with the corresponding min value.

### multiply

  
  
```ts  
function multiply( v: Vector3 ): this;  
```  

Multiplies this vector by [v](en\math\Vector3.html).

### multiplyScalar

  
  
```ts  
function multiplyScalar( s: Float ): this;  
```  

Multiplies this vector by scalar [s](#).

### multiplyVectors

  
  
```ts  
function multiplyVectors( a: Vector3, b: Vector3 ): this;  
```  

Sets this vector equal to [a](en\math\Vector3.html) *
[b](en\math\Vector3.html), component-wise.

### negate

  
  
```ts  
function negate( ): this;  
```  

Inverts this vector - i.e. sets x = -x, y = -y and z = -z.

### normalize

  
  
```ts  
function normalize( ): this;  
```  

Convert this vector to a <a
href="https://en.wikipedia.org/wiki/Unit_vector">unit vector</a> \- that is,
sets it equal to a vector with the same direction as this one, but
[.length](#length) 1.

### project

  
  
```ts  
function project( camera: Camera ): this;  
```  

[camera](en\cameras\Camera.html) — camera to use in the projection.  
  
Projects this vector from world space into the camera's normalized device
coordinate (NDC) space.

### projectOnPlane

  
  
```ts  
function projectOnPlane( planeNormal: Vector3 ): this;  
```  

[planeNormal](en\math\Vector3.html) - A vector representing a plane normal.  
  
<a href="https://en.wikipedia.org/wiki/Vector_projection">Projects</a> this
vector onto a plane by subtracting this vector projected onto the plane's
normal from this vector.

### projectOnVector

  
  
```ts  
function projectOnVector( v: Vector3 ): this;  
```  

<a href="https://en.wikipedia.org/wiki/Vector_projection">Projects</a> this
vector onto [v](en\math\Vector3.html).

### reflect

  
  
```ts  
function reflect( normal: Vector3 ): this;  
```  

[normal](en\math\Vector3.html) - the normal to the reflecting plane  
  
Reflect this vector off of plane orthogonal to [normal](en\math\Vector3.html).
Normal is assumed to have unit length.

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
function set( x: Float, y: Float, z: Float ): this;  
```  

Sets the [.x](#x), [.y](#y) and [.z](#z) components of this vector.

### setComponent

  
  
```ts  
function setComponent( index: Integer, value: Float ): this;  
```  

[index](#) - `0`, `1` or `2`.  
[value](#) - [Float](#)  
  
If index equals `0` set [.x](#x) to [.loat](#loat).  
If index equals `1` set [.y](#y) to [.loat](#loat).  
If index equals `2` set [.z](#z) to [.loat](#loat)

### setFromColor

  
  
```ts  
function setFromColor( color: Color ): this;  
```  

Sets this vector's [.x](#x), [.y](#y) and [.z](#z) components from the r, g,
and b components of the specified [.olor](#olor).

### setFromCylindrical

  
  
```ts  
function setFromCylindrical( c: Cylindrical ): this;  
```  

Sets this vector from the cylindrical coordinates
[c](en\math\Cylindrical.html).

### setFromCylindricalCoords

  
  
```ts  
function setFromCylindricalCoords( radius: Float, theta: Float, y: Float ):
this;  
```  

Sets this vector from the cylindrical coordinates
[radius](en\math\Cylindrical.html), [theta](en\math\Cylindrical.html) and
[y](en\math\Cylindrical.html).

### setFromEuler

  
  
```ts  
function setFromEuler( euler: Euler ): this;  
```  

Sets this vector's [.x](#x), [.y](#y) and [.z](#z) components from the x, y,
and z components of the specified [.uler](#uler).

### setFromMatrixColumn

  
  
```ts  
function setFromMatrixColumn( matrix: Matrix4, index: Integer ): this;  
```  

Sets this vector's [.x](#x), [.y](#y) and [.z](#z) components from
[.nteger](#nteger) column of [.atrix4](#atrix4).

### setFromMatrix3Column

  
  
```ts  
function setFromMatrix3Column( matrix: Matrix3, index: Integer ): this;  
```  

Sets this vector's [.x](#x), [.y](#y) and [.z](#z) components from
[.nteger](#nteger) column of [.atrix3](#atrix3).

### setFromMatrixPosition

  
  
```ts  
function setFromMatrixPosition( m: Matrix4 ): this;  
```  

Sets this vector to the position elements of the <a
href="https://en.wikipedia.org/wiki/Transformation_matrix">transformation
matrix</a> [m](en\math\Matrix4.html).

### setFromMatrixScale

  
  
```ts  
function setFromMatrixScale( m: Matrix4 ): this;  
```  

Sets this vector to the scale elements of the <a
href="https://en.wikipedia.org/wiki/Transformation_matrix">transformation
matrix</a> [m](en\math\Matrix4.html).

### setFromSpherical

  
  
```ts  
function setFromSpherical( s: Spherical ): this;  
```  

Sets this vector from the spherical coordinates [s](en\math\Spherical.html).

### setFromSphericalCoords

  
  
```ts  
function setFromSphericalCoords( radius: Float, phi: Float, theta: Float ):
this;  
```  

Sets this vector from the spherical coordinates
[radius](en\math\Spherical.html), [phi](en\math\Spherical.html) and
[theta](en\math\Spherical.html).

### setLength

  
  
```ts  
function setLength( l: Float ): this;  
```  

Set this vector to a vector with the same direction as this one, but
[.length](#length) [.loat](#loat).

### setScalar

  
  
```ts  
function setScalar( scalar: Float ): this;  
```  

Set the [.x](#x), [.y](#y) and [.z](#z) values of this vector both equal to
[.loat](#loat).

### setX

  
  
```ts  
function setX( x: Float ): this;  
```  

Replace this vector's [.x](#x) value with [.loat](#loat).

### setY

  
  
```ts  
function setY( y: Float ): this;  
```  

Replace this vector's [.y](#y) value with [.loat](#loat).

### setZ

  
  
```ts  
function setZ( z: Float ): this;  
```  

Replace this vector's [.z](#z) value with [.loat](#loat).

### sub

  
  
```ts  
function sub( v: Vector3 ): this;  
```  

Subtracts [v](en\math\Vector3.html) from this vector.

### subScalar

  
  
```ts  
function subScalar( s: Float ): this;  
```  

Subtracts [.loat](#loat) from this vector's [.x](#x), [.y](#y) and [.z](#z)
components.

### subVectors

  
  
```ts  
function subVectors( a: Vector3, b: Vector3 ): this;  
```  

Sets this vector to [a](en\math\Vector3.html) - [b](en\math\Vector3.html).

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - (optional) array to store this vector to. If this is not provided
a new array will be created.  
[offset](#) - (optional) optional offset into the array.  
  
Returns an array [x, y, z], or copies x, y and z into the provided [array](#).

### transformDirection

  
  
```ts  
function transformDirection( m: Matrix4 ): this;  
```  

Transforms the direction of this vector by a matrix (the upper left 3 x 3
subset of a [.atrix4](#atrix4)) and then [.normalize](#normalize) the result.

### unproject

  
  
```ts  
function unproject( camera: Camera ): this;  
```  

[camera](en\cameras\Camera.html) — camera to use in the projection.  
  
Projects this vector from the camera's normalized device coordinate (NDC)
space into world space.

### random

  
  
```ts  
function random( ): this;  
```  

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

### randomDirection

  
  
```ts  
function randomDirection( ): this;  
```  

Sets this vector to a uniformly random point on a unit sphere.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Vector3.js">src/math/Vector3.js</a>

