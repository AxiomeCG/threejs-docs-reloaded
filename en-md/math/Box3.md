# [name]

Represents an axis-aligned bounding box (AABB) in 3D space.

## Code Example

  
```ts  
const box = new THREE.Box3();  
  
const mesh = new THREE.Mesh(  
new THREE.SphereGeometry(),  
new THREE.MeshBasicMaterial()  
);  
  
// ensure the bounding box is computed for its geometry  
// this should be done only once (assuming static geometries)  
mesh.geometry.computeBoundingBox();  
  
// ...  
  
// in the animation loop, compute the current bounding box with the world
matrix  
box.copy( mesh.geometry.boundingBox ).applyMatrix4( mesh.matrixWorld );  
```  

## Constructor

### [name]( [param:Vector3 min], [param:Vector3 max] )

[page:Vector3 min] - (optional) [page:Vector3] representing the lower (x, y,
z) boundary of the box. Default is ( + Infinity, + Infinity, + Infinity ).  
[page:Vector3 max] - (optional) [page:Vector3] representing the upper (x, y,
z) boundary of the box. Default is ( - Infinity, - Infinity, - Infinity ).  
  
Creates a [name] bounded by min and max.

## Properties

### <br/> Boolean isBox3; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Vector3 min; <br/>

[page:Vector3] representing the lower (x, y, z) boundary of the box.  
Default is ( + Infinity, + Infinity, + Infinity ).

### <br/> Vector3 max; <br/>

[page:Vector3] representing the upper (x, y, z) boundary of the box.  
Default is ( - Infinity, - Infinity, - Infinity ).

## Methods

### <br/> function applyMatrix4( matrix: Matrix4 ): applyMatrix4; <br/>

[page:Matrix4 matrix] - The [page:Matrix4] to apply  
  
Transforms this Box3 with the supplied matrix.

###  [method:Vector3 clampPoint]( [param:Vector3 point], [param:Vector3
target] )

[page:Vector3 point] - [page:Vector3] to clamp.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
[link:https://en.wikipedia.org/wiki/Clamping_(graphics) Clamps] the
[page:Vector3 point] within the bounds of this box.  

### [method:Box3 clone]()

Returns a new [page:Box3] with the same [page:.min min] and [page:.max max] as
this one.

### [method:Boolean containsBox]( [param:Box3 box] )

[page:Box3 box] - [page:Box3 Box3] to test for inclusion.  
  
Returns true if this box includes the entirety of [page:Box3 box]. If this and
[page:Box3 box] are identical,  
this function also returns true.

### [method:Boolean containsPoint]( [param:Vector3 point] )

[page:Vector3 point] - [page:Vector3] to check for inclusion.  
  
Returns true if the specified [page:Vector3 point] lies within or on the
boundaries of this box.

### <br/> function copy( box: Box3 ): copy; <br/>

[page:Box3 box] - [page:Box3] to copy.  
  
Copies the [page:.min min] and [page:.max max] from [page:Box3 box] to this
box.

### [method:Float distanceToPoint]( [param:Vector3 point] )

[page:Vector3 point] - [page:Vector3] to measure distance to.  
  
Returns the distance from any edge of this box to the specified point. If the
[page:Vector3 point] lies inside of this box, the distance will be `0`.

### [method:Boolean equals]( [param:Box3 box] )

[page:Box3 box] - Box to compare with this one.  
  
Returns true if this box and [page:Box3 box] share the same lower and upper
bounds.

### <br/> function expandByObject( object: Object3D, precise: Boolean? ):
expandByObject; <br/>

[page:Object3D object] - [page:Object3D] to expand the box by.  
precise - (optional) expand the bounding box as little as necessary at the
expense of more computation. Default is false.  
  
Expands the boundaries of this box to include [page:Object3D object] and its
children, accounting for the object's, and children's, world transforms. The
function may result in a larger box than strictly necessary (unless the
precise parameter is set to true).

### <br/> function expandByPoint( point: Vector3 ): expandByPoint; <br/>

[page:Vector3 point] - [page:Vector3] that should be included in the box.  
  
Expands the boundaries of this box to include [page:Vector3 point].

### <br/> function expandByScalar( scalar: Float ): expandByScalar; <br/>

[page:Float scalar] - Distance to expand the box by.  
  
Expands each dimension of the box by [page:Float scalar]. If negative, the
dimensions of the box will be contracted.

### <br/> function expandByVector( vector: Vector3 ): expandByVector; <br/>

[page:Vector3 vector] - [page:Vector3] to expand the box by.  
  
Expands this box equilaterally by [page:Vector3 vector]. The width of this box
will be expanded by the x component of [page:Vector3 vector] in both
directions. The height of this box will be expanded by the y component of
[page:Vector3 vector] in both directions. The depth of this box will be
expanded by the z component of `vector` in both directions.

### [method:Sphere getBoundingSphere]( [param:Sphere target] )

[page:Sphere target] — the result will be copied into this Sphere.  
  
Gets a [page:Sphere] that bounds the box.

### [method:Vector3 getCenter]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the center point of the box as a [page:Vector3].

###  [method:Vector3 getParameter]( [param:Vector3 point], [param:Vector3
target] )

