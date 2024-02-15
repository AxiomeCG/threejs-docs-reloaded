[KeyframeTrack](en\animation\KeyframeTrack.html) →

# BooleanKeyframeTrack

A Track of boolean keyframe values.

## Constructor

### BooleanKeyframeTrack

  
  
```ts  
function BooleanKeyframeTrack( name: String, times: Array, values: Array ):
void;  
```  

[name](#) - (required) identifier for the KeyframeTrack.  
[times](#) - (required) array of keyframe times.  
[values](#) - values for the keyframes at the times specified.  

## Properties

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited properties.

### DefaultInterpolation

  
  
```ts  
DefaultInterpolation: Constant;  
```  

The default interpolation type to use,
[InterpolateDiscrete](en\constants\Animation.html).

### ValueBufferType

  
  
```ts  
ValueBufferType: Array;  
```  

A normal Array (no Float32Array in this case, unlike `ValueBufferType` of
[KeyframeTrack](en\animation\KeyframeTrack.html)).

### ValueTypeName

  
  
```ts  
ValueTypeName: String;  
```  

String 'bool'.

## Methods

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited methods.

### InterpolantFactoryMethodLinear

  
  
```ts  
function InterpolantFactoryMethodLinear( ): undefined;  
```  

The value of this method here is 'undefined', as it does not make sense for
discrete properties.

### InterpolantFactoryMethodSmooth

  
  
```ts  
function InterpolantFactoryMethodSmooth( ): undefined;  
```  

The value of this method here is 'undefined', as it does not make sense for
discrete properties.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/tracks/BooleanKeyframeTrack.js">src/animation/tracks/BooleanKeyframeTrack.js</a>

