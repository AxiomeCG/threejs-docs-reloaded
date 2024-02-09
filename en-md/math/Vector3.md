# [name]

Class representing a 3D [link:https://en.wikipedia.org/wiki/Vector_space
vector]. A 3D vector is an ordered triplet of numbers (labeled x, y, and z),
which can be used to represent a number of things, such as:

  * A point in 3D space.
  * A direction and length in 3D space. In three.js the length will always be the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance] (straight-line distance) from `(0, 0, 0)` to `(x, y, z)` and the direction is also measured from `(0, 0, 0)` towards `(x, y, z)`. 
  * Any arbitrary ordered triplet of numbers.

There are other things a 3D vector can be used to represent, such as momentum
vectors and so on, however these are the most common uses in three.js.

Iterating through a [name] instance will yield its components `(x, y, z)` in
the corresponding order.

## Code Example

  
```ts  
const a = new THREE.Vector3( 0, 1, 0 );  
  
//no arguments; will be initialised to (0, 0, 0)  
const b = new THREE.Vector3( );  
  
const d = a.distanceTo( b );  
```  

## Constructor

### [name]( [param:Float x], [param:Float y], [param:Float z] )

[page:Float x] - the x value of this vector. Default is `0`.  
[page:Float y] - the y value of this vector. Default is `0`.  
[page:Float z] - the z value of this vector. Default is `0`.  
  
Creates a new [name].

## Properties

### <br/> Boolean isVector3; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Float x; <br/>

### <br/> Float y; <br/>

### <br/> Float z; <br/>

## Methods

### <br/> function add( v: Vector3 ): add; <br/>

Adds [page:Vector3 v] to this vector.

### <br/> function addScalar( s: Float ): addScalar; <br/>

Adds the scalar value s to this vector's [page:.x x], [page:.y y] and [page:.z
z] values.

### <br/> function addScaledVector( v: Vector3, s: Float ): addScaledVector;
<br/>

Adds the multiple of [page:Vector3 v] and [page:Float s] to this vector.

### <br/> function addVectors( a: Vector3, b: Vector3 ): addVectors; <br/>

Sets this vector to [page:Vector3 a] + [page:Vector3 b].

### <br/> function applyAxisAngle( axis: Vector3, angle: Float ):
applyAxisAngle; <br/>

[page:Vector3 axis] - A normalized [page:Vector3].  
[page:Float angle] - An angle in radians.  
  
Applies a rotation specified by an axis and an angle to this vector.

### <br/> function applyEuler( euler: Euler ): applyEuler; <br/>

Applies euler transform to this vector by converting the [page:Euler] object
to a [page:Quaternion] and applying.

### <br/> function applyMatrix3( m: Matrix3 ): applyMatrix3; <br/>

Multiplies this vector by [page:Matrix3 m]

### <br/> function applyMatrix4( m: Matrix4 ): applyMatrix4; <br/>

Multiplies this vector (with an implicit 1 in the 4th dimension) by m, and
divides by perspective.

### <br/> function applyNormalMatrix( m: Matrix3 ): applyNormalMatrix; <br/>

Multiplies this vector by normal matrix [page:Matrix3 m] and normalizes the
result.

### <br/> function applyQuaternion( quaternion: Quaternion ): applyQuaternion;
<br/>

Applies a [page:Quaternion] transform to this vector.

### [method:Float angleTo]( [param:Vector3 v] )

Returns the angle between this vector and vector [page:Vector3 v] in radians.

### <br/> function ceil( ): ceil; <br/>

The [page:.x x], [page:.y y] and [page:.z z] components of this vector are
rounded up to the nearest integer value.

### <br/> function clamp( min: Vector3, max: Vector3 ): clamp; <br/>

[page:Vector3 min] - the minimum [page:.x x], [page:.y y] and [page:.z z]
values.  
[page:Vector3 max] - the maximum [page:.x x], [page:.y y] and [page:.z z]
values in the desired range  
  
If this vector's x, y or z value is greater than the max vector's x, y or z
value, it is replaced by the corresponding value.  
  
