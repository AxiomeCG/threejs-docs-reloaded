# AnimationUtils

An object with various functions to assist with animations, used internally.

## Methods

### arraySlice

  
  
```ts  
function arraySlice( ): Array;  
```  

This is the same as Array.prototype.slice, but also works on typed arrays.

### convertArray

  
  
```ts  
function convertArray( ): Array;  
```  

Converts an array to a specific type.

### flattenJSON

  
  
```ts  
function flattenJSON( ): Array;  
```  

Used for parsing AOS keyframe formats.

### getKeyframeOrder

  
  
```ts  
function getKeyframeOrder( ): Array;  
```  

Returns an array by which times and values can be sorted.

### isTypedArray

  
  
```ts  
function isTypedArray( ): Boolean;  
```  

Returns `true` if the object is a typed array.

### makeClipAdditive

  
  
```ts  
function makeClipAdditive( targetClip: AnimationClip, referenceFrame: Number,
referenceClip: AnimationClip, fps: Number ): AnimationClip;  
```  

Converts the keyframes of the given animation clip to an additive format.

### sortedArray

  
  
```ts  
function sortedArray( ): Array;  
```  

Sorts the array previously returned by [getKeyframeOrder](#).

### subclip

  
  
```ts  
function subclip( clip: AnimationClip, name: String, startFrame: Number,
endFrame: Number, fps: Number ): AnimationClip;  
```  

Creates a new clip, containing only the segment of the original clip between
the given frames.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/AnimationUtils.js">src/animation/AnimationUtils.js</a>

