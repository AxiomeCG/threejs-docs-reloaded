# [name]

A KeyframeTrack is a timed sequence of
[link:https://en.wikipedia.org/wiki/Key_frame keyframes], which are composed
of lists of times and related values, and which are used to animate a specific
property of an object.

For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

In contrast to the animation hierarchy of the
[link:https://github.com/mrdoob/three.js/wiki/JSON-Model-format-3 JSON model
format] a `KeyframeTrack` doesn't store its single keyframes as objects in a
"keys" array (holding the times and the values for each frame together in one
place).

Instead of this there are always two arrays in a `KeyframeTrack`: the
[page:.times times] array stores the time values for all keyframes of this
track in sequential order, and the [page:.values values] array contains the
corresponding changing values of the animated property.

A single value, belonging to a certain point of time, can not only be a simple
number, but (for example) a vector (if a position is animated) or a quaternion
(if a rotation is animated). For this reason the values array (which is a flat
array, too) might be three or four times as long as the times array.

Corresponding to the different possible types of animated values there are
several subclasses of `KeyframeTrack`, inheriting the most properties and
methods:

  * [page:BooleanKeyframeTrack]
  * [page:ColorKeyframeTrack]
  * [page:NumberKeyframeTrack]
  * [page:QuaternionKeyframeTrack]
  * [page:StringKeyframeTrack]
  * [page:VectorKeyframeTrack]

Some examples of how to manually create [page:AnimationClip AnimationClips]
with different sorts of KeyframeTracks can be found in the
[link:https://threejs.org/examples/jsm/animation/AnimationClipCreator.js
AnimationClipCreator] file.

Since explicit values are only specified for the discrete points of time
stored in the times array, all values in between have to be interpolated.

The track's name is important for the connection of this track with a specific
property of the animated node (done by [page:PropertyBinding]).

## Constructor

### [name]( [param:String name], [param:Array times], [param:Array values],
[param:Constant interpolation] )

[page:String name] - the identifier for the `KeyframeTrack`.  
[page:Array times] - an array of keyframe times, converted internally to a
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array Float32Array].  
[page:Array values] - an array with the values related to the times array,
converted internally to a [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array Float32Array].  
[page:Constant interpolation] - the type of interpolation to use. See
[page:Animation Animation Constants] for possible values. Default is
[page:Animation InterpolateLinear].

## Properties

### <br/> String name; <br/>

The track's name can refer to morph targets or [page:SkinnedMesh bones] or
possibly other values within an animated object. See
[page:PropertyBinding.parseTrackName] for the forms of strings that can be
parsed for property binding:

The name can specify the node either using its name or its uuid (although it
needs to be in the subtree of the scene graph node passed into the mixer). Or,
if the track name starts with a dot, the track applies to the root node that
was passed into the mixer.

Usually after the node a property will be specified directly. But you can also
specify a subproperty, such as .rotation[x], if you just want to drive the X
component of the rotation via a float track.

You can also specify bones or multimaterials by using an object name, for
example: .bones[R_hand].scale; the red channel of the diffuse color of the
fourth material in a materials array - as a further example - can be accessed
with .materials[3].diffuse[r].

PropertyBinding will also resolve morph target names, for example:
.morphTargetInfluences[run].

Note: The track's name does not necessarily have to be unique. Multiple tracks
can drive the same property. The result should be based on a weighted blend
between the multiple tracks according to the weights of their respective
actions.

### <br/> Float32Array times; <br/>

A [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array Float32Array],
converted from the times array which is passed in the constructor.

### <br/> Float32Array values; <br/>

A [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array Float32Array],
converted from the values array which is passed in the constructor.

### <br/> Constant DefaultInterpolation; <br/>

The default interpolation type: [page:Animation InterpolateLinear].

### [property:Constant TimeBufferType ]

[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array Float32Array],
the type of the buffer internally used for the times.

### [property:Constant ValueBufferType ]

[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array Float32Array],
the type of the buffer internally used for the values.

## Methods

### [method:KeyframeTrack clone]()

Returns a copy of this track.

### [method:Interpolant createInterpolant]()

Creates a [page:LinearInterpolant LinearInterpolant], [page:CubicInterpolant
CubicInterpolant] or [page:DiscreteInterpolant DiscreteInterpolant], depending
on the value of the interpolation parameter passed in the constructor.

### [method:Interpolant getInterpolation]()

Returns the interpolation type.

### [method:Number getValueSize]()

Returns the size of each value (that is the length of the [page:.values
values] array divided by the length of the [page:.times times] array).

###  [method:DiscreteInterpolant InterpolantFactoryMethodDiscrete](
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array result] )

Creates a new [page:DiscreteInterpolant DiscreteInterpolant] from the
[page:KeyframeTrack.times times] and [page:KeyframeTrack.times values]. A
Float32Array can be passed which will receive the results. Otherwise a new
array with the appropriate size will be created automatically.

###  [method:LinearInterpolant InterpolantFactoryMethodLinear](
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array result] )

Creates a new [page:LinearInterpolant LinearInterpolant] from the
[page:KeyframeTrack.times times] and [page:KeyframeTrack.times values]. A
Float32Array can be passed which will receive the results. Otherwise a new
array with the appropriate size will be created automatically.

###  [method:CubicInterpolant InterpolantFactoryMethodSmooth](
[link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array result] )

Create a new [page:CubicInterpolant CubicInterpolant] from the
[page:KeyframeTrack.times times] and [page:KeyframeTrack.times values]. A
Float32Array can be passed which will receive the results. Otherwise a new
array with the appropriate size will be created automatically.

### <br/> function optimize( ): optimize; <br/>

Removes equivalent sequential keys, which are common in morph target
sequences.

### <br/> function scale( ): scale; <br/>

Scales all keyframe times by a factor.  
  
Note: This is useful, for example, for conversions to a certain rate of frames
per seconds (as it is done internally by
[page:AnimationClip.CreateFromMorphTargetSequence
animationClip.CreateFromMorphTargetSequence]).

### <br/> function setInterpolation( interpolationType: Constant ):
setInterpolation; <br/>

Sets the interpolation type. See [page:Animation Animation Constants] for
choices.

### <br/> function shift( timeOffsetInSeconds: Number ): shift; <br/>

Moves all keyframes either forward or backward in time.

### <br/> function trim( startTimeInSeconds: Number, endTimeInSeconds: Number
): trim; <br/>

Removes keyframes before `startTime` and after `endTime`, without changing any
values within the range [`startTime`, `endTime`].

### [method:Boolean validate]()

Performs minimal validation on the tracks. Returns true if valid.

This method logs errors to the console, if a track is empty, if the
[page:.valueSize value size] is not valid, if an item in the [page:.times
times] or [page:.values values] array is not a valid number or if the items in
the `times` array are out of order.

## Static Methods

### [method:JSON toJSON]( [param:KeyframeTrack track] )

Converts the track to JSON.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

