[page:KeyframeTrack] →

# VectorKeyframeTrack

A Track of vector keyframe values.

## Constructor

###  function VectorKeyframeTrack( name: String, times: Array, values: Array
): void;

[page:String name] - (required) identifier for the KeyframeTrack.  
[page:Array times] - (required) array of keyframe times.  
[page:Array values] - values for the keyframes at the times specified, a flat
array of vector components.  
[page:Constant interpolation] - the type of interpolation to use. See
[page:Animation Animation Constants] for possible values. Default is
[page:Animation InterpolateLinear].

## Properties

See [page:KeyframeTrack] for inherited properties.

###  String ValueTypeName;

String 'vector'.

## Methods

See [page:KeyframeTrack] for inherited methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

