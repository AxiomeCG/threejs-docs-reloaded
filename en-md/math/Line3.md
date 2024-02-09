# [name]

A geometric line segment represented by a start and end point.

## Constructor

### [name]( [param:Vector3 start], [param:Vector3 end] )

[page:Vector3 start] - Start of the line segment. Default is `(0, 0, 0)`.  
[page:Vector3 end] - End of the line segment. Default is `(0, 0, 0)`.  
  
Creates a new [name].

## Properties

### <br/> Vector3 start; <br/>

[page:Vector3] representing the start point of the line.

### <br/> Vector3 end; <br/>

[page:Vector3] representing the end point of the line.

## Methods

### <br/> function applyMatrix4( matrix: Matrix4 ): applyMatrix4; <br/>

Applies a matrix transform to the line segment.

### [method:Vector3 at]( [param:Float t], [param:Vector3 target] )

[page:Float t] - Use values 0-1 to return a position along the line segment.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a vector at a certain position along the line. When [page:Float t] =
0, it returns the start vector, and when [page:Float t] = 1 it returns the end
vector.  

### [method:Line3 clone]()

Returns a new [page:Line3] with the same [page:.start start] and [page:.end
end] vectors as this one.

###  [method:Vector3 closestPointToPoint]( [param:Vector3 point],
[param:Boolean clampToLine], [param:Vector3 target] )

[page:Vector3 point] - return the closest point on the line to this point.  
[page:Boolean clampToLine] - whether to clamp the returned value to the line
segment.  
[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the closets point on the line. If [page:Boolean clampToLine] is true,
then the returned value will be clamped to the line segment.

###  [method:Float closestPointToPointParameter]( [param:Vector3 point],
[param:Boolean clampToLine] )

[page:Vector3 point] - the point for which to return a point parameter.  
[page:Boolean clampToLine] - Whether to clamp the result to the range `[0,
1]`.  
  
Returns a point parameter based on the closest point as projected on the line
segment. If [page:Boolean clampToLine] is true, then the returned value will
be between `0` and `1`.

### <br/> function copy( line: Line3 ): copy; <br/>

Copies the passed line's [page:.start start] and [page:.end end] vectors to
this line.

### [method:Vector3 delta]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the delta vector of the line segment ( [page:.end end] vector minus
the [page:.start start] vector).

### [method:Float distance]()

Returns the [link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean
distance] (straight-line distance) between the line's [page:.start start] and
[page:.end end] points.

### [method:Float distanceSq]()

Returns the square of the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance]
(straight-line distance) between the line's [page:.start start] and [page:.end
end] vectors.

### [method:Boolean equals]( [param:Line3 line] )

[page:Line3 line] - [page:Line3] to compare with this one.  
  
Returns true if both line's [page:.start start] and [page:.end end] points are
equal.

### [method:Vector3 getCenter]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns the center of the line segment.

### <br/> function set( start: Vector3, end: Vector3 ): set; <br/>

[page:Vector3 start] - set the [page:.start start point] of the line.  
[page:Vector3 end] - set the [page:.end end point] of the line.  
  
Sets the start and end values by copying the provided vectors.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

