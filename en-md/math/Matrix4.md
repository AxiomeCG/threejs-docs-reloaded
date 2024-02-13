# Matrix4

A class representing a 4x4
[link:https://en.wikipedia.org/wiki/Matrix_(mathematics) matrix].  
  
The most common use of a 4x4 matrix in 3D computer graphics is as a
[link:https://en.wikipedia.org/wiki/Transformation_matrix Transformation
Matrix]. For an introduction to transformation matrices as used in WebGL,
check out [link:http://www.opengl-tutorial.org/beginners-
tutorials/tutorial-3-matrices this tutorial].  
  
This allows a [page:Vector3] representing a point in 3D space to undergo
transformations such as translation, rotation, shear, scale, reflection,
orthogonal or perspective projection and so on, by being multiplied by the
matrix. This is known as `applying` the matrix to the vector.  
  
Every [page:Object3D] has three associated Matrix4s:

  * [page:Object3D.matrix]: This stores the local transform of the object. This is the object's transformation relative to its parent.
  * [page:Object3D.matrixWorld]: The global or world transform of the object. If the object has no parent, then this is identical to the local transform stored in [page:Object3D.matrix matrix].
  * [page:Object3D.modelViewMatrix]: This represents the object's transformation relative to the camera's coordinate system. An object's modelViewMatrix is the object's matrixWorld pre-multiplied by the camera's matrixWorldInverse.

[page:Camera Cameras] have three additional Matrix4s:

  * [page:Camera.matrixWorldInverse]: The view matrix - the inverse of the Camera's [page:Object3D.matrixWorld matrixWorld].
  * [page:Camera.projectionMatrix]: Represents the information how to project the scene to clip space.
  * [page:Camera.projectionMatrixInverse]: The inverse of projectionMatrix.

Note: [page:Object3D.normalMatrix] is not a Matrix4, but a [page:Matrix3].

## A Note on Row-Major and Column-Major Ordering

The constructor and [page:set]() method take arguments in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order row-major] order, while internally they are stored in the
[page:.elements elements] array in column-major order.  
  
This means that calling  
```ts  
const m = new THREE.Matrix4(); m.set( 11, 12, 13, 14, 21, 22, 23, 24, 31, 32,
33, 34, 41, 42, 43, 44 );  
```  
will result in the [page:.elements elements] array containing:  
```ts  
m.elements = [ 11, 21, 31, 41, 12, 22, 32, 42, 13, 23, 33, 43, 14, 24, 34, 44
];  
```  
and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and most
people are used to thinking about matrices in row-major order, the three.js
documentation shows matrices in row-major order. Just bear in mind that if you
are reading the source code, you'll have to take the
[link:https://en.wikipedia.org/wiki/Transpose transpose] of any matrices
outlined here to make sense of the calculations.

## Extracting position, rotation and scale

There are several options available for extracting position, rotation and
scale from a Matrix4.

  * [page:Vector3.setFromMatrixPosition]: can be used to extract the translation component.
  * [page:Vector3.setFromMatrixScale]: can be used to extract the scale component.
  * [page:Quaternion.setFromRotationMatrix], [page:Euler.setFromRotationMatrix] or [page:.extractRotation extractRotation] can be used to extract the rotation component from a pure (unscaled) matrix.
  * [page:.decompose decompose] can be used to extract position, rotation and scale all at once.

## Constructor

###  function Matrix4( n11: Number, n12: Number, n13: Number, n14: Number,
n21: Number, n22: Number, n23: Number, n24: Number, n31: Number, n32: Number,
n33: Number, n34: Number, n41: Number, n42: Number, n43: Number, n44: Number
): void;

Creates a 4x4 matrix with the given arguments in row-major order. If no
arguments are provided, the constructor initializes the Matrix4 to the 4x4
[link:https://en.wikipedia.org/wiki/Identity_matrix identity matrix].

## Properties

###  Array elements;

A [link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order column-major] list of matrix values.

## Methods

###  function clone( ): Matrix4;

Creates a new Matrix4 with identical [page:.elements elements] to this one.

###  function compose( position: Vector3, quaternion: Quaternion, scale:
Vector3 ): this;

Sets this matrix to the transformation composed of [page:Vector3 position],
[page:Quaternion quaternion] and [page:Vector3 scale].

###  function copy( m: Matrix4 ): this;

Copies the [page:.elements elements] of matrix [page:Matrix4 m] into this
matrix.

###  function copyPosition( m: Matrix4 ): this;

Copies the translation component of the supplied matrix [page:Matrix4 m] into
this matrix's translation component.

###  function decompose( position: Vector3, quaternion: Quaternion, scale:
Vector3 ): this;

Decomposes this matrix into its [page:Vector3 position], [page:Quaternion
quaternion] and [page:Vector3 scale] components.  
  
