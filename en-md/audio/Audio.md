[page:Object3D] →

# Audio

Create a non-positional ( global ) audio object.  
  
This uses the [link:https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API Web Audio API].

## Code Example

  
```ts  
// create an AudioListener and add it to the camera const listener = new
THREE.AudioListener(); camera.add( listener ); // create a global audio source
const sound = new THREE.Audio( listener ); // load a sound and set it as the
Audio object's buffer const audioLoader = new THREE.AudioLoader();
audioLoader.load( 'sounds/ambient.ogg', function( buffer ) { sound.setBuffer(
buffer ); sound.setLoop( true ); sound.setVolume( 0.5 ); sound.play(); });  
```  

## Examples

[example:webaudio_sandbox webaudio / sandbox ]  
[example:webaudio_visualizer webaudio / visualizer ]

## Constructor

###  function Audio( listener: AudioListener ): void;

listener — (required) [page:AudioListener AudioListener] instance.

## Properties

###  Boolean autoplay;

Whether to start playback automatically. Default is `false`.

###  AudioContext context;

The [link:https://developer.mozilla.org/en-US/docs/Web/API/AudioContext
AudioContext] of the [page:AudioListener listener] given in the constructor.

###  Number detune;

Modify pitch, measured in cents. +/- 100 is a semitone. +/- 1200 is an octave.
Default is `0`.

###  Array filters;

Represents an array of [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioNode AudioNodes]. Can be used to apply a variety of low-
order filters to create more complex sound effects. In most cases, the array
contains instances of [link:https://developer.mozilla.org/en-
US/docs/Web/API/BiquadFilterNode BiquadFilterNodes]. Filters are set via
[page:Audio.setFilter] or [page:Audio.setFilters].

###  GainNode gain;

A [link:https://developer.mozilla.org/en-US/docs/Web/API/GainNode GainNode]
created using [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createGain AudioContext.createGain]().

###  Boolean hasPlaybackControl;

Whether playback can be controlled using the [page:Audio.play play](),
[page:Audio.pause pause]() etc. methods. Default is `true`.

###  Boolean isPlaying;

Whether the audio is currently playing.

###  AudioListener listener;

A reference to the listener object of this audio.

###  Number playbackRate;

Speed of playback. Default is `1`.

###  Number offset;

An offset to the time within the audio buffer that playback should begin. Same
as the `offset` parameter of [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/start AudioBufferSourceNode.start]().
Default is `0`.

###  Number duration;

Overrides the duration of the audio. Same as the `duration` parameter of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/start AudioBufferSourceNode.start]().
Default is `undefined` to play the whole buffer.

###  AudioNode source;

An [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode AudioBufferSourceNode] created using
[link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createBufferSource
AudioContext.createBufferSource]().

###  String sourceType;

Type of the audio source. Default is string 'empty'.

###  String type;

String denoting the type, set to 'Audio'.

## Methods

###  function connect( ): this;

Connect to the [page:Audio.source]. This is used internally on initialisation
and when setting / removing filters.

###  function disconnect( ): this;

Disconnect from the [page:Audio.source]. This is used internally when setting
/ removing filters.

###  function getDetune( ): Float;

Returns the detuning of oscillation in cents.

###  function getFilter( ): BiquadFilterNode;

Returns the first element of the [page:Audio.filters filters] array.

###  function getFilters( ): Array;

Returns the [page:Audio.filters filters] array.

###  function getLoop( ): Boolean;

Return the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loop source.loop] (whether playback
should loop).

###  function getOutput( ): GainNode;

Return the [page:Audio.gain gainNode].

###  function getPlaybackRate( ): Float;

Return the value of [page:Audio.playbackRate playbackRate].

###  function getVolume( ): Float;

Return the current volume.

###  function play( ): this;

If [page:Audio.hasPlaybackControl hasPlaybackControl] is true, starts
playback.

###  function pause( ): this;

If [page:Audio.hasPlaybackControl hasPlaybackControl] is true, pauses
playback.

###  function onEnded( ): undefined;

Called automatically when playback finished.

###  function setBuffer( ): this;

Setup the [page:Audio.source source] to the audioBuffer, and sets
[page:Audio.sourceType sourceType] to 'buffer'.  
If [page:Audio.autoplay autoplay], also starts playback.

###  function setDetune( value: Float ): this;

Defines the detuning of oscillation in cents.

###  function setFilter( ): this;

Applies a single filter node to the audio.

###  function setFilters( value: Array ): this;

value - arrays of filters.  
Applies an array of filter nodes to the audio.

###  function setLoop( value: Boolean ): this;

Set [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loop source.loop] to `value` (whether
playback should loop).

###  function setLoopStart( value: Float ): this;

Set [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loopStart source.loopStart] to `value`.

###  function setLoopEnd( value: Float ): this;

Set [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loopEnd source.loopEnd] to `value`.

###  function setMediaElementSource( ): this;

Applies the given object of type [link:https://developer.mozilla.org/en-
US/docs/Web/API/HTMLMediaElement HTMLMediaElement] as the source of this
audio.  
Also sets [page:Audio.hasPlaybackControl hasPlaybackControl] to false.

###  function setMediaStreamSource( ): this;

Applies the given object of type [link:https://developer.mozilla.org/en-
US/docs/Web/API/MediaStream MediaStream] as the source of this audio.  
Also sets [page:Audio.hasPlaybackControl hasPlaybackControl] to false.

###  function setNodeSource( ): this;

Setup the [page:Audio.source source] to the audioBuffer, and sets
[page:Audio.sourceType sourceType] to 'audioNode'.  
Also sets [page:Audio.hasPlaybackControl hasPlaybackControl] to false.

###  function setPlaybackRate( value: Float ): this;

If [page:Audio.hasPlaybackControl hasPlaybackControl] is enabled, set the
[page:Audio.playbackRate playbackRate] to `value`.

###  function setVolume( value: Float ): this;

Set the volume.

###  function stop( ): this;

If [page:Audio.hasPlaybackControl hasPlaybackControl] is enabled, stops
playback.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

