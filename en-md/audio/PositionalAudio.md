[page:Object3D] → [page:Audio] →

# PositionalAudio

Create a positional audio object.  
  
This uses the [link:https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API Web Audio API].

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

###  function PositionalAudio( listener: AudioListener ): void;

listener — (required) [page:AudioListener AudioListener] instance.

## Properties

See the [page:Audio Audio] class for inherited properties.

###  PannerNode panner;

The PositionalAudio's [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode PannerNode].

## Methods

See the [page:Audio Audio] class for inherited methods.

###  function getOutput( ): PannerNode;

Returns the [page:PositionalAudio.panner panner].

###  function getRefDistance( ): Float;

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/refDistance panner.refDistance].

###  function setRefDistance( value: Float ): this;

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/refDistance panner.refDistance].

###  function getRolloffFactor( ): Float;

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/rolloffFactor panner.rolloffFactor].

###  function setRolloffFactor( value: Float ): this;

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/rolloffFactor panner.rolloffFactor].

###  function getDistanceModel( ): String;

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/distanceModel panner.distanceModel].

###  function setDistanceModel( value: String ): this;

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/distanceModel panner.distanceModel].

###  function getMaxDistance( ): Float;

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/maxDistance panner.maxDistance].

###  function setMaxDistance( value: Float ): this;

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/maxDistance panner.maxDistance].

###  function setDirectionalCone( coneInnerAngle: Float, coneOuterAngle:
Float, coneOuterGain: Float ): this;

This method can be used in order to transform an omnidirectional sound into a
[link:https://developer.mozilla.org/en-US/docs/Web/API/PannerNode directional
sound].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

