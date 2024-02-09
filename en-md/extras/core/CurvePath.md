[page:Curve] →

# [name]

An abstract base class extending [page:Curve]. A CurvePath is simply an array
of connected curves, but retains the api of a curve.

## Constructor

### [name]()

The constructor take no parameters.

## Properties

See the base [page:Curve] class for common properties.

### <br/> Array curves; <br/>

The array of [page:Curve Curves].

### <br/> Boolean autoClose; <br/>

Whether or not to automatically close the path.

## Methods

See the base [page:Curve] class for common methods.

### [method:undefined add]( [param:Curve curve] )

Add a curve to the [page:.curves] array.

### [method:undefined closePath]()

Adds a [page:LineCurve lineCurve] to close the path.

### [method:Array getCurveLengths]()

Get list of cumulative curve lengths of the curves in the [page:.curves]
array.

### [method:Array getPoints]( [param:Integer divisions] )

divisions -- number of pieces to divide the curve into. Default is `12`.  
  
Returns an array of points representing a sequence of curves. The `division`
parameter defines the number of pieces each curve is divided into. However,
for optimization and quality purposes, the actual sampling resolution for each
curve depends on its type. For example, for a [page:LineCurve], the returned
number of points is always just 2.

### [method:Array getSpacedPoints]( [param:Integer divisions] )

divisions -- number of pieces to divide the curve into. Default is `40`.  
  
Returns a set of divisions + 1 equi-spaced points using getPointAt( u ).

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