Note: Not all matrices are decomposable in this way. For example, if an object
has a non-uniformly scaled parent, then the object's world matrix may not be
decomposable, and this method may not be appropriate.

###  function determinant( ): Float;

Computes and returns the [link:https://en.wikipedia.org/wiki/Determinant
determinant] of this matrix.  
  
Based on the method outlined
[link:http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/fourD/index.html
here].

###  function equals( m: Matrix4 ): Boolean;

Return true if this matrix and [page:Matrix4 m] are equal.

###  function extractBasis( xAxis: Vector3, yAxis: Vector3, zAxis: Vector3 ):
this;

Extracts the [link:https://en.wikipedia.org/wiki/Basis_(linear_algebra) basis]
of this matrix into the three axis vectors provided. If this matrix is:  
```ts  
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p  
```  
then the [page:Vector3 xAxis], [page:Vector3 yAxis], [page:Vector3 zAxis] will
be set to:  
```ts  
xAxis = (a, e, i) yAxis = (b, f, j) zAxis = (c, g, k)  
```  

###  function extractRotation( m: Matrix4 ): this;

Extracts the rotation component of the supplied matrix [page:Matrix4 m] into
this matrix's rotation component.

###  function fromArray( array: Array, offset: Integer ): this;

[page:Array array] - the array to read the elements from.  
[page:Integer offset] - ( optional ) offset into the array. Default is 0.  
  
Sets the elements of this matrix based on an [page:Array array] in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order column-major] format.

###  function invert( ): this;

Inverts this matrix, using the
[link:https://en.wikipedia.org/wiki/Invertible_matrix#Analytic_solution
analytic method]. You can not invert with a determinant of zero. If you
attempt this, the method produces a zero matrix instead.

###  function getMaxScaleOnAxis( ): Float;

Gets the maximum scale value of the 3 axes.

###  function identity( ): this;

Resets this matrix to the [link:https://en.wikipedia.org/wiki/Identity_matrix
identity matrix].

###  function lookAt( eye: Vector3, target: Vector3, up: Vector3 ): this;

Constructs a rotation matrix, looking from [page:Vector3 eye] towards
[page:Vector3 target] oriented by the [page:Vector3 up] vector.

###  function makeRotationAxis( axis: Vector3, theta: Float ): this;

[page:Vector3 axis] — Rotation axis, should be normalized.  
[page:Float theta] — Rotation angle in radians.  
  
Sets this matrix as rotation transform around [page:Vector3 axis] by
[page:Float theta] radians.  
This is a somewhat controversial but mathematically sound alternative to
rotating via [page:Quaternion Quaternions]. See the discussion
[link:https://www.gamedev.net/articles/programming/math-and-physics/do-we-
really-need-quaternions-r1199 here].

###  function makeBasis( xAxis: Vector3, yAxis: Vector3, zAxis: Vector3 ):
this;

Set this to the [link:https://en.wikipedia.org/wiki/Basis_(linear_algebra)
basis] matrix consisting of the three provided basis vectors:  
```ts  
xAxis.x, yAxis.x, zAxis.x, 0, xAxis.y, yAxis.y, zAxis.y, 0, xAxis.z, yAxis.z,
zAxis.z, 0, 0, 0, 0, 1  
```  

###  function makePerspective( left: Float, right: Float, top: Float, bottom:
Float, near: Float, far: Float ): this;

Creates a
[link:https://en.wikipedia.org/wiki/3D_projection#Perspective_projection
perspective projection] matrix. This is used internally by
[page:PerspectiveCamera.updateProjectionMatrix]()

###  function makeOrthographic( left: Float, right: Float, top: Float, bottom:
Float, near: Float, far: Float ): this;

Creates an [link:https://en.wikipedia.org/wiki/Orthographic_projection
orthographic projection] matrix. This is used internally by
[page:OrthographicCamera.updateProjectionMatrix]().

###  function makeRotationFromEuler( euler: Euler ): this;

Sets the rotation component (the upper left 3x3 matrix) of this matrix to the
rotation specified by the given [page:Euler Euler Angle]. The rest of the
matrix is set to the identity. Depending on the [page:Euler.order order] of
the [page:Euler euler], there are six possible outcomes. See
[link:https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix this page]
for a complete list.

###  function makeRotationFromQuaternion( q: Quaternion ): this;

