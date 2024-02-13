# Sphere

A sphere defined by a center and radius.

## Constructor

###  function Sphere( center: Vector3, radius: Float ): void;

[page:Vector3 center] - center of the sphere. Default is a [page:Vector3] at
`(0, 0, 0)`.  
[page:Float radius] - radius of the sphere. Default is `-1`.  
  
Creates a new Sphere.

## Properties

###  Vector3 center;

A [page:Vector3] defining the center of the sphere. Default is `(0, 0, 0)`.

###  Float radius;

The radius of the sphere. Default is -1.

## Methods

###  function applyMatrix4( matrix: Matrix4 ): this;

[page:Matrix4 matrix] - the [Page:Matrix4] to apply  
  
Transforms this sphere with the provided [page:Matrix4].

###  function clampPoint( point: Vector3, target: Vector3 ): Vector3;

[page:Vector3 point] - [page:Vector3] The point to clamp.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Clamps a point within the sphere. If the point is outside the sphere, it will
clamp it to the closest point on the edge of the sphere. Points already inside
the sphere will not be affected.

###  function clone( ): Sphere;

Returns a new sphere with the same [page:.center center] and [page:.radius
radius] as this one.

###  function containsPoint( point: Vector3 ): Boolean;

[page:Vector3 point] - the [page:Vector3] to be checked  
  
Checks to see if the sphere contains the provided [page:Vector3 point]
inclusive of the surface of the sphere.

###  function copy( sphere: Sphere ): this;

Copies the values of the passed sphere's [page:.center center] and
[page:.radius radius] properties to this sphere.

###  function distanceToPoint( point: Vector3 ): Float;

Returns the closest distance from the boundary of the sphere to the
[page:Vector3 point]. If the sphere contains the point, the distance will be
negative.

###  function expandByPoint( point: Vector3 ): this;

[page:Vector3 point] - [page:Vector3] that should be included in the sphere.  
  
Expands the boundaries of this sphere to include [page:Vector3 point].

###  function isEmpty( ): Boolean;

Checks to see if the sphere is empty (the radius set to a negative number).  
Spheres with a radius of `0` contain only their center point and are not
considered to be empty.

###  function makeEmpty( ): this;

Makes the sphere empty by setting [page:.center center] to (0, 0, 0) and
[page:.radius radius] to -1.

###  function equals( sphere: Sphere ): Boolean;

Checks to see if the two spheres' centers and radii are equal.

###  function getBoundingBox( target: Box3 ): Box3;

[page:Box3 target] — the result will be copied into this Box3.  
  
Returns a[link:https://en.wikipedia.org/wiki/Minimum_bounding_box Minimum
Bounding Box] for the sphere.

###  function intersectsBox( box: Box3 ): Boolean;

[page:Box3 box] - [page:Box3] to check for intersection against.  
  
Determines whether or not this sphere intersects a given [page:Box3 box].

###  function intersectsPlane( plane: Plane ): Boolean;

[page:Plane plane] - Plane to check for intersection against.  
  
Determines whether or not this sphere intersects a given [page:Plane plane].

###  function intersectsSphere( sphere: Sphere ): Boolean;

[page:Sphere sphere] - Sphere to check for intersection against.  
  
Checks to see if two spheres intersect.

###  function set( center: Vector3, radius: Float ): this;

[page:Vector3 center] - center of the sphere.  
[page:Float radius] - radius of the sphere.  
  
Sets the [page:.center center] and [page:.radius radius] properties of this
sphere.  
Please note that this method only copies the values from the given center.

###  function setFromPoints( points: Array, optionalCenter: Vector3 ): this;

[page:Array points] - an [page:Array] of [page:Vector3] positions.  
[page:Vector3 optionalCenter] - Optional [page:Vector3] position for the
sphere's center.  
  
Computes the minimum bounding sphere for an array of [page:Array points]. If
[page:Vector3 optionalCenter]is given, it is used as the sphere's center.
Otherwise, the center of the axis-aligned bounding box encompassing
[page:Array points] is calculated.

###  function translate( offset: Vector3 ): this;

Translate the sphere's center by the provided offset [page:Vector3].

###  function union( sphere: Sphere ): this;

[page:Sphere sphere] - Bounding sphere that will be unioned with this sphere.  
  
Expands this sphere to enclose both the original sphere and the given sphere.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

