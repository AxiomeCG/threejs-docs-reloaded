[Object3D](en\core\Object3D.html) → [Audio](en\audio\Audio.html) →

# PositionalAudio

Create a positional audio object.  
  
This uses the <a href="https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API">Web Audio API</a>.

## Code Example

  
```ts  
// create an AudioListener and add it to the camera const listener = new
THREE.AudioListener(); camera.add( listener ); // create the PositionalAudio
object (passing in the listener) const sound = new THREE.PositionalAudio(
listener ); // load a sound and set it as the PositionalAudio object's buffer
const audioLoader = new THREE.AudioLoader(); audioLoader.load(
'sounds/song.ogg', function( buffer ) { sound.setBuffer( buffer );
sound.setRefDistance( 20 ); sound.play(); }); // create an object for the
sound to play from const sphere = new THREE.SphereGeometry( 20, 32, 16 );
const material = new THREE.MeshPhongMaterial( { color: 0xff2200 } ); const
mesh = new THREE.Mesh( sphere, material ); scene.add( mesh ); // finally add
the sound to the mesh mesh.add( sound );  
```  

## Examples

[example:webaudio_orientation webaudio / orientation ]  
[example:webaudio_sandbox webaudio / sandbox ]  
[example:webaudio_timing webaudio / timing ]

## Constructor

### PositionalAudio

  
  
```ts  
function PositionalAudio( listener: AudioListener ): void;  
```  

listener — (required) [AudioListener](en\audio\AudioListener.html) instance.

## Properties

See the [Audio](en\audio\Audio.html) class for inherited properties.

### panner

  
  
```ts  
panner: PannerNode;  
```  

The PositionalAudio's <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode">PannerNode</a>.

## Methods

See the [Audio](en\audio\Audio.html) class for inherited methods.

### getOutput

  
  
```ts  
function getOutput( ): PannerNode;  
```  

Returns the [panner](#).

### getRefDistance

  
  
```ts  
function getRefDistance( ): Float;  
```  

Returns the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/refDistance">panner.refDistance</a>.

### setRefDistance

  
  
```ts  
function setRefDistance( value: Float ): this;  
```  

Sets the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/refDistance">panner.refDistance</a>.

### getRolloffFactor

  
  
```ts  
function getRolloffFactor( ): Float;  
```  

Returns the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/rolloffFactor">panner.rolloffFactor</a>.

### setRolloffFactor

  
  
```ts  
function setRolloffFactor( value: Float ): this;  
```  

Sets the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/rolloffFactor">panner.rolloffFactor</a>.

### getDistanceModel

  
  
```ts  
function getDistanceModel( ): String;  
```  

Returns the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/distanceModel">panner.distanceModel</a>.

### setDistanceModel

  
  
```ts  
function setDistanceModel( value: String ): this;  
```  

Sets the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/distanceModel">panner.distanceModel</a>.

### getMaxDistance

  
  
```ts  
function getMaxDistance( ): Float;  
```  

Returns the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/maxDistance">panner.maxDistance</a>.

### setMaxDistance

  
  
```ts  
function setMaxDistance( value: Float ): this;  
```  

Sets the value of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/maxDistance">panner.maxDistance</a>.

### setDirectionalCone

  
  
```ts  
function setDirectionalCone( coneInnerAngle: Float, coneOuterAngle: Float,
coneOuterGain: Float ): this;  
```  

This method can be used in order to transform an omnidirectional sound into a
<a href="https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode">directional sound</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/audio/PositionalAudio.js">src/audio/PositionalAudio.js</a>

