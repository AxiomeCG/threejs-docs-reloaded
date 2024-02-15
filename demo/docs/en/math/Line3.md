# Line3

A geometric line segment represented by a start and end point.

## Constructor

### Line3

  
  
```ts  
function Line3( start: Vector3, end: Vector3 ): void;  
```  

[start](en\math\Vector3.html) - Start of the line segment. Default is `(0, 0,
0)`.  
[end](en\math\Vector3.html) - End of the line segment. Default is `(0, 0, 0)`.  
  
Creates a new Line3.

## Properties

### start

  
  
```ts  
start: Vector3;  
```  

[Vector3](en\math\Vector3.html) representing the start point of the line.

### end

  
  
```ts  
end: Vector3;  
```  

[Vector3](en\math\Vector3.html) representing the end point of the line.

## Methods

### applyMatrix4

  
  
```ts  
function applyMatrix4( matrix: Matrix4 ): this;  
```  

Applies a matrix transform to the line segment.

### at

  
  
```ts  
function at( t: Float, target: Vector3 ): Vector3;  
```  

[t](#) - Use values 0-1 to return a position along the line segment.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns a vector at a certain position along the line. When [t](#) = 0, it
returns the start vector, and when [t](#) = 1 it returns the end vector.  

### clone

  
  
```ts  
function clone( ): Line3;  
```  

Returns a new [Line3](en\math\Line3.html) with the same [.start](#start) and
[.end](#end) vectors as this one.

### closestPointToPoint

  
  
```ts  
function closestPointToPoint( point: Vector3, clampToLine: Boolean, target:
Vector3 ): Vector3;  
```  

[point](en\math\Vector3.html) - return the closest point on the line to this
point.  
[clampToLine](#) - whether to clamp the returned value to the line segment.  
[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns the closets point on the line. If [clampToLine](#) is true, then the
returned value will be clamped to the line segment.

### closestPointToPointParameter

  
  
```ts  
function closestPointToPointParameter( point: Vector3, clampToLine: Boolean ):
Float;  
```  

[point](en\math\Vector3.html) - the point for which to return a point
parameter.  
[clampToLine](#) - Whether to clamp the result to the range `[0, 1]`.  
  
Returns a point parameter based on the closest point as projected on the line
segment. If [clampToLine](#) is true, then the returned value will be between
`0` and `1`.

### copy

  
  
```ts  
function copy( line: Line3 ): this;  
```  

Copies the passed line's [.start](#start) and [.end](#end) vectors to this
line.

### delta

  
  
```ts  
function delta( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns the delta vector of the line segment ( [.end](#end) vector minus the
[.start](#start) vector).

### distance

  
  
```ts  
function distance( ): Float;  
```  

Returns the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a>
(straight-line distance) between the line's [.start](#start) and [.end](#end)
points.

### distanceSq

  
  
```ts  
function distanceSq( ): Float;  
```  

Returns the square of the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a>
(straight-line distance) between the line's [.start](#start) and [.end](#end)
vectors.

### equals

  
  
```ts  
function equals( line: Line3 ): Boolean;  
```  

[line](en\math\Line3.html) - [Line3](en\math\Line3.html) to compare with this
one.  
  
Returns true if both line's [.start](#start) and [.end](#end) points are
equal.

### getCenter

  
  
```ts  
function getCenter( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns the center of the line segment.

### set

  
  
```ts  
function set( start: Vector3, end: Vector3 ): this;  
```  

[.ector3](#ector3) - set the [.start](#start) of the line.  
[.ector3](#ector3) - set the [.end](#end) of the line.  
  
Sets the start and end values by copying the provided vectors.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Line3.js">src/math/Line3.js</a>

