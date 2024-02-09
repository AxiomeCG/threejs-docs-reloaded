[page:Interpolant] →

# [name]

## Code Example

  
```ts  
const interpolant = new THREE.[name](  
new Float32Array( 2 ),  
new Float32Array( 2 ),  
1,  
new Float32Array( 1 )  
);  
  
interpolant.evaluate( 0.5 );  
```  

## Constructor

###  [name]( parameterPositions, sampleValues, sampleSize, resultBuffer )

parameterPositions -- array of positions  
sampleValues -- array of samples  
sampleSize -- number of samples  
resultBuffer -- buffer to store the interpolation results.  
  

## Properties

### <br/> null parameterPositions; <br/>

### <br/> null resultBuffer; <br/>

### <br/> null sampleValues; <br/>

### <br/> Object settings; <br/>

### <br/> null valueSize; <br/>

## Methods

### [method:Array evaluate]( [param:Number t] )

Evaluate the interpolant at position *t*.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

