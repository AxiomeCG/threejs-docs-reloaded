# Line3

A geometric line segment represented by a start and end point.

## Constructor

###  function Line3( start: Vector3, end: Vector3 ): void;

[page:Vector3 start] - Start of the line segment. Default is `(0, 0, 0)`.  
[page:Vector3 end] - End of the line segment. Default is `(0, 0, 0)`.  
  
Creates a new Line3.

## Properties

###  Vector3 start;

[page:Vector3] representing the start point of the line.

###  Vector3 end;

[page:Vector3] representing the end point of the line.

## Methods

###  function applyMatrix4( matrix: Matrix4 ): this;

Applies a matrix transform to the line segment.

###  function at( t: Float, target: Vector3 ): Vector3;

[page:Float t] - Use values 0-1 to return a position along the line segment.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a vector at a certain position along the line. When [page:Float t] =
0, it returns the start vector, and when [page:Float t] = 1 it returns the end
vector.  

###  function clone( ): Line3;

Returns a new [page:Line3] with the same [page:.start start] and [page:.end
end] vectors as this one.

###  function closestPointToPoint( point: Vector3, clampToLine: Boolean,
target: Vector3 ): Vector3;

[page:Vector3 point] - return the closest point on the line to this point.  
[page:Boolean clampToLine] - whether to clamp the returned value to the line
segment.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the closets point on the line. If [page:Boolean clampToLine] is true,
then the returned value will be clamped to the line segment.

###  function closestPointToPointParameter( point: Vector3, clampToLine:
Boolean ): Float;

[page:Vector3 point] - the point for which to return a point parameter.  
[page:Boolean clampToLine] - Whether to clamp the result to the range `[0,
1]`.  
  
Returns a point parameter based on the closest point as projected on the line
segment. If [page:Boolean clampToLine] is true, then the returned value will
be between `0` and `1`.

###  function copy( line: Line3 ): this;

Copies the passed line's [page:.start start] and [page:.end end] vectors to
this line.

###  function delta( target: Vector3 ): Vector3;

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the delta vector of the line segment ( [page:.end end] vector minus
the [page:.start start] vector).

###  function distance( ): Float;

Returns the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
distance] (straight-line distance) between the line's [page:.start start] and
[page:.end end] points.

###  function distanceSq( ): Float;

Returns the square of the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance]
(straight-line distance) between the line's [page:.start start] and [page:.end
end] vectors.

###  function equals( line: Line3 ): Boolean;

[page:Line3 line] - [page:Line3] to compare with this one.  
  
Returns true if both line's [page:.start start] and [page:.end end] points are
equal.

###  function getCenter( target: Vector3 ): Vector3;

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the center of the line segment.

###  function set( start: Vector3, end: Vector3 ): this;

[page:Vector3 start] - set the [page:.start start point] of the line.  
[page:Vector3 end] - set the [page:.end end point] of the line.  
  
Sets the start and end values by copying the provided vectors.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

