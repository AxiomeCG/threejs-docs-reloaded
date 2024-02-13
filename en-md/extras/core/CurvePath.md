[page:Curve] →

# CurvePath

An abstract base class extending [page:Curve]. A CurvePath is simply an array
of connected curves, but retains the api of a curve.

## Constructor

###  function CurvePath( ): void;

The constructor take no parameters.

## Properties

See the base [page:Curve] class for common properties.

###  Array curves;

The array of [page:Curve Curves].

###  Boolean autoClose;

Whether or not to automatically close the path.

## Methods

See the base [page:Curve] class for common methods.

###  function add( curve: Curve ): undefined;

Add a curve to the [page:.curves] array.

###  function closePath( ): undefined;

Adds a [page:LineCurve lineCurve] to close the path.

###  function getCurveLengths( ): Array;

Get list of cumulative curve lengths of the curves in the [page:.curves]
array.

###  function getPoints( divisions: Integer ): Array;

divisions -- number of pieces to divide the curve into. Default is `12`.  
  
Returns an array of points representing a sequence of curves. The `division`
parameter defines the number of pieces each curve is divided into. However,
for optimization and quality purposes, the actual sampling resolution for each
curve depends on its type. For example, for a [page:LineCurve], the returned
number of points is always just 2.

###  function getSpacedPoints( divisions: Integer ): Array;

divisions -- number of pieces to divide the curve into. Default is `40`.  
  
Returns a set of divisions + 1 equi-spaced points using getPointAt( u ).

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

