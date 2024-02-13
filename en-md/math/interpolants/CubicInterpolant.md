[page:Interpolant] →

# CubicInterpolant

## Code Example

  
```ts  
  
function CubicInterpolant( ): void;  
  
```  

## Constructor

###  function CubicInterpolant( ): void;

parameterPositions -- array of positions  
sampleValues -- array of samples  
sampleSize -- number of samples  
resultBuffer -- buffer to store the interpolation results.  
  

## Properties

###  null parameterPositions;

###  null resultBuffer;

###  null sampleValues;

###  Object settings;

###  null valueSize;

## Methods

###  function evaluate( t: Number ): Array;

Evaluate the interpolant at position *t*.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

