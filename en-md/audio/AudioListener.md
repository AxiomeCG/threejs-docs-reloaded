[page:Object3D] →

# AudioListener

The AudioListener represents a virtual [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioListener listener] of the all positional and non-
positional audio effects in the scene.  
A three.js application usually creates a single instance of AudioListener. It
is a mandatory constructor parameter for audios entities like [page:Audio
Audio] and [page:PositionalAudio PositionalAudio].  
In most cases, the listener object is a child of the camera. So the 3D
transformation of the camera represents the 3D transformation of the listener.

## Code Example

  
```ts  
// create an AudioListener and add it to the camera const listener = new
THREE.AudioListener(); camera.add( listener ); // create a global audio source
const sound = new THREE.Audio( listener ); // load a sound and set it as the
Audio object's buffer const audioLoader = new THREE.AudioLoader();
audioLoader.load( 'sounds/ambient.ogg', function( buffer ) { sound.setBuffer(
buffer ); sound.setLoop(true); sound.setVolume(0.5); sound.play(); });  
```  

## Examples

[example:webaudio_sandbox webaudio / sandbox ]  
[example:webaudio_timing webaudio / timing ]  
[example:webaudio_visualizer webaudio / visualizer ]

## Constructor

###  function AudioListener( ): void;

Create a new AudioListener.

## Properties

###  AudioContext context;

The [link:https://developer.mozilla.org/en-US/docs/Web/API/AudioContext
AudioContext] of the [page:AudioListener listener] given in the constructor.

###  GainNode gain;

A [link:https://developer.mozilla.org/en-US/docs/Web/API/GainNode GainNode]
created using [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createGain AudioContext.createGain]().

###  AudioNode filter;

Default is `null`.

###  Number timeDelta;

Time delta value for audio entities. Use in context of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioParam/linearRampToValueAtTime
AudioParam.linearRampToValueAtTimeDefault](). Default is .

## Methods

###  function getInput( ): GainNode;

Return the [page:AudioListener.gain gainNode].

###  function removeFilter( ): this;

Set the [page:AudioListener.filter filter] property to `null`.

###  function getFilter( ): AudioNode;

Returns the value of the [page:AudioListener.filter filter] property.

###  function setFilter( value: AudioNode ): this;

Set the [page:AudioListener.filter filter] property to `value`.

###  function getMasterVolume( ): Float;

Return the volume.

###  function setMasterVolume( value: Number ): this;

Set the volume.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