[page:Vector3 point] - [page:Vector3].  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a point as a proportion of this box's width, height and depth.

### [method:Vector3 getSize]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the width, height and depth of this box.

### <br/> function intersect( box: Box3 ): intersect; <br/>

[page:Box3 box] - Box to intersect with.  
  
Computes the intersection of this and [page:Box3 box], setting the upper bound
of this box to the lesser of the two boxes' upper bounds and the lower bound
of this box to the greater of the two boxes' lower bounds. If there's no
overlap, makes this box empty.

### [method:Boolean intersectsBox]( [param:Box3 box] )

[page:Box3 box] - Box to check for intersection against.  
  
Determines whether or not this box intersects [page:Box3 box].

### [method:Boolean intersectsPlane]( [param:Plane plane] )

[page:Plane plane] - [page:Plane] to check for intersection against.  
  
Determines whether or not this box intersects [page:Plane plane].

### [method:Boolean intersectsSphere]( [param:Sphere sphere] )

[page:Sphere sphere] - [page:Sphere] to check for intersection against.  
  
Determines whether or not this box intersects [page:Sphere sphere].

### [method:Boolean intersectsTriangle]( [param:Triangle triangle] )

[page:Triangle triangle] - [page:Triangle] to check for intersection against.  
  
Determines whether or not this box intersects [page:Triangle triangle].

### [method:Boolean isEmpty]()

Returns true if this box includes zero points within its bounds.  
Note that a box with equal lower and upper bounds still includes one point,
the one both bounds share.

### <br/> function makeEmpty( ): makeEmpty; <br/>

Makes this box empty.

### <br/> function set( min: Vector3, max: Vector3 ): set; <br/>

[page:Vector3 min] - [page:Vector3] representing the lower (x, y, z) boundary
of the box.  
[page:Vector3 max] - [page:Vector3] representing the upper (x, y, z) boundary
of the box.  
  
Sets the lower and upper (x, y, z) boundaries of this box.  
Please note that this method only copies the values from the given objects.

### <br/> function setFromArray( array: Array ): setFromArray; <br/>

array -- An array of position data that the resulting box will envelop.  
  
Sets the upper and lower bounds of this box to include all of the data in
`array`.

### <br/> function setFromBufferAttribute( attribute: BufferAttribute ):
setFromBufferAttribute; <br/>

[page:BufferAttribute attribute] - A buffer attribute of position data that
the resulting box will envelop.  
  
Sets the upper and lower bounds of this box to include all of the data in
[page:BufferAttribute attribute].

### <br/> function setFromCenterAndSize( center: Vector3, size: Vector3 ):
setFromCenterAndSize; <br/>

[page:Vector3 center], - Desired center position of the box.  
[page:Vector3 size] - Desired x, y and z dimensions of the box.  
  
Centers this box on [page:Vector3 center] and sets this box's width, height
and depth to the values specified  
in [page:Vector3 size]

### <br/> function setFromObject( object: Object3D, precise: Boolean? ):
setFromObject; <br/>

[page:Object3D object] - [page:Object3D] to compute the bounding box of.  
precise - (optional) compute the smallest world-axis-aligned bounding box at
the expense of more computation. Default is false.  
  
Computes the world-axis-aligned bounding box of an [page:Object3D] (including
its children), accounting for the object's, and children's, world transforms.
The function may result in a larger box than strictly necessary.

### <br/> function setFromPoints( points: Array ): setFromPoints; <br/>

[page:Array points] - Array of [page:Vector3 Vector3s] that the resulting box
will contain.  
  
Sets the upper and lower bounds of this box to include all of the points in
[page:Array points].

### <br/> function translate( offset: Vector3 ): translate; <br/>

[page:Vector3 offset] - Direction and distance of offset.  
  
Adds [page:Vector3 offset] to both the upper and lower bounds of this box,
effectively moving this box [page:Vector3 offset] units in 3D space.

### <br/> function union( box: Box3 ): union; <br/>

[page:Box3 box] - Box that will be unioned with this box.  
  
Computes the union of this box and [page:Box3 box], setting the upper bound of
this box to the greater of the two boxes' upper bounds and the lower bound of
this box to the lesser of the two boxes' lower bounds.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

