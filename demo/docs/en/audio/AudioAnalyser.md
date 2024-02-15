# AudioAnalyser

Create a AudioAnalyser object, which uses an <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AnalyserNode">AnalyserNode</a> to analyse audio data.  
  
This uses the <a href="https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API">Web Audio API</a>.

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

### AudioAnalyser

  
  
```ts  
function AudioAnalyser( ): void;  
```  

Create a new [AudioAnalyser](en\audio\AudioAnalyser.html).

## Properties

### analyser

  
  
```ts  
analyser: AnalyserNode;  
```  

An <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AnalyserNode">AnalyserNode</a> used to analyze audio.

### fftSize

  
  
```ts  
fftSize: Integer;  
```  

A non-zero power of two up to 2048, representing the size of the FFT (Fast
Fourier Transform) to be used to determine the frequency domain. See <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AnalyserNode/fftSize">this page</a> for details.

### data

  
  
```ts  
data: Uint8Array;  
```  

A Uint8Array with size determined by <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AnalyserNode/frequencyBinCount">analyser.frequencyBinCount</a>
used to hold analysis data.

## Methods

### getFrequencyData

  
  
```ts  
function getFrequencyData( ): Uint8Array;  
```  

Uses the Web Audio's <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AnalyserNode/getByteFrequencyData">getByteFrequencyData</a>
method. See that page.

### getAverageFrequency

  
  
```ts  
function getAverageFrequency( ): Number;  
```  

Get the average of the frequencies returned by the [getFrequencyData](#)
method.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/audio/AudioAnalyser.js">src/audio/AudioAnalyser.js</a>

