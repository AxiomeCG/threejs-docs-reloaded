# [name]

A geometric triangle as defined by three [page:Vector3 Vector3s] representing
its three corners.

## Constructor

### [name]( [param:Vector3 a], [param:Vector3 b], [param:Vector3 c] )

[page:Vector3 a] - the first corner of the triangle. Default is a
[page:Vector3] at `(0, 0, 0)`.  
[page:Vector3 b] - the second corner of the triangle. Default is a
[page:Vector3] at `(0, 0, 0)`.  
[page:Vector3 c] - the final corner of the triangle. Default is a
[page:Vector3] at `(0, 0, 0)`.  
  
Creates a new [name].

## Properties

### <br/> Vector3 a; <br/>

The first corner of the triangle. Default is a [page:Vector3] at `(0, 0, 0)`.

### <br/> Vector3 b; <br/>

The second corner of the triangle. Default is a [page:Vector3] at `(0, 0, 0)`.

### <br/> Vector3 c; <br/>

The final corner of the triangle. Default is a [page:Vector3] at `(0, 0, 0)`.

## Methods

### [method:Triangle clone]()

Returns a new triangle with the same [page:.a a], [page:.b b] and [page:.c c]
properties as this one.

###  [method:Vector3 closestPointToPoint]( [param:Vector3 point],
[param:Vector3 target] )

[page:Vector3 point] - [page:Vector3]  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the closest point on the triangle to [page:Vector3 point].

### [method:Boolean containsPoint]( [param:Vector3 point] )

[page:Vector3 point] - [page:Vector3] to check.  
  
Returns true if the passed point, when projected onto the plane of the
triangle, lies within the triangle.

### <br/> function copy( triangle: Triangle ): copy; <br/>

Copies the values of the passed triangles's [page:.a a], [page:.b b] and
[page:.c c] properties to this triangle.

### [method:Boolean equals]( [param:Triangle triangle] )

Returns true if the two triangles have identical [page:.a a], [page:.b b] and
[page:.c c] properties.

### [method:Float getArea]()

Return the area of the triangle.

###  [method:Vector3 getBarycoord]( [param:Vector3 point], [param:Vector3
target] )

[page:Vector3 point] - [page:Vector3]  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Return a [link:https://en.wikipedia.org/wiki/Barycentric_coordinate_system
barycentric coordinate] from the given vector.  
  
[link:http://commons.wikimedia.org/wiki/File:Barycentric_coordinates_1.png
Picture of barycentric coordinates]

### [method:Vector3 getMidpoint]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Calculate the midpoint of the triangle.

### [method:Vector3 getNormal]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Calculate the [link:https://en.wikipedia.org/wiki/Normal_(geometry) normal
vector] of the triangle.

### [method:Plane getPlane]( [param:Plane target] )

[page:Plane target] — the result will be copied into this Plane.  
  
Calculate a [page:Plane plane] based on the triangle. .

###  [method:Vector getInterpolation]( [param:Vector3 point], [param:Vector3
p1], [param:Vector3 p2], [param:Vector3 p3], [param:Vector v1], [param:Vector
v2], [param:Vector v3], [param:Vector target] )

[page:Vector3 point] - Position of interpolated point.  
[page:Vector3 p1] - Position of first vertex.  
[page:Vector3 p2] - Position of second vertex.  
[page:Vector3 p3] - Position of third vertex.  
[page:Vector v1] - Value of first vertex.  
[page:Vector v2] - Value of second vertex.  
[page:Vector v3] - Value of third vertex.  
[page:Vector target] — Result will be copied into this Vector.  
  
Returns the value barycentrically interpolated for the given point on the
triangle.

### [method:Boolean intersectsBox]( [param:Box3 box] )

[page:Box3 box] - Box to check for intersection against.  
  
Determines whether or not this triangle intersects [page:Box3 box].

### [method:Boolean isFrontFacing]( [param:Vector3 direction] )

[page:Vector3 direction] - The direction to test.  
  
Whether the triangle is oriented towards the given direction or not.

### <br/> function set( a: Vector3, b: Vector3, c: Vector3 ): set; <br/>

Sets the triangle's [page:.a a], [page:.b b] and [page:.c c] properties to the
passed [page:Vector3 vector3s].  
Please note that this method only copies the values from the given objects.

### <br/> function setFromAttributeAndIndices( attribute: BufferAttribute, i0:
Integer, i1: Integer, i2: Integer ): setFromAttributeAndIndices; <br/>

attribute - [page:BufferAttribute] of vertex data  
i0 - [page:Integer] index  
i1 - [page:Integer] index  
i2 - [page:Integer] index  
  
Sets the triangle's vertices from the buffer attribute vertex data.

### <br/> function setFromPointsAndIndices( points: Array, i0: Integer, i1:
Integer, i2: Integer ): setFromPointsAndIndices; <br/>

points - [page:Array] of [page:Vector3]s  
i0 - [page:Integer] index  
i1 - [page:Integer] index  
i2 - [page:Integer] index  
  
Sets the triangle's vectors to the vectors in the array.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

