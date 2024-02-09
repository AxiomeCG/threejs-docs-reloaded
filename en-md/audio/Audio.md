[page:Object3D] →

# [name]

Create a non-positional ( global ) audio object.  
  
This uses the [link:https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API Web Audio API].

## Code Example

  
```ts  
  
// create an AudioListener and add it to the camera  
const listener = new THREE.AudioListener();  
camera.add( listener );  
  
// create a global audio source  
const sound = new THREE.Audio( listener );  
  
// load a sound and set it as the Audio object's buffer  
const audioLoader = new THREE.AudioLoader();  
audioLoader.load( 'sounds/ambient.ogg', function( buffer ) {  
sound.setBuffer( buffer );  
sound.setLoop( true );  
sound.setVolume( 0.5 );  
sound.play();  
});  
```  

## Examples

[example:webaudio_sandbox webaudio / sandbox ]  
[example:webaudio_visualizer webaudio / visualizer ]

## Constructor

### [name]( [param:AudioListener listener] )

listener — (required) [page:AudioListener AudioListener] instance.

## Properties

### <br/> Boolean autoplay; <br/>

Whether to start playback automatically. Default is `false`.

### <br/> AudioContext context; <br/>

The [link:https://developer.mozilla.org/en-US/docs/Web/API/AudioContext
AudioContext] of the [page:AudioListener listener] given in the constructor.

### <br/> Number detune; <br/>

Modify pitch, measured in cents. +/- 100 is a semitone. +/- 1200 is an octave.
Default is `0`.

### <br/> Array filters; <br/>

Represents an array of [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioNode AudioNodes]. Can be used to apply a variety of low-
order filters to create more complex sound effects. In most cases, the array
contains instances of [link:https://developer.mozilla.org/en-
US/docs/Web/API/BiquadFilterNode BiquadFilterNodes]. Filters are set via
[page:Audio.setFilter] or [page:Audio.setFilters].

### <br/> GainNode gain; <br/>

A [link:https://developer.mozilla.org/en-US/docs/Web/API/GainNode GainNode]
created using [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createGain AudioContext.createGain]().

### <br/> Boolean hasPlaybackControl; <br/>

Whether playback can be controlled using the [page:Audio.play play](),
[page:Audio.pause pause]() etc. methods. Default is `true`.

### <br/> Boolean isPlaying; <br/>

Whether the audio is currently playing.

### <br/> AudioListener listener; <br/>

A reference to the listener object of this audio.

### <br/> Number playbackRate; <br/>

Speed of playback. Default is `1`.

### <br/> Number offset; <br/>

An offset to the time within the audio buffer that playback should begin. Same
as the `offset` parameter of [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/start AudioBufferSourceNode.start]().
Default is `0`.

### <br/> Number duration; <br/>

Overrides the duration of the audio. Same as the `duration` parameter of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/start AudioBufferSourceNode.start]().
Default is `undefined` to play the whole buffer.

### <br/> AudioNode source; <br/>

An [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode AudioBufferSourceNode] created using
[link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createBufferSource
AudioContext.createBufferSource]().

### <br/> String sourceType; <br/>

Type of the audio source. Default is string 'empty'.

### <br/> String type; <br/>

String denoting the type, set to 'Audio'.

## Methods

### <br/> function connect( ): connect; <br/>

Connect to the [page:Audio.source]. This is used internally on initialisation
and when setting / removing filters.

### <br/> function disconnect( ): disconnect; <br/>

Disconnect from the [page:Audio.source]. This is used internally when setting
/ removing filters.

### [method:Float getDetune]()

Returns the detuning of oscillation in cents.

### [method:BiquadFilterNode getFilter]()

Returns the first element of the [page:Audio.filters filters] array.

### [method:Array getFilters]()

Returns the [page:Audio.filters filters] array.

### [method:Boolean getLoop]()

Return the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loop source.loop] (whether playback
should loop).

### [method:GainNode getOutput]()

Return the [page:Audio.gain gainNode].

### [method:Float getPlaybackRate]()

Return the value of [page:Audio.playbackRate playbackRate].

### [method:Float getVolume]( value )

Return the current volume.

### <br/> function play( ): play; <br/>

If [page:Audio.hasPlaybackControl hasPlaybackControl] is true, starts
playback.

### <br/> function pause( ): pause; <br/>

If [page:Audio.hasPlaybackControl hasPlaybackControl] is true, pauses
playback.

### [method:undefined onEnded]()

Called automatically when playback finished.

### <br/> function setBuffer( ): setBuffer; <br/>

Setup the [page:Audio.source source] to the audioBuffer, and sets
[page:Audio.sourceType sourceType] to 'buffer'.  
If [page:Audio.autoplay autoplay], also starts playback.

### <br/> function setDetune( value: Float ): setDetune; <br/>

Defines the detuning of oscillation in cents.

### <br/> function setFilter( ): setFilter; <br/>

Applies a single filter node to the audio.

### <br/> function setFilters( value: Array ): setFilters; <br/>

value - arrays of filters.  
Applies an array of filter nodes to the audio.

### <br/> function setLoop( value: Boolean? ): setLoop; <br/>

Set [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loop source.loop] to `value` (whether
playback should loop).

### <br/> function setLoopStart( value: Float ): setLoopStart; <br/>

Set [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loopStart source.loopStart] to `value`.

### <br/> function setLoopEnd( value: Float ): setLoopEnd; <br/>

Set [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loopEnd source.loopEnd] to `value`.

### <br/> function setMediaElementSource( ): setMediaElementSource; <br/>

Applies the given object of type [link:https://developer.mozilla.org/en-
US/docs/Web/API/HTMLMediaElement HTMLMediaElement] as the source of this
audio.  
Also sets [page:Audio.hasPlaybackControl hasPlaybackControl] to false.

### <br/> function setMediaStreamSource( ): setMediaStreamSource; <br/>

Applies the given object of type [link:https://developer.mozilla.org/en-
US/docs/Web/API/MediaStream MediaStream] as the source of this audio.  
Also sets [page:Audio.hasPlaybackControl hasPlaybackControl] to false.

### <br/> function setNodeSource( ): setNodeSource; <br/>

Setup the [page:Audio.source source] to the audioBuffer, and sets
[page:Audio.sourceType sourceType] to 'audioNode'.  
Also sets [page:Audio.hasPlaybackControl hasPlaybackControl] to false.

### <br/> function setPlaybackRate( value: Float ): setPlaybackRate; <br/>

If [page:Audio.hasPlaybackControl hasPlaybackControl] is enabled, set the
[page:Audio.playbackRate playbackRate] to `value`.

### <br/> function setVolume( value: Float ): setVolume; <br/>

Set the volume.

### <br/> function stop( ): stop; <br/>

If [page:Audio.hasPlaybackControl hasPlaybackControl] is enabled, stops
playback.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