If this vector's x, y or z value is less than the min vector's x, y or z
value, it is replaced by the corresponding value.

### <br/> function clampLength( min: Float, max: Float ): clampLength; <br/>

[page:Float min] - the minimum value the length will be clamped to  
[page:Float max] - the maximum value the length will be clamped to  
  
If this vector's length is greater than the max value, the vector will be
scaled down so its length is the max value.  
  
If this vector's length is less than the min value, the vector will be scaled
up so its length is the min value.

### <br/> function clampScalar( min: Float, max: Float ): clampScalar; <br/>

[page:Float min] - the minimum value the components will be clamped to  
[page:Float max] - the maximum value the components will be clamped to  
  
If this vector's x, y or z values are greater than the max value, they are
replaced by the max value.  
  
If this vector's x, y or z values are less than the min value, they are
replaced by the min value.

### [method:Vector3 clone]()

Returns a new vector3 with the same [page:.x x], [page:.y y] and [page:.z z]
values as this one.

### <br/> function copy( v: Vector3 ): copy; <br/>

Copies the values of the passed vector3's [page:.x x], [page:.y y] and
[page:.z z] properties to this vector3.

### <br/> function cross( v: Vector3 ): cross; <br/>

Sets this vector to [link:https://en.wikipedia.org/wiki/Cross_product cross
product] of itself and [page:Vector3 v].

### <br/> function crossVectors( a: Vector3, b: Vector3 ): crossVectors; <br/>

Sets this vector to [link:https://en.wikipedia.org/wiki/Cross_product cross
product] of [page:Vector3 a] and [page:Vector3 b].

### [method:Float distanceTo]( [param:Vector3 v] )

Computes the distance from this vector to [page:Vector3 v].

### [method:Float manhattanDistanceTo]( [param:Vector3 v] )

Computes the [link:https://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
distance] from this vector to [page:Vector3 v].

### [method:Float distanceToSquared]( [param:Vector3 v] )

Computes the squared distance from this vector to [page:Vector3 v]. If you are
just comparing the distance with another distance, you should compare the
distance squared instead as it is slightly more efficient to calculate.

### <br/> function divide( v: Vector3 ): divide; <br/>

Divides this vector by [page:Vector3 v].

### <br/> function divideScalar( s: Float ): divideScalar; <br/>

Divides this vector by scalar [page:Float s].

### [method:Float dot]( [param:Vector3 v] )

Calculate the [link:https://en.wikipedia.org/wiki/Dot_product dot product] of
this vector and [page:Vector3 v].

### [method:Boolean equals]( [param:Vector3 v] )

Returns `true` if the components of this vector and [page:Vector3 v] are
strictly equal; `false` otherwise.

### <br/> function floor( ): floor; <br/>

The components of this vector are rounded down to the nearest integer value.

### <br/> function fromArray( array: Array, offset: Integer ): fromArray;
<br/>

[page:Array array] - the source array.  
[page:Integer offset] - ( optional) offset into the array. Default is 0.  
  
Sets this vector's [page:.x x] value to be `array[ offset + 0 ]`, [page:.y y]
value to be `array[ offset + 1 ]` and [page:.z z] value to be `array[ offset +
2 ]`.

### <br/> function fromBufferAttribute( attribute: BufferAttribute, index:
Integer ): fromBufferAttribute; <br/>

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets this vector's [page:.x x], [page:.y y] and [page:.z z] values from the
[page:BufferAttribute attribute].

### [method:Float getComponent]( [param:Integer index] )

[page:Integer index] - `0`, `1` or `2`.  
  
If index equals `0` returns the [page:.x x] value.  
If index equals `1` returns the [page:.y y] value.  
If index equals `2` returns the [page:.z z] value.

### [method:Float length]()

Computes the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
length] (straight-line length) from (0, 0, 0) to (x, y, z).

### [method:Float manhattanLength]()

Computes the [link:http://en.wikipedia.org/wiki/Taxicab_geometry Manhattan
length] of this vector.

### [method:Float lengthSq]()

Computes the square of the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean length]
(straight-line length) from (0, 0, 0) to (x, y, z). If you are comparing the
lengths of vectors, you should compare the length squared instead as it is
slightly more efficient to calculate.

