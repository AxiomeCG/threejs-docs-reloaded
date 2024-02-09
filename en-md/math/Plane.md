# [name]

A two dimensional surface that extends infinitely in 3d space, represented in
[link:http://mathworld.wolfram.com/HessianNormalForm.html Hessian normal form]
by a unit length normal vector and a constant.

## Constructor

### [name]( [param:Vector3 normal], [param:Float constant] )

[page:Vector3 normal] - (optional) a unit length [page:Vector3] defining the
normal of the plane. Default is `(1, 0, 0)`.  
[page:Float constant] - (optional) the signed distance from the origin to the
plane. Default is `0`.

## Properties

### <br/> Boolean isPlane; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Vector3 normal; <br/>

### <br/> Float constant; <br/>

## Methods

### <br/> function applyMatrix4( matrix: Matrix4, optionalNormalMatrix:
Matrix3 ): applyMatrix4; <br/>

[page:Matrix4 matrix] - the [Page:Matrix4] to apply.  
[page:Matrix3 optionalNormalMatrix] - (optional) pre-computed normal
[Page:Matrix3] of the Matrix4 being applied.  
  
Apply a Matrix4 to the plane. The matrix must be an affine, homogeneous
transform.  
If supplying an [page:Matrix3 optionalNormalMatrix], it can be created like
so:  
```ts  
const optionalNormalMatrix = new THREE.Matrix3().getNormalMatrix( matrix );  
```  

### [method:Plane clone]()

Returns a new plane with the same [page:.normal normal] and [page:.constant
constant] as this one.

### [method:Vector3 coplanarPoint]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a [page:Vector3] coplanar to the plane, by calculating the projection
of the normal vector at the origin onto the plane.

### <br/> function copy( plane: Plane ): copy; <br/>

Copies the values of the passed plane's [page:.normal normal] and
[page:.constant constant] properties to this plane.

### [method:Float distanceToPoint]( [param:Vector3 point] )

Returns the signed distance from the [page:Vector3 point] to the plane.

### [method:Float distanceToSphere]( [param:Sphere sphere] )

Returns the signed distance from the [page:Sphere sphere] to the plane.

### [method:Boolean equals]( [param:Plane plane] )

Checks to see if two planes are equal (their [page:.normal normal] and
[page:.constant constant] properties match).

###  [method:Vector3 intersectLine]( [param:Line3 line], [param:Vector3
target] )

[page:Line3 line] - the [page:Line3] to check for intersection.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the intersection point of the passed line and the plane. Returns null
if the line does not intersect. Returns the line's starting point if the line
is coplanar with the plane.

### [method:Boolean intersectsBox]( [param:Box3 box] )

[page:Box3 box] - the [page:Box3] to check for intersection.  
  
Determines whether or not this plane intersects [page:Box3 box].

### [method:Boolean intersectsLine]( [param:Line3 line] )

[page:Line3 line] - the [page:Line3] to check for intersection.  
  
Tests whether a line segment intersects with (passes through) the plane.

### [method:Boolean intersectsSphere]( [param:Sphere sphere] )

[page:Sphere sphere] - the [page:Sphere] to check for intersection.  
  
Determines whether or not this plane intersects [page:Sphere sphere].

### <br/> function negate( ): negate; <br/>

Negates both the normal vector and the constant.

### <br/> function normalize( ): normalize; <br/>

Normalizes the [page:.normal normal] vector, and adjusts the [page:.constant
constant] value accordingly.

###  [method:Vector3 projectPoint]( [param:Vector3 point], [param:Vector3
target] )

[page:Vector3 point] - the [page:Vector3] to project onto the plane.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Projects a [page:Vector3 point] onto the plane.

### <br/> function set( normal: Vector3, constant: Float ): set; <br/>

[page:Vector3 normal] - a unit length [page:Vector3] defining the normal of
the plane.  
[page:Float constant] - the signed distance from the origin to the plane.
Default is `0`.  
  
Sets this plane's [page:.normal normal] and [page:.constant constant]
properties by copying the values from the given normal.

### <br/> function setComponents( x: Float, y: Float, z: Float, w: Float ):
setComponents; <br/>

[page:Float x] - x value of the unit length normal vector.  
[page:Float y] - y value of the unit length normal vector.  
[page:Float z] - z value of the unit length normal vector.  
[page:Float w] - the value of the plane's [page:.constant constant] property.  
  
Set the individual components that define the plane.

### <br/> function setFromCoplanarPoints( a: Vector3, b: Vector3, c: Vector3
): setFromCoplanarPoints; <br/>

[page:Vector3 a] - first point on the plane.  
[page:Vector3 b] - second point on the plane.  
[page:Vector3 c] - third point on the plane.  
  
Defines the plane based on the 3 provided points. The winding order is assumed
to be counter-clockwise, and determines the direction of the [page:.normal
normal].

### <br/> function setFromNormalAndCoplanarPoint( normal: Vector3, point:
Vector3 ): setFromNormalAndCoplanarPoint; <br/>

[page:Vector3 normal] - a unit length [page:Vector3] defining the normal of
the plane.  
[page:Vector3 point] - [page:Vector3]  
  
Sets the plane's properties as defined by a [page:Vector3 normal] and an
arbitrary coplanar [page:Vector3 point].

### <br/> function translate( offset: Vector3 ): translate; <br/>

[page:Vector3 offset] - the amount to move the plane by.  
  
Translates the plane by the distance defined by the [page:Vector3 offset]
vector. Note that this only affects the plane constant and will not affect the
normal vector.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

