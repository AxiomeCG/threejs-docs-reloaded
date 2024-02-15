# Sphere

A sphere defined by a center and radius.

## Constructor

### Sphere

  
  
```ts  
function Sphere( center: Vector3, radius: Float ): void;  
```  

[center](en\math\Vector3.html) - center of the sphere. Default is a
[Vector3](en\math\Vector3.html) at `(0, 0, 0)`.  
[radius](#) - radius of the sphere. Default is `-1`.  
  
Creates a new Sphere.

## Properties

### center

  
  
```ts  
center: Vector3;  
```  

A [Vector3](en\math\Vector3.html) defining the center of the sphere. Default
is `(0, 0, 0)`.

### radius

  
  
```ts  
radius: Float;  
```  

The radius of the sphere. Default is -1.

## Methods

### applyMatrix4

  
  
```ts  
function applyMatrix4( matrix: Matrix4 ): this;  
```  

[matrix](en\math\Matrix4.html) - the [Page:Matrix4] to apply  
  
Transforms this sphere with the provided [Matrix4](en\math\Matrix4.html).

### clampPoint

  
  
```ts  
function clampPoint( point: Vector3, target: Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) The point to
clamp.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Clamps a point within the sphere. If the point is outside the sphere, it will
clamp it to the closest point on the edge of the sphere. Points already inside
the sphere will not be affected.

### clone

  
  
```ts  
function clone( ): Sphere;  
```  

Returns a new sphere with the same [.center](#center) and [.radius](#radius)
as this one.

### containsPoint

  
  
```ts  
function containsPoint( point: Vector3 ): Boolean;  
```  

[point](en\math\Vector3.html) - the [Vector3](en\math\Vector3.html) to be
checked  
  
Checks to see if the sphere contains the provided
[point](en\math\Vector3.html) inclusive of the surface of the sphere.

### copy

  
  
```ts  
function copy( sphere: Sphere ): this;  
```  

Copies the values of the passed sphere's [.center](#center) and
[.radius](#radius) properties to this sphere.

### distanceToPoint

  
  
```ts  
function distanceToPoint( point: Vector3 ): Float;  
```  

Returns the closest distance from the boundary of the sphere to the
[point](en\math\Vector3.html). If the sphere contains the point, the distance
will be negative.

### expandByPoint

  
  
```ts  
function expandByPoint( point: Vector3 ): this;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) that should be
included in the sphere.  
  
Expands the boundaries of this sphere to include
[point](en\math\Vector3.html).

### isEmpty

  
  
```ts  
function isEmpty( ): Boolean;  
```  

Checks to see if the sphere is empty (the radius set to a negative number).  
Spheres with a radius of `0` contain only their center point and are not
considered to be empty.

### makeEmpty

  
  
```ts  
function makeEmpty( ): this;  
```  

Makes the sphere empty by setting [.center](#center) to (0, 0, 0) and
[.radius](#radius) to -1.

### equals

  
  
```ts  
function equals( sphere: Sphere ): Boolean;  
```  

Checks to see if the two spheres' centers and radii are equal.

### getBoundingBox

  
  
```ts  
function getBoundingBox( target: Box3 ): Box3;  
```  

[target](en\math\Box3.html) — the result will be copied into this Box3.  
  
Returns a<a href="https://en.wikipedia.org/wiki/Minimum_bounding_box">Minimum
Bounding Box</a> for the sphere.

### intersectsBox

  
  
```ts  
function intersectsBox( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - [Box3](en\math\Box3.html) to check for intersection
against.  
  
Determines whether or not this sphere intersects a given
[box](en\math\Box3.html).

### intersectsPlane

  
  
```ts  
function intersectsPlane( plane: Plane ): Boolean;  
```  

[plane](en\math\Plane.html) - Plane to check for intersection against.  
  
Determines whether or not this sphere intersects a given
[plane](en\math\Plane.html).

### intersectsSphere

  
  
```ts  
function intersectsSphere( sphere: Sphere ): Boolean;  
```  

[sphere](en\math\Sphere.html) - Sphere to check for intersection against.  
  
Checks to see if two spheres intersect.

### set

  
  
```ts  
function set( center: Vector3, radius: Float ): this;  
```  

[center](en\math\Vector3.html) - center of the sphere.  
[radius](#) - radius of the sphere.  
  
Sets the [.center](#center) and [.radius](#radius) properties of this sphere.  
Please note that this method only copies the values from the given center.

### setFromPoints

  
  
```ts  
function setFromPoints( points: Array, optionalCenter: Vector3 ): this;  
```  

[points](#) - an [Array](#) of [Vector3](en\math\Vector3.html) positions.  
[optionalCenter](en\math\Vector3.html) - Optional
[Vector3](en\math\Vector3.html) position for the sphere's center.  
  
Computes the minimum bounding sphere for an array of [points](#). If
[optionalCenter](en\math\Vector3.html)is given, it is used as the sphere's
center. Otherwise, the center of the axis-aligned bounding box encompassing
[points](#) is calculated.

### translate

  
  
```ts  
function translate( offset: Vector3 ): this;  
```  

Translate the sphere's center by the provided offset
[Vector3](en\math\Vector3.html).

### union

  
  
```ts  
function union( sphere: Sphere ): this;  
```  

[sphere](en\math\Sphere.html) - Bounding sphere that will be unioned with this
sphere.  
  
Expands this sphere to enclose both the original sphere and the given sphere.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Sphere.js">src/math/Sphere.js</a>

