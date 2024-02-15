[Interpolant](en\math\Interpolant.html) →

# LinearInterpolant

## Code Example

  
```ts  
const interpolant = new THREE.LinearInterpolant( new Float32Array( 2 ), new
Float32Array( 2 ), 1, new Float32Array( 1 ));interpolant.evaluate( 0.5 );  
```  

## Constructor

### LinearInterpolant

  
  
```ts  
function LinearInterpolant( ): void;  
```  

parameterPositions -- array of positions  
sampleValues -- array of samples  
sampleSize -- number of samples  
resultBuffer -- buffer to store the interpolation results.  
  

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
href="https://github.com/mrdoob/three.js/blob/master/src/math/interpolants/LinearInterpolant.js">src/math/interpolants/LinearInterpolant.js</a>

