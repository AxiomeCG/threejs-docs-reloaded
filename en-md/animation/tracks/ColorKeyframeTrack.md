[page:KeyframeTrack] →

# [name]

A Track of keyframe values that represent color changes.  
  
The very basic implementation of this subclass has nothing special yet.
However, this is the place for color space parameterization.

## Constructor

###  [name]( [param:String name], [param:Array times], [param:Array values] )

[page:String name] - (required) identifier for the KeyframeTrack.  
[page:Array times] - (required) array of keyframe times.  
[page:Array values] - values for the keyframes at the times specified, a flat
array of color components between `0` and `1`.  
[page:Constant interpolation] - the type of interpolation to use. See
[page:Animation Animation Constants] for possible values. Default is
[page:Animation InterpolateLinear].

## Properties

See [page:KeyframeTrack] for inherited properties.

### <br/> String ValueTypeName; <br/>

String 'color'.

## Methods

See [page:KeyframeTrack] for inherited methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

