[KeyframeTrack](en\animation\KeyframeTrack.html) →

# QuaternionKeyframeTrack

A Track of quaternion keyframe values.

## Constructor

### QuaternionKeyframeTrack

  
  
```ts  
function QuaternionKeyframeTrack( name: String, times: Array, values: Array ):
void;  
```  

[name](#) (required) identifier for the KeyframeTrack.  
[times](#) (required) array of keyframe times.  
[values](#) values for the keyframes at the times specified, a flat array of
quaternion components.  
[interpolation](#) the type of interpolation to use. See [Animation
Constants](en\constants\Animation.html) for possible values. Default is
[InterpolateLinear](en\constants\Animation.html).

## Properties

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited properties.

### DefaultInterpolation

  
  
```ts  
DefaultInterpolation: Constant;  
```  

The default interpolation type to use,
[InterpolateLinear](en\constants\Animation.html).

### ValueTypeName

  
  
```ts  
ValueTypeName: String;  
```  

String 'quaternion'.

## Methods

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited methods.

### InterpolantFactoryMethodLinear

  
  
```ts  
function InterpolantFactoryMethodLinear( ): QuaternionLinearInterpolant;  
```  

Returns a new
[QuaternionLinearInterpolant](en\math\interpolants\QuaternionLinearInterpolant.html)
based on the [values](#), [times](#) and [valueSize](#) of the keyframes.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/tracks/QuaternionKeyframeTrack.js">src/animation/tracks/QuaternionKeyframeTrack.js</a>

