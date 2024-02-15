[KeyframeTrack](en\animation\KeyframeTrack.html) →

# ColorKeyframeTrack

A Track of keyframe values that represent color changes.  
  
The very basic implementation of this subclass has nothing special yet.
However, this is the place for color space parameterization.

## Constructor

### ColorKeyframeTrack

  
  
```ts  
function ColorKeyframeTrack( name: String, times: Array, values: Array ):
void;  
```  

[name](#) - (required) identifier for the KeyframeTrack.  
[times](#) - (required) array of keyframe times.  
[values](#) - values for the keyframes at the times specified, a flat array of
color components between `0` and `1`.  
[interpolation](#) - the type of interpolation to use. See [Animation
Constants](en\constants\Animation.html) for possible values. Default is
[InterpolateLinear](en\constants\Animation.html).

## Properties

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited properties.

### ValueTypeName

  
  
```ts  
ValueTypeName: String;  
```  

String 'color'.

## Methods

See [KeyframeTrack](en\animation\KeyframeTrack.html) for inherited methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/tracks/ColorKeyframeTrack.js">src/animation/tracks/ColorKeyframeTrack.js</a>

