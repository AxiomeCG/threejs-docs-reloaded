# Plane

A two dimensional surface that extends infinitely in 3d space, represented in
<a href="http://mathworld.wolfram.com/HessianNormalForm.html">Hessian normal
form</a> by a unit length normal vector and a constant.

## Constructor

### Plane

  
  
```ts  
function Plane( normal: Vector3, constant: Float ): void;  
```  

[normal](en\math\Vector3.html) - (optional) a unit length
[Vector3](en\math\Vector3.html) defining the normal of the plane. Default is
`(1, 0, 0)`.  
[constant](#) - (optional) the signed distance from the origin to the plane.
Default is `0`.

## Properties

### isPlane

  
  
```ts  
isPlane: Boolean;  
```  

Read-only flag to check if a given object is of type Plane.

### normal

  
  
```ts  
normal: Vector3;  
```  

### constant

  
  
```ts  
constant: Float;  
```  

## Methods

### applyMatrix4

  
  
```ts  
function applyMatrix4( matrix: Matrix4, optionalNormalMatrix: Matrix3 ): this;  
```  

[matrix](en\math\Matrix4.html) - the [Page:Matrix4] to apply.  
[optionalNormalMatrix](en\math\Matrix3.html) - (optional) pre-computed normal
[Page:Matrix3] of the Matrix4 being applied.  
  
Apply a Matrix4 to the plane. The matrix must be an affine, homogeneous
transform.  
If supplying an [optionalNormalMatrix](en\math\Matrix3.html), it can be
created like so:  
```ts  
const optionalNormalMatrix = new THREE.Matrix3().getNormalMatrix( matrix );  
```  

### clone

  
  
```ts  
function clone( ): Plane;  
```  

Returns a new plane with the same [.normal](#normal) and
[.constant](#constant) as this one.

### coplanarPoint

  
  
```ts  
function coplanarPoint( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns a [Vector3](en\math\Vector3.html) coplanar to the plane, by
calculating the projection of the normal vector at the origin onto the plane.

### copy

  
  
```ts  
function copy( plane: Plane ): this;  
```  

Copies the values of the passed plane's [.normal](#normal) and
[.constant](#constant) properties to this plane.

### distanceToPoint

  
  
```ts  
function distanceToPoint( point: Vector3 ): Float;  
```  

Returns the signed distance from the [point](en\math\Vector3.html) to the
plane.

### distanceToSphere

  
  
```ts  
function distanceToSphere( sphere: Sphere ): Float;  
```  

Returns the signed distance from the [sphere](en\math\Sphere.html) to the
plane.

### equals

  
  
```ts  
function equals( plane: Plane ): Boolean;  
```  

Checks to see if two planes are equal (their [.normal](#normal) and
[.constant](#constant) properties match).

### intersectLine

  
  
```ts  
function intersectLine( line: Line3, target: Vector3 ): Vector3;  
```  

[line](en\math\Line3.html) - the [Line3](en\math\Line3.html) to check for
intersection.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns the intersection point of the passed line and the plane. Returns null
if the line does not intersect. Returns the line's starting point if the line
is coplanar with the plane.

### intersectsBox

  
  
```ts  
function intersectsBox( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - the [Box3](en\math\Box3.html) to check for
intersection.  
  
Determines whether or not this plane intersects [box](en\math\Box3.html).

### intersectsLine

  
  
```ts  
function intersectsLine( line: Line3 ): Boolean;  
```  

[line](en\math\Line3.html) - the [Line3](en\math\Line3.html) to check for
intersection.  
  
Tests whether a line segment intersects with (passes through) the plane.

### intersectsSphere

  
  
```ts  
function intersectsSphere( sphere: Sphere ): Boolean;  
```  

[sphere](en\math\Sphere.html) - the [Sphere](en\math\Sphere.html) to check for
intersection.  
  
Determines whether or not this plane intersects [sphere](en\math\Sphere.html).

### negate

  
  
```ts  
function negate( ): this;  
```  

Negates both the normal vector and the constant.

### normalize

  
  
```ts  
function normalize( ): this;  
```  

Normalizes the [.normal](#normal) vector, and adjusts the
[.constant](#constant) value accordingly.

### projectPoint

  
  
```ts  
function projectPoint( point: Vector3, target: Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - the [Vector3](en\math\Vector3.html) to project
onto the plane.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Projects a [point](en\math\Vector3.html) onto the plane.

### set

  
  
```ts  
function set( normal: Vector3, constant: Float ): this;  
```  

[normal](en\math\Vector3.html) - a unit length [Vector3](en\math\Vector3.html)
defining the normal of the plane.  
[constant](#) - the signed distance from the origin to the plane. Default is
`0`.  
  
Sets this plane's [.normal](#normal) and [.constant](#constant) properties by
copying the values from the given normal.

### setComponents

  
  
```ts  
function setComponents( x: Float, y: Float, z: Float, w: Float ): this;  
```  

[x](#) - x value of the unit length normal vector.  
[y](#) - y value of the unit length normal vector.  
[z](#) - z value of the unit length normal vector.  
[.loat](#loat) - the value of the plane's [.constant](#constant) property.  
  
Set the individual components that define the plane.

### setFromCoplanarPoints

  
  
```ts  
function setFromCoplanarPoints( a: Vector3, b: Vector3, c: Vector3 ): this;  
```  

[a](en\math\Vector3.html) - first point on the plane.  
[b](en\math\Vector3.html) - second point on the plane.  
[c](en\math\Vector3.html) - third point on the plane.  
  
Defines the plane based on the 3 provided points. The winding order is assumed
to be counter-clockwise, and determines the direction of the
[.normal](#normal).

### setFromNormalAndCoplanarPoint

  
  
```ts  
function setFromNormalAndCoplanarPoint( normal: Vector3, point: Vector3 ):
this;  
```  

[normal](en\math\Vector3.html) - a unit length [Vector3](en\math\Vector3.html)
defining the normal of the plane.  
[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html)  
  
Sets the plane's properties as defined by a [normal](en\math\Vector3.html) and
an arbitrary coplanar [point](en\math\Vector3.html).

### translate

  
  
```ts  
function translate( offset: Vector3 ): this;  
```  

[offset](en\math\Vector3.html) - the amount to move the plane by.  
  
Translates the plane by the distance defined by the
[offset](en\math\Vector3.html) vector. Note that this only affects the plane
constant and will not affect the normal vector.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Plane.js">src/math/Plane.js</a>

