# Interpolations

Interpolations contains spline and Bézier functions internally used by
concrete curve classes.

## Methods

###  function CatmullRom( t: Float, p0: Float, p1: Float, p2: Float, p3: Float
): Float;

t -- interpolation weight.  
p0, p1, p2, p3 -- the points defining the spline curve.  
  
Used internally by [page:SplineCurve SplineCurve].

###  function QuadraticBezier( t: Float, p0: Float, p1: Float, p2: Float ):
Float;

t -- interpolation weight.  
p0, p1, p2 -- the starting, control and end points defining the curve.  
  
Used internally by [page:QuadraticBezierCurve3 QuadraticBezierCurve3] and
[page:QuadraticBezierCurve QuadraticBezierCurve].

###  function CubicBezier( t: Float, p0: Float, p1: Float, p2: Float, p3:
Float ): Float;

t -- interpolation weight.  
p0, p1, p2, p3 -- the starting, control(twice) and end points defining the
curve.  
  
Used internally by [page:CubicBezierCurve3 CubicBezierCurve3] and
[page:CubicBezierCurve CubicBezierCurve].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

