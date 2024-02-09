# [name]

Implementation of a [link:http://en.wikipedia.org/wiki/Quaternion quaternion].  
Quaternions are used in three.js to represent
[link:https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
rotations].

Iterating through a [name] instance will yield its components (x, y, z, w) in
the corresponding order.

## Code Example

  
```ts  
const quaternion = new THREE.Quaternion();  
quaternion.setFromAxisAngle( new THREE.Vector3( 0, 1, 0 ), Math.PI / 2 );  
  
const vector = new THREE.Vector3( 1, 0, 0 );  
vector.applyQuaternion( quaternion );  
```  

## Constructor

###  [name]( [param:Float x], [param:Float y], [param:Float z], [param:Float
w] )

[page:Float x] - x coordinate  
[page:Float y] - y coordinate  
[page:Float z] - z coordinate  
[page:Float w] - w coordinate

## Properties

### <br/> Boolean isQuaternion; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Float x; <br/>

### <br/> Float y; <br/>

### <br/> Float z; <br/>

### <br/> Float w; <br/>

## Methods

### [method:Float angleTo]( [param:Quaternion q] )

Returns the angle between this quaternion and quaternion [page:Quaternion q]
in radians.

### [method:Quaternion clone]()

Creates a new Quaternion with identical [page:.x x], [page:.y y], [page:.z z]
and [page:.w w] properties to this one.

### <br/> function conjugate( ): conjugate; <br/>

Returns the rotational conjugate of this quaternion. The conjugate of a
quaternion represents the same rotation in the opposite direction about the
rotational axis.

### <br/> function copy( q: Quaternion ): copy; <br/>

Copies the [page:.x x], [page:.y y], [page:.z z] and [page:.w w] properties of
[page:Quaternion q] into this quaternion.

### [method:Boolean equals]( [param:Quaternion v] )

[page:Quaternion v] - Quaternion that this quaternion will be compared to.  
  
Compares the [page:.x x], [page:.y y], [page:.z z] and [page:.w w] properties
of [page:Quaternion v] to the equivalent properties of this quaternion to
determine if they represent the same rotation.

### [method:Float dot]( [param:Quaternion v] )

Calculates the [link:https://en.wikipedia.org/wiki/Dot_product dot product] of
quaternions [page:Quaternion v] and this one.

### <br/> function fromArray( array: Array, offset: Integer ): fromArray;
<br/>

[page:Array array] - array of format (x, y, z, w) used to construct the
quaternion.  
[page:Integer offset] - (optional) an offset into the array.  
  
Sets this quaternion's [page:.x x], [page:.y y], [page:.z z] and [page:.w w]
properties from an array.

### <br/> function identity( ): identity; <br/>

Sets this quaternion to the identity quaternion; that is, to the quaternion
that represents "no rotation".

### <br/> function invert( ): invert; <br/>

Inverts this quaternion - calculates the [page:.conjugate conjugate]. The
quaternion is assumed to have unit length.

### [method:Float length]()

Computes the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
length] (straight-line length) of this quaternion, considered as a 4
dimensional vector.

### [method:Float lengthSq]()

Computes the squared [link:https://en.wikipedia.org/wiki/Euclidean_distance
Euclidean length] (straight-line length) of this quaternion, considered as a 4
dimensional vector. This can be useful if you are comparing the lengths of two
quaternions, as this is a slightly more efficient calculation than
[page:.length length]().

### <br/> function normalize( ): normalize; <br/>

[link:https://en.wikipedia.org/wiki/Normalized_vector Normalizes] this
quaternion - that is, calculated the quaternion that performs the same
rotation as this one, but has [page:.length length] equal to `1`.

### <br/> function multiply( q: Quaternion ): multiply; <br/>

Multiplies this quaternion by [page:Quaternion q].

### <br/> function multiplyQuaternions( a: Quaternion, b: Quaternion ):
multiplyQuaternions; <br/>

Sets this quaternion to [page:Quaternion a] x [page:Quaternion b].  
Adapted from the method outlined
[link:http://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/code/index.html
here].

### <br/> function premultiply( q: Quaternion ): premultiply; <br/>

Pre-multiplies this quaternion by [page:Quaternion q].

### <br/> function random( ): random; <br/>

Sets this quaternion to a uniformly random, normalized quaternion.

### <br/> function rotateTowards( q: Quaternion, step: Float ): rotateTowards;
<br/>

[page:Quaternion q] - The target quaternion.  
[page:Float step] - The angular step in radians.  
  
Rotates this quaternion by a given angular step to the defined quaternion *q*.
The method ensures that the final quaternion will not overshoot *q*.

### <br/> function slerp( qb: Quaternion, t: Float ): slerp; <br/>

[page:Quaternion qb] - The other quaternion rotation  
[page:Float t] - interpolation factor in the closed interval `[0, 1]`.  
  
Handles the spherical linear interpolation between quaternions. [page:Float t]
represents the amount of rotation between this quaternion (where [page:Float
t] is 0) and [page:Quaternion qb] (where [page:Float t] is 1). This quaternion
is set to the result. Also see the static version of the `slerp` below.  
```ts  
// rotate a mesh towards a target quaternion  
mesh.quaternion.slerp( endQuaternion, 0.01 );  
```  

### <br/> function slerpQuaternions( qa: Quaternion, qb: Quaternion, t: Float
): slerpQuaternions; <br/>

