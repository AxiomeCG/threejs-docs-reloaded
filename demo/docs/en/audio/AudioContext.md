# AudioContext

This contains methods for setting up an <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext">AudioContext</a>.  
  
Used internally by the [AudioListener](en\audio\AudioListener.html) and
[AudioLoader](en\loaders\AudioLoader.html) classes.  
  
This uses the <a href="https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API">Web Audio API</a>.

## Methods

### getContext

  
  
```ts  
function getContext( ): AudioContext;  
```  

Return the value of the variable `context` in the outer scope, if defined,
otherwise set it to a new <a href="https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext">AudioContext</a>.

### setContext

  
  
```ts  
function setContext( value: AudioContext ): AudioContext;  
```  

Set the variable `context` in the outer scope to `value`.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/audio/AudioContext.js">src/audio/AudioContext.js</a>

