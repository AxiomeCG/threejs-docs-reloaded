# AnimationClip

An AnimationClip is a reusable set of keyframe tracks which represent an
animation.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Constructor

###  function AnimationClip( name: String, duration: Number, tracks: Array ):
void;

[page:String name] - a name for this clip.  
[page:Number duration] - the duration of this clip (in seconds). If a negative
value is passed, the duration will be calculated from the passed `tracks`
array.  
[page:Array tracks] - an array of [page:KeyframeTrack KeyframeTracks].  
[page:Number blendMode] - defines how the animation is blended/combined when
two or more animations are simultaneously played.  
  
Note: Instead of instantiating an AnimationClip directly with the constructor,
you can use one of its static methods to create AnimationClips: from JSON
([page:.parse parse]), from morph target sequences
([page:.CreateFromMorphTargetSequence CreateFromMorphTargetSequence],
[page:.CreateClipsFromMorphTargetSequences
CreateClipsFromMorphTargetSequences]) or from animation hierarchies
([page:.parseAnimation parseAnimation]) - if your model doesn't already hold
AnimationClips in its geometry's animations array.

## Properties

###  Number blendMode;

Defines how the animation is blended/combined when two or more animations are
simultaneously played. Valid values are *NormalAnimationBlendMode* (default)
and *AdditiveAnimationBlendMode*.

###  Number duration;

The duration of this clip (in seconds). This can be calculated from the
[page:.tracks tracks] array via [page:.resetDuration resetDuration].

###  String name;

A name for this clip. A certain clip can be searched via [page:.findByName
findByName].

###  Array tracks;

An array containing a [page:KeyframeTrack] for each property that are animated
by this clip.

###  String uuid;

The [link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of
this clip instance. It gets automatically assigned and shouldn't be edited.

## Methods

###  function clone( ): AnimationClip;

Returns a copy of this clip.

###  function optimize( ): this;

Optimizes each track by removing equivalent sequential keys (which are common
in morph target sequences).

###  function resetDuration( ): this;

Sets the [page:.duration duration] of the clip to the duration of its longest
[page:KeyframeTrack].

###  function toJSON( ): Object;

Returns a JSON object representing the serialized animation clip.

###  function trim( ): this;

Trims all tracks to the clip's duration.

###  function validate( ): Boolean;

Performs minimal validation on each track in the clip. Returns true if all
tracks are valid.

## Static Methods

###  function CreateClipsFromMorphTargetSequences( name: String,
morphTargetSequence: Array, fps: Number, noLoop: Boolean ): Array;

Returns an array of new AnimationClips created from the morph target sequences
of a geometry, trying to sort morph target names into animation-group-based
patterns like "Walk_001, Walk_002, Run_001, Run_002...".

###  function CreateFromMorphTargetSequence( name: String,
morphTargetSequence: Array, fps: Number, noLoop: Boolean ): AnimationClip;

Returns a new AnimationClip from the passed morph targets array of a geometry,
taking a name and the number of frames per second.  
  
Note: The fps parameter is required, but the animation speed can be overridden
in an `AnimationAction` via [page:AnimationAction.setDuration
animationAction.setDuration].

###  function findByName( objectOrClipArray: Object, name: String ):
AnimationClip;

Searches for an AnimationClip by name, taking as its first parameter either an
array of AnimationClips, or a mesh or geometry that contains an array named
"animations".

###  function parse( json: Object ): AnimationClip;

Parses a JSON representation of a clip and returns an AnimationClip.

###  function parseAnimation( animation: Object, bones: Array ):
AnimationClip;

Parses the animation.hierarchy format and returns an AnimationClip.

###  function toJSON( clip: AnimationClip ): Object;

Takes an AnimationClip and returns a JSON object.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

