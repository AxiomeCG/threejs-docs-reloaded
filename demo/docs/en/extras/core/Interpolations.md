# Interpolations

Interpolations contains spline and Bézier functions internally used by
concrete curve classes.

## Methods

### CatmullRom

  
  
```ts  
function CatmullRom( t: Float, p0: Float, p1: Float, p2: Float, p3: Float ):
Float;  
```  

t -- interpolation weight.  
p0, p1, p2, p3 -- the points defining the spline curve.  
  
Used internally by [SplineCurve](en\extras\curves\SplineCurve.html).

### QuadraticBezier

  
  
```ts  
function QuadraticBezier( t: Float, p0: Float, p1: Float, p2: Float ): Float;  
```  

t -- interpolation weight.  
p0, p1, p2 -- the starting, control and end points defining the curve.  
  
Used internally by
[QuadraticBezierCurve3](en\extras\curves\QuadraticBezierCurve3.html) and
[QuadraticBezierCurve](en\extras\curves\QuadraticBezierCurve.html).

### CubicBezier

  
  
```ts  
function CubicBezier( t: Float, p0: Float, p1: Float, p2: Float, p3: Float ):
Float;  
```  

t -- interpolation weight.  
p0, p1, p2, p3 -- the starting, control(twice) and end points defining the
curve.  
  
Used internally by
[CubicBezierCurve3](en\extras\curves\CubicBezierCurve3.html) and
[CubicBezierCurve](en\extras\curves\CubicBezierCurve.html).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/core/Interpolations.js">src/extras/core/Interpolations.js</a>

