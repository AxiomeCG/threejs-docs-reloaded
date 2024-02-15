# SphericalHarmonics3

Represents a third-order spherical harmonics (SH). Light probes use this class
to encode lighting information.

## Constructor

### SphericalHarmonics3

  
  
```ts  
function SphericalHarmonics3( ): void;  
```  

Creates a new instance of SphericalHarmonics3.

## Properties

### coefficients

  
  
```ts  
coefficients: Array;  
```  

An array holding the (9) SH coefficients. A single coefficient is represented
as an instance of [Vector3](en\math\Vector3.html).

### isSphericalHarmonics3

  
  
```ts  
isSphericalHarmonics3: Boolean;  
```  

Read-only flag to check if a given object is of type SphericalHarmonics3.

## Methods

### add

  
  
```ts  
function add( sh: SphericalHarmonics3 ): this;  
```  

[sh](en\math\SphericalHarmonics3.html) - The SH to add.  
  
Adds the given SH to this instance.

### addScaledSH

  
  
```ts  
function addScaledSH( sh: SphericalHarmonics3, scale: Number ): this;  
```  

[sh](en\math\SphericalHarmonics3.html) - The SH to add.  
[scale](#) - The scale factor.  
  
A convenience method for performing [.add](#)() and [.scale](#)() at once.

### clone

  
  
```ts  
function clone( ): SphericalHarmonics3;  
```  

Returns a new instance of SphericalHarmonics3 with equal coefficients.

### copy

  
  
```ts  
function copy( sh: SphericalHarmonics3 ): this;  
```  

[sh](en\math\SphericalHarmonics3.html) - The SH to copy.  
  
Copies the given SH to this instance.

### equals

  
  
```ts  
function equals( sh: SphericalHarmonics3 ): Boolean;  
```  

[sh](en\math\SphericalHarmonics3.html) - The SH to compare with.  
  
Returns true if the given SH and this instance have equal coefficients.

### fromArray

  
  
```ts  
function fromArray( array: Array, offset: Number ): this;  
```  

[array](#) - The array holding the numbers of the SH coefficients.  
[offset](#) - (optional) The array offset.  
  
Sets the coefficients of this instance from the given array.

### getAt

  
  
```ts  
function getAt( normal: Vector3, target: Vector3 ): Vector3;  
```  

[normal](en\math\Vector3.html) - The normal vector (assumed to be unit
length).  
[target](en\math\Vector3.html) - The result vector.  
  
Returns the radiance in the direction of the given normal.

### getIrradianceAt

  
  
```ts  
function getIrradianceAt( normal: Vector3, target: Vector3 ): Vector3;  
```  

[normal](en\math\Vector3.html) - The normal vector (assumed to be unit
length).  
[target](en\math\Vector3.html) - The result vector.  
  
Returns the irradiance (radiance convolved with cosine lobe) in the direction
of the given normal.

### lerp

  
  
```ts  
function lerp( sh: SphericalHarmonics3, alpha: Number ): this;  
```  

[sh](en\math\SphericalHarmonics3.html) - The SH to interpolate with.  
[alpha](#) - The alpha factor.  
  
Linear interpolates between the given SH and this instance by the given alpha
factor.

### scale

  
  
```ts  
function scale( scale: Number ): this;  
```  

[scale](#) - The scale factor.  
  
Scales this SH by the given scale factor.

### set

  
  
```ts  
function set( coefficients: Array ): this;  
```  

[coefficients](#) - An array of SH coefficients.  
  
Sets the given SH coefficients to this instance.

### toArray

  
  
```ts  
function toArray( array: Array, offset: Number ): Array;  
```  

[array](#) - (optional) The target array.  
[offset](#) - (optional) The array offset.  
  
Returns an array with the coefficients, or copies them into the provided
array. The coefficients are represented as numbers.

### zero

  
  
```ts  
function zero( ): this;  
```  

Sets all SH coefficients to `0`.

## Static Methods

### getBasisAt

  
  
```ts  
function getBasisAt( normal: Vector3, shBasis: Array ): undefined;  
```  

[normal](en\math\Vector3.html) - The normal vector (assumed to be unit
length).  
[shBasis](#) - The resulting SH basis.  
  
Computes the SH basis for the given normal vector.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/SphericalHarmonics3.js">src/math/SphericalHarmonics3.js</a>

