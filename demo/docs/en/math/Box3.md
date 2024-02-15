# Box3

Represents an axis-aligned bounding box (AABB) in 3D space.

## Code Example

  
```ts  
const box = new THREE.Box3(); const mesh = new THREE.Mesh( new
THREE.SphereGeometry(), new THREE.MeshBasicMaterial() ); // ensure the
bounding box is computed for its geometry // this should be done only once
(assuming static geometries) mesh.geometry.computeBoundingBox(); // ... // in
the animation loop, compute the current bounding box with the world matrix
box.copy( mesh.geometry.boundingBox ).applyMatrix4( mesh.matrixWorld );  
```  

## Constructor

### Box3

  
  
```ts  
function Box3( min: Vector3, max: Vector3 ): void;  
```  

[min](en\math\Vector3.html) - (optional) [Vector3](en\math\Vector3.html)
representing the lower (x, y, z) boundary of the box. Default is ( + Infinity,
+ Infinity, + Infinity ).  
[max](en\math\Vector3.html) - (optional) [Vector3](en\math\Vector3.html)
representing the upper (x, y, z) boundary of the box. Default is ( - Infinity,
- Infinity, - Infinity ).  
  
Creates a Box3 bounded by min and max.

## Properties

### isBox3

  
  
```ts  
isBox3: Boolean;  
```  

Read-only flag to check if a given object is of type Box3.

### min

  
  
```ts  
min: Vector3;  
```  

[Vector3](en\math\Vector3.html) representing the lower (x, y, z) boundary of
the box.  
Default is ( + Infinity, + Infinity, + Infinity ).

### max

  
  
```ts  
max: Vector3;  
```  

[Vector3](en\math\Vector3.html) representing the upper (x, y, z) boundary of
the box.  
Default is ( - Infinity, - Infinity, - Infinity ).

## Methods

### applyMatrix4

  
  
```ts  
function applyMatrix4( matrix: Matrix4 ): this;  
```  

[matrix](en\math\Matrix4.html) - The [Matrix4](en\math\Matrix4.html) to apply  
  
Transforms this Box3 with the supplied matrix.

### clampPoint

  
  
```ts  
function clampPoint( point: Vector3, target: Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to clamp.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
<a href="https://en.wikipedia.org/wiki/Clamping_(graphics)">Clamps</a> the
[point](en\math\Vector3.html) within the bounds of this box.  

### clone

  
  
```ts  
function clone( ): Box3;  
```  

Returns a new [Box3](en\math\Box3.html) with the same [.min](#min) and
[.max](#max) as this one.

### containsBox

  
  
```ts  
function containsBox( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - [Box3](en\math\Box3.html) to test for inclusion.  
  
Returns true if this box includes the entirety of [box](en\math\Box3.html). If
this and [box](en\math\Box3.html) are identical,  
this function also returns true.

### containsPoint

  
  
```ts  
function containsPoint( point: Vector3 ): Boolean;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to check for
inclusion.  
  
Returns true if the specified [point](en\math\Vector3.html) lies within or on
the boundaries of this box.

### copy

  
  
```ts  
function copy( box: Box3 ): this;  
```  

[box](en\math\Box3.html) - [Box3](en\math\Box3.html) to copy.  
  
Copies the [.min](#min) and [.max](#max) from [.ox3](#ox3) to this box.

### distanceToPoint

  
  
```ts  
function distanceToPoint( point: Vector3 ): Float;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to measure
distance to.  
  
Returns the distance from any edge of this box to the specified point. If the
[point](en\math\Vector3.html) lies inside of this box, the distance will be
`0`.

### equals

  
  
```ts  
function equals( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - Box to compare with this one.  
  
Returns true if this box and [box](en\math\Box3.html) share the same lower and
upper bounds.

### expandByObject

  
  
```ts  
function expandByObject( object: Object3D, precise: Boolean ): this;  
```  

[object](en\core\Object3D.html) - [Object3D](en\core\Object3D.html) to expand
the box by.  
precise - (optional) expand the bounding box as little as necessary at the
expense of more computation. Default is false.  
  
Expands the boundaries of this box to include [object](en\core\Object3D.html)
and its children, accounting for the object's, and children's, world
transforms. The function may result in a larger box than strictly necessary
(unless the precise parameter is set to true).

### expandByPoint

  
  
```ts  
function expandByPoint( point: Vector3 ): this;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) that should be
included in the box.  
  
Expands the boundaries of this box to include [point](en\math\Vector3.html).

### expandByScalar

  
  
```ts  
function expandByScalar( scalar: Float ): this;  
```  

