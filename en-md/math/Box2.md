# Box2

Represents an axis-aligned bounding box (AABB) in 2D space.

## Constructor

###  function Box2( min: Vector2, max: Vector2 ): void;

[page:Vector2 min] - (optional) [page:Vector2] representing the lower (x, y)
boundary of the box. Default is ( + Infinity, + Infinity ).  
[page:Vector2 max] - (optional) [page:Vector2] representing the upper (x, y)
boundary of the box. Default is ( - Infinity, - Infinity ).  
  
Creates a Box2 bounded by min and max.

## Properties

###  Vector2 min;

[page:Vector2] representing the lower (x, y) boundary of the box.  
Default is ( + Infinity, + Infinity ).

###  Vector2 max;

[page:Vector2] representing the lower upper (x, y) boundary of the box.  
Default is ( - Infinity, - Infinity ).

## Methods

###  function clampPoint( point: Vector2, target: Vector2 ): Vector2;

[page:Vector2 point] - [page:Vector2] to clamp.  
[page:Vector2 target] — the result will be copied into this Vector2.  
  
[link:https://en.wikipedia.org/wiki/Clamping_(graphics) Clamps] the
[page:Vector2 point] within the bounds of this box.  

###  function clone( ): Box2;

Returns a new [page:Box2] with the same [page:.min min] and [page:.max max] as
this one.

###  function containsBox( box: Box2 ): Boolean;

[page:Box2 box] - [page:Box2 Box2] to test for inclusion.  
  
Returns true if this box includes the entirety of [page:Box2 box]. If this and
[page:Box2 box] are identical,  
this function also returns true.

###  function containsPoint( point: Vector2 ): Boolean;

[page:Vector2 point] - [page:Vector2] to check for inclusion.  
  
Returns true if the specified [page:Vector2 point] lies within or on the
boundaries of this box.

###  function copy( box: Box2 ): this;

Copies the [page:.min min] and [page:.max max] from [page:Box2 box] to this
box.

###  function distanceToPoint( point: Vector2 ): Float;

[page:Vector2 point] - [page:Vector2] to measure distance to.  
  
Returns the distance from any edge of this box to the specified point. If the
[page:Vector2 point] lies inside of this box, the distance will be `0`.

###  function equals( box: Box2 ): Boolean;

[page:Box2 box] - Box to compare with this one.  
  
Returns true if this box and [page:Box2 box] share the same lower and upper
bounds.

###  function expandByPoint( point: Vector2 ): this;

[page:Vector2 point] - [page:Vector2] that should be included in the box.  
  
Expands the boundaries of this box to include [page:Vector2 point].

###  function expandByScalar( scalar: Float ): this;

[page:Float scalar] - Distance to expand the box by.  
  
Expands each dimension of the box by [page:Float scalar]. If negative, the
dimensions of the box will be contracted.

###  function expandByVector( vector: Vector2 ): this;

[page:Vector2 vector] - [page:Vector2] to expand the box by.  
  
Expands this box equilaterally by [page:Vector2 vector]. The width of this box
will be expanded by the x component of [page:Vector2 vector] in both
directions. The height of this box will be expanded by the y component of
[page:Vector2 vector] in both directions.

###  function getCenter( target: Vector2 ): Vector2;

[page:Vector2 target] — the result will be copied into this Vector2.  
  
Returns the center point of the box as a [page:Vector2].

###  function getParameter( point: Vector2, target: Vector2 ): Vector2;

[page:Vector2 point] - [page:Vector2].  
[page:Vector2 target] — the result will be copied into this Vector2.  
  
Returns a point as a proportion of this box's width and height.

###  function getSize( target: Vector2 ): Vector2;

[page:Vector2 target] — the result will be copied into this Vector2.  
  
Returns the width and height of this box.

###  function intersect( box: Box2 ): this;

[page:Box2 box] - Box to intersect with.  
  
Returns the intersection of this and [page:Box2 box], setting the upper bound
of this box to the lesser of the two boxes' upper bounds and the lower bound
of this box to the greater of the two boxes' lower bounds.

###  function intersectsBox( box: Box2 ): Boolean;

[page:Box2 box] - Box to check for intersection against.  
  
Determines whether or not this box intersects [page:Box2 box].

###  function isEmpty( ): Boolean;

Returns true if this box includes zero points within its bounds.  
Note that a box with equal lower and upper bounds still includes one point,
the one both bounds share.

###  function makeEmpty( ): this;

Makes this box empty.

###  function set( min: Vector2, max: Vector2 ): this;

[page:Vector2 min] - (required ) [page:Vector2] representing the lower (x, y)
boundary of the box.  
[page:Vector2 max] - (required) [page:Vector2] representing the upper (x, y)
boundary of the box.  
  
Sets the lower and upper (x, y) boundaries of this box.  
Please note that this method only copies the values from the given objects.

###  function setFromCenterAndSize( center: Vector2, size: Vector2 ): this;

[page:Vector2 center] - Desired center position of the box ([page:Vector2]).  
[page:Vector2 size] - Desired x and y dimensions of the box ([page:Vector2]).  
  
Centers this box on [page:Vector2 center] and sets this box's width and height
to the values specified in [page:Vector2 size].

###  function setFromPoints( points: Array ): this;

[page:Array points] - Array of [page:Vector2 Vector2s] that the resulting box
will contain.  
  
Sets the upper and lower bounds of this box to include all of the points in
[page:Array points].

###  function translate( offset: Vector2 ): this;

[page:Vector2 offset] - Direction and distance of offset.  
  
Adds [page:Vector2 offset] to both the upper and lower bounds of this box,
effectively moving this box [page:Vector2 offset] units in 2D space.

###  function union( box: Box2 ): this;

[page:Box2 box] - Box that will be unioned with this box.  
  
Unions this box with [page:Box2 box], setting the upper bound of this box to
the greater of the two boxes' upper bounds and the lower bound of this box to
the lesser of the two boxes' lower bounds.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

