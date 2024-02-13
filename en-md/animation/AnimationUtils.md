# AnimationUtils

An object with various functions to assist with animations, used internally.

## Methods

###  function arraySlice( ): Array;

This is the same as Array.prototype.slice, but also works on typed arrays.

###  function convertArray( ): Array;

Converts an array to a specific type.

###  function flattenJSON( ): Array;

Used for parsing AOS keyframe formats.

###  function getKeyframeOrder( ): Array;

Returns an array by which times and values can be sorted.

###  function isTypedArray( ): Boolean;

Returns `true` if the object is a typed array.

###  function makeClipAdditive( targetClip: AnimationClip, referenceFrame:
Number, referenceClip: AnimationClip, fps: Number ): AnimationClip;

Converts the keyframes of the given animation clip to an additive format.

###  function sortedArray( ): Array;

Sorts the array previously returned by [page:AnimationUtils.getKeyframeOrder
getKeyframeOrder].

###  function subclip( clip: AnimationClip, name: String, startFrame: Number,
endFrame: Number, fps: Number ): AnimationClip;

Creates a new clip, containing only the segment of the original clip between
the given frames.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

