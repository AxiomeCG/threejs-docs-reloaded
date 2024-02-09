# [name]

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

###  [name]( parameterPositions, sampleValues, sampleSize, resultBuffer )

parameterPositions -- array of positions  
sampleValues -- array of samples  
sampleSize -- number of samples  
resultBuffer -- buffer to store the interpolation results.  
  
Note: This is not designed to be called directly.

## Properties

### <br/> null parameterPositions; <br/>

### <br/> null resultBuffer; <br/>

### <br/> null sampleValues; <br/>

### <br/> Object settings; <br/>

Optional, subclass-specific settings structure.

### <br/> null valueSize; <br/>

## Methods

### [method:Array evaluate]( [param:Number t] )

Evaluate the interpolant at position *t*.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

