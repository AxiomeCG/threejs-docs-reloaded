# Box2

Represents an axis-aligned bounding box (AABB) in 2D space.

## Constructor

### Box2

  
  
```ts  
function Box2( min: Vector2, max: Vector2 ): void;  
```  

[min](en\math\Vector2.html) - (optional) [Vector2](en\math\Vector2.html)
representing the lower (x, y) boundary of the box. Default is ( + Infinity, +
Infinity ).  
[max](en\math\Vector2.html) - (optional) [Vector2](en\math\Vector2.html)
representing the upper (x, y) boundary of the box. Default is ( - Infinity, -
Infinity ).  
  
Creates a Box2 bounded by min and max.

## Properties

### min

  
  
```ts  
min: Vector2;  
```  

[Vector2](en\math\Vector2.html) representing the lower (x, y) boundary of the
box.  
Default is ( + Infinity, + Infinity ).

### max

  
  
```ts  
max: Vector2;  
```  

[Vector2](en\math\Vector2.html) representing the lower upper (x, y) boundary
of the box.  
Default is ( - Infinity, - Infinity ).

## Methods

### clampPoint

  
  
```ts  
function clampPoint( point: Vector2, target: Vector2 ): Vector2;  
```  

[point](en\math\Vector2.html) - [Vector2](en\math\Vector2.html) to clamp.  
[target](en\math\Vector2.html) — the result will be copied into this Vector2.  
  
<a href="https://en.wikipedia.org/wiki/Clamping_(graphics)">Clamps</a> the
[point](en\math\Vector2.html) within the bounds of this box.  

### clone

  
  
```ts  
function clone( ): Box2;  
```  

Returns a new [Box2](en\math\Box2.html) with the same [.min](#min) and
[.max](#max) as this one.

### containsBox

  
  
```ts  
function containsBox( box: Box2 ): Boolean;  
```  

[box](en\math\Box2.html) - [Box2](en\math\Box2.html) to test for inclusion.  
  
Returns true if this box includes the entirety of [box](en\math\Box2.html). If
this and [box](en\math\Box2.html) are identical,  
this function also returns true.

### containsPoint

  
  
```ts  
function containsPoint( point: Vector2 ): Boolean;  
```  

[point](en\math\Vector2.html) - [Vector2](en\math\Vector2.html) to check for
inclusion.  
  
Returns true if the specified [point](en\math\Vector2.html) lies within or on
the boundaries of this box.

### copy

  
  
```ts  
function copy( box: Box2 ): this;  
```  

Copies the [.min](#min) and [.max](#max) from [.ox2](#ox2) to this box.

### distanceToPoint

  
  
```ts  
function distanceToPoint( point: Vector2 ): Float;  
```  

[point](en\math\Vector2.html) - [Vector2](en\math\Vector2.html) to measure
distance to.  
  
Returns the distance from any edge of this box to the specified point. If the
[point](en\math\Vector2.html) lies inside of this box, the distance will be
`0`.

### equals

  
  
```ts  
function equals( box: Box2 ): Boolean;  
```  

[box](en\math\Box2.html) - Box to compare with this one.  
  
Returns true if this box and [box](en\math\Box2.html) share the same lower and
upper bounds.

### expandByPoint

  
  
```ts  
function expandByPoint( point: Vector2 ): this;  
```  

[point](en\math\Vector2.html) - [Vector2](en\math\Vector2.html) that should be
included in the box.  
  
Expands the boundaries of this box to include [point](en\math\Vector2.html).

### expandByScalar

  
  
```ts  
function expandByScalar( scalar: Float ): this;  
```  

[scalar](#) - Distance to expand the box by.  
  
Expands each dimension of the box by [scalar](#). If negative, the dimensions
of the box will be contracted.

### expandByVector

  
  
```ts  
function expandByVector( vector: Vector2 ): this;  
```  

[vector](en\math\Vector2.html) - [Vector2](en\math\Vector2.html) to expand the
box by.  
  
Expands this box equilaterally by [vector](en\math\Vector2.html). The width of
this box will be expanded by the x component of [vector](en\math\Vector2.html)
in both directions. The height of this box will be expanded by the y component
of [vector](en\math\Vector2.html) in both directions.

### getCenter

  
  
```ts  
function getCenter( target: Vector2 ): Vector2;  
```  

[target](en\math\Vector2.html) — the result will be copied into this Vector2.  
  
Returns the center point of the box as a [Vector2](en\math\Vector2.html).

### getParameter

  
  
```ts  
function getParameter( point: Vector2, target: Vector2 ): Vector2;  
```  

[point](en\math\Vector2.html) - [Vector2](en\math\Vector2.html).  
[target](en\math\Vector2.html) — the result will be copied into this Vector2.  
  
Returns a point as a proportion of this box's width and height.

### getSize

  
  
```ts  
function getSize( target: Vector2 ): Vector2;  
```  

[target](en\math\Vector2.html) — the result will be copied into this Vector2.  
  
Returns the width and height of this box.

### intersect

  
  
```ts  
function intersect( box: Box2 ): this;  
```  

[box](en\math\Box2.html) - Box to intersect with.  
  
Returns the intersection of this and [box](en\math\Box2.html), setting the
upper bound of this box to the lesser of the two boxes' upper bounds and the
lower bound of this box to the greater of the two boxes' lower bounds.

### intersectsBox

  
  
```ts  
function intersectsBox( box: Box2 ): Boolean;  
```  

[box](en\math\Box2.html) - Box to check for intersection against.  
  
Determines whether or not this box intersects [box](en\math\Box2.html).

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
function set( min: Vector2, max: Vector2 ): this;  
```  

[min](en\math\Vector2.html) - (required ) [Vector2](en\math\Vector2.html)
representing the lower (x, y) boundary of the box.  
[max](en\math\Vector2.html) - (required) [Vector2](en\math\Vector2.html)
representing the upper (x, y) boundary of the box.  
  
Sets the lower and upper (x, y) boundaries of this box.  
Please note that this method only copies the values from the given objects.

### setFromCenterAndSize

  
  
```ts  
function setFromCenterAndSize( center: Vector2, size: Vector2 ): this;  
```  

[center](en\math\Vector2.html) - Desired center position of the box
([Vector2](en\math\Vector2.html)).  
[size](en\math\Vector2.html) - Desired x and y dimensions of the box
([Vector2](en\math\Vector2.html)).  
  
Centers this box on [center](en\math\Vector2.html) and sets this box's width
and height to the values specified in [size](en\math\Vector2.html).

### setFromPoints

  
  
```ts  
function setFromPoints( points: Array ): this;  
```  

[points](#) - Array of [Vector2s](en\math\Vector2.html) that the resulting box
will contain.  
  
Sets the upper and lower bounds of this box to include all of the points in
[points](#).

### translate

  
  
```ts  
function translate( offset: Vector2 ): this;  
```  

[offset](en\math\Vector2.html) - Direction and distance of offset.  
  
Adds [offset](en\math\Vector2.html) to both the upper and lower bounds of this
box, effectively moving this box [offset](en\math\Vector2.html) units in 2D
space.

### union

  
  
```ts  
function union( box: Box2 ): this;  
```  

[box](en\math\Box2.html) - Box that will be unioned with this box.  
  
Unions this box with [box](en\math\Box2.html), setting the upper bound of this
box to the greater of the two boxes' upper bounds and the lower bound of this
box to the lesser of the two boxes' lower bounds.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Box2.js">src/math/Box2.js</a>

