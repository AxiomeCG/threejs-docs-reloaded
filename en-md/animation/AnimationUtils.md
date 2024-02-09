# [name]

An object with various functions to assist with animations, used internally.

## Methods

### [method:Array arraySlice]( array, from, to )

This is the same as Array.prototype.slice, but also works on typed arrays.

### [method:Array convertArray]( array, type, forceClone )

Converts an array to a specific type.

### [method:Array flattenJSON]( jsonKeys, times, values, valuePropertyName )

Used for parsing AOS keyframe formats.

### [method:Array getKeyframeOrder]( times )

Returns an array by which times and values can be sorted.

### [method:Boolean isTypedArray]( object )

Returns `true` if the object is a typed array.

### [method:AnimationClip makeClipAdditive]( [param:AnimationClip targetClip],
[param:Number referenceFrame], [param:AnimationClip referenceClip],
[param:Number fps] )

Converts the keyframes of the given animation clip to an additive format.

### [method:Array sortedArray]( values, stride, order )

Sorts the array previously returned by [page:AnimationUtils.getKeyframeOrder
getKeyframeOrder].

### [method:AnimationClip subclip]( [param:AnimationClip clip], [param:String
name], [param:Number startFrame], [param:Number endFrame], [param:Number fps]
)

Creates a new clip, containing only the segment of the original clip between
the given frames.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

