# [name]

An [name] is a reusable set of keyframe tracks which represent an animation.  
  
For an overview of the different elements of the three.js animation system see
the "Animation System" article in the "Next Steps" section of the manual.

## Constructor

###  [name]( [param:String name], [param:Number duration], [param:Array
tracks] )

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

### <br/> Number blendMode; <br/>

Defines how the animation is blended/combined when two or more animations are
simultaneously played. Valid values are *NormalAnimationBlendMode* (default)
and *AdditiveAnimationBlendMode*.

### <br/> Number duration; <br/>

The duration of this clip (in seconds). This can be calculated from the
[page:.tracks tracks] array via [page:.resetDuration resetDuration].

### <br/> String name; <br/>

A name for this clip. A certain clip can be searched via [page:.findByName
findByName].

### <br/> Array tracks; <br/>

An array containing a [page:KeyframeTrack] for each property that are animated
by this clip.

### <br/> String uuid; <br/>

The [link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of
this clip instance. It gets automatically assigned and shouldn't be edited.

## Methods

### [method:AnimationClip clone]()

Returns a copy of this clip.

### <br/> function optimize( ): optimize; <br/>

Optimizes each track by removing equivalent sequential keys (which are common
in morph target sequences).

### <br/> function resetDuration( ): resetDuration; <br/>

Sets the [page:.duration duration] of the clip to the duration of its longest
[page:KeyframeTrack].

### [method:Object toJSON]()

Returns a JSON object representing the serialized animation clip.

### <br/> function trim( ): trim; <br/>

Trims all tracks to the clip's duration.

### [method:Boolean validate]()

Performs minimal validation on each track in the clip. Returns true if all
tracks are valid.

## Static Methods

### [method:Array CreateClipsFromMorphTargetSequences]( [param:String name],
[param:Array morphTargetSequence], [param:Number fps], [param:Boolean noLoop]
)

Returns an array of new AnimationClips created from the morph target sequences
of a geometry, trying to sort morph target names into animation-group-based
patterns like "Walk_001, Walk_002, Run_001, Run_002...".

### [method:AnimationClip CreateFromMorphTargetSequence]( [param:String name],
[param:Array morphTargetSequence], [param:Number fps], [param:Boolean noLoop]
)

Returns a new AnimationClip from the passed morph targets array of a geometry,
taking a name and the number of frames per second.  
  
Note: The fps parameter is required, but the animation speed can be overridden
in an `AnimationAction` via [page:AnimationAction.setDuration
animationAction.setDuration].

### [method:AnimationClip findByName]( [param:Object objectOrClipArray],
[param:String name] )

Searches for an AnimationClip by name, taking as its first parameter either an
array of AnimationClips, or a mesh or geometry that contains an array named
"animations".

### [method:AnimationClip parse]( [param:Object json] )

Parses a JSON representation of a clip and returns an AnimationClip.

###  [method:AnimationClip parseAnimation]( [param:Object animation],
[param:Array bones] )

Parses the animation.hierarchy format and returns an AnimationClip.

### [method:Object toJSON]( [param:AnimationClip clip] )

Takes an AnimationClip and returns a JSON object.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

