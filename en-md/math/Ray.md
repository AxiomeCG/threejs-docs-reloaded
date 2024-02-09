# [name]

A ray that emits from an origin in a certain direction. This is used by the
[page:Raycaster] to assist with
[link:https://en.wikipedia.org/wiki/Ray_casting raycasting]. Raycasting is
used for mouse picking (working out what objects in the 3D space the mouse is
over) amongst other things.

## Constructor

### [name]( [param:Vector3 origin], [param:Vector3 direction] )

[page:Vector3 origin] - (optional) the origin of the [page:Ray]. Default is a
[page:Vector3] at (0, 0, 0).  
[page:Vector3 direction] - [page:Vector3] The direction of the [page:Ray].
This must be normalized (with [page:Vector3.normalize]) for the methods to
operate properly. Default is a [page:Vector3] at (0, 0, -1).  
  
Creates a new [name].

## Properties

### <br/> Vector3 origin; <br/>

The origin of the [page:Ray]. Default is a [page:Vector3] at `(0, 0, 0)`.

### <br/> Vector3 direction; <br/>

The direction of the [page:Ray]. This must be normalized (with
[page:Vector3.normalize]) for the methods to operate properly. Default is a
[page:Vector3] at (0, 0, -1).

## Methods

### <br/> function applyMatrix4( matrix4: Matrix4 ): applyMatrix4; <br/>

[page:Matrix4 matrix4] - the [page:Matrix4] to apply to this [page:Ray].  
  
Transform this [page:Ray] by the [page:Matrix4].

### [method:Vector3 at]( [param:Float t], [param:Vector3 target] )

[page:Float t] - the distance along the [page:Ray] to retrieve a position for.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Get a [page:Vector3] that is a given distance along this [page:Ray].

### [method:Ray clone]()

Creates a new Ray with identical [page:.origin origin] and [page:.direction
direction] to this one.

###  [method:Vector3 closestPointToPoint]( [param:Vector3 point],
[param:Vector3 target] )

[page:Vector3 point] - the point to get the closest approach to.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Get the point along this [page:Ray] that is closest to the [page:Vector3]
provided.

### <br/> function copy( ray: Ray ): copy; <br/>

Copies the [page:.origin origin] and [page:.direction direction] properties of
[page:Ray ray] into this ray.

### [method:Float distanceSqToPoint]( [param:Vector3 point] )

[page:Vector3 point] - the [page:Vector3] to compute a distance to.  
  
Get the squared distance of the closest approach between the [page:Ray] and
the [page:Vector3].

###  [method:Float distanceSqToSegment]( [param:Vector3 v0], [param:Vector3
v1], [param:Vector3 optionalPointOnRay], [param:Vector3
optionalPointOnSegment] )

[page:Vector3 v0] - the start of the line segment.  
[page:Vector3 v1] - the end of the line segment.  
optionalPointOnRay - (optional) if this is provided, it receives the point on
this [page:Ray] that is closest to the segment.  
optionalPointOnSegment - (optional) if this is provided, it receives the point
on the line segment that is closest to this [page:Ray].  
  
Get the squared distance between this [page:Ray] and a line segment.

### [method:Float distanceToPlane]( [param:Plane plane] )

[page:Plane plane] - the [page:Plane] to get the distance to.  
  
Get the distance from [page:.origin origin] to the [page:Plane], or `null` if
the [page:Ray] doesn't intersect the [page:Plane].

### [method:Float distanceToPoint]( [param:Vector3 point] )

[page:Vector3 point] - [page:Vector3] The [page:Vector3] to compute a distance
to.  
  
Get the distance of the closest approach between the [page:Ray] and the
[page:Vector3 point].

### [method:Boolean equals]( [param:Ray ray] )

[page:Ray ray] - the [page:Ray] to compare to.  
  
Returns true if this and the other [page:Ray ray] have equal [page:.origin
origin] and [page:.direction direction].

###  [method:Vector3 intersectBox]( [param:Box3 box], [param:Vector3 target] )

[page:Box3 box] - the [page:Box3] to intersect with.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Intersect this [page:Ray] with a [page:Box3], returning the intersection point
or `null` if there is no intersection.

###  [method:Vector3 intersectPlane]( [param:Plane plane], [param:Vector3
target] )

[page:Plane plane] - the [page:Plane] to intersect with.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Intersect this [page:Ray] with a [page:Plane], returning the intersection
point or `null` if there is no intersection.

###  [method:Vector3 intersectSphere]( [param:Sphere sphere], [param:Vector3
target] )

[page:Sphere sphere] - the [page:Sphere] to intersect with.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Intersect this [page:Ray] with a [page:Sphere], returning the intersection
point or `null` if there is no intersection.

###  [method:Vector3 intersectTriangle]( [param:Vector3 a], [param:Vector3 b],
[param:Vector3 c], [param:Boolean backfaceCulling], [param:Vector3 target] )

[page:Vector3 a], [page:Vector3 b], [page:Vector3 c] - The [page:Vector3]
points making up the triangle.  
[page:Boolean backfaceCulling] - whether to use backface culling.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Intersect this [page:Ray] with a triangle, returning the intersection point or
`null` if there is no intersection.

### [method:Boolean intersectsBox]( [param:Box3 box] )

[page:Box3 box] - the [page:Box3] to intersect with.  
  
Return true if this [page:Ray] intersects with the [page:Box3].

### [method:Boolean intersectsPlane]( [param:Plane plane] )

[page:Plane plane] - the [page:Plane] to intersect with.  
  
Return true if this [page:Ray] intersects with the [page:Plane].

### [method:Boolean intersectsSphere]( [param:Sphere sphere] )

[page:Sphere sphere] - the [page:Sphere] to intersect with.  
  
Return true if this [page:Ray] intersects with the [page:Sphere].

### <br/> function lookAt( v: Vector3 ): lookAt; <br/>

[page:Vector3 v] - The [page:Vector3] to look at.  
  
Adjusts the direction of the ray to point at the vector in world coordinates.

### <br/> function recast( t: Float ): recast; <br/>

[page:Float t] - The distance along the [page:Ray] to interpolate.  
  
Shift the origin of this [page:Ray] along its direction by the distance given.

### <br/> function set( origin: Vector3, direction: Vector3 ): set; <br/>

[page:Vector3 origin] - the [page:.origin origin] of the [page:Ray].  
[page:Vector3 direction] - the [page:.direction direction] of the [page:Ray].
This must be normalized (with [page:Vector3.normalize]) for the methods to
operate properly.  
  
Sets this ray's [page:.origin origin] and [page:.direction direction]
properties by copying the values from the given objects.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

