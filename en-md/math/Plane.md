# Plane

A two dimensional surface that extends infinitely in 3d space, represented in
[link:http://mathworld.wolfram.com/HessianNormalForm.html Hessian normal form]
by a unit length normal vector and a constant.

## Constructor

###  function Plane( normal: Vector3, constant: Float ): void;

[page:Vector3 normal] - (optional) a unit length [page:Vector3] defining the
normal of the plane. Default is `(1, 0, 0)`.  
[page:Float constant] - (optional) the signed distance from the origin to the
plane. Default is `0`.

## Properties

###  Boolean isPlane;

Read-only flag to check if a given object is of type Plane.

###  Vector3 normal;

###  Float constant;

## Methods

###  function applyMatrix4( matrix: Matrix4, optionalNormalMatrix: Matrix3 ):
this;

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

###  function clone( ): Plane;

Returns a new plane with the same [page:.normal normal] and [page:.constant
constant] as this one.

###  function coplanarPoint( target: Vector3 ): Vector3;

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a [page:Vector3] coplanar to the plane, by calculating the projection
of the normal vector at the origin onto the plane.

###  function copy( plane: Plane ): this;

Copies the values of the passed plane's [page:.normal normal] and
[page:.constant constant] properties to this plane.

###  function distanceToPoint( point: Vector3 ): Float;

Returns the signed distance from the [page:Vector3 point] to the plane.

###  function distanceToSphere( sphere: Sphere ): Float;

Returns the signed distance from the [page:Sphere sphere] to the plane.

###  function equals( plane: Plane ): Boolean;

Checks to see if two planes are equal (their [page:.normal normal] and
[page:.constant constant] properties match).

###  function intersectLine( line: Line3, target: Vector3 ): Vector3;

[page:Line3 line] - the [page:Line3] to check for intersection.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the intersection point of the passed line and the plane. Returns null
if the line does not intersect. Returns the line's starting point if the line
is coplanar with the plane.

###  function intersectsBox( box: Box3 ): Boolean;

[page:Box3 box] - the [page:Box3] to check for intersection.  
  
Determines whether or not this plane intersects [page:Box3 box].

###  function intersectsLine( line: Line3 ): Boolean;

[page:Line3 line] - the [page:Line3] to check for intersection.  
  
Tests whether a line segment intersects with (passes through) the plane.

###  function intersectsSphere( sphere: Sphere ): Boolean;

[page:Sphere sphere] - the [page:Sphere] to check for intersection.  
  
Determines whether or not this plane intersects [page:Sphere sphere].

###  function negate( ): this;

Negates both the normal vector and the constant.

###  function normalize( ): this;

Normalizes the [page:.normal normal] vector, and adjusts the [page:.constant
constant] value accordingly.

###  function projectPoint( point: Vector3, target: Vector3 ): Vector3;

[page:Vector3 point] - the [page:Vector3] to project onto the plane.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Projects a [page:Vector3 point] onto the plane.

###  function set( normal: Vector3, constant: Float ): this;

[page:Vector3 normal] - a unit length [page:Vector3] defining the normal of
the plane.  
[page:Float constant] - the signed distance from the origin to the plane.
Default is `0`.  
  
Sets this plane's [page:.normal normal] and [page:.constant constant]
properties by copying the values from the given normal.

###  function setComponents( x: Float, y: Float, z: Float, w: Float ): this;

[page:Float x] - x value of the unit length normal vector.  
[page:Float y] - y value of the unit length normal vector.  
[page:Float z] - z value of the unit length normal vector.  
[page:Float w] - the value of the plane's [page:.constant constant] property.  
  
Set the individual components that define the plane.

###  function setFromCoplanarPoints( a: Vector3, b: Vector3, c: Vector3 ):
this;

[page:Vector3 a] - first point on the plane.  
[page:Vector3 b] - second point on the plane.  
[page:Vector3 c] - third point on the plane.  
  
Defines the plane based on the 3 provided points. The winding order is assumed
to be counter-clockwise, and determines the direction of the [page:.normal
normal].

###  function setFromNormalAndCoplanarPoint( normal: Vector3, point: Vector3
): this;

[page:Vector3 normal] - a unit length [page:Vector3] defining the normal of
the plane.  
[page:Vector3 point] - [page:Vector3]  
  
Sets the plane's properties as defined by a [page:Vector3 normal] and an
arbitrary coplanar [page:Vector3 point].

###  function translate( offset: Vector3 ): this;

[page:Vector3 offset] - the amount to move the plane by.  
  
Translates the plane by the distance defined by the [page:Vector3 offset]
vector. Note that this only affects the plane constant and will not affect the
normal vector.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

