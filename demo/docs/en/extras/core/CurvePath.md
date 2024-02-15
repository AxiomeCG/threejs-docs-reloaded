[Curve](en\extras\core\Curve.html) →

# CurvePath

An abstract base class extending [Curve](en\extras\core\Curve.html). A
CurvePath is simply an array of connected curves, but retains the api of a
curve.

## Constructor

### CurvePath

  
  
```ts  
function CurvePath( ): void;  
```  

The constructor take no parameters.

## Properties

See the base [Curve](en\extras\core\Curve.html) class for common properties.

### curves

  
  
```ts  
curves: Array;  
```  

The array of [Curves](en\extras\core\Curve.html).

### autoClose

  
  
```ts  
autoClose: Boolean;  
```  

Whether or not to automatically close the path.

## Methods

See the base [Curve](en\extras\core\Curve.html) class for common methods.

### add

  
  
```ts  
function add( curve: Curve ): undefined;  
```  

Add a curve to the [.curves](#) array.

### closePath

  
  
```ts  
function closePath( ): undefined;  
```  

Adds a [lineCurve](en\extras\curves\LineCurve.html) to close the path.

### getCurveLengths

  
  
```ts  
function getCurveLengths( ): Array;  
```  

Get list of cumulative curve lengths of the curves in the [.curves](#) array.

### getPoints

  
  
```ts  
function getPoints( divisions: Integer ): Array;  
```  

divisions -- number of pieces to divide the curve into. Default is `12`.  
  
Returns an array of points representing a sequence of curves. The `division`
parameter defines the number of pieces each curve is divided into. However,
for optimization and quality purposes, the actual sampling resolution for each
curve depends on its type. For example, for a
[LineCurve](en\extras\curves\LineCurve.html), the returned number of points is
always just 2.

### getSpacedPoints

  
  
```ts  
function getSpacedPoints( divisions: Integer ): Array;  
```  

divisions -- number of pieces to divide the curve into. Default is `40`.  
  
Returns a set of divisions + 1 equi-spaced points using getPointAt( u ).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/core/CurvePath.js">src/extras/core/CurvePath.js</a>