Sets the rotation component of this matrix to the rotation specified by
[page:Quaternion q], as outlined
[link:https://en.wikipedia.org/wiki/Rotation_matrix#Quaternion here]. The rest
of the matrix is set to the identity. So, given [page:Quaternion q] = w + xi +
yj + zk, the resulting matrix will be:  
```ts  
1-2y²-2z² 2xy-2zw 2xz+2yw 0 2xy+2zw 1-2x²-2z² 2yz-2xw 0 2xz-2yw 2yz+2xw
1-2x²-2y² 0 0 0 0 1  
```  

###  function makeRotationX( theta: Float ): this;

[page:Float theta] — Rotation angle in radians.  
  
Sets this matrix as a rotational transformation around the X axis by
[page:Float theta] (θ) radians. The resulting matrix will be:  
```ts  
1 0 0 0 0 cos(θ) -sin(θ) 0 0 sin(θ) cos(θ) 0 0 0 0 1  
```  

###  function makeRotationY( theta: Float ): this;

[page:Float theta] — Rotation angle in radians.  
  
Sets this matrix as a rotational transformation around the Y axis by
[page:Float theta] (θ) radians. The resulting matrix will be:  
```ts  
cos(θ) 0 sin(θ) 0 0 1 0 0 -sin(θ) 0 cos(θ) 0 0 0 0 1  
```  

###  function makeRotationZ( theta: Float ): this;

[page:Float theta] — Rotation angle in radians.  
  
Sets this matrix as a rotational transformation around the Z axis by
[page:Float theta] (θ) radians. The resulting matrix will be:  
```ts  
cos(θ) -sin(θ) 0 0 sin(θ) cos(θ) 0 0 0 0 1 0 0 0 0 1  
```  

###  function makeScale( x: Float, y: Float, z: Float ): this;

[page:Float x] - the amount to scale in the X axis.  
[page:Float y] - the amount to scale in the Y axis.  
[page:Float z] - the amount to scale in the Z axis.  
  
Sets this matrix as scale transform:  
```ts  
x, 0, 0, 0, 0, y, 0, 0, 0, 0, z, 0, 0, 0, 0, 1  
```  

###  function makeShear( xy: Float, xz: Float, yx: Float, yz: Float, zx:
Float, zy: Float ): this;

[page:Float xy] - the amount to shear X by Y.  
[page:Float xz] - the amount to shear X by Z.  
[page:Float yx] - the amount to shear Y by X.  
[page:Float yz] - the amount to shear Y by Z.  
[page:Float zx] - the amount to shear Z by X.  
[page:Float zy] - the amount to shear Z by Y.  
  
Sets this matrix as a shear transform:  
```ts  
1, yx, zx, 0, xy, 1, zy, 0, xz, yz, 1, 0, 0, 0, 0, 1  
```  

###  function makeTranslation( v: Vector3 ): this;

###  function makeTranslation( x: Float, y: Float, z: Float ): this;

Sets this matrix as a translation transform from vector [page:Vector3 v], or
numbers [page:Float x], [page:Float y] and [page:Float z]:  
```ts  
1, 0, 0, x, 0, 1, 0, y, 0, 0, 1, z, 0, 0, 0, 1  
```  

###  function multiply( m: Matrix4 ): this;

Post-multiplies this matrix by [page:Matrix4 m].

###  function multiplyMatrices( a: Matrix4, b: Matrix4 ): this;

Sets this matrix to [page:Matrix4 a] x [page:Matrix4 b].

###  function multiplyScalar( s: Float ): this;

Multiplies every component of the matrix by a scalar value [page:Float s].

###  function premultiply( m: Matrix4 ): this;

Pre-multiplies this matrix by [page:Matrix4 m].

###  function scale( v: Vector3 ): this;

Multiplies the columns of this matrix by vector [page:Vector3 v].

###  function set( n11: Float, n12: Float, n13: Float, n14: Float, n21: Float,
n22: Float, n23: Float, n24: Float, n31: Float, n32: Float, n33: Float, n34:
Float, n41: Float, n42: Float, n43: Float, n44: Float ): this;

Set the [page:.elements elements] of this matrix to the supplied row-major
values [page:Float n11], [page:Float n12], ... [page:Float n44].

###  function setFromMatrix3( m: Matrix3 ): this;

Set the upper 3x3 elements of this matrix to the values of the Matrix3
[page:Matrix3 m].

###  function setPosition( v: Vector3 ): this;

###  function setPosition( x: Float, y: Float, z: Float ): this;

Sets the position component for this matrix from vector [page:Vector3 v],
without affecting the rest of the matrix - i.e. if the matrix is currently:  
```ts  
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p  
```  
This becomes:  
```ts  
a, b, c, v.x, e, f, g, v.y, i, j, k, v.z, m, n, o, p  
```  

###  function toArray( array: Array, offset: Integer ): Array;

[page:Array array] - (optional) array to store the resulting vector in.  
[page:Integer offset] - (optional) offset in the array at which to put the
result.  
  
Writes the elements of this matrix to an array in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order column-major] format.

###  function transpose( ): this;

[link:https://en.wikipedia.org/wiki/Transpose Transposes] this matrix.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

