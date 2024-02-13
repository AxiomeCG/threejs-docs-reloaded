# MathUtils

An object with several math utility functions.

## Functions

###  function clamp( value: Float, min: Float, max: Float ): Float;

[page:Float value] — Value to be clamped.  
[page:Float min] — Minimum value.  
[page:Float max] — Maximum value.  
  
Clamps the [page:Float value] to be between [page:Float min] and [page:Float
max].

###  function degToRad( degrees: Float ): Float;

Converts degrees to radians.

###  function euclideanModulo( n: Integer, m: Integer ): Integer;

[page:Integer n], [page:Integer m] - Integers  
  
Computes the Euclidean modulo of [page:Integer m] % [page:Integer n], that is:  
```ts  
( ( n % m ) + m ) % m  
```  

###  function generateUUID( ): UUID;

Generate a [link:https://en.wikipedia.org/wiki/Universally_unique_identifier
UUID] (universally unique identifier).

###  function isPowerOfTwo( n: Number ): Boolean;

Return `true` if [page:Number n] is a power of 2.

###  function inverseLerp( x: Float, y: Float, value: Float ): Float;

[page:Float x] - Start point.  
[page:Float y] - End point.  
[page:Float value] - A value between start and end.  
  
Returns the percentage in the closed interval `[0, 1]` of the given value
between the start and end point.

###  function lerp( x: Float, y: Float, t: Float ): Float;

[page:Float x] - Start point.  
[page:Float y] - End point.  
[page:Float t] - interpolation factor in the closed interval `[0, 1]`.  
  
Returns a value [link:https://en.wikipedia.org/wiki/Linear_interpolation
linearly interpolated] from two known points based on the given interval -
[page:Float t] = 0 will return [page:Float x] and [page:Float t] = 1 will
return [page:Float y].

###  function damp( x: Float, y: Float, lambda: Float, dt: Float ): Float;

[page:Float x] - Current point.  
[page:Float y] - Target point.  
[page:Float lambda] - A higher lambda value will make the movement more
sudden, and a lower value will make the movement more gradual.  
[page:Float dt] - Delta time in seconds.  
  
Smoothly interpolate a number from [page:Float x] toward [page:Float y] in a
spring-like manner using the [page:Float dt] to maintain frame rate
independent movement. For details, see
[link:http://www.rorydriscoll.com/2016/03/07/frame-rate-independent-damping-
using-lerp/ Frame rate independent damping using lerp].

###  function mapLinear( x: Float, a1: Float, a2: Float, b1: Float, b2: Float
): Float;

[page:Float x] — Value to be mapped.  
[page:Float a1] — Minimum value for range A.  
[page:Float a2] — Maximum value for range A.  
[page:Float b1] — Minimum value for range B.  
[page:Float b2] — Maximum value for range B.  
  
Linear mapping of [page:Float x] from range [[page:Float a1], [page:Float a2]]
to range [[page:Float b1], [page:Float b2]].

###  function pingpong( x: Float, length: Float ): Float;

[page:Float x] — The value to pingpong.  
[page:Float length] — The positive value the function will pingpong to.
Default is `1`.  
  
Returns a value that alternates between `0` and [param:Float length].

###  function ceilPowerOfTwo( n: Number ): Integer;

Returns the smallest power of 2 that is greater than or equal to [page:Number
n].

###  function floorPowerOfTwo( n: Number ): Integer;

Returns the largest power of `2` that is less than or equal to [page:Number
n].

###  function radToDeg( radians: Float ): Float;

Converts radians to degrees.

###  function randFloat( low: Float, high: Float ): Float;

Random float in the interval [[page:Float low], [page:Float high]].

###  function randFloatSpread( range: Float ): Float;

Random float in the interval [- [page:Float range] / 2, [page:Float range] /
2].

###  function randInt( low: Integer, high: Integer ): Integer;

Random integer in the interval [[page:Float low], [page:Float high]].

###  function seededRandom( seed: Integer ): Float;

Deterministic pseudo-random float in the interval `[0, 1]`. The integer
[page:Integer seed] is optional.

###  function smoothstep( x: Float, min: Float, max: Float ): Float;

[page:Float x] - The value to evaluate based on its position between min and
max.  
[page:Float min] - Any x value below min will be `0`.  
[page:Float max] - Any x value above max will be `1`.  
  
Returns a value between 0-1 that represents the percentage that x has moved
between min and max, but smoothed or slowed down the closer X is to the min
and max.  
  
See [link:http://en.wikipedia.org/wiki/Smoothstep Smoothstep] for details.

###  function smootherstep( x: Float, min: Float, max: Float ): Float;

[page:Float x] - The value to evaluate based on its position between min and
max.  
[page:Float min] - Any x value below min will be `0`.  
[page:Float max] - Any x value above max will be `1`.  
  
Returns a value between 0-1. A
[link:https://en.wikipedia.org/wiki/Smoothstep#Variations variation on
smoothstep] that has zero 1st and 2nd order derivatives at x=0 and x=1.

###  function setQuaternionFromProperEuler( q: Quaternion, a: Float, b: Float,
c: Float, order: String ): undefined;

[page:Quaternion q] - the quaternion to be set  
[page:Float a] - the rotation applied to the first axis, in radians  
[page:Float b] - the rotation applied to the second axis, in radians  
[page:Float c] - the rotation applied to the third axis, in radians  
[page:String order] - a string specifying the axes order: 'XYX', 'XZX', 'YXY',
'YZY', 'ZXZ', or 'ZYZ'  
  
Sets quaternion [page:Quaternion q] from the
[link:http://en.wikipedia.org/wiki/Euler_angles intrinsic Proper Euler Angles]
defined by angles [page:Float a], [page:Float b], and [page:Float c], and
order [page:String order].  
Rotations are applied to the axes in the order specified by [page:String
order]: rotation by angle [page:Float a] is applied first, then by angle
[page:Float b], then by angle [page:Float c]. Angles are in radians.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

