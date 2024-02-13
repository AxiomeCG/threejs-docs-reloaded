# SphericalHarmonics3

Represents a third-order spherical harmonics (SH). Light probes use this class
to encode lighting information.

## Constructor

###  function SphericalHarmonics3( ): void;

Creates a new instance of SphericalHarmonics3.

## Properties

###  Array coefficients;

An array holding the (9) SH coefficients. A single coefficient is represented
as an instance of [page:Vector3].

###  Boolean isSphericalHarmonics3;

Read-only flag to check if a given object is of type SphericalHarmonics3.

## Methods

###  function add( sh: SphericalHarmonics3 ): this;

[page:SphericalHarmonics3 sh] - The SH to add.  
  
Adds the given SH to this instance.

###  function addScaledSH( sh: SphericalHarmonics3, scale: Number ): this;

[page:SphericalHarmonics3 sh] - The SH to add.  
[page:Number scale] - The scale factor.  
  
A convenience method for performing [page:.add]() and [page:.scale]() at once.

###  function clone( ): SphericalHarmonics3;

Returns a new instance of SphericalHarmonics3 with equal coefficients.

###  function copy( sh: SphericalHarmonics3 ): this;

[page:SphericalHarmonics3 sh] - The SH to copy.  
  
Copies the given SH to this instance.

###  function equals( sh: SphericalHarmonics3 ): Boolean;

[page:SphericalHarmonics3 sh] - The SH to compare with.  
  
Returns true if the given SH and this instance have equal coefficients.

###  function fromArray( array: Array, offset: Number ): this;

[page:Array array] - The array holding the numbers of the SH coefficients.  
[page:Number offset] - (optional) The array offset.  
  
Sets the coefficients of this instance from the given array.

###  function getAt( normal: Vector3, target: Vector3 ): Vector3;

[page:Vector3 normal] - The normal vector (assumed to be unit length).  
[page:Vector3 target] - The result vector.  
  
Returns the radiance in the direction of the given normal.

###  function getIrradianceAt( normal: Vector3, target: Vector3 ): Vector3;

[page:Vector3 normal] - The normal vector (assumed to be unit length).  
[page:Vector3 target] - The result vector.  
  
Returns the irradiance (radiance convolved with cosine lobe) in the direction
of the given normal.

###  function lerp( sh: SphericalHarmonics3, alpha: Number ): this;

[page:SphericalHarmonics3 sh] - The SH to interpolate with.  
[page:Number alpha] - The alpha factor.  
  
Linear interpolates between the given SH and this instance by the given alpha
factor.

###  function scale( scale: Number ): this;

[page:Number scale] - The scale factor.  
  
Scales this SH by the given scale factor.

###  function set( coefficients: Array ): this;

[page:Array coefficients] - An array of SH coefficients.  
  
Sets the given SH coefficients to this instance.

###  function toArray( array: Array, offset: Number ): Array;

[page:Array array] - (optional) The target array.  
[page:Number offset] - (optional) The array offset.  
  
Returns an array with the coefficients, or copies them into the provided
array. The coefficients are represented as numbers.

###  function zero( ): this;

Sets all SH coefficients to `0`.

## Static Methods

###  function getBasisAt( normal: Vector3, shBasis: Array ): undefined;

[page:Vector3 normal] - The normal vector (assumed to be unit length).  
[page:Array shBasis] - The resulting SH basis.  
  
Computes the SH basis for the given normal vector.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

