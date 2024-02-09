# [name]

[name] contains spline and Bézier functions internally used by concrete curve
classes.

## Methods

### [method:Float CatmullRom]( [param:Float t], [param:Float p0], [param:Float
p1], [param:Float p2], [param:Float p3] )

t -- interpolation weight.  
p0, p1, p2, p3 -- the points defining the spline curve.  
  
Used internally by [page:SplineCurve SplineCurve].

### [method:Float QuadraticBezier]( [param:Float t], [param:Float p0],
[param:Float p1], [param:Float p2] )

t -- interpolation weight.  
p0, p1, p2 -- the starting, control and end points defining the curve.  
  
Used internally by [page:QuadraticBezierCurve3 QuadraticBezierCurve3] and
[page:QuadraticBezierCurve QuadraticBezierCurve].

### [method:Float CubicBezier]( [param:Float t], [param:Float p0],
[param:Float p1], [param:Float p2], [param:Float p3] )

t -- interpolation weight.  
p0, p1, p2, p3 -- the starting, control(twice) and end points defining the
curve.  
  
Used internally by [page:CubicBezierCurve3 CubicBezierCurve3] and
[page:CubicBezierCurve CubicBezierCurve].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

