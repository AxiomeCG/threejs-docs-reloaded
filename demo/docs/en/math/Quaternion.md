# Quaternion

Implementation of a <a
href="http://en.wikipedia.org/wiki/Quaternion">quaternion</a>.  
Quaternions are used in three.js to represent <a
href="https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation">rotations</a>.

Iterating through a Quaternion instance will yield its components (x, y, z, w)
in the corresponding order.

## Code Example

  
```ts  
const quaternion = new THREE.Quaternion(); quaternion.setFromAxisAngle( new
THREE.Vector3( 0, 1, 0 ), Math.PI / 2 ); const vector = new THREE.Vector3( 1,
0, 0 ); vector.applyQuaternion( quaternion );  
```  

## Constructor

### Quaternion

  
  
```ts  
function Quaternion( x: Float, y: Float, z: Float, w: Float ): void;  
```  

[x](#) - x coordinate  
[y](#) - y coordinate  
[z](#) - z coordinate  
[w](#) - w coordinate

## Properties

### isQuaternion

  
  
```ts  
isQuaternion: Boolean;  
```  

Read-only flag to check if a given object is of type Quaternion.

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

## Methods

### angleTo

  
  
```ts  
function angleTo( q: Quaternion ): Float;  
```  

Returns the angle between this quaternion and quaternion
[q](en\math\Quaternion.html) in radians.

### clone

  
  
```ts  
function clone( ): Quaternion;  
```  

Creates a new Quaternion with identical [.x](#x), [.y](#y), [.z](#z) and
[.w](#w) properties to this one.

### conjugate

  
  
```ts  
function conjugate( ): this;  
```  

Returns the rotational conjugate of this quaternion. The conjugate of a
quaternion represents the same rotation in the opposite direction about the
rotational axis.

### copy

  
  
```ts  
function copy( q: Quaternion ): this;  
```  

Copies the [.x](#x), [.y](#y), [.z](#z) and [.w](#w) properties of
[.uaternion](#uaternion) into this quaternion.

### equals

  
  
```ts  
function equals( v: Quaternion ): Boolean;  
```  

[v](en\math\Quaternion.html) - Quaternion that this quaternion will be
compared to.  
  
Compares the [.x](#x), [.y](#y), [.z](#z) and [.w](#w) properties of
[.uaternion](#uaternion) to the equivalent properties of this quaternion to
determine if they represent the same rotation.

### dot

  
  
```ts  
function dot( v: Quaternion ): Float;  
```  

Calculates the <a href="https://en.wikipedia.org/wiki/Dot_product">dot
product</a> of quaternions [v](en\math\Quaternion.html) and this one.

### fromArray

  
  
```ts  
function fromArray( array: Array, offset: Integer ): this;  
```  

[array](#) - array of format (x, y, z, w) used to construct the quaternion.  
[offset](#) - (optional) an offset into the array.  
  
Sets this quaternion's [.x](#x), [.y](#y), [.z](#z) and [.w](#w) properties
from an array.

### identity

  
  
```ts  
function identity( ): this;  
```  

Sets this quaternion to the identity quaternion; that is, to the quaternion
that represents "no rotation".

### invert

  
  
```ts  
function invert( ): this;  
```  

Inverts this quaternion - calculates the [.conjugate](#conjugate). The
quaternion is assumed to have unit length.

### length

  
  
```ts  
function length( ): Float;  
```  

Computes the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean length</a>
(straight-line length) of this quaternion, considered as a 4 dimensional
vector.

### lengthSq

  
  
```ts  
function lengthSq( ): Float;  
```  

Computes the squared <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean length</a>
(straight-line length) of this quaternion, considered as a 4 dimensional
vector. This can be useful if you are comparing the lengths of two
quaternions, as this is a slightly more efficient calculation than
[.length](#length)().

### normalize

  
  
```ts  
function normalize( ): this;  
```  

<a href="https://en.wikipedia.org/wiki/Normalized_vector">Normalizes</a> this
quaternion - that is, calculated the quaternion that performs the same
rotation as this one, but has [.length](#length) equal to `1`.

### multiply

  
  
```ts  
function multiply( q: Quaternion ): this;  
```  

Multiplies this quaternion by [q](en\math\Quaternion.html).

### multiplyQuaternions

  
  
```ts  
function multiplyQuaternions( a: Quaternion, b: Quaternion ): this;  
```  

Sets this quaternion to [a](en\math\Quaternion.html) x
[b](en\math\Quaternion.html).  
Adapted from the method outlined <a
href="http://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/code/index.html">here</a>.

### premultiply

  
  
```ts  
function premultiply( q: Quaternion ): this;  
```  

Pre-multiplies this quaternion by [q](en\math\Quaternion.html).

### random

  
  
```ts  
function random( ): this;  
```  

Sets this quaternion to a uniformly random, normalized quaternion.

### rotateTowards

  
  
```ts  
function rotateTowards( q: Quaternion, step: Float ): this;  
```  

[q](en\math\Quaternion.html) - The target quaternion.  
[step](#) - The angular step in radians.  
  
Rotates this quaternion by a given angular step to the defined quaternion *q*.
The method ensures that the final quaternion will not overshoot *q*.

### slerp

  
  
```ts  
function slerp( qb: Quaternion, t: Float ): this;  
```  

[qb](en\math\Quaternion.html) - The other quaternion rotation  
[t](#) - interpolation factor in the closed interval `[0, 1]`.  
  
Handles the spherical linear interpolation between quaternions. [t](#)
represents the amount of rotation between this quaternion (where [t](#) is 0)
and [qb](en\math\Quaternion.html) (where [t](#) is 1). This quaternion is set
to the result. Also see the static version of the `slerp` below.  
```ts  
// rotate a mesh towards a target quaternion mesh.quaternion.slerp(
endQuaternion, 0.01 );  
```  

### slerpQuaternions

  
  
```ts  
function slerpQuaternions( qa: Quaternion, qb: Quaternion, t: Float ): this;  
```  

Performs a spherical linear interpolation between the given quaternions and
stores the result in this quaternion.

### set

  
  
```ts  
function set( x: Float, y: Float, z: Float, w: Float ): this;  
```  

Sets [.x](#x), [.y](#y), [.z](#z), [.w](#w) properties of this quaternion.

### setFromAxisAngle

  
  
```ts  
function setFromAxisAngle( axis: Vector3, angle: Float ): this;  
```  

Sets this quaternion from rotation specified by [axis](en\math\Vector3.html)
and [angle](#).  
Adapted from the method <a
href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/angleToQuaternion/index.html">here</a>.  
`Axis` is assumed to be normalized, `angle` is in radians.

### setFromEuler

  
  
```ts  
function setFromEuler( euler: Euler ): this;  
```  

Sets this quaternion from the rotation specified by
[Euler](en\math\Euler.html) angle.

### setFromRotationMatrix

  
  
```ts  
function setFromRotationMatrix( m: Matrix4 ): this;  
```  

[m](en\math\Matrix4.html) - a [Matrix4](en\math\Matrix4.html) of which the
upper 3x3 of matrix is a pure <a
href="https://en.wikipedia.org/wiki/Rotation_matrix">rotation matrix</a> (i.e.
unscaled).  
Sets this quaternion from rotation component of [m](en\math\Matrix4.html).  
Adapted from the method <a
href="http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToQuaternion/index.html">here</a>.

### setFromUnitVectors

  
  
```ts  
function setFromUnitVectors( vFrom: Vector3, vTo: Vector3 ): this;  
```  

Sets this quaternion to the rotation required to rotate direction vector
[vFrom](en\math\Vector3.html) to direction vector [vTo](en\math\Vector3.html).  
Adapted from the method <a
href="http://lolengine.net/blog/2013/09/18/beautiful-maths-quaternion-from-
vectors">here</a>.  
[vFrom](en\math\Vector3.html) and [vTo](en\math\Vector3.html) are assumed to
be normalized.

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - An optional array to store the quaternion. If not specified, a
new array will be created.  
[offset](#) - (optional) if specified, the result will be copied into this
[Array](#).  
  
Returns the numerical elements of this quaternion in an array of format [x, y,
z, w].

### toJSON

  
  
```ts  
function toJSON( ): Array;  
```  

This methods defines the serialization result of Quaternion. Returns the
numerical elements of this quaternion in an array of format [x, y, z, w].

### fromBufferAttribute

  
  
```ts  
function fromBufferAttribute( attribute: BufferAttribute, index: Integer ):
this;  
```  

[attribute](en\core\BufferAttribute.html) - the source attribute.  
[index](#) - index in the attribute.  
  
Sets [.x](#x), [.y](#y), [.z](#z), [.w](#w) properties of this quaternion from
the [.ufferAttribute](#ufferAttribute).

## Static Methods

### slerpFlat

  
  
```ts  
function slerpFlat( dst: Array, dstOffset: Integer, src0: Array, srcOffset0:
Integer, src1: Array, srcOffset1: Integer, t: Float ): undefined;  
```  

[dst](#) - The output array.  
[dstOffset](#) - An offset into the output array.  
[src0](#) - The source array of the starting quaternion.  
[srcOffset0](#) - An offset into the array `src0`.  
[src1](#) - The source array of the target quaternion.  
[srcOffset1](#) - An offset into the array `src1`.  
[t](#) - Normalized interpolation factor (between `0` and `1`).  
  
This SLERP implementation assumes the quaternion data are managed in flat
arrays.

### multiplyQuaternionsFlat

  
  
```ts  
function multiplyQuaternionsFlat( dst: Array, dstOffset: Integer, src0: Array,
srcOffset0: Integer, src1: Array, srcOffset1: Integer ): Array;  
```  

[dst](#) - The output array.  
[dstOffset](#) - An offset into the output array.  
[src0](#) - The source array of the starting quaternion.  
[srcOffset0](#) - An offset into the array `src0`.  
[src1](#) - The source array of the target quaternion.  
[srcOffset1](#) - An offset into the array `src1`.  
  
This multiplication implementation assumes the quaternion data are managed in
flat arrays.

Note: Do not add non-static methods to the bottom of this page. Put them above
the <h2>Static Methods</h2>

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Quaternion.js">src/math/Quaternion.js</a>

