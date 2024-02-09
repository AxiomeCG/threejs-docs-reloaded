# [name]

[link:http://en.wikipedia.org/wiki/Frustum Frustums] are used to determine
what is inside the camera's field of view. They help speed up the rendering
process - objects which lie outside a camera's frustum can safely be excluded
from rendering.  
  
This class is mainly intended for use internally by a renderer for calculating
a [page:Camera camera] or [page:LightShadow.camera shadowCamera]'s frustum.

## Constructor

###  [name]([param:Plane p0], [param:Plane p1], [param:Plane p2], [param:Plane
p3], [param:Plane p4], [param:Plane p5])

[page:Plane p0] - (optional) defaults to a new [page:Plane].  
[page:Plane p1] - (optional) defaults to a new [page:Plane].  
[page:Plane p2] - (optional) defaults to a new [page:Plane].  
[page:Plane p3] - (optional) defaults to a new [page:Plane].  
[page:Plane p4] - (optional) defaults to a new [page:Plane].  
[page:Plane p5] - (optional) defaults to a new [page:Plane].  
  
Creates a new [name].

## Properties

### <br/> Array planes; <br/>

Array of 6 [page:Plane planes].

## Methods

### [method:Frustum clone]()

Return a new Frustum with the same parameters as this one.

### [method:Boolean containsPoint]( [param:Vector3 point] )

[page:Vector3 point] - [page:Vector3] to test.  
  
Checks to see if the frustum contains the [page:Vector3 point].

### <br/> function copy( frustum: Frustum ): copy; <br/>

[page:Frustum frustum] - The frustum to copy  
  
Copies the properties of the passed [page:Frustum frustum] into this one.

### [method:Boolean intersectsBox]( [param:Box3 box] )

[page:Box3 box] - [page:Box3] to check for intersection.  
  
Return true if [page:Box3 box] intersects with this frustum.

### [method:Boolean intersectsObject]( [param:Object3D object] )

Checks whether the [page:Object3D object]'s
[page:BufferGeometry.boundingSphere bounding sphere] is intersecting the
Frustum.  
  
Note that the object must have a [page:BufferGeometry geometry] so that the
bounding sphere can be calculated.

### [method:Boolean intersectsSphere]( [param:Sphere sphere] )

[page:Sphere sphere] - [page:Sphere] to check for intersection.  
  
Return true if [page:Sphere sphere] intersects with this frustum.

### [method:Boolean intersectsSprite]( [param:Sprite sprite] )

Checks whether the [page:Sprite sprite] is intersecting the Frustum.  
  

### <br/> function set( p0: Plane, p1: Plane, p2: Plane, p3: Plane, p4: Plane,
p5: Plane ): set; <br/>

Sets the frustum from the passed planes. No plane order is implied.  
Note that this method only copies the values from the given objects.

### <br/> function setFromProjectionMatrix( matrix: Matrix4 ):
setFromProjectionMatrix; <br/>

[page:Matrix4 matrix] - Projection [page:Matrix4] used to set the
[page:.planes planes]  
  
Sets the frustum planes from the projection matrix.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