### <br/> function lerp( v: Vector3, alpha: Float ): lerp; <br/>

[page:Vector3 v] - [page:Vector3] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Linearly interpolate between this vector and [page:Vector3 v], where alpha is
the percent distance along the line - alpha = 0 will be this vector, and alpha
= 1 will be [page:Vector3 v].

### <br/> function lerpVectors( v1: Vector3, v2: Vector3, alpha: Float ):
lerpVectors; <br/>

[page:Vector3 v1] - the starting [page:Vector3].  
[page:Vector3 v2] - [page:Vector3] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Sets this vector to be the vector linearly interpolated between [page:Vector3
v1] and [page:Vector3 v2] where alpha is the percent distance along the line
connecting the two vectors - alpha = 0 will be [page:Vector3 v1], and alpha =
1 will be [page:Vector3 v2].

### <br/> function max( v: Vector3 ): max; <br/>

If this vector's x, y or z value is less than [page:Vector3 v]'s x, y or z
value, replace that value with the corresponding max value.

### <br/> function min( v: Vector3 ): min; <br/>

If this vector's x, y or z value is greater than [page:Vector3 v]'s x, y or z
value, replace that value with the corresponding min value.

### <br/> function multiply( v: Vector3 ): multiply; <br/>

Multiplies this vector by [page:Vector3 v].

### <br/> function multiplyScalar( s: Float ): multiplyScalar; <br/>

Multiplies this vector by scalar [page:Float s].

### <br/> function multiplyVectors( a: Vector3, b: Vector3 ): multiplyVectors;
<br/>

Sets this vector equal to [page:Vector3 a] * [page:Vector3 b], component-wise.

### <br/> function negate( ): negate; <br/>

Inverts this vector - i.e. sets x = -x, y = -y and z = -z.

### <br/> function normalize( ): normalize; <br/>

Convert this vector to a [link:https://en.wikipedia.org/wiki/Unit_vector unit
vector] \- that is, sets it equal to a vector with the same direction as this
one, but [page:.length length] 1.

### <br/> function project( camera: Camera ): project; <br/>

[page:Camera camera] — camera to use in the projection.  
  
Projects this vector from world space into the camera's normalized device
coordinate (NDC) space.

### <br/> function projectOnPlane( planeNormal: Vector3 ): projectOnPlane;
<br/>

[page:Vector3 planeNormal] - A vector representing a plane normal.  
  