Performs a spherical linear interpolation between the given quaternions and
stores the result in this quaternion.

### <br/> function set( x: Float, y: Float, z: Float, w: Float ): set; <br/>

Sets [page:.x x], [page:.y y], [page:.z z], [page:.w w] properties of this
quaternion.

### <br/> function setFromAxisAngle( axis: Vector3, angle: Float ):
setFromAxisAngle; <br/>

Sets this quaternion from rotation specified by [page:Vector3 axis] and
[page:Float angle].  
Adapted from the method
[link:http://www.euclideanspace.com/maths/geometry/rotations/conversions/angleToQuaternion/index.html
here].  
`Axis` is assumed to be normalized, `angle` is in radians.

### <br/> function setFromEuler( euler: Euler ): setFromEuler; <br/>

Sets this quaternion from the rotation specified by [page:Euler] angle.

### <br/> function setFromRotationMatrix( m: Matrix4 ): setFromRotationMatrix;
<br/>

[page:Matrix4 m] - a [page:Matrix4] of which the upper 3x3 of matrix is a pure
[link:https://en.wikipedia.org/wiki/Rotation_matrix rotation matrix] (i.e.
unscaled).  
Sets this quaternion from rotation component of [page:Matrix4 m].  
Adapted from the method
[link:http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToQuaternion/index.html
here].

### <br/> function setFromUnitVectors( vFrom: Vector3, vTo: Vector3 ):
setFromUnitVectors; <br/>

Sets this quaternion to the rotation required to rotate direction vector
[page:Vector3 vFrom] to direction vector [page:Vector3 vTo].  
Adapted from the method [link:http://lolengine.net/blog/2013/09/18/beautiful-
maths-quaternion-from-vectors here].  
[page:Vector3 vFrom] and [page:Vector3 vTo] are assumed to be normalized.

###  [method:Array toArray]( [param:Array array], [param:Integer offset] )

[page:Array array] - An optional array to store the quaternion. If not
specified, a new array will be created.  
[page:Integer offset] - (optional) if specified, the result will be copied
into this [page:Array].  
  
Returns the numerical elements of this quaternion in an array of format [x, y,
z, w].

### [method:Array toJSON]()

This methods defines the serialization result of [name]. Returns the numerical
elements of this quaternion in an array of format [x, y, z, w].

### <br/> function fromBufferAttribute( attribute: BufferAttribute, index:
Integer ): fromBufferAttribute; <br/>

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets [page:.x x], [page:.y y], [page:.z z], [page:.w w] properties of this
quaternion from the [page:BufferAttribute attribute].

## Static Methods

###  [method:undefined slerpFlat]( [param:Array dst], [param:Integer
dstOffset], [param:Array src0], [param:Integer srcOffset0], [param:Array
src1], [param:Integer srcOffset1], [param:Float t] )

[page:Array dst] - The output array.  
[page:Integer dstOffset] - An offset into the output array.  
[page:Array src0] - The source array of the starting quaternion.  
[page:Integer srcOffset0] - An offset into the array `src0`.  
[page:Array src1] - The source array of the target quaternion.  
[page:Integer srcOffset1] - An offset into the array `src1`.  
[page:Float t] - Normalized interpolation factor (between `0` and `1`).  
  
This SLERP implementation assumes the quaternion data are managed in flat
arrays.

###  [method:Array multiplyQuaternionsFlat]( [param:Array dst], [param:Integer
dstOffset], [param:Array src0], [param:Integer srcOffset0], [param:Array
src1], [param:Integer srcOffset1] )

[page:Array dst] - The output array.  
[page:Integer dstOffset] - An offset into the output array.  
[page:Array src0] - The source array of the starting quaternion.  
[page:Integer srcOffset0] - An offset into the array `src0`.  
[page:Array src1] - The source array of the target quaternion.  
[page:Integer srcOffset1] - An offset into the array `src1`.  
  
This multiplication implementation assumes the quaternion data are managed in
flat arrays.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

