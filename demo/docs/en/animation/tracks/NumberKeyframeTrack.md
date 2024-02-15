[KeyframeTrack](en\animation\KeyframeTrack.html) →

# NumberKeyframeTrack

A Track of numeric keyframe values.

## Constructor

### NumberKeyframeTrack

  
  
```ts  
function NumberKeyframeTrack( name: String, times: Array, values: Array ):
void;  
```  

[name](#) - (required) identifier for the KeyframeTrack.  
[times](#) - (required) array of keyframe times.  
[values](#) - values for the keyframes at the times specified.  
[interpolation](#) - the type of interpolation to use. See [Animation
Constants](en\constants\Animation.html) for possible values. Default is
[InterpolateLinear](en\constants\Animation.html).

## Properties

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited properties.

### ValueTypeName

  
  
```ts  
ValueTypeName: String;  
```  

String 'number'.

## Methods

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/tracks/NumberKeyframeTrack.js">src/animation/tracks/NumberKeyframeTrack.js</a>

