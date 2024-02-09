# [name]

An object with several math utility functions.

## Functions

###  [method:Float clamp]( [param:Float value], [param:Float min],
[param:Float max] )

[page:Float value] — Value to be clamped.  
[page:Float min] — Minimum value.  
[page:Float max] — Maximum value.  
  
Clamps the [page:Float value] to be between [page:Float min] and [page:Float
max].

### [method:Float degToRad]( [param:Float degrees] )

Converts degrees to radians.

###  [method:Integer euclideanModulo]( [param:Integer n], [param:Integer m] )

[page:Integer n], [page:Integer m] - Integers  
  
Computes the Euclidean modulo of [page:Integer m] % [page:Integer n], that is:  
```ts ( ( n % m ) + m ) % m ```  

### [method:UUID generateUUID]( )

Generate a [link:https://en.wikipedia.org/wiki/Universally_unique_identifier
UUID] (universally unique identifier).

### [method:Boolean isPowerOfTwo]( [param:Number n] )

Return `true` if [page:Number n] is a power of 2.

###  [method:Float inverseLerp]( [param:Float x], [param:Float y],
[param:Float value] )

[page:Float x] - Start point.  
[page:Float y] - End point.  
[page:Float value] - A value between start and end.  
  
Returns the percentage in the closed interval `[0, 1]` of the given value
between the start and end point.

###  [method:Float lerp]( [param:Float x], [param:Float y], [param:Float t] )

[page:Float x] - Start point.  
[page:Float y] - End point.  
[page:Float t] - interpolation factor in the closed interval `[0, 1]`.  
  
Returns a value [link:https://en.wikipedia.org/wiki/Linear_interpolation
linearly interpolated] from two known points based on the given interval -
[page:Float t] = 0 will return [page:Float x] and [page:Float t] = 1 will
return [page:Float y].

###  [method:Float damp]( [param:Float x], [param:Float y], [param:Float
lambda], [param:Float dt] )

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

###  [method:Float mapLinear]( [param:Float x], [param:Float a1], [param:Float
a2], [param:Float b1], [param:Float b2] )

[page:Float x] — Value to be mapped.  
[page:Float a1] — Minimum value for range A.  
[page:Float a2] — Maximum value for range A.  
[page:Float b1] — Minimum value for range B.  
[page:Float b2] — Maximum value for range B.  
  
Linear mapping of [page:Float x] from range [[page:Float a1], [page:Float a2]]
to range [[page:Float b1], [page:Float b2]].

### [method:Float pingpong]( [param:Float x], [param:Float length] )

[page:Float x] — The value to pingpong.  
[page:Float length] — The positive value the function will pingpong to.
Default is `1`.  
  
Returns a value that alternates between `0` and [param:Float length].

### [method:Integer ceilPowerOfTwo]( [param:Number n] )

Returns the smallest power of 2 that is greater than or equal to [page:Number
n].

### [method:Integer floorPowerOfTwo]( [param:Number n] )

Returns the largest power of `2` that is less than or equal to [page:Number
n].

### [method:Float radToDeg]( [param:Float radians] )

Converts radians to degrees.

### [method:Float randFloat]( [param:Float low], [param:Float high] )

Random float in the interval [[page:Float low], [page:Float high]].

### [method:Float randFloatSpread]( [param:Float range] )

Random float in the interval [- [page:Float range] / 2, [page:Float range] /
2].

###  [method:Integer randInt]( [param:Integer low], [param:Integer high] )

Random integer in the interval [[page:Float low], [page:Float high]].

### [method:Float seededRandom]( [param:Integer seed] )

Deterministic pseudo-random float in the interval `[0, 1]`. The integer
[page:Integer seed] is optional.

###  [method:Float smoothstep]( [param:Float x], [param:Float min],
[param:Float max] )

[page:Float x] - The value to evaluate based on its position between min and
max.  
[page:Float min] - Any x value below min will be `0`.  
[page:Float max] - Any x value above max will be `1`.  
  
Returns a value between 0-1 that represents the percentage that x has moved
between min and max, but smoothed or slowed down the closer X is to the min
and max.  
  
See [link:http://en.wikipedia.org/wiki/Smoothstep Smoothstep] for details.

###  [method:Float smootherstep]( [param:Float x], [param:Float min],
[param:Float max] )

[page:Float x] - The value to evaluate based on its position between min and
max.  
[page:Float min] - Any x value below min will be `0`.  
[page:Float max] - Any x value above max will be `1`.  
  
Returns a value between 0-1. A
[link:https://en.wikipedia.org/wiki/Smoothstep#Variations variation on
smoothstep] that has zero 1st and 2nd order derivatives at x=0 and x=1.

###  [method:undefined setQuaternionFromProperEuler]( [param:Quaternion q],
[param:Float a], [param:Float b], [param:Float c], [param:String order] )

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

