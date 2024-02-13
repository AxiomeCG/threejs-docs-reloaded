# AudioAnalyser

Create a AudioAnalyser object, which uses an
[link:https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode
AnalyserNode] to analyse audio data.  
  
This uses the [link:https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API Web Audio API].

## Code Example

  
```ts  
// create an AudioListener and add it to the camera const listener = new
THREE.AudioListener(); camera.add( listener ); // create an Audio source const
sound = new THREE.Audio( listener ); // load a sound and set it as the Audio
object's buffer const audioLoader = new THREE.AudioLoader(); audioLoader.load(
'sounds/ambient.ogg', function( buffer ) { sound.setBuffer( buffer );
sound.setLoop(true); sound.setVolume(0.5); sound.play(); }); // create an
AudioAnalyser, passing in the sound and desired fftSize const analyser = new
THREE.AudioAnalyser( sound, 32 ); // get the average frequency of the sound
const data = analyser.getAverageFrequency();  
```  

## Examples

[example:webaudio_sandbox webaudio / sandbox ]  
[example:webaudio_visualizer webaudio / visualizer ]

## Constructor

###  function AudioAnalyser( ): void;

Create a new [page:AudioAnalyser AudioAnalyser].

## Properties

###  AnalyserNode analyser;

An [link:https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode
AnalyserNode] used to analyze audio.

###  Integer fftSize;

A non-zero power of two up to 2048, representing the size of the FFT (Fast
Fourier Transform) to be used to determine the frequency domain. See
[link:https://developer.mozilla.org/en-US/docs/Web/API/AnalyserNode/fftSize
this page] for details.

###  Uint8Array data;

A Uint8Array with size determined by [link:https://developer.mozilla.org/en-
US/docs/Web/API/AnalyserNode/frequencyBinCount analyser.frequencyBinCount]
used to hold analysis data.

## Methods

###  function getFrequencyData( ): Uint8Array;

Uses the Web Audio's [link:https://developer.mozilla.org/en-
US/docs/Web/API/AnalyserNode/getByteFrequencyData getByteFrequencyData]
method. See that page.

###  function getAverageFrequency( ): Number;

Get the average of the frequencies returned by the
[page:AudioAnalyser.getFrequencyData getFrequencyData] method.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

