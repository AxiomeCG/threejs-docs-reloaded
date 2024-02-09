# [name]

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
m.set( 11, 12, 13,  
21, 22, 23,  
31, 32, 33 );  
```  
will result in the [page:.elements elements] array containing:  
```ts  
m.elements = [ 11, 21, 31,  
12, 22, 32,  
13, 23, 33 ];  
```  
and internally all calculations are performed using column-major ordering.
However, as the actual ordering makes no difference mathematically and most
people are used to thinking about matrices in row-major order, the three.js
documentation shows matrices in row-major order. Just bear in mind that if you
are reading the source code, you'll have to take the
[link:https://en.wikipedia.org/wiki/Transpose transpose] of any matrices
outlined here to make sense of the calculations.

## Constructor

### [name]( [param:Number n11], [param:Number n12], [param:Number n13],
[param:Number n21], [param:Number n22], [param:Number n22], [param:Number
n31], [param:Number n32], [param:Number n33] )

Creates a 3x3 matrix with the given arguments in row-major order. If no
arguments are provided, the constructor initializes the [name] to the 3x3
[link:https://en.wikipedia.org/wiki/Identity_matrix identity matrix].

## Properties

### <br/> Array elements; <br/>

A [link:https://en.wikipedia.org/wiki/Row-_and_column-major_order column-
major] list of matrix values.

## Methods

### [method:Matrix3 clone]()

Creates a new Matrix3 and with identical elements to this one.

### <br/> function copy( m: Matrix3 ): copy; <br/>

Copies the elements of matrix [page:Matrix3 m] into this matrix.

### [method:Float determinant]()

Computes and returns the [link:https://en.wikipedia.org/wiki/Determinant
determinant] of this matrix.

### [method:Boolean equals]( [param:Matrix3 m] )

Return true if this matrix and [page:Matrix3 m] are equal.

### <br/> function extractBasis( xAxis: Vector3, yAxis: Vector3, zAxis:
Vector3 ): extractBasis; <br/>

Extracts the [link:https://en.wikipedia.org/wiki/Basis_(linear_algebra) basis]
of this matrix into the three axis vectors provided. If this matrix is:  
```ts  
a, b, c,  
d, e, f,  
g, h, i  
```  
then the [page:Vector3 xAxis], [page:Vector3 yAxis], [page:Vector3 zAxis] will
be set to:  
```ts  
xAxis = (a, d, g)  
yAxis = (b, e, h)  
zAxis = (c, f, i)  
```  

### <br/> function fromArray( array: Array, offset: Integer ): fromArray;
<br/>

[page:Array array] - the array to read the elements from.  
[page:Integer offset] - (optional) index of first element in the array.
Default is `0`.  
  
Sets the elements of this matrix based on an array in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order column-major] format.

### <br/> function invert( ): invert; <br/>

Inverts this matrix, using the
[link:https://en.wikipedia.org/wiki/Invertible_matrix#Analytic_solution
analytic method]. You can not invert with a determinant of zero. If you
attempt this, the method produces a zero matrix instead.

### <br/> function getNormalMatrix( m: Matrix4 ): getNormalMatrix; <br/>

[page:Matrix4 m] - [page:Matrix4]  
  
Sets this matrix as the upper left 3x3 of the
[link:https://en.wikipedia.org/wiki/Normal_matrix normal matrix] of the passed
[page:Matrix4 matrix4]. The normal matrix is the
[link:https://en.wikipedia.org/wiki/Invertible_matrix inverse]
[link:https://en.wikipedia.org/wiki/Transpose transpose] of the matrix
[page:Matrix4 m].

### <br/> function identity( ): identity; <br/>

Resets this matrix to the 3x3 identity matrix:  
```ts  
1, 0, 0  
0, 1, 0  
0, 0, 1 ```  

### <br/> function makeRotation( theta: Float ): makeRotation; <br/>

[page:Float theta] — Rotation angle in radians. Positive values rotate
counterclockwise.  
  
Sets this matrix as a 2D rotational transformation by [page:Float theta]
radians. The resulting matrix will be:  
```ts  
cos(θ) -sin(θ) 0  
sin(θ) cos(θ) 0  
0 0 1  
```  

### <br/> function makeScale( x: Float, y: Float ): makeScale; <br/>

[page:Float x] - the amount to scale in the X axis.  
[page:Float y] - the amount to scale in the Y axis.  
Sets this matrix as a 2D scale transform:  
```ts  
x, 0, 0,  
0, y, 0,  
0, 0, 1 ```  

### <br/> function makeTranslation( v: Vector2 ): makeTranslation; <br/>

### <br/> function makeTranslation( x: Float, y: Float ): makeTranslation;
<br/>

[page:Vector2 v] a translation transform from vector.  
or  
[page:Float x] - the amount to translate in the X axis.  
[page:Float y] - the amount to translate in the Y axis.  
Sets this matrix as a 2D translation transform:  
```ts  
1, 0, x,  
0, 1, y,  
0, 0, 1 ```  

### <br/> function multiply( m: Matrix3 ): multiply; <br/>

Post-multiplies this matrix by [page:Matrix3 m].

### <br/> function multiplyMatrices( a: Matrix3, b: Matrix3 ):
multiplyMatrices; <br/>

Sets this matrix to [page:Matrix3 a] x [page:Matrix3 b].

### <br/> function multiplyScalar( s: Float ): multiplyScalar; <br/>

Multiplies every component of the matrix by the scalar value *s*.

### <br/> function rotate( theta: Float ): rotate; <br/>

Rotates this matrix by the given angle (in radians).

### <br/> function scale( sx: Float, sy: Float ): scale; <br/>

Scales this matrix with the given scalar values.

### <br/> function set( n11: Float, n12: Float, n13: Float, n21: Float, n22:
Float, n23: Float, n31: Float, n32: Float, n33: Float ): set; <br/>

[page:Float n11] - value to put in row 1, col 1.  
[page:Float n12] - value to put in row 1, col 2.  
...  
...  
[page:Float n32] - value to put in row 3, col 2.  
[page:Float n33] - value to put in row 3, col 3.  
  
Sets the 3x3 matrix values to the given
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order row-major]
sequence of values.

### <br/> function premultiply( m: Matrix3 ): premultiply; <br/>

Pre-multiplies this matrix by [page:Matrix3 m].

### <br/> function setFromMatrix4( m: Matrix4 ): setFromMatrix4; <br/>

Set this matrix to the upper 3x3 matrix of the Matrix4 [page:Matrix4 m].

### <br/> function setUvTransform( tx: Float, ty: Float, sx: Float, sy: Float,
rotation: Float, cx: Float, cy: Float ): setUvTransform; <br/>

[page:Float tx] - offset x  
[page:Float ty] - offset y  
[page:Float sx] - repeat x  
[page:Float sy] - repeat y  
[page:Float rotation] - rotation, in radians. Positive values rotate
counterclockwise  
[page:Float cx] - center x of rotation  
[page:Float cy] - center y of rotation  
  
Sets the UV transform matrix from offset, repeat, rotation, and center.

###  [method:Array toArray]( [param:Array array], [param:Integer offset] )

[page:Array array] - (optional) array to store the resulting vector in. If not
given a new array will be created.  
[page:Integer offset] - (optional) offset in the array at which to put the
result.  
  
Writes the elements of this matrix to an array in
[link:https://en.wikipedia.org/wiki/Row-_and_column-major_order#Column-
major_order column-major] format.

### <br/> function translate( tx: Float, ty: Float ): translate; <br/>

Translates this matrix by the given scalar values.

### <br/> function transpose( ): transpose; <br/>

[link:https://en.wikipedia.org/wiki/Transpose Transposes] this matrix in
place.

### <br/> function transposeIntoArray( array: Array ): transposeIntoArray;
<br/>

[page:Array array] - array to store the resulting vector in.  
  
[link:https://en.wikipedia.org/wiki/Transpose Transposes] this matrix into the
supplied array, and returns itself unchanged.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

