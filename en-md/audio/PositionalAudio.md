[page:Object3D] → [page:Audio] →

# [name]

Create a positional audio object.  
  
This uses the [link:https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API Web Audio API].

## Code Example

  
```ts  
// create an AudioListener and add it to the camera  
const listener = new THREE.AudioListener();  
camera.add( listener );  
  
// create the PositionalAudio object (passing in the listener)  
const sound = new THREE.PositionalAudio( listener );  
  
// load a sound and set it as the PositionalAudio object's buffer  
const audioLoader = new THREE.AudioLoader();  
audioLoader.load( 'sounds/song.ogg', function( buffer ) {  
sound.setBuffer( buffer );  
sound.setRefDistance( 20 );  
sound.play();  
});  
  
// create an object for the sound to play from  
const sphere = new THREE.SphereGeometry( 20, 32, 16 );  
const material = new THREE.MeshPhongMaterial( { color: 0xff2200 } );  
const mesh = new THREE.Mesh( sphere, material );  
scene.add( mesh );  
  
// finally add the sound to the mesh  
mesh.add( sound );  
```  

## Examples

[example:webaudio_orientation webaudio / orientation ]  
[example:webaudio_sandbox webaudio / sandbox ]  
[example:webaudio_timing webaudio / timing ]

## Constructor

### [name]( [param:AudioListener listener] )

listener — (required) [page:AudioListener AudioListener] instance.

## Properties

See the [page:Audio Audio] class for inherited properties.

### <br/> PannerNode panner; <br/>

The PositionalAudio's [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode PannerNode].

## Methods

See the [page:Audio Audio] class for inherited methods.

### [method:PannerNode getOutput]()

Returns the [page:PositionalAudio.panner panner].

### [method:Float getRefDistance]()

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/refDistance panner.refDistance].

### <br/> function setRefDistance( value: Float ): setRefDistance; <br/>

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/refDistance panner.refDistance].

### [method:Float getRolloffFactor]()

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/rolloffFactor panner.rolloffFactor].

### <br/> function setRolloffFactor( value: Float ): setRolloffFactor; <br/>

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/rolloffFactor panner.rolloffFactor].

### [method:String getDistanceModel]()

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/distanceModel panner.distanceModel].

### <br/> function setDistanceModel( value: String ): setDistanceModel; <br/>

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/distanceModel panner.distanceModel].

### [method:Float getMaxDistance]()

Returns the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/maxDistance panner.maxDistance].

### <br/> function setMaxDistance( value: Float ): setMaxDistance; <br/>

Sets the value of [link:https://developer.mozilla.org/en-
US/docs/Web/API/PannerNode/maxDistance panner.maxDistance].

### <br/> function setDirectionalCone( coneInnerAngle: Float, coneOuterAngle:
Float, coneOuterGain: Float ): setDirectionalCone; <br/>

This method can be used in order to transform an omnidirectional sound into a
[link:https://developer.mozilla.org/en-US/docs/Web/API/PannerNode directional
sound].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

