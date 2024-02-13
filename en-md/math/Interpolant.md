# Interpolant

Abstract base class of interpolants over parametric samples.  
  
The parameter domain is one dimensional, typically the time or a path along a
curve defined by the data.  
  
The sample values can have any dimensionality and derived classes may apply
special interpretations to the data.  
  
This class provides the interval seek in a Template Method, deferring the
actual interpolation to derived classes.  
  
Time complexity is `O(1)` for linear access crossing at most two points and
`O(log N)` for random access, where *N* is the number of positions.  
  
References: [link:http://www.oodesign.com/template-method-pattern.html
http://www.oodesign.com/template-method-pattern.html]

## Constructor

###  function Interpolant( ): void;

parameterPositions -- array of positions  
sampleValues -- array of samples  
sampleSize -- number of samples  
resultBuffer -- buffer to store the interpolation results.  
  
Note: This is not designed to be called directly.

## Properties

###  null parameterPositions;

###  null resultBuffer;

###  null sampleValues;

###  Object settings;

Optional, subclass-specific settings structure.

###  null valueSize;

## Methods

###  function evaluate( t: Number ): Array;

Evaluate the interpolant at position *t*.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

