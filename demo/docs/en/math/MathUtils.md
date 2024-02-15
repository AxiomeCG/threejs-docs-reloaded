# MathUtils

An object with several math utility functions.

## Functions

### clamp

  
  
```ts  
function clamp( value: Float, min: Float, max: Float ): Float;  
```  

[value](#) — Value to be clamped.  
[min](#) — Minimum value.  
[max](#) — Maximum value.  
  
Clamps the [value](#) to be between [min](#) and [max](#).

### degToRad

  
  
```ts  
function degToRad( degrees: Float ): Float;  
```  

Converts degrees to radians.

### euclideanModulo

  
  
```ts  
function euclideanModulo( n: Integer, m: Integer ): Integer;  
```  

[n](#), [m](#) - Integers  
  
Computes the Euclidean modulo of [m](#) % [n](#), that is:  
```ts  
( ( n % m ) + m ) % m  
```  

### generateUUID

  
  
```ts  
function generateUUID( ): UUID;  
```  

Generate a <a
href="https://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a>
(universally unique identifier).

### isPowerOfTwo

  
  
```ts  
function isPowerOfTwo( n: Number ): Boolean;  
```  

Return `true` if [n](#) is a power of 2.

### inverseLerp

  
  
```ts  
function inverseLerp( x: Float, y: Float, value: Float ): Float;  
```  

[x](#) - Start point.  
[y](#) - End point.  
[value](#) - A value between start and end.  
  
Returns the percentage in the closed interval `[0, 1]` of the given value
between the start and end point.

### lerp

  
  
```ts  
function lerp( x: Float, y: Float, t: Float ): Float;  
```  

[x](#) - Start point.  
[y](#) - End point.  
[t](#) - interpolation factor in the closed interval `[0, 1]`.  
  
Returns a value <a
href="https://en.wikipedia.org/wiki/Linear_interpolation">linearly
interpolated</a> from two known points based on the given interval - [t](#) =
0 will return [x](#) and [t](#) = 1 will return [y](#).

### damp

  
  
```ts  
function damp( x: Float, y: Float, lambda: Float, dt: Float ): Float;  
```  

[x](#) - Current point.  
[y](#) - Target point.  
[lambda](#) - A higher lambda value will make the movement more sudden, and a
lower value will make the movement more gradual.  
[dt](#) - Delta time in seconds.  
  
Smoothly interpolate a number from [x](#) toward [y](#) in a spring-like
manner using the [dt](#) to maintain frame rate independent movement. For
details, see <a href="http://www.rorydriscoll.com/2016/03/07/frame-rate-
independent-damping-using-lerp/">Frame rate independent damping using
lerp</a>.

### mapLinear

  
  
```ts  
function mapLinear( x: Float, a1: Float, a2: Float, b1: Float, b2: Float ):
Float;  
```  

[x](#) — Value to be mapped.  
[a1](#) — Minimum value for range A.  
[a2](#) — Maximum value for range A.  
[b1](#) — Minimum value for range B.  
[b2](#) — Maximum value for range B.  
  
Linear mapping of [x](#) from range [[a1](#), [a2](#)] to range [[b1](#),
[b2](#)].

### pingpong

  
  
```ts  
function pingpong( x: Float, length: Float ): Float;  
```  

[x](#) — The value to pingpong.  
[length](#) — The positive value the function will pingpong to. Default is
`1`.  
  
Returns a value that alternates between `0` and [param:Float length].

### ceilPowerOfTwo

  
  
```ts  
function ceilPowerOfTwo( n: Number ): Integer;  
```  

Returns the smallest power of 2 that is greater than or equal to [n](#).

### floorPowerOfTwo

  
  
```ts  
function floorPowerOfTwo( n: Number ): Integer;  
```  

Returns the largest power of `2` that is less than or equal to [n](#).

### radToDeg

  
  
```ts  
function radToDeg( radians: Float ): Float;  
```  

Converts radians to degrees.

### randFloat

  
  
```ts  
function randFloat( low: Float, high: Float ): Float;  
```  

Random float in the interval [[low](#), [high](#)].

### randFloatSpread

  
  
```ts  
function randFloatSpread( range: Float ): Float;  
```  

Random float in the interval [- [range](#) / 2, [range](#) / 2].

### randInt

  
  
```ts  
function randInt( low: Integer, high: Integer ): Integer;  
```  

Random integer in the interval [[low](#), [high](#)].

### seededRandom

  
  
```ts  
function seededRandom( seed: Integer ): Float;  
```  

Deterministic pseudo-random float in the interval `[0, 1]`. The integer
[seed](#) is optional.

### smoothstep

  
  
```ts  
function smoothstep( x: Float, min: Float, max: Float ): Float;  
```  

[x](#) - The value to evaluate based on its position between min and max.  
[min](#) - Any x value below min will be `0`.  
[max](#) - Any x value above max will be `1`.  
  
Returns a value between 0-1 that represents the percentage that x has moved
between min and max, but smoothed or slowed down the closer X is to the min
and max.  
  
See <a href="http://en.wikipedia.org/wiki/Smoothstep">Smoothstep</a> for
details.

### smootherstep

  
  
```ts  
function smootherstep( x: Float, min: Float, max: Float ): Float;  
```  

[x](#) - The value to evaluate based on its position between min and max.  
[min](#) - Any x value below min will be `0`.  
[max](#) - Any x value above max will be `1`.  
  
Returns a value between 0-1. A <a
href="https://en.wikipedia.org/wiki/Smoothstep#Variations">variation on
smoothstep</a> that has zero 1st and 2nd order derivatives at x=0 and x=1.

### setQuaternionFromProperEuler

  
  
```ts  
function setQuaternionFromProperEuler( q: Quaternion, a: Float, b: Float, c:
Float, order: String ): undefined;  
```  

[q](en\math\Quaternion.html) - the quaternion to be set  
[a](#) - the rotation applied to the first axis, in radians  
[b](#) - the rotation applied to the second axis, in radians  
[c](#) - the rotation applied to the third axis, in radians  
[order](#) - a string specifying the axes order: 'XYX', 'XZX', 'YXY', 'YZY',
'ZXZ', or 'ZYZ'  
  
Sets quaternion [q](en\math\Quaternion.html) from the <a
href="http://en.wikipedia.org/wiki/Euler_angles">intrinsic Proper Euler
Angles</a> defined by angles [a](#), [b](#), and [c](#), and order [order](#).  
Rotations are applied to the axes in the order specified by [order](#):
rotation by angle [a](#) is applied first, then by angle [b](#), then by angle
[c](#). Angles are in radians.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/MathUtils.js">src/math/MathUtils.js</a>

