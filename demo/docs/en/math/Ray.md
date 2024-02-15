# Ray

A ray that emits from an origin in a certain direction. This is used by the
[Raycaster](en\core\Raycaster.html) to assist with <a
href="https://en.wikipedia.org/wiki/Ray_casting">raycasting</a>. Raycasting is
used for mouse picking (working out what objects in the 3D space the mouse is
over) amongst other things.

## Constructor

### Ray

  
  
```ts  
function Ray( origin: Vector3, direction: Vector3 ): void;  
```  

[origin](en\math\Vector3.html) - (optional) the origin of the
[Ray](en\math\Ray.html). Default is a [Vector3](en\math\Vector3.html) at (0,
0, 0).  
[direction](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) The
direction of the [Ray](en\math\Ray.html). This must be normalized (with
[Vector3.normalize](#)) for the methods to operate properly. Default is a
[Vector3](en\math\Vector3.html) at (0, 0, -1).  
  
Creates a new Ray.

## Properties

### origin

  
  
```ts  
origin: Vector3;  
```  

The origin of the [Ray](en\math\Ray.html). Default is a
[Vector3](en\math\Vector3.html) at `(0, 0, 0)`.

### direction

  
  
```ts  
direction: Vector3;  
```  

The direction of the [Ray](en\math\Ray.html). This must be normalized (with
[Vector3.normalize](#)) for the methods to operate properly. Default is a
[Vector3](en\math\Vector3.html) at (0, 0, -1).

## Methods

### applyMatrix4

  
  
```ts  
function applyMatrix4( matrix4: Matrix4 ): this;  
```  

[matrix4](en\math\Matrix4.html) - the [Matrix4](en\math\Matrix4.html) to apply
to this [Ray](en\math\Ray.html).  
  
Transform this [Ray](en\math\Ray.html) by the [Matrix4](en\math\Matrix4.html).

### at

  
  
```ts  
function at( t: Float, target: Vector3 ): Vector3;  
```  

[t](#) - the distance along the [Ray](en\math\Ray.html) to retrieve a position
for.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Get a [Vector3](en\math\Vector3.html) that is a given distance along this
[Ray](en\math\Ray.html).

### clone

  
  
```ts  
function clone( ): Ray;  
```  

Creates a new Ray with identical [.origin](#origin) and
[.direction](#direction) to this one.

### closestPointToPoint

  
  
```ts  
function closestPointToPoint( point: Vector3, target: Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - the point to get the closest approach to.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Get the point along this [Ray](en\math\Ray.html) that is closest to the
[Vector3](en\math\Vector3.html) provided.

### copy

  
  
```ts  
function copy( ray: Ray ): this;  
```  

Copies the [.origin](#origin) and [.direction](#direction) properties of
[.ay](#ay) into this ray.

### distanceSqToPoint

  
  
```ts  
function distanceSqToPoint( point: Vector3 ): Float;  
```  

[point](en\math\Vector3.html) - the [Vector3](en\math\Vector3.html) to compute
a distance to.  
  
Get the squared distance of the closest approach between the
[Ray](en\math\Ray.html) and the [Vector3](en\math\Vector3.html).

### distanceSqToSegment

  
  
```ts  
function distanceSqToSegment( v0: Vector3, v1: Vector3, optionalPointOnRay:
Vector3, optionalPointOnSegment: Vector3 ): Float;  
```  

[v0](en\math\Vector3.html) - the start of the line segment.  
[v1](en\math\Vector3.html) - the end of the line segment.  
optionalPointOnRay - (optional) if this is provided, it receives the point on
this [Ray](en\math\Ray.html) that is closest to the segment.  
optionalPointOnSegment - (optional) if this is provided, it receives the point
on the line segment that is closest to this [Ray](en\math\Ray.html).  
  
Get the squared distance between this [Ray](en\math\Ray.html) and a line
segment.

### distanceToPlane

  
  
```ts  
function distanceToPlane( plane: Plane ): Float;  
```  

[plane](en\math\Plane.html) - the [Plane](en\math\Plane.html) to get the
distance to.  
  
Get the distance from [.origin](#origin) to the [Plane](en\math\Plane.html),
or `null` if the [Ray](en\math\Ray.html) doesn't intersect the
[Plane](en\math\Plane.html).

### distanceToPoint

  
  
```ts  
function distanceToPoint( point: Vector3 ): Float;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) The
[Vector3](en\math\Vector3.html) to compute a distance to.  
  
Get the distance of the closest approach between the [Ray](en\math\Ray.html)
and the [point](en\math\Vector3.html).

### equals

  
  
```ts  
function equals( ray: Ray ): Boolean;  
```  

[ray](en\math\Ray.html) - the [Ray](en\math\Ray.html) to compare to.  
  
Returns true if this and the other [.ay](#ay) have equal [.origin](#origin)
and [.direction](#direction).

### intersectBox

  
  
```ts  
function intersectBox( box: Box3, target: Vector3 ): Vector3;  
```  

[box](en\math\Box3.html) - the [Box3](en\math\Box3.html) to intersect with.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Intersect this [Ray](en\math\Ray.html) with a [Box3](en\math\Box3.html),
returning the intersection point or `null` if there is no intersection.

### intersectPlane

  
  
```ts  
function intersectPlane( plane: Plane, target: Vector3 ): Vector3;  
```  

[plane](en\math\Plane.html) - the [Plane](en\math\Plane.html) to intersect
with.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Intersect this [Ray](en\math\Ray.html) with a [Plane](en\math\Plane.html),
returning the intersection point or `null` if there is no intersection.

### intersectSphere

  
  
```ts  
function intersectSphere( sphere: Sphere, target: Vector3 ): Vector3;  
```  

[sphere](en\math\Sphere.html) - the [Sphere](en\math\Sphere.html) to intersect
with.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Intersect this [Ray](en\math\Ray.html) with a [Sphere](en\math\Sphere.html),
returning the intersection point or `null` if there is no intersection.

### intersectTriangle

  
  
```ts  
function intersectTriangle( a: Vector3, b: Vector3, c: Vector3,
backfaceCulling: Boolean, target: Vector3 ): Vector3;  
```  

[a](en\math\Vector3.html), [b](en\math\Vector3.html),
[c](en\math\Vector3.html) - The [Vector3](en\math\Vector3.html) points making
up the triangle.  
[backfaceCulling](#) - whether to use backface culling.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Intersect this [Ray](en\math\Ray.html) with a triangle, returning the
intersection point or `null` if there is no intersection.

### intersectsBox

  
  
```ts  
function intersectsBox( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - the [Box3](en\math\Box3.html) to intersect with.  
  
Return true if this [Ray](en\math\Ray.html) intersects with the
[Box3](en\math\Box3.html).

### intersectsPlane

  
  
```ts  
function intersectsPlane( plane: Plane ): Boolean;  
```  

[plane](en\math\Plane.html) - the [Plane](en\math\Plane.html) to intersect
with.  
  
Return true if this [Ray](en\math\Ray.html) intersects with the
[Plane](en\math\Plane.html).

### intersectsSphere

  
  
```ts  
function intersectsSphere( sphere: Sphere ): Boolean;  
```  

[sphere](en\math\Sphere.html) - the [Sphere](en\math\Sphere.html) to intersect
with.  
  
Return true if this [Ray](en\math\Ray.html) intersects with the
[Sphere](en\math\Sphere.html).

### lookAt

  
  
```ts  
function lookAt( v: Vector3 ): this;  
```  

[v](en\math\Vector3.html) - The [Vector3](en\math\Vector3.html) to look at.  
  
Adjusts the direction of the ray to point at the vector in world coordinates.

### recast

  
  
```ts  
function recast( t: Float ): this;  
```  

[t](#) - The distance along the [Ray](en\math\Ray.html) to interpolate.  
  
Shift the origin of this [Ray](en\math\Ray.html) along its direction by the
distance given.

### set

  
  
```ts  
function set( origin: Vector3, direction: Vector3 ): this;  
```  

[.ector3](#ector3) - the [.origin](#origin) of the [Ray](en\math\Ray.html).  
[.ector3](#ector3) - the [.direction](#direction) of the
[Ray](en\math\Ray.html). This must be normalized (with [Vector3.normalize](#))
for the methods to operate properly.  
  
Sets this ray's [.origin](#origin) and [.direction](#direction) properties by
copying the values from the given objects.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Ray.js">src/math/Ray.js</a>

