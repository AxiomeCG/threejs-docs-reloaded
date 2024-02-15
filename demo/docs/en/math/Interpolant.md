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
  
References: <a href="http://www.oodesign.com/template-method-
pattern.html">http://www.oodesign.com/template-method-pattern.html</a>

## Constructor

### Interpolant

  
  
```ts  
function Interpolant( ): void;  
```  

parameterPositions -- array of positions  
sampleValues -- array of samples  
sampleSize -- number of samples  
resultBuffer -- buffer to store the interpolation results.  
  
Note: This is not designed to be called directly.

## Properties

### parameterPositions

  
  
```ts  
parameterPositions: null;  
```  

### resultBuffer

  
  
```ts  
resultBuffer: null;  
```  

### sampleValues

  
  
```ts  
sampleValues: null;  
```  

### settings

  
  
```ts  
settings: Object;  
```  

Optional, subclass-specific settings structure.

### valueSize

  
  
```ts  
valueSize: null;  
```  

## Methods

### evaluate

  
  
```ts  
function evaluate( t: Number ): Array;  
```  

Evaluate the interpolant at position *t*.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Interpolant.js">src/math/Interpolant.js</a>

