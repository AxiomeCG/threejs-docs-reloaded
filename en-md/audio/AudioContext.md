# AudioContext

This contains methods for setting up an
[link:https://developer.mozilla.org/en-US/docs/Web/API/AudioContext
AudioContext].  
  
Used internally by the [page:AudioListener AudioListener] and
[page:AudioLoader AudioLoader] classes.  
  
This uses the [link:https://developer.mozilla.org/en-
US/docs/Web/API/Web_Audio_API Web Audio API].

## Methods

###  function getContext( ): AudioContext;

Return the value of the variable `context` in the outer scope, if defined,
otherwise set it to a new [link:https://developer.mozilla.org/en-
US/docs/Web/API/AudioContext AudioContext].

###  function setContext( value: AudioContext ): AudioContext;

Set the variable `context` in the outer scope to `value`.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

