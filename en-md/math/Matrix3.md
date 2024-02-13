# Matrix3

A class representing a 3x3
[link:https://en.wikipedia.org/wiki/Matrix_(mathematics) matrix].

## Code Example

  
```ts  
const m = new Matrix3();  
```  

## A Note on Row-Major and Column-Major Ordering

The constructor and [page:set]() method take arguments in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order row-major] order, while internally they are stored in the
[page:.elements elements] array in column-major order.  
  
This means that calling  
```ts  
m.set( 11, 12, 13, 21, 22, 23, 31, 32, 33 );  
```  
will result in the [page:.elements elements] array containing:  
```ts  
m.elements = [ 11, 21, 31, 12, 22, 32, 13, 23, 33 ];  
```  
and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and most
people are used to thinking about matrices in row-major order, the three.js
documentation shows matrices in row-major order. Just bear in mind that if you
are reading the source code, you'll have to take the
[link:https://en.wikipedia.org/wiki/Transpose transpose] of any matrices
outlined here to make sense of the calculations.

## Constructor

###  function Matrix3( n11: Number, n12: Number, n13: Number, n21: Number,
n22: Number, n22: Number, n31: Number, n32: Number, n33: Number ): void;

Creates a 3x3 matrix with the given arguments in row-major order. If no
arguments are provided, the constructor initializes the Matrix3 to the 3x3
[link:https://en.wikipedia.org/wiki/Identity_matrix identity matrix].

## Properties

###  Array elements;

A [link:https://en.wikipedia.org/wiki/Row-_and_column-major_order column-
major] list of matrix values.

## Methods

###  function clone( ): Matrix3;

Creates a new Matrix3 and with identical elements to this one.

###  function copy( m: Matrix3 ): this;

Copies the elements of matrix [page:Matrix3 m] into this matrix.

###  function determinant( ): Float;

Computes and returns the [link:https://en.wikipedia.org/wiki/Determinant
determinant] of this matrix.

###  function equals( m: Matrix3 ): Boolean;

Return true if this matrix and [page:Matrix3 m] are equal.

###  function extractBasis( xAxis: Vector3, yAxis: Vector3, zAxis: Vector3 ):
this;

Extracts the [link:https://en.wikipedia.org/wiki/Basis_(linear_algebra) basis]
of this matrix into the three axis vectors provided. If this matrix is:  
```ts  
a, b, c, d, e, f, g, h, i  
```  
then the [page:Vector3 xAxis], [page:Vector3 yAxis], [page:Vector3 zAxis] will
be set to:  
```ts  
xAxis = (a, d, g) yAxis = (b, e, h) zAxis = (c, f, i)  
```  

###  function fromArray( array: Array, offset: Integer ): this;

[page:Array array] - the array to read the elements from.  
[page:Integer offset] - (optional) index of first element in the array.
Default is `0`.  
  
Sets the elements of this matrix based on an array in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order column-major] format.

###  function invert( ): this;

Inverts this matrix, using the
[link:https://en.wikipedia.org/wiki/Invertible_matrix#Analytic_solution
analytic method]. You can not invert with a determinant of zero. If you
attempt this, the method produces a zero matrix instead.

###  function getNormalMatrix( m: Matrix4 ): this;

[page:Matrix4 m] - [page:Matrix4]  
  
Sets this matrix as the upper left 3x3 of the
[link:https://en.wikipedia.org/wiki/Normal_matrix normal matrix] of the passed
[page:Matrix4 matrix4]. The normal matrix is the
[link:https://en.wikipedia.org/wiki/Invertible_matrix inverse]
[link:https://en.wikipedia.org/wiki/Transpose transpose] of the matrix
[page:Matrix4 m].

###  function identity( ): this;

Resets this matrix to the 3x3 identity matrix:  
```ts  
1, 0, 0 0, 1, 0 0, 0, 1  
```  

###  function makeRotation( theta: Float ): this;

[page:Float theta] — Rotation angle in radians. Positive values rotate
counterclockwise.  
  
Sets this matrix as a 2D rotational transformation by [page:Float theta]
radians. The resulting matrix will be:  
```ts  
cos(θ) -sin(θ) 0 sin(θ) cos(θ) 0 0 0 1  
```  

###  function makeScale( x: Float, y: Float ): this;

[page:Float x] - the amount to scale in the X axis.  
[page:Float y] - the amount to scale in the Y axis.  
Sets this matrix as a 2D scale transform:  
```ts  
x, 0, 0, 0, y, 0, 0, 0, 1  
```  

###  function makeTranslation( v: Vector2 ): this;

###  function makeTranslation( x: Float, y: Float ): this;

[page:Vector2 v] a translation transform from vector.  
or  
[page:Float x] - the amount to translate in the X axis.  
[page:Float y] - the amount to translate in the Y axis.  
Sets this matrix as a 2D translation transform:  
```ts  
1, 0, x, 0, 1, y, 0, 0, 1  
```  

###  function multiply( m: Matrix3 ): this;

Post-multiplies this matrix by [page:Matrix3 m].

###  function multiplyMatrices( a: Matrix3, b: Matrix3 ): this;

Sets this matrix to [page:Matrix3 a] x [page:Matrix3 b].

###  function multiplyScalar( s: Float ): this;

Multiplies every component of the matrix by the scalar value *s*.

###  function rotate( theta: Float ): this;

Rotates this matrix by the given angle (in radians).

###  function scale( sx: Float, sy: Float ): this;

Scales this matrix with the given scalar values.

###  function set( n11: Float, n12: Float, n13: Float, n21: Float, n22: Float,
n23: Float, n31: Float, n32: Float, n33: Float ): this;

[page:Float n11] - value to put in row 1, col 1.  
[page:Float n12] - value to put in row 1, col 2.  
...  
...  
[page:Float n32] - value to put in row 3, col 2.  
[page:Float n33] - value to put in row 3, col 3.  
  
Sets the 3x3 matrix values to the given
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order row-major]
sequence of values.

###  function premultiply( m: Matrix3 ): this;

Pre-multiplies this matrix by [page:Matrix3 m].

###  function setFromMatrix4( m: Matrix4 ): this;

Set this matrix to the upper 3x3 matrix of the Matrix4 [page:Matrix4 m].

###  function setUvTransform( tx: Float, ty: Float, sx: Float, sy: Float,
rotation: Float, cx: Float, cy: Float ): this;

[page:Float tx] - offset x  
[page:Float ty] - offset y  
[page:Float sx] - repeat x  
[page:Float sy] - repeat y  
[page:Float rotation] - rotation, in radians. Positive values rotate
counterclockwise  
[page:Float cx] - center x of rotation  
[page:Float cy] - center y of rotation  
  
Sets the UV transform matrix from offset, repeat, rotation, and center.

###  function toArray( array: Array, offset: Integer ): Array;

[page:Array array] - (optional) array to store the resulting vector in. If not
given a new array will be created.  
[page:Integer offset] - (optional) offset in the array at which to put the
result.  
  
Writes the elements of this matrix to an array in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order column-major] format.

###  function translate( tx: Float, ty: Float ): this;

Translates this matrix by the given scalar values.

###  function transpose( ): this;

[link:https://en.wikipedia.org/wiki/Transpose Transposes] this matrix in
place.

###  function transposeIntoArray( array: Array ): this;

[page:Array array] - array to store the resulting vector in.  
  
[link:https://en.wikipedia.org/wiki/Transpose Transposes] this matrix into the
supplied array, and returns itself unchanged.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

