# [name]

Represents a third-order spherical harmonics (SH). Light probes use this class
to encode lighting information.

## Constructor

### [name]()

Creates a new instance of [name].

## Properties

### <br/> Array coefficients; <br/>

An array holding the (9) SH coefficients. A single coefficient is represented
as an instance of [page:Vector3].

### <br/> Boolean isSphericalHarmonics3; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

### <br/> function add( sh: SphericalHarmonics3 ): add; <br/>

[page:SphericalHarmonics3 sh] - The SH to add.  
  
Adds the given SH to this instance.

### <br/> function addScaledSH( sh: SphericalHarmonics3, scale: Number ):
addScaledSH; <br/>

[page:SphericalHarmonics3 sh] - The SH to add.  
[page:Number scale] - The scale factor.  
  
A convenience method for performing [page:.add]() and [page:.scale]() at once.

### [method:SphericalHarmonics3 clone]()

Returns a new instance of [name] with equal coefficients.

### <br/> function copy( sh: SphericalHarmonics3 ): copy; <br/>

[page:SphericalHarmonics3 sh] - The SH to copy.  
  
Copies the given SH to this instance.

### [method:Boolean equals]( [param:SphericalHarmonics3 sh] )

[page:SphericalHarmonics3 sh] - The SH to compare with.  
  
Returns true if the given SH and this instance have equal coefficients.

### <br/> function fromArray( array: Array, offset: Number ): fromArray; <br/>

[page:Array array] - The array holding the numbers of the SH coefficients.  
[page:Number offset] - (optional) The array offset.  
  
Sets the coefficients of this instance from the given array.

###  [method:Vector3 getAt]( [param:Vector3 normal], [param:Vector3 target] )

[page:Vector3 normal] - The normal vector (assumed to be unit length).  
[page:Vector3 target] - The result vector.  
  
Returns the radiance in the direction of the given normal.

###  [method:Vector3 getIrradianceAt]( [param:Vector3 normal], [param:Vector3
target] )

[page:Vector3 normal] - The normal vector (assumed to be unit length).  
[page:Vector3 target] - The result vector.  
  
Returns the irradiance (radiance convolved with cosine lobe) in the direction
of the given normal.

### <br/> function lerp( sh: SphericalHarmonics3, alpha: Number ): lerp; <br/>

[page:SphericalHarmonics3 sh] - The SH to interpolate with.  
[page:Number alpha] - The alpha factor.  
  
Linear interpolates between the given SH and this instance by the given alpha
factor.

### <br/> function scale( scale: Number ): scale; <br/>

[page:Number scale] - The scale factor.  
  
Scales this SH by the given scale factor.

### <br/> function set( coefficients: Array ): set; <br/>

[page:Array coefficients] - An array of SH coefficients.  
  
Sets the given SH coefficients to this instance.

###  [method:Array toArray]( [param:Array array], [param:Number offset] )

[page:Array array] - (optional) The target array.  
[page:Number offset] - (optional) The array offset.  
  
Returns an array with the coefficients, or copies them into the provided
array. The coefficients are represented as numbers.

### <br/> function zero( ): zero; <br/>

Sets all SH coefficients to `0`.

## Static Methods

###  [method:undefined getBasisAt]( [param:Vector3 normal], [param:Array
shBasis] )

[page:Vector3 normal] - The normal vector (assumed to be unit length).  
[page:Array shBasis] - The resulting SH basis.  
  
Computes the SH basis for the given normal vector.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

