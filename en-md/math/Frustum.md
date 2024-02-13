# Frustum

[link:http://en.wikipedia.org/wiki/Frustum Frustums] are used to determine
what is inside the camera's field of view. They help speed up the rendering
process - objects which lie outside a camera's frustum can safely be excluded
from rendering.  
  
This class is mainly intended for use internally by a renderer for calculating
a [page:Camera camera] or [page:LightShadow.camera shadowCamera]'s frustum.

## Constructor

###  function Frustum( p0: Plane, p1: Plane, p2: Plane, p3: Plane, p4: Plane,
p5: Plane ): void;

[page:Plane p0] - (optional) defaults to a new [page:Plane].  
[page:Plane p1] - (optional) defaults to a new [page:Plane].  
[page:Plane p2] - (optional) defaults to a new [page:Plane].  
[page:Plane p3] - (optional) defaults to a new [page:Plane].  
[page:Plane p4] - (optional) defaults to a new [page:Plane].  
[page:Plane p5] - (optional) defaults to a new [page:Plane].  
  
Creates a new Frustum.

## Properties

###  Array planes;

Array of 6 [page:Plane planes].

## Methods

###  function clone( ): Frustum;

Return a new Frustum with the same parameters as this one.

###  function containsPoint( point: Vector3 ): Boolean;

[page:Vector3 point] - [page:Vector3] to test.  
  
Checks to see if the frustum contains the [page:Vector3 point].

###  function copy( frustum: Frustum ): this;

[page:Frustum frustum] - The frustum to copy  
  
Copies the properties of the passed [page:Frustum frustum] into this one.

###  function intersectsBox( box: Box3 ): Boolean;

[page:Box3 box] - [page:Box3] to check for intersection.  
  
Return true if [page:Box3 box] intersects with this frustum.

###  function intersectsObject( object: Object3D ): Boolean;

Checks whether the [page:Object3D object]'s
[page:BufferGeometry.boundingSphere bounding sphere] is intersecting the
Frustum.  
  
Note that the object must have a [page:BufferGeometry geometry] so that the
bounding sphere can be calculated.

###  function intersectsSphere( sphere: Sphere ): Boolean;

[page:Sphere sphere] - [page:Sphere] to check for intersection.  
  
Return true if [page:Sphere sphere] intersects with this frustum.

###  function intersectsSprite( sprite: Sprite ): Boolean;

Checks whether the [page:Sprite sprite] is intersecting the Frustum.  
  

###  function set( p0: Plane, p1: Plane, p2: Plane, p3: Plane, p4: Plane, p5:
Plane ): this;

Sets the frustum from the passed planes. No plane order is implied.  
Note that this method only copies the values from the given objects.

###  function setFromProjectionMatrix( matrix: Matrix4 ): this;

[page:Matrix4 matrix] - Projection [page:Matrix4] used to set the
[page:.planes planes]  
  
Sets the frustum planes from the projection matrix.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

