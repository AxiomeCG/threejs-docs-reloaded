# Triangle

A geometric triangle as defined by three [Vector3s](en\math\Vector3.html)
representing its three corners.

## Constructor

### Triangle

  
  
```ts  
function Triangle( a: Vector3, b: Vector3, c: Vector3 ): void;  
```  

[a](en\math\Vector3.html) - the first corner of the triangle. Default is a
[Vector3](en\math\Vector3.html) at `(0, 0, 0)`.  
[b](en\math\Vector3.html) - the second corner of the triangle. Default is a
[Vector3](en\math\Vector3.html) at `(0, 0, 0)`.  
[c](en\math\Vector3.html) - the final corner of the triangle. Default is a
[Vector3](en\math\Vector3.html) at `(0, 0, 0)`.  
  
Creates a new Triangle.

## Properties

### a

  
  
```ts  
a: Vector3;  
```  

The first corner of the triangle. Default is a [Vector3](en\math\Vector3.html)
at `(0, 0, 0)`.

### b

  
  
```ts  
b: Vector3;  
```  

The second corner of the triangle. Default is a
[Vector3](en\math\Vector3.html) at `(0, 0, 0)`.

### c

  
  
```ts  
c: Vector3;  
```  

The final corner of the triangle. Default is a [Vector3](en\math\Vector3.html)
at `(0, 0, 0)`.

## Methods

### clone

  
  
```ts  
function clone( ): Triangle;  
```  

Returns a new triangle with the same [.a](#a), [.b](#b) and [.c](#c)
properties as this one.

### closestPointToPoint

  
  
```ts  
function closestPointToPoint( point: Vector3, target: Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html)  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns the closest point on the triangle to [point](en\math\Vector3.html).

### containsPoint

  
  
```ts  
function containsPoint( point: Vector3 ): Boolean;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to check.  
  
Returns true if the passed point, when projected onto the plane of the
triangle, lies within the triangle.

### copy

  
  
```ts  
function copy( triangle: Triangle ): this;  
```  

Copies the values of the passed triangles's [.a](#a), [.b](#b) and [.c](#c)
properties to this triangle.

### equals

  
  
```ts  
function equals( triangle: Triangle ): Boolean;  
```  

Returns true if the two triangles have identical [.a](#a), [.b](#b) and
[.c](#c) properties.

### getArea

  
  
```ts  
function getArea( ): Float;  
```  

Return the area of the triangle.

### getBarycoord

  
  
```ts  
function getBarycoord( point: Vector3, target: Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html)  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Return a <a
href="https://en.wikipedia.org/wiki/Barycentric_coordinate_system">barycentric
coordinate</a> from the given vector.  
  
<a
href="http://commons.wikimedia.org/wiki/File:Barycentric_coordinates_1.png">Picture
of barycentric coordinates</a>

### getMidpoint

  
  
```ts  
function getMidpoint( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Calculate the midpoint of the triangle.

### getNormal

  
  
```ts  
function getNormal( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Calculate the <a href="https://en.wikipedia.org/wiki/Normal_(geometry)">normal
vector</a> of the triangle.

### getPlane

  
  
```ts  
function getPlane( target: Plane ): Plane;  
```  

[target](en\math\Plane.html) — the result will be copied into this Plane.  
  
Calculate a [plane](en\math\Plane.html) based on the triangle. .

### getInterpolation

  
  
```ts  
function getInterpolation( point: Vector3, p1: Vector3, p2: Vector3, p3:
Vector3, v1: Vector, v2: Vector, v3: Vector, target: Vector ): Vector;  
```  

[point](en\math\Vector3.html) - Position of interpolated point.  
[p1](en\math\Vector3.html) - Position of first vertex.  
[p2](en\math\Vector3.html) - Position of second vertex.  
[p3](en\math\Vector3.html) - Position of third vertex.  
[v1](#) - Value of first vertex.  
[v2](#) - Value of second vertex.  
[v3](#) - Value of third vertex.  
[target](#) — Result will be copied into this Vector.  
  
Returns the value barycentrically interpolated for the given point on the
triangle.

### intersectsBox

  
  
```ts  
function intersectsBox( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - Box to check for intersection against.  
  
Determines whether or not this triangle intersects [box](en\math\Box3.html).

### isFrontFacing

  
  
```ts  
function isFrontFacing( direction: Vector3 ): Boolean;  
```  

[direction](en\math\Vector3.html) - The direction to test.  
  
Whether the triangle is oriented towards the given direction or not.

### set

  
  
```ts  
function set( a: Vector3, b: Vector3, c: Vector3 ): this;  
```  

Sets the triangle's [.a](#a), [.b](#b) and [.c](#c) properties to the passed
[.ector3](#ector3).  
Please note that this method only copies the values from the given objects.

### setFromAttributeAndIndices

  
  
```ts  
function setFromAttributeAndIndices( attribute: BufferAttribute, i0: Integer,
i1: Integer, i2: Integer ): this;  
```  

attribute - [BufferAttribute](en\core\BufferAttribute.html) of vertex data  
i0 - [Integer](#) index  
i1 - [Integer](#) index  
i2 - [Integer](#) index  
  
Sets the triangle's vertices from the buffer attribute vertex data.

### setFromPointsAndIndices

  
  
```ts  
function setFromPointsAndIndices( points: Array, i0: Integer, i1: Integer, i2:
Integer ): this;  
```  

points - [Array](#) of [Vector3](en\math\Vector3.html)s  
i0 - [Integer](#) index  
i1 - [Integer](#) index  
i2 - [Integer](#) index  
  
Sets the triangle's vectors to the vectors in the array.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Triangle.js">src/math/Triangle.js</a>

