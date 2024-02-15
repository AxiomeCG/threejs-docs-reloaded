# Matrix4

A class representing a 4x4 <a
href="https://en.wikipedia.org/wiki/Matrix_(mathematics)">matrix</a>.  
  
The most common use of a 4x4 matrix in 3D computer graphics is as a <a
href="https://en.wikipedia.org/wiki/Transformation_matrix">Transformation
Matrix</a>. For an introduction to transformation matrices as used in WebGL,
check out <a href="http://www.opengl-tutorial.org/beginners-
tutorials/tutorial-3-matrices">this tutorial</a>.  
  
This allows a [Vector3](en\math\Vector3.html) representing a point in 3D space
to undergo transformations such as translation, rotation, shear, scale,
reflection, orthogonal or perspective projection and so on, by being
multiplied by the matrix. This is known as `applying` the matrix to the
vector.  
  
Every [Object3D](en\core\Object3D.html) has three associated Matrix4s:

  * [Object3D.matrix](#): This stores the local transform of the object. This is the object's transformation relative to its parent.
  * [Object3D.matrixWorld](#): The global or world transform of the object. If the object has no parent, then this is identical to the local transform stored in [matrix](#).
  * [Object3D.modelViewMatrix](#): This represents the object's transformation relative to the camera's coordinate system. An object's modelViewMatrix is the object's matrixWorld pre-multiplied by the camera's matrixWorldInverse.

[Cameras](en\cameras\Camera.html) have three additional Matrix4s:

  * [Camera.matrixWorldInverse](#): The view matrix - the inverse of the Camera's [matrixWorld](#).
  * [Camera.projectionMatrix](#): Represents the information how to project the scene to clip space.
  * [Camera.projectionMatrixInverse](#): The inverse of projectionMatrix.

Note: [Object3D.normalMatrix](#) is not a Matrix4, but a
[Matrix3](en\math\Matrix3.html).

## A Note on Row-Major and Column-Major Ordering

The constructor and [set](#)() method take arguments in <a
href="https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order">row-major</a> order, while internally they are stored in the
[.elements](#elements) array in column-major order.  
  
This means that calling  
```ts  
const m = new THREE.Matrix4(); m.set( 11, 12, 13, 14, 21, 22, 23, 24, 31, 32,
33, 34, 41, 42, 43, 44 );  
```  
will result in the [.elements](#elements) array containing:  
```ts  
m.elements = [ 11, 21, 31, 41, 12, 22, 32, 42, 13, 23, 33, 43, 14, 24, 34, 44
];  
```  
and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and most
people are used to thinking about matrices in row-major order, the three.js
documentation shows matrices in row-major order. Just bear in mind that if you
are reading the source code, you'll have to take the <a
href="https://en.wikipedia.org/wiki/Transpose">transpose</a> of any matrices
outlined here to make sense of the calculations.

## Extracting position, rotation and scale

There are several options available for extracting position, rotation and
scale from a Matrix4.

  * [Vector3.setFromMatrixPosition](#): can be used to extract the translation component.
  * [Vector3.setFromMatrixScale](#): can be used to extract the scale component.
  * [Quaternion.setFromRotationMatrix](#), [Euler.setFromRotationMatrix](#) or [.extractRotation](#extractRotation) can be used to extract the rotation component from a pure (unscaled) matrix.
  * [.decompose](#decompose) can be used to extract position, rotation and scale all at once.

## Constructor

### Matrix4

  
  
```ts  
function Matrix4( n11: Number, n12: Number, n13: Number, n14: Number, n21:
Number, n22: Number, n23: Number, n24: Number, n31: Number, n32: Number, n33:
Number, n34: Number, n41: Number, n42: Number, n43: Number, n44: Number ):
void;  
```  

Creates a 4x4 matrix with the given arguments in row-major order. If no
arguments are provided, the constructor initializes the Matrix4 to the 4x4 <a
href="https://en.wikipedia.org/wiki/Identity_matrix">identity matrix</a>.

## Properties

### elements

  
  
```ts  
elements: Array;  
```  

A <a href="https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order">column-major</a> list of matrix values.

## Methods

### clone

  
  
```ts  
function clone( ): Matrix4;  
```  

Creates a new Matrix4 with identical [.elements](#elements) to this one.

### compose

  
  
```ts  
function compose( position: Vector3, quaternion: Quaternion, scale: Vector3 ):
this;  
```  

Sets this matrix to the transformation composed of
[position](en\math\Vector3.html), [quaternion](en\math\Quaternion.html) and
[scale](en\math\Vector3.html).

### copy

  
  
```ts  
function copy( m: Matrix4 ): this;  
```  

Copies the [.elements](#elements) of matrix [.atrix4](#atrix4) into this
matrix.

### copyPosition

  
  
```ts  
function copyPosition( m: Matrix4 ): this;  
```  

Copies the translation component of the supplied matrix
[m](en\math\Matrix4.html) into this matrix's translation component.

### decompose

  
  
```ts  
function decompose( position: Vector3, quaternion: Quaternion, scale: Vector3
): this;  
```  

Decomposes this matrix into its [position](en\math\Vector3.html),
[quaternion](en\math\Quaternion.html) and [scale](en\math\Vector3.html)
components.  
  
Note: Not all matrices are decomposable in this way. For example, if an object
has a non-uniformly scaled parent, then the object's world matrix may not be
decomposable, and this method may not be appropriate.

### determinant

  
  
```ts  
function determinant( ): Float;  
```  

Computes and returns the <a
href="https://en.wikipedia.org/wiki/Determinant">determinant</a> of this
matrix.  
  
Based on the method outlined <a
href="http://www.euclideanspace.com/maths/algebra/matrix/functions/inverse/fourD/index.html">here</a>.

### equals

  
  
```ts  
function equals( m: Matrix4 ): Boolean;  
```  

Return true if this matrix and [m](en\math\Matrix4.html) are equal.

### extractBasis

  
  
```ts  
function extractBasis( xAxis: Vector3, yAxis: Vector3, zAxis: Vector3 ): this;  
```  

Extracts the <a
href="https://en.wikipedia.org/wiki/Basis_(linear_algebra)">basis</a> of this
matrix into the three axis vectors provided. If this matrix is:  
```ts  
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p  
```  
then the [xAxis](en\math\Vector3.html), [yAxis](en\math\Vector3.html),
[zAxis](en\math\Vector3.html) will be set to:  
```ts  
xAxis = (a, e, i) yAxis = (b, f, j) zAxis = (c, g, k)  
```  

### extractRotation

  
  
```ts  
function extractRotation( m: Matrix4 ): this;  
```  

Extracts the rotation component of the supplied matrix
[m](en\math\Matrix4.html) into this matrix's rotation component.

### fromArray

  
  
```ts  
function fromArray( array: Array, offset: Integer ): this;  
```  

[array](#) - the array to read the elements from.  
[offset](#) - ( optional ) offset into the array. Default is 0.  
  
Sets the elements of this matrix based on an [array](#) in <a
href="https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order">column-major</a> format.

### invert

  
  
```ts  
function invert( ): this;  
```  

Inverts this matrix, using the <a
href="https://en.wikipedia.org/wiki/Invertible_matrix#Analytic_solution">analytic
method</a>. You can not invert with a determinant of zero. If you attempt
this, the method produces a zero matrix instead.

### getMaxScaleOnAxis

  
  
```ts  
function getMaxScaleOnAxis( ): Float;  
```  

Gets the maximum scale value of the 3 axes.

### identity

  
  
```ts  
function identity( ): this;  
```  

Resets this matrix to the <a
href="https://en.wikipedia.org/wiki/Identity_matrix">identity matrix</a>.

### lookAt

  
  
```ts  
function lookAt( eye: Vector3, target: Vector3, up: Vector3 ): this;  
```  

Constructs a rotation matrix, looking from [eye](en\math\Vector3.html) towards
[target](en\math\Vector3.html) oriented by the [up](en\math\Vector3.html)
vector.

### makeRotationAxis

  
  
```ts  
function makeRotationAxis( axis: Vector3, theta: Float ): this;  
```  

[axis](en\math\Vector3.html) — Rotation axis, should be normalized.  
[theta](#) — Rotation angle in radians.  
  
Sets this matrix as rotation transform around [axis](en\math\Vector3.html) by
[theta](#) radians.  
This is a somewhat controversial but mathematically sound alternative to
rotating via [Quaternions](en\math\Quaternion.html). See the discussion <a
href="https://www.gamedev.net/articles/programming/math-and-physics/do-we-
really-need-quaternions-r1199">here</a>.

### makeBasis

  
  
```ts  
function makeBasis( xAxis: Vector3, yAxis: Vector3, zAxis: Vector3 ): this;  
```  

Set this to the <a
href="https://en.wikipedia.org/wiki/Basis_(linear_algebra)">basis</a> matrix
consisting of the three provided basis vectors:  
```ts  
xAxis.x, yAxis.x, zAxis.x, 0, xAxis.y, yAxis.y, zAxis.y, 0, xAxis.z, yAxis.z,
zAxis.z, 0, 0, 0, 0, 1  
```  

### makePerspective

  
  
```ts  
function makePerspective( left: Float, right: Float, top: Float, bottom:
Float, near: Float, far: Float ): this;  
```  

Creates a <a
href="https://en.wikipedia.org/wiki/3D_projection#Perspective_projection">perspective
projection</a> matrix. This is used internally by
[PerspectiveCamera.updateProjectionMatrix](#)()

### makeOrthographic

  
  
```ts  
function makeOrthographic( left: Float, right: Float, top: Float, bottom:
Float, near: Float, far: Float ): this;  
```  

Creates an <a
href="https://en.wikipedia.org/wiki/Orthographic_projection">orthographic
projection</a> matrix. This is used internally by
[OrthographicCamera.updateProjectionMatrix](#)().

### makeRotationFromEuler

  
  
```ts  
function makeRotationFromEuler( euler: Euler ): this;  
```  

Sets the rotation component (the upper left 3x3 matrix) of this matrix to the
rotation specified by the given [Euler Angle](en\math\Euler.html). The rest of
the matrix is set to the identity. Depending on the [order](#) of the
[euler](en\math\Euler.html), there are six possible outcomes. See <a
href="https://en.wikipedia.org/wiki/Euler_angles#Rotation_matrix">this
page</a> for a complete list.

### makeRotationFromQuaternion

  
  
```ts  
function makeRotationFromQuaternion( q: Quaternion ): this;  
```  

Sets the rotation component of this matrix to the rotation specified by
[q](en\math\Quaternion.html), as outlined <a
href="https://en.wikipedia.org/wiki/Rotation_matrix#Quaternion">here</a>. The
rest of the matrix is set to the identity. So, given
[q](en\math\Quaternion.html) = w + xi + yj + zk, the resulting matrix will be:  
```ts  
1-2y²-2z² 2xy-2zw 2xz+2yw 0 2xy+2zw 1-2x²-2z² 2yz-2xw 0 2xz-2yw 2yz+2xw
1-2x²-2y² 0 0 0 0 1  
```  

### makeRotationX

  
  
```ts  
function makeRotationX( theta: Float ): this;  
```  

[theta](#) — Rotation angle in radians.  
  
Sets this matrix as a rotational transformation around the X axis by
[theta](#) (θ) radians. The resulting matrix will be:  
```ts  
1 0 0 0 0 cos(θ) -sin(θ) 0 0 sin(θ) cos(θ) 0 0 0 0 1  
```  

### makeRotationY

  
  
```ts  
function makeRotationY( theta: Float ): this;  
```  

[theta](#) — Rotation angle in radians.  
  
Sets this matrix as a rotational transformation around the Y axis by
[theta](#) (θ) radians. The resulting matrix will be:  
```ts  
cos(θ) 0 sin(θ) 0 0 1 0 0 -sin(θ) 0 cos(θ) 0 0 0 0 1  
```  

### makeRotationZ

  
  
```ts  
function makeRotationZ( theta: Float ): this;  
```  

[theta](#) — Rotation angle in radians.  
  
Sets this matrix as a rotational transformation around the Z axis by
[theta](#) (θ) radians. The resulting matrix will be:  
```ts  
cos(θ) -sin(θ) 0 0 sin(θ) cos(θ) 0 0 0 0 1 0 0 0 0 1  
```  

### makeScale

  
  
```ts  
function makeScale( x: Float, y: Float, z: Float ): this;  
```  

[x](#) - the amount to scale in the X axis.  
[y](#) - the amount to scale in the Y axis.  
[z](#) - the amount to scale in the Z axis.  
  
Sets this matrix as scale transform:  
```ts  
x, 0, 0, 0, 0, y, 0, 0, 0, 0, z, 0, 0, 0, 0, 1  
```  

### makeShear

  
  
```ts  
function makeShear( xy: Float, xz: Float, yx: Float, yz: Float, zx: Float, zy:
Float ): this;  
```  

[xy](#) - the amount to shear X by Y.  
[xz](#) - the amount to shear X by Z.  
[yx](#) - the amount to shear Y by X.  
[yz](#) - the amount to shear Y by Z.  
[zx](#) - the amount to shear Z by X.  
[zy](#) - the amount to shear Z by Y.  
  
Sets this matrix as a shear transform:  
```ts  
1, yx, zx, 0, xy, 1, zy, 0, xz, yz, 1, 0, 0, 0, 0, 1  
```  

### makeTranslation

  
  
```ts  
function makeTranslation( v: Vector3 ): this;  
```  

### makeTranslation

  
  
```ts  
function makeTranslation( x: Float, y: Float, z: Float ): this;  
```  

Sets this matrix as a translation transform from vector
[v](en\math\Vector3.html), or numbers [x](#), [y](#) and [z](#):  
```ts  
1, 0, 0, x, 0, 1, 0, y, 0, 0, 1, z, 0, 0, 0, 1  
```  

### multiply

  
  
```ts  
function multiply( m: Matrix4 ): this;  
```  

Post-multiplies this matrix by [m](en\math\Matrix4.html).

### multiplyMatrices

  
  
```ts  
function multiplyMatrices( a: Matrix4, b: Matrix4 ): this;  
```  

Sets this matrix to [a](en\math\Matrix4.html) x [b](en\math\Matrix4.html).

### multiplyScalar

  
  
```ts  
function multiplyScalar( s: Float ): this;  
```  

Multiplies every component of the matrix by a scalar value [s](#).

### premultiply

  
  
```ts  
function premultiply( m: Matrix4 ): this;  
```  

Pre-multiplies this matrix by [m](en\math\Matrix4.html).

### scale

  
  
```ts  
function scale( v: Vector3 ): this;  
```  

Multiplies the columns of this matrix by vector [v](en\math\Vector3.html).

### set

  
  
```ts  
function set( n11: Float, n12: Float, n13: Float, n14: Float, n21: Float, n22:
Float, n23: Float, n24: Float, n31: Float, n32: Float, n33: Float, n34: Float,
n41: Float, n42: Float, n43: Float, n44: Float ): this;  
```  

Set the [.elements](#elements) of this matrix to the supplied row-major values
[.loat](#loat), [.loat](#loat), ... [.loat](#loat).

### setFromMatrix3

  
  
```ts  
function setFromMatrix3( m: Matrix3 ): this;  
```  

Set the upper 3x3 elements of this matrix to the values of the Matrix3
[m](en\math\Matrix3.html).

### setPosition

  
  
```ts  
function setPosition( v: Vector3 ): this;  
```  

### setPosition

  
  
```ts  
function setPosition( x: Float, y: Float, z: Float ): this;  
```  

Sets the position component for this matrix from vector
[v](en\math\Vector3.html), without affecting the rest of the matrix - i.e. if
the matrix is currently:  
```ts  
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p  
```  
This becomes:  
```ts  
a, b, c, v.x, e, f, g, v.y, i, j, k, v.z, m, n, o, p  
```  

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - (optional) array to store the resulting vector in.  
[offset](#) - (optional) offset in the array at which to put the result.  
  
Writes the elements of this matrix to an array in <a
href="https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order">column-major</a> format.

### transpose

  
  
```ts  
function transpose( ): this;  
```  

<a href="https://en.wikipedia.org/wiki/Transpose">Transposes</a> this matrix.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Matrix4.js">src/math/Matrix4.js</a>

