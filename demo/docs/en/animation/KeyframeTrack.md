# KeyframeTrack

A KeyframeTrack is a timed sequence of <a
href="https://en.wikipedia.org/wiki/Key_frame">keyframes</a>, which are
composed of lists of times and related values, and which are used to animate a
specific property of an object.

For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

In contrast to the animation hierarchy of the <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Model-format-3">JSON model
format</a> a `KeyframeTrack` doesn't store its single keyframes as objects in
a "keys" array (holding the times and the values for each frame together in
one place).

Instead of this there are always two arrays in a `KeyframeTrack`: the
[.times](#times) array stores the time values for all keyframes of this track
in sequential order, and the [.values](#values) array contains the
corresponding changing values of the animated property.

A single value, belonging to a certain point of time, can not only be a simple
number, but (for example) a vector (if a position is animated) or a quaternion
(if a rotation is animated). For this reason the values array (which is a flat
array, too) might be three or four times as long as the times array.

Corresponding to the different possible types of animated values there are
several subclasses of `KeyframeTrack`, inheriting the most properties and
methods:

  * [BooleanKeyframeTrack](en\animation\tracks\BooleanKeyframeTrack.html)
  * [ColorKeyframeTrack](en\animation\tracks\ColorKeyframeTrack.html)
  * [NumberKeyframeTrack](en\animation\tracks\NumberKeyframeTrack.html)
  * [QuaternionKeyframeTrack](en\animation\tracks\QuaternionKeyframeTrack.html)
  * [StringKeyframeTrack](en\animation\tracks\StringKeyframeTrack.html)
  * [VectorKeyframeTrack](en\animation\tracks\VectorKeyframeTrack.html)

Some examples of how to manually create
[AnimationClips](en\animation\AnimationClip.html) with different sorts of
KeyframeTracks can be found in the <a
href="https://threejs.org/examples/jsm/animation/AnimationClipCreator.js">AnimationClipCreator</a>
file.

Since explicit values are only specified for the discrete points of time
stored in the times array, all values in between have to be interpolated.

The track's name is important for the connection of this track with a specific
property of the animated node (done by
[PropertyBinding](en\animation\PropertyBinding.html)).

## Constructor

### KeyframeTrack

  
  
```ts  
function KeyframeTrack( name: String, times: Array, values: Array,
interpolation: Constant ): void;  
```  

[name](#) - the identifier for the `KeyframeTrack`.  
[times](#) - an array of keyframe times, converted internally to a <a
href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array">Float32Array</a>.  
[values](#) - an array with the values related to the times array, converted
internally to a <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array">Float32Array</a>.  
[interpolation](#) - the type of interpolation to use. See [Animation
Constants](en\constants\Animation.html) for possible values. Default is
[InterpolateLinear](en\constants\Animation.html).

## Properties

### name

  
  
```ts  
name: String;  
```  

The track's name can refer to morph targets or
[bones](en\objects\SkinnedMesh.html) or possibly other values within an
animated object. See [PropertyBinding.parseTrackName](#) for the forms of
strings that can be parsed for property binding:

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

### times

  
  
```ts  
times: Float32Array;  
```  

A <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array">Float32Array</a>,
converted from the times array which is passed in the constructor.

### values

  
  
```ts  
values: Float32Array;  
```  

A <a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array">Float32Array</a>,
converted from the values array which is passed in the constructor.

### DefaultInterpolation

  
  
```ts  
DefaultInterpolation: Constant;  
```  

The default interpolation type:
[InterpolateLinear](en\constants\Animation.html).

### [property:Constant TimeBufferType ]

<a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array">Float32Array</a>,
the type of the buffer internally used for the times.

### [property:Constant ValueBufferType ]

<a href="https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array">Float32Array</a>,
the type of the buffer internally used for the values.

## Methods

### clone

  
  
```ts  
function clone( ): KeyframeTrack;  
```  

Returns a copy of this track.

### createInterpolant

  
  
```ts  
function createInterpolant( ): Interpolant;  
```  

Creates a [LinearInterpolant](en\math\interpolants\LinearInterpolant.html),
[CubicInterpolant](en\math\interpolants\CubicInterpolant.html) or
[DiscreteInterpolant](en\math\interpolants\DiscreteInterpolant.html),
depending on the value of the interpolation parameter passed in the
constructor.

### getInterpolation

  
  
```ts  
function getInterpolation( ): Interpolant;  
```  

Returns the interpolation type.

### getValueSize

  
  
```ts  
function getValueSize( ): Number;  
```  

Returns the size of each value (that is the length of the [.values](#values)
array divided by the length of the [.times](#times) array).

### InterpolantFactoryMethodDiscrete

  
  
```ts  
function InterpolantFactoryMethodDiscrete( ): DiscreteInterpolant;  
```  

Creates a new
[DiscreteInterpolant](en\math\interpolants\DiscreteInterpolant.html) from the
[times](#) and [values](#). A Float32Array can be passed which will receive
the results. Otherwise a new array with the appropriate size will be created
automatically.

### InterpolantFactoryMethodLinear

  
  
```ts  
function InterpolantFactoryMethodLinear( ): LinearInterpolant;  
```  

Creates a new [LinearInterpolant](en\math\interpolants\LinearInterpolant.html)
from the [times](#) and [values](#). A Float32Array can be passed which will
receive the results. Otherwise a new array with the appropriate size will be
created automatically.

### InterpolantFactoryMethodSmooth

  
  
```ts  
function InterpolantFactoryMethodSmooth( ): CubicInterpolant;  
```  

Create a new [CubicInterpolant](en\math\interpolants\CubicInterpolant.html)
from the [times](#) and [values](#). A Float32Array can be passed which will
receive the results. Otherwise a new array with the appropriate size will be
created automatically.

### optimize

  
  
```ts  
function optimize( ): this;  
```  

Removes equivalent sequential keys, which are common in morph target
sequences.

### scale

  
  
```ts  
function scale( ): this;  
```  

Scales all keyframe times by a factor.  
  
Note: This is useful, for example, for conversions to a certain rate of frames
per seconds (as it is done internally by
[animationClip.CreateFromMorphTargetSequence](#)).

### setInterpolation

  
  
```ts  
function setInterpolation( interpolationType: Constant ): this;  
```  

Sets the interpolation type. See [Animation
Constants](en\constants\Animation.html) for choices.

### shift

  
  
```ts  
function shift( timeOffsetInSeconds: Number ): this;  
```  

Moves all keyframes either forward or backward in time.

### trim

  
  
```ts  
function trim( startTimeInSeconds: Number, endTimeInSeconds: Number ): this;  
```  

Removes keyframes before `startTime` and after `endTime`, without changing any
values within the range [`startTime`, `endTime`].

### validate

  
  
```ts  
function validate( ): Boolean;  
```  

Performs minimal validation on the tracks. Returns true if valid.

This method logs errors to the console, if a track is empty, if the
[.valueSize](#valueSize) is not valid, if an item in the [.times](#times) or
[.values](#values) array is not a valid number or if the items in the `times`
array are out of order.

## Static Methods

### toJSON

  
  
```ts  
function toJSON( track: KeyframeTrack ): JSON;  
```  

Converts the track to JSON.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/KeyframeTrack.js">src/animation/KeyframeTrack.js</a>

