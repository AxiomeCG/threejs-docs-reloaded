# Matrix3

A class representing a 3x3 <a
href="https://en.wikipedia.org/wiki/Matrix_(mathematics)">matrix</a>.

## Code Example

  
```ts  
const m = new Matrix3();  
```  

## A Note on Row-Major and Column-Major Ordering

The constructor and [set](#)() method take arguments in <a
href="https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order">row-major</a> order, while internally they are stored in the
[.elements](#elements) array in column-major order.  
  
This means that calling  
```ts  
m.set( 11, 12, 13, 21, 22, 23, 31, 32, 33 );  
```  
will result in the [.elements](#elements) array containing:  
```ts  
m.elements = [ 11, 21, 31, 12, 22, 32, 13, 23, 33 ];  
```  
and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and most
people are used to thinking about matrices in row-major order, the three.js
documentation shows matrices in row-major order. Just bear in mind that if you
are reading the source code, you'll have to take the <a
href="https://en.wikipedia.org/wiki/Transpose">transpose</a> of any matrices
outlined here to make sense of the calculations.

## Constructor

### Matrix3

  
  
```ts  
function Matrix3( n11: Number, n12: Number, n13: Number, n21: Number, n22:
Number, n22: Number, n31: Number, n32: Number, n33: Number ): void;  
```  

Creates a 3x3 matrix with the given arguments in row-major order. If no
arguments are provided, the constructor initializes the Matrix3 to the 3x3 <a
href="https://en.wikipedia.org/wiki/Identity_matrix">identity matrix</a>.

## Properties

### elements

  
  
```ts  
elements: Array;  
```  

A <a href="https://en.wikipedia.org/wiki/Row-_and_column-major_order">column-
major</a> list of matrix values.

## Methods

### clone

  
  
```ts  
function clone( ): Matrix3;  
```  

Creates a new Matrix3 and with identical elements to this one.

### copy

  
  
```ts  
function copy( m: Matrix3 ): this;  
```  

Copies the elements of matrix [m](en\math\Matrix3.html) into this matrix.

### determinant

  
  
```ts  
function determinant( ): Float;  
```  

Computes and returns the <a
href="https://en.wikipedia.org/wiki/Determinant">determinant</a> of this
matrix.

### equals

  
  
```ts  
function equals( m: Matrix3 ): Boolean;  
```  

Return true if this matrix and [m](en\math\Matrix3.html) are equal.

### extractBasis

  
  
```ts  
function extractBasis( xAxis: Vector3, yAxis: Vector3, zAxis: Vector3 ): this;  
```  

Extracts the <a
href="https://en.wikipedia.org/wiki/Basis_(linear_algebra)">basis</a> of this
matrix into the three axis vectors provided. If this matrix is:  
```ts  
a, b, c, d, e, f, g, h, i  
```  
then the [xAxis](en\math\Vector3.html), [yAxis](en\math\Vector3.html),
[zAxis](en\math\Vector3.html) will be set to:  
```ts  
xAxis = (a, d, g) yAxis = (b, e, h) zAxis = (c, f, i)  
```  

### fromArray

  
  
```ts  
function fromArray( array: Array, offset: Integer ): this;  
```  

[array](#) - the array to read the elements from.  
[offset](#) - (optional) index of first element in the array. Default is `0`.  
  
Sets the elements of this matrix based on an array in <a
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

### getNormalMatrix

  
  
```ts  
function getNormalMatrix( m: Matrix4 ): this;  
```  

[m](en\math\Matrix4.html) - [Matrix4](en\math\Matrix4.html)  
  
Sets this matrix as the upper left 3x3 of the <a
href="https://en.wikipedia.org/wiki/Normal_matrix">normal matrix</a> of the
passed [matrix4](en\math\Matrix4.html). The normal matrix is the <a
href="https://en.wikipedia.org/wiki/Invertible_matrix">inverse</a> <a
href="https://en.wikipedia.org/wiki/Transpose">transpose</a> of the matrix
[m](en\math\Matrix4.html).

### identity

  
  
```ts  
function identity( ): this;  
```  

Resets this matrix to the 3x3 identity matrix:  
```ts  
1, 0, 0 0, 1, 0 0, 0, 1  
```  

### makeRotation

  
  
```ts  
function makeRotation( theta: Float ): this;  
```  

[theta](#) — Rotation angle in radians. Positive values rotate
counterclockwise.  
  
Sets this matrix as a 2D rotational transformation by [theta](#) radians. The
resulting matrix will be:  
```ts  
cos(θ) -sin(θ) 0 sin(θ) cos(θ) 0 0 0 1  
```  

### makeScale

  
  
```ts  
function makeScale( x: Float, y: Float ): this;  
```  

[x](#) - the amount to scale in the X axis.  
[y](#) - the amount to scale in the Y axis.  
Sets this matrix as a 2D scale transform:  
```ts  
x, 0, 0, 0, y, 0, 0, 0, 1  
```  

### makeTranslation

  
  
```ts  
function makeTranslation( v: Vector2 ): this;  
```  

### makeTranslation

  
  
```ts  
function makeTranslation( x: Float, y: Float ): this;  
```  

[v](en\math\Vector2.html) a translation transform from vector.  
or  
[x](#) - the amount to translate in the X axis.  
[y](#) - the amount to translate in the Y axis.  
Sets this matrix as a 2D translation transform:  
```ts  
1, 0, x, 0, 1, y, 0, 0, 1  
```  

### multiply

  
  
```ts  
function multiply( m: Matrix3 ): this;  
```  

Post-multiplies this matrix by [m](en\math\Matrix3.html).

### multiplyMatrices

  
  
```ts  
function multiplyMatrices( a: Matrix3, b: Matrix3 ): this;  
```  

Sets this matrix to [a](en\math\Matrix3.html) x [b](en\math\Matrix3.html).

### multiplyScalar

  
  
```ts  
function multiplyScalar( s: Float ): this;  
```  

Multiplies every component of the matrix by the scalar value *s*.

### rotate

  
  
```ts  
function rotate( theta: Float ): this;  
```  

Rotates this matrix by the given angle (in radians).

### scale

  
  
```ts  
function scale( sx: Float, sy: Float ): this;  
```  

Scales this matrix with the given scalar values.

### set

  
  
```ts  
function set( n11: Float, n12: Float, n13: Float, n21: Float, n22: Float, n23:
Float, n31: Float, n32: Float, n33: Float ): this;  
```  

[n11](#) - value to put in row 1, col 1.  
[n12](#) - value to put in row 1, col 2.  
...  
...  
[n32](#) - value to put in row 3, col 2.  
[n33](#) - value to put in row 3, col 3.  
  
Sets the 3x3 matrix values to the given <a
href="https://en.wikipedia.org/wiki/Row-_and_column-major_order">row-major</a>
sequence of values.

### premultiply

  
  
```ts  
function premultiply( m: Matrix3 ): this;  
```  

Pre-multiplies this matrix by [m](en\math\Matrix3.html).

### setFromMatrix4

  
  
```ts  
function setFromMatrix4( m: Matrix4 ): this;  
```  

Set this matrix to the upper 3x3 matrix of the Matrix4
[m](en\math\Matrix4.html).

### setUvTransform

  
  
```ts  
function setUvTransform( tx: Float, ty: Float, sx: Float, sy: Float, rotation:
Float, cx: Float, cy: Float ): this;  
```  

[tx](#) - offset x  
[ty](#) - offset y  
[sx](#) - repeat x  
[sy](#) - repeat y  
[rotation](#) - rotation, in radians. Positive values rotate counterclockwise  
[cx](#) - center x of rotation  
[cy](#) - center y of rotation  
  
Sets the UV transform matrix from offset, repeat, rotation, and center.

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - (optional) array to store the resulting vector in. If not given a
new array will be created.  
[offset](#) - (optional) offset in the array at which to put the result.  
  
Writes the elements of this matrix to an array in <a
href="https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order">column-major</a> format.

### translate

  
  
```ts  
function translate( tx: Float, ty: Float ): this;  
```  

Translates this matrix by the given scalar values.

### transpose

  
  
```ts  
function transpose( ): this;  
```  

<a href="https://en.wikipedia.org/wiki/Transpose">Transposes</a> this matrix
in place.

### transposeIntoArray

  
  
```ts  
function transposeIntoArray( array: Array ): this;  
```  

[array](#) - array to store the resulting vector in.  
  
<a href="https://en.wikipedia.org/wiki/Transpose">Transposes</a> this matrix
into the supplied array, and returns itself unchanged.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Matrix3.js">src/math/Matrix3.js</a>

