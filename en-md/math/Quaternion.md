# Quaternion

Implementation of a [link:http://en.wikipedia.org/wiki/Quaternion quaternion].  
Quaternions are used in three.js to represent
[link:https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
rotations].

Iterating through a Quaternion instance will yield its components (x, y, z, w)
in the corresponding order.

## Code Example

  
```ts  
const quaternion = new THREE.Quaternion(); quaternion.setFromAxisAngle( new
THREE.Vector3( 0, 1, 0 ), Math.PI / 2 ); const vector = new THREE.Vector3( 1,
0, 0 ); vector.applyQuaternion( quaternion );  
```  

## Constructor

###  function Quaternion( x: Float, y: Float, z: Float, w: Float ): void;

[page:Float x] - x coordinate  
[page:Float y] - y coordinate  
[page:Float z] - z coordinate  
[page:Float w] - w coordinate

## Properties

###  Boolean isQuaternion;

Read-only flag to check if a given object is of type Quaternion.

###  Float x;

###  Float y;

###  Float z;

###  Float w;

## Methods

###  function angleTo( q: Quaternion ): Float;

Returns the angle between this quaternion and quaternion [page:Quaternion q]
in radians.

###  function clone( ): Quaternion;

Creates a new Quaternion with identical [page:.x x], [page:.y y], [page:.z z]
and [page:.w w] properties to this one.

###  function conjugate( ): this;

Returns the rotational conjugate of this quaternion. The conjugate of a
quaternion represents the same rotation in the opposite direction about the
rotational axis.

###  function copy( q: Quaternion ): this;

Copies the [page:.x x], [page:.y y], [page:.z z] and [page:.w w] properties of
[page:Quaternion q] into this quaternion.

###  function equals( v: Quaternion ): Boolean;

[page:Quaternion v] - Quaternion that this quaternion will be compared to.  
  
Compares the [page:.x x], [page:.y y], [page:.z z] and [page:.w w] properties
of [page:Quaternion v] to the equivalent properties of this quaternion to
determine if they represent the same rotation.

###  function dot( v: Quaternion ): Float;

Calculates the [link:https://en.wikipedia.org/wiki/Dot_product dot product] of
quaternions [page:Quaternion v] and this one.

###  function fromArray( array: Array, offset: Integer ): this;

[page:Array array] - array of format (x, y, z, w) used to construct the
quaternion.  
[page:Integer offset] - (optional) an offset into the array.  
  
Sets this quaternion's [page:.x x], [page:.y y], [page:.z z] and [page:.w w]
properties from an array.

###  function identity( ): this;

Sets this quaternion to the identity quaternion; that is, to the quaternion
that represents "no rotation".

###  function invert( ): this;

Inverts this quaternion - calculates the [page:.conjugate conjugate]. The
quaternion is assumed to have unit length.

###  function length( ): Float;

Computes the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
length] (straight-line length) of this quaternion, considered as a 4
dimensional vector.

###  function lengthSq( ): Float;

Computes the squared [link:https://en.wikipedia.org/wiki/Euclidean_distance
Euclidean length] (straight-line length) of this quaternion, considered as a 4
dimensional vector. This can be useful if you are comparing the lengths of two
quaternions, as this is a slightly more efficient calculation than
[page:.length length]().

###  function normalize( ): this;

[link:https://en.wikipedia.org/wiki/Normalized_vector Normalizes] this
quaternion - that is, calculated the quaternion that performs the same
rotation as this one, but has [page:.length length] equal to `1`.

###  function multiply( q: Quaternion ): this;

Multiplies this quaternion by [page:Quaternion q].

###  function multiplyQuaternions( a: Quaternion, b: Quaternion ): this;

Sets this quaternion to [page:Quaternion a] x [page:Quaternion b].  
Adapted from the method outlined
[link:http://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/code/index.html
here].

###  function premultiply( q: Quaternion ): this;

Pre-multiplies this quaternion by [page:Quaternion q].

###  function random( ): this;

Sets this quaternion to a uniformly random, normalized quaternion.

###  function rotateTowards( q: Quaternion, step: Float ): this;

[page:Quaternion q] - The target quaternion.  
[page:Float step] - The angular step in radians.  
  
Rotates this quaternion by a given angular step to the defined quaternion *q*.
The method ensures that the final quaternion will not overshoot *q*.

###  function slerp( qb: Quaternion, t: Float ): this;

[page:Quaternion qb] - The other quaternion rotation  
[page:Float t] - interpolation factor in the closed interval `[0, 1]`.  
  
Handles the spherical linear interpolation between quaternions. [page:Float t]
represents the amount of rotation between this quaternion (where [page:Float
t] is 0) and [page:Quaternion qb] (where [page:Float t] is 1). This quaternion
is set to the result. Also see the static version of the `slerp` below.  
```ts  
// rotate a mesh towards a target quaternion mesh.quaternion.slerp(
endQuaternion, 0.01 );  
```  

###  function slerpQuaternions( qa: Quaternion, qb: Quaternion, t: Float ):
this;

Performs a spherical linear interpolation between the given quaternions and
stores the result in this quaternion.

###  function set( x: Float, y: Float, z: Float, w: Float ): this;

Sets [page:.x x], [page:.y y], [page:.z z], [page:.w w] properties of this
quaternion.

###  function setFromAxisAngle( axis: Vector3, angle: Float ): this;

Sets this quaternion from rotation specified by [page:Vector3 axis] and
[page:Float angle].  
Adapted from the method
[link:http://www.euclideanspace.com/maths/geometry/rotations/conversions/angleToQuaternion/index.html
here].  
`Axis` is assumed to be normalized, `angle` is in radians.

###  function setFromEuler( euler: Euler ): this;

Sets this quaternion from the rotation specified by [page:Euler] angle.

###  function setFromRotationMatrix( m: Matrix4 ): this;

[page:Matrix4 m] - a [page:Matrix4] of which the upper 3x3 of matrix is a pure
[link:https://en.wikipedia.org/wiki/Rotation_matrix rotation matrix] (i.e.
unscaled).  
Sets this quaternion from rotation component of [page:Matrix4 m].  
Adapted from the method
[link:http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToQuaternion/index.html
here].

###  function setFromUnitVectors( vFrom: Vector3, vTo: Vector3 ): this;

Sets this quaternion to the rotation required to rotate direction vector
[page:Vector3 vFrom] to direction vector [page:Vector3 vTo].  
Adapted from the method [link:http://lolengine.net/blog/2013/09/18/beautiful-
maths-quaternion-from-vectors here].  
[page:Vector3 vFrom] and [page:Vector3 vTo] are assumed to be normalized.

###  function toArray( array: Array, offset: Integer ): Array;

[page:Array array] - An optional array to store the quaternion. If not
specified, a new array will be created.  
[page:Integer offset] - (optional) if specified, the result will be copied
into this [page:Array].  
  
Returns the numerical elements of this quaternion in an array of format [x, y,
z, w].

###  function toJSON( ): Array;

This methods defines the serialization result of Quaternion. Returns the
numerical elements of this quaternion in an array of format [x, y, z, w].

###  function fromBufferAttribute( attribute: BufferAttribute, index: Integer
): this;

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets [page:.x x], [page:.y y], [page:.z z], [page:.w w] properties of this
quaternion from the [page:BufferAttribute attribute].

## Static Methods

###  function slerpFlat( dst: Array, dstOffset: Integer, src0: Array,
srcOffset0: Integer, src1: Array, srcOffset1: Integer, t: Float ): undefined;

[page:Array dst] - The output array.  
[page:Integer dstOffset] - An offset into the output array.  
[page:Array src0] - The source array of the starting quaternion.  
[page:Integer srcOffset0] - An offset into the array `src0`.  
[page:Array src1] - The source array of the target quaternion.  
[page:Integer srcOffset1] - An offset into the array `src1`.  
[page:Float t] - Normalized interpolation factor (between `0` and `1`).  
  
This SLERP implementation assumes the quaternion data are managed in flat
arrays.

###  function multiplyQuaternionsFlat( dst: Array, dstOffset: Integer, src0:
Array, srcOffset0: Integer, src1: Array, srcOffset1: Integer ): Array;

[page:Array dst] - The output array.  
[page:Integer dstOffset] - An offset into the output array.  
[page:Array src0] - The source array of the starting quaternion.  
[page:Integer srcOffset0] - An offset into the array `src0`.  
[page:Array src1] - The source array of the target quaternion.  
[page:Integer srcOffset1] - An offset into the array `src1`.  
  
This multiplication implementation assumes the quaternion data are managed in
flat arrays.

Note: Do not add non-static methods to the bottom of this page. Put them above
the <h2>Static Methods</h2>

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

