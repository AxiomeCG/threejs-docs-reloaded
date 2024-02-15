[Object3D](en\core\Object3D.html) →

# AudioListener

The AudioListener represents a virtual <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioListener">listener</a> of the all positional and non-
positional audio effects in the scene.  
A three.js application usually creates a single instance of AudioListener. It
is a mandatory constructor parameter for audios entities like
[Audio](en\audio\Audio.html) and
[PositionalAudio](en\audio\PositionalAudio.html).  
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

### AudioListener

  
  
```ts  
function AudioListener( ): void;  
```  

Create a new AudioListener.

## Properties

### context

  
  
```ts  
context: AudioContext;  
```  

The <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext">AudioContext</a> of the
[listener](en\audio\AudioListener.html) given in the constructor.

### gain

  
  
```ts  
gain: GainNode;  
```  

A <a href="https://developer.mozilla.org/en-
US/docs/Web/API/GainNode">GainNode</a> created using <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createGain">AudioContext.createGain</a>().

### filter

  
  
```ts  
filter: AudioNode;  
```  

Default is `null`.

### timeDelta

  
  
```ts  
timeDelta: Number;  
```  

Time delta value for audio entities. Use in context of <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioParam/linearRampToValueAtTime">AudioParam.linearRampToValueAtTimeDefault</a>().
Default is .

## Methods

### getInput

  
  
```ts  
function getInput( ): GainNode;  
```  

Return the [gainNode](#).

### removeFilter

  
  
```ts  
function removeFilter( ): this;  
```  

Set the [filter](#) property to `null`.

### getFilter

  
  
```ts  
function getFilter( ): AudioNode;  
```  

Returns the value of the [filter](#) property.

### setFilter

  
  
```ts  
function setFilter( value: AudioNode ): this;  
```  

Set the [filter](#) property to `value`.

### getMasterVolume

  
  
```ts  
function getMasterVolume( ): Float;  
```  

Return the volume.

### setMasterVolume

  
  
```ts  
function setMasterVolume( value: Number ): this;  
```  

Set the volume.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/audio/AudioListener.js">src/audio/AudioListener.js</a>

