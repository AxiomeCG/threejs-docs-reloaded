[page:KeyframeTrack] →

# StringKeyframeTrack

A Track of string keyframe values.

## Constructor

###  function StringKeyframeTrack( name: String, times: Array, values: Array
): void;

[page:String name] - (required) identifier for the KeyframeTrack.  
[page:Array times] - (required) array of keyframe times.  
[page:Array values] - values for the keyframes at the times specified.  
[page:Constant interpolation] - the type of interpolation to use. See
[page:Animation Animation Constants] for possible values. Default is
[page:Animation InterpolateDiscrete].

## Properties

See [page:KeyframeTrack] for inherited properties.

###  Constant DefaultInterpolation;

The default interpolation type to use, [page:Animation InterpolateDiscrete].

###  Array ValueBufferType;

A normal Array (no Float32Array in this case, unlike `ValueBufferType` of
[page:KeyframeTrack]).

###  String ValueTypeName;

String 'string'.

## Methods

See [page:KeyframeTrack] for inherited methods.

###  function InterpolantFactoryMethodLinear( ): undefined;

The value of this method here is 'undefined', as it does not make sense for
discrete properties.

###  function InterpolantFactoryMethodSmooth( ): undefined;

The value of this method here is 'undefined', as it does not make sense for
discrete properties.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

