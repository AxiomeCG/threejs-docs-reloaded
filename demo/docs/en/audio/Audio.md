[Object3D](en\core\Object3D.html) →

# Audio

Create a non-positional ( global ) audio object.  
  
This uses the <a href="https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API">Web Audio API</a>.

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

### Audio

  
  
```ts  
function Audio( listener: AudioListener ): void;  
```  

listener — (required) [AudioListener](en\audio\AudioListener.html) instance.

## Properties

### autoplay

  
  
```ts  
autoplay: Boolean;  
```  

Whether to start playback automatically. Default is `false`.

### context

  
  
```ts  
context: AudioContext;  
```  

The <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext">AudioContext</a> of the
[listener](en\audio\AudioListener.html) given in the constructor.

### detune

  
  
```ts  
detune: Number;  
```  

Modify pitch, measured in cents. +/- 100 is a semitone. +/- 1200 is an octave.
Default is `0`.

### filters

  
  
```ts  
filters: Array;  
```  

Represents an array of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioNode">AudioNodes</a>. Can be used to apply a variety of
low-order filters to create more complex sound effects. In most cases, the
array contains instances of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/BiquadFilterNode">BiquadFilterNodes</a>. Filters are set via
[Audio.setFilter](#) or [Audio.setFilters](#).

### gain

  
  
```ts  
gain: GainNode;  
```  

A <a href="https://developer.mozilla.org/en-
US/docs/Web/API/GainNode">GainNode</a> created using <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createGain">AudioContext.createGain</a>().

### hasPlaybackControl

  
  
```ts  
hasPlaybackControl: Boolean;  
```  

Whether playback can be controlled using the [play](#)(), [pause](#)() etc.
methods. Default is `true`.

### isPlaying

  
  
```ts  
isPlaying: Boolean;  
```  

Whether the audio is currently playing.

### listener

  
  
```ts  
listener: AudioListener;  
```  

A reference to the listener object of this audio.

### playbackRate

  
  
```ts  
playbackRate: Number;  
```  

Speed of playback. Default is `1`.

### offset

  
  
```ts  
offset: Number;  
```  

An offset to the time within the audio buffer that playback should begin. Same
as the `offset` parameter of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/start">AudioBufferSourceNode.start</a>().
Default is `0`.

### duration

  
  
```ts  
duration: Number;  
```  

Overrides the duration of the audio. Same as the `duration` parameter of <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/start">AudioBufferSourceNode.start</a>().
Default is `undefined` to play the whole buffer.

### source

  
  
```ts  
source: AudioNode;  
```  

An <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode">AudioBufferSourceNode</a> created using
<a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createBufferSource">AudioContext.createBufferSource</a>().

### sourceType

  
  
```ts  
sourceType: String;  
```  

Type of the audio source. Default is string 'empty'.

### type

  
  
```ts  
type: String;  
```  

String denoting the type, set to 'Audio'.

## Methods

### connect

  
  
```ts  
function connect( ): this;  
```  

Connect to the [Audio.source](#). This is used internally on initialisation
and when setting / removing filters.

### disconnect

  
  
```ts  
function disconnect( ): this;  
```  

Disconnect from the [Audio.source](#). This is used internally when setting /
removing filters.

### getDetune

  
  
```ts  
function getDetune( ): Float;  
```  

Returns the detuning of oscillation in cents.

### getFilter

  
  
```ts  
function getFilter( ): BiquadFilterNode;  
```  

Returns the first element of the [filters](#) array.

### getFilters

  
  
```ts  
function getFilters( ): Array;  
```  

Returns the [filters](#) array.

### getLoop

  
  
```ts  
function getLoop( ): Boolean;  
```  

Return the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loop">source.loop</a> (whether playback
should loop).

### getOutput

  
  
```ts  
function getOutput( ): GainNode;  
```  

Return the [gainNode](#).

### getPlaybackRate

  
  
```ts  
function getPlaybackRate( ): Float;  
```  

Return the value of [playbackRate](#).

### getVolume

  
  
```ts  
function getVolume( ): Float;  
```  

Return the current volume.

### play

  
  
```ts  
function play( ): this;  
```  

If [hasPlaybackControl](#) is true, starts playback.

### pause

  
  
```ts  
function pause( ): this;  
```  

If [hasPlaybackControl](#) is true, pauses playback.

### onEnded

  
  
```ts  
function onEnded( ): undefined;  
```  

Called automatically when playback finished.

### setBuffer

  
  
```ts  
function setBuffer( ): this;  
```  

Setup the [source](#) to the audioBuffer, and sets [sourceType](#) to
'buffer'.  
If [autoplay](#), also starts playback.

### setDetune

  
  
```ts  
function setDetune( value: Float ): this;  
```  

Defines the detuning of oscillation in cents.

### setFilter

  
  
```ts  
function setFilter( ): this;  
```  

Applies a single filter node to the audio.

### setFilters

  
  
```ts  
function setFilters( value: Array ): this;  
```  

value - arrays of filters.  
Applies an array of filter nodes to the audio.

### setLoop

  
  
```ts  
function setLoop( value: Boolean ): this;  
```  

Set <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loop">source.loop</a> to `value`
(whether playback should loop).

### setLoopStart

  
  
```ts  
function setLoopStart( value: Float ): this;  
```  

Set <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loopStart">source.loopStart</a> to
`value`.

### setLoopEnd

  
  
```ts  
function setLoopEnd( value: Float ): this;  
```  

Set <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioBufferSourceNode/loopEnd">source.loopEnd</a> to `value`.

### setMediaElementSource

  
  
```ts  
function setMediaElementSource( ): this;  
```  

Applies the given object of type <a href="https://developer.mozilla.org/en-
US/docs/Web/API/HTMLMediaElement">HTMLMediaElement</a> as the source of this
audio.  
Also sets [hasPlaybackControl](#) to false.

### setMediaStreamSource

  
  
```ts  
function setMediaStreamSource( ): this;  
```  

Applies the given object of type <a href="https://developer.mozilla.org/en-
US/docs/Web/API/MediaStream">MediaStream</a> as the source of this audio.  
Also sets [hasPlaybackControl](#) to false.

### setNodeSource

  
  
```ts  
function setNodeSource( ): this;  
```  

Setup the [source](#) to the audioBuffer, and sets [sourceType](#) to
'audioNode'.  
Also sets [hasPlaybackControl](#) to false.

### setPlaybackRate

  
  
```ts  
function setPlaybackRate( value: Float ): this;  
```  

If [hasPlaybackControl](#) is enabled, set the [playbackRate](#) to `value`.

### setVolume

  
  
```ts  
function setVolume( value: Float ): this;  
```  

Set the volume.

### stop

  
  
```ts  
function stop( ): this;  
```  

If [hasPlaybackControl](#) is enabled, stops playback.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/audio/Audio.js">src/audio/Audio.js</a>