[link:https://en.wikipedia.org/wiki/Vector_projection Projects] this vector
onto a plane by subtracting this vector projected onto the plane's normal from
this vector.

### <br/> function projectOnVector( v: Vector3 ): projectOnVector; <br/>

[link:https://en.wikipedia.org/wiki/Vector_projection Projects] this vector
onto [page:Vector3 v].

### <br/> function reflect( normal: Vector3 ): reflect; <br/>

[page:Vector3 normal] - the normal to the reflecting plane  
  
Reflect this vector off of plane orthogonal to [page:Vector3 normal]. Normal
is assumed to have unit length.

### <br/> function round( ): round; <br/>

The components of this vector are rounded to the nearest integer value.

### <br/> function roundToZero( ): roundToZero; <br/>

The components of this vector are rounded towards zero (up if negative, down
if positive) to an integer value.

### <br/> function set( x: Float, y: Float, z: Float ): set; <br/>

Sets the [page:.x x], [page:.y y] and [page:.z z] components of this vector.

### <br/> function setComponent( index: Integer, value: Float ): setComponent;
<br/>

[page:Integer index] - `0`, `1` or `2`.  
[page:Float value] - [page:Float]  
  
If index equals `0` set [page:.x x] to [page:Float value].  
If index equals `1` set [page:.y y] to [page:Float value].  
If index equals `2` set [page:.z z] to [page:Float value]

### <br/> function setFromColor( color: Color ): setFromColor; <br/>

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
the r, g, and b components of the specified [page:Color color].

### <br/> function setFromCylindrical( c: Cylindrical ): setFromCylindrical;
<br/>

Sets this vector from the cylindrical coordinates [page:Cylindrical c].

### <br/> function setFromCylindricalCoords( radius: Float, theta: Float, y:
Float ): setFromCylindricalCoords; <br/>

Sets this vector from the cylindrical coordinates [page:Cylindrical radius],
[page:Cylindrical theta] and [page:Cylindrical y].

### <br/> function setFromEuler( euler: Euler ): setFromEuler; <br/>

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
the x, y, and z components of the specified [page:Euler Euler Angle].

### <br/> function setFromMatrixColumn( matrix: Matrix4, index: Integer ):
setFromMatrixColumn; <br/>

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
[page:Integer index] column of [page:Matrix4 matrix].

### <br/> function setFromMatrix3Column( matrix: Matrix3, index: Integer ):
setFromMatrix3Column; <br/>

Sets this vector's [page:.x x], [page:.y y] and [page:.z z] components from
[page:Integer index] column of [page:Matrix3 matrix].

### <br/> function setFromMatrixPosition( m: Matrix4 ): setFromMatrixPosition;
<br/>

Sets this vector to the position elements of the
[link:https://en.wikipedia.org/wiki/Transformation_matrix transformation
matrix] [page:Matrix4 m].

### <br/> function setFromMatrixScale( m: Matrix4 ): setFromMatrixScale; <br/>

Sets this vector to the scale elements of the
[link:https://en.wikipedia.org/wiki/Transformation_matrix transformation
matrix] [page:Matrix4 m].

### <br/> function setFromSpherical( s: Spherical ): setFromSpherical; <br/>

Sets this vector from the spherical coordinates [page:Spherical s].

### <br/> function setFromSphericalCoords( radius: Float, phi: Float, theta:
Float ): setFromSphericalCoords; <br/>

Sets this vector from the spherical coordinates [page:Spherical radius],
[page:Spherical phi] and [page:Spherical theta].

### <br/> function setLength( l: Float ): setLength; <br/>

Set this vector to a vector with the same direction as this one, but
[page:.length length] [page:Float l].

### <br/> function setScalar( scalar: Float ): setScalar; <br/>

Set the [page:.x x], [page:.y y] and [page:.z z] values of this vector both
equal to [page:Float scalar].

### <br/> function setX( x: Float ): setX; <br/>

Replace this vector's [page:.x x] value with [page:Float x].

### <br/> function setY( y: Float ): setY; <br/>

Replace this vector's [page:.y y] value with [page:Float y].

### <br/> function setZ( z: Float ): setZ; <br/>

Replace this vector's [page:.z z] value with [page:Float z].

### <br/> function sub( v: Vector3 ): sub; <br/>

Subtracts [page:Vector3 v] from this vector.

### <br/> function subScalar( s: Float ): subScalar; <br/>

Subtracts [page:Float s] from this vector's [page:.x x], [page:.y y] and
[page:.z z] components.

### <br/> function subVectors( a: Vector3, b: Vector3 ): subVectors; <br/>

Sets this vector to [page:Vector3 a] - [page:Vector3 b].

###  [method:Array toArray]( [param:Array array], [param:Integer offset] )

[page:Array array] - (optional) array to store this vector to. If this is not
provided a new array will be created.  
[page:Integer offset] - (optional) optional offset into the array.  
  
Returns an array [x, y, z], or copies x, y and z into the provided [page:Array
array].

### <br/> function transformDirection( m: Matrix4 ): transformDirection; <br/>

Transforms the direction of this vector by a matrix (the upper left 3 x 3
subset of a [page:Matrix4 m]) and then [page:.normalize normalizes] the
result.

### <br/> function unproject( camera: Camera ): unproject; <br/>

[page:Camera camera] — camera to use in the projection.  
  
Projects this vector from the camera's normalized device coordinate (NDC)
space into world space.

### <br/> function random( ): random; <br/>

Sets each component of this vector to a pseudo-random value between `0` and
`1`, excluding `1`.

### <br/> function randomDirection( ): randomDirection; <br/>

Sets this vector to a uniformly random point on a unit sphere.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

