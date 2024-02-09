[page:KeyframeTrack] →

# [name]

A Track of quaternion keyframe values.

## Constructor

###  [name]( [param:String name], [param:Array times], [param:Array values] )

[page:String name] (required) identifier for the KeyframeTrack.  
[page:Array times] (required) array of keyframe times.  
[page:Array values] values for the keyframes at the times specified, a flat
array of quaternion components.  
[page:Constant interpolation] the type of interpolation to use. See
[page:Animation Animation Constants] for possible values. Default is
[page:Animation InterpolateLinear].

## Properties

See [page:KeyframeTrack] for inherited properties.

### <br/> Constant DefaultInterpolation; <br/>

The default interpolation type to use, [page:Animation InterpolateLinear].

### <br/> String ValueTypeName; <br/>

String 'quaternion'.

## Methods

See [page:KeyframeTrack] for inherited methods.

###  [method:QuaternionLinearInterpolant InterpolantFactoryMethodLinear]()

Returns a new [page:QuaternionLinearInterpolant QuaternionLinearInterpolant]
based on the [page:KeyframeTrack.values values], [page:KeyframeTrack.times
times] and [page:KeyframeTrack.valueSize valueSize] of the keyframes.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