[scalar](#) - Distance to expand the box by.  
  
Expands each dimension of the box by [scalar](#). If negative, the dimensions
of the box will be contracted.

### expandByVector

  
  
```ts  
function expandByVector( vector: Vector3 ): this;  
```  

[vector](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to expand the
box by.  
  
Expands this box equilaterally by [vector](en\math\Vector3.html). The width of
this box will be expanded by the x component of [vector](en\math\Vector3.html)
in both directions. The height of this box will be expanded by the y component
of [vector](en\math\Vector3.html) in both directions. The depth of this box
will be expanded by the z component of `vector` in both directions.

### getBoundingSphere

  
  
```ts  
function getBoundingSphere( target: Sphere ): Sphere;  
```  

[target](en\math\Sphere.html) — the result will be copied into this Sphere.  
  
Gets a [Sphere](en\math\Sphere.html) that bounds the box.

### getCenter

  
  
```ts  
function getCenter( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns the center point of the box as a [Vector3](en\math\Vector3.html).

### getParameter

  
  
```ts  
function getParameter( point: Vector3, target: Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html).  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns a point as a proportion of this box's width, height and depth.

### getSize

  
  
```ts  
function getSize( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns the width, height and depth of this box.

### intersect

  
  
```ts  
function intersect( box: Box3 ): this;  
```  

[box](en\math\Box3.html) - Box to intersect with.  
  
Computes the intersection of this and [box](en\math\Box3.html), setting the
upper bound of this box to the lesser of the two boxes' upper bounds and the
lower bound of this box to the greater of the two boxes' lower bounds. If
there's no overlap, makes this box empty.

### intersectsBox

  
  
```ts  
function intersectsBox( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - Box to check for intersection against.  
  
Determines whether or not this box intersects [box](en\math\Box3.html).

### intersectsPlane

  
  
```ts  
function intersectsPlane( plane: Plane ): Boolean;  
```  

[plane](en\math\Plane.html) - [Plane](en\math\Plane.html) to check for
intersection against.  
  
Determines whether or not this box intersects [plane](en\math\Plane.html).

### intersectsSphere

  
  
```ts  
function intersectsSphere( sphere: Sphere ): Boolean;  
```  

[sphere](en\math\Sphere.html) - [Sphere](en\math\Sphere.html) to check for
intersection against.  
  
Determines whether or not this box intersects [sphere](en\math\Sphere.html).

### intersectsTriangle

  
  
```ts  
function intersectsTriangle( triangle: Triangle ): Boolean;  
```  

[triangle](en\math\Triangle.html) - [Triangle](en\math\Triangle.html) to check
for intersection against.  
  
Determines whether or not this box intersects
[triangle](en\math\Triangle.html).

### isEmpty

  
  
```ts  
function isEmpty( ): Boolean;  
```  

Returns true if this box includes zero points within its bounds.  
Note that a box with equal lower and upper bounds still includes one point,
the one both bounds share.

### makeEmpty

  
  
```ts  
function makeEmpty( ): this;  
```  

Makes this box empty.

### set

  
  
```ts  
function set( min: Vector3, max: Vector3 ): this;  
```  

[min](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) representing the
lower (x, y, z) boundary of the box.  
[max](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) representing the
upper (x, y, z) boundary of the box.  
  
Sets the lower and upper (x, y, z) boundaries of this box.  
Please note that this method only copies the values from the given objects.

### setFromArray

  
  
```ts  
function setFromArray( array: Array ): this;  
```  

array -- An array of position data that the resulting box will envelop.  
  
Sets the upper and lower bounds of this box to include all of the data in
`array`.

### setFromBufferAttribute

  
  
```ts  
function setFromBufferAttribute( attribute: BufferAttribute ): this;  
```  

[attribute](en\core\BufferAttribute.html) - A buffer attribute of position
data that the resulting box will envelop.  
  
Sets the upper and lower bounds of this box to include all of the data in
[attribute](en\core\BufferAttribute.html).

### setFromCenterAndSize

  
  
```ts  
function setFromCenterAndSize( center: Vector3, size: Vector3 ): this;  
```  

[center](en\math\Vector3.html), - Desired center position of the box.  
[size](en\math\Vector3.html) - Desired x, y and z dimensions of the box.  
  
Centers this box on [center](en\math\Vector3.html) and sets this box's width,
height and depth to the values specified  
in [size](en\math\Vector3.html)

### setFromObject

  
  
```ts  
function setFromObject( object: Object3D, precise: Boolean ): this;  
```  

[object](en\core\Object3D.html) - [Object3D](en\core\Object3D.html) to compute
the bounding box of.  
precise - (optional) compute the smallest world-axis-aligned bounding box at
the expense of more computation. Default is false.  
  
Computes the world-axis-aligned bounding box of an
[Object3D](en\core\Object3D.html) (including its children), accounting for the
object's, and children's, world transforms. The function may result in a
larger box than strictly necessary.

### setFromPoints

  
  
```ts  
function setFromPoints( points: Array ): this;  
```  

[points](#) - Array of [Vector3s](en\math\Vector3.html) that the resulting box
will contain.  
  
Sets the upper and lower bounds of this box to include all of the points in
[points](#).

### translate

  
  
```ts  
function translate( offset: Vector3 ): this;  
```  

[offset](en\math\Vector3.html) - Direction and distance of offset.  
  
Adds [offset](en\math\Vector3.html) to both the upper and lower bounds of this
box, effectively moving this box [offset](en\math\Vector3.html) units in 3D
space.

### union

  
  
```ts  
function union( box: Box3 ): this;  
```  

[box](en\math\Box3.html) - Box that will be unioned with this box.  
  
Computes the union of this box and [box](en\math\Box3.html), setting the upper
bound of this box to the greater of the two boxes' upper bounds and the lower
bound of this box to the lesser of the two boxes' lower bounds.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Box3.js">src/math/Box3.js</a>

