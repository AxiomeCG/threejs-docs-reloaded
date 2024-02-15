[KeyframeTrack](en\animation\KeyframeTrack.html) →

# StringKeyframeTrack

A Track of string keyframe values.

## Constructor

### StringKeyframeTrack

  
  
```ts  
function StringKeyframeTrack( name: String, times: Array, values: Array ):
void;  
```  

[name](#) - (required) identifier for the KeyframeTrack.  
[times](#) - (required) array of keyframe times.  
[values](#) - values for the keyframes at the times specified.  
[interpolation](#) - the type of interpolation to use. See [Animation
Constants](en\constants\Animation.html) for possible values. Default is
[InterpolateDiscrete](en\constants\Animation.html).

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

String 'string'.

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
href="https://github.com/mrdoob/three.js/blob/master/src/animation/tracks/StringKeyframeTrack.js">src/animation/tracks/StringKeyframeTrack.js</a>

