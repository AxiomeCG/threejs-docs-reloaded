[page:Object3D] →

# [name]

The [name] represents a virtual [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioListener listener] of the all positional and non-
positional audio effects in the scene.  
A three.js application usually creates a single instance of [name]. It is a
mandatory constructor parameter for audios entities like [page:Audio Audio]
and [page:PositionalAudio PositionalAudio].  
In most cases, the listener object is a child of the camera. So the 3D
transformation of the camera represents the 3D transformation of the listener.

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
sound.setLoop(true);  
sound.setVolume(0.5);  
sound.play();  
});  
  
```  

## Examples

[example:webaudio_sandbox webaudio / sandbox ]  
[example:webaudio_timing webaudio / timing ]  
[example:webaudio_visualizer webaudio / visualizer ]

## Constructor

### [name]( )

Create a new AudioListener.

## Properties

### <br/> AudioContext context; <br/>

The [link:https://developer.mozilla.org/en-US/docs/Web/API/AudioContext
AudioContext] of the [page:AudioListener listener] given in the constructor.

### <br/> GainNode gain; <br/>

A [link:https://developer.mozilla.org/en-US/docs/Web/API/GainNode GainNode]
created using [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext/createGain AudioContext.createGain]().

### <br/> AudioNode filter; <br/>

Default is `null`.

### <br/> Number timeDelta; <br/>

Time delta value for audio entities. Use in context of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioParam/linearRampToValueAtTime
AudioParam.linearRampToValueAtTimeDefault](). Default is .

## Methods

### [method:GainNode getInput]()

Return the [page:AudioListener.gain gainNode].

### <br/> function removeFilter( ): removeFilter; <br/>

Set the [page:AudioListener.filter filter] property to `null`.

### [method:AudioNode getFilter]()

Returns the value of the [page:AudioListener.filter filter] property.

### <br/> function setFilter( value: AudioNode ): setFilter; <br/>

Set the [page:AudioListener.filter filter] property to `value`.

### [method:Float getMasterVolume]()

Return the volume.

### <br/> function setMasterVolume( value: Number ): setMasterVolume; <br/>

Set the volume.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

