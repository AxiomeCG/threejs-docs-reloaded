# Euler

A class representing <a href="http://en.wikipedia.org/wiki/Euler_angles">Euler
Angles</a>.  
  
Euler angles describe a rotational transformation by rotating an object on its
various axes in specified amounts per axis, and a specified axis order.

Iterating through a Euler instance will yield its components (x, y, z, order)
in the corresponding order.

## Code Example

  
```ts  
const a = new THREE.Euler( 0, 1, 1.57, 'XYZ' );const b = new THREE.Vector3( 1,
0, 1 );b.applyEuler(a);  
```  

## Constructor

### Euler

  
  
```ts  
function Euler( x: Float, y: Float, z: Float, order: String ): void;  
```  

[x](#) - (optional) the angle of the x axis in radians. Default is `0`.  
[y](#) - (optional) the angle of the y axis in radians. Default is `0`.  
[z](#) - (optional) the angle of the z axis in radians. Default is `0`.  
[order](#) - (optional) a string representing the order that the rotations are
applied, defaults to 'XYZ' (must be upper case).  
  

## Properties

### isEuler

  
  
```ts  
isEuler: Boolean;  
```  

Read-only flag to check if a given object is of type Euler.

### order

  
  
```ts  
order: String;  
```  

The order in which to apply rotations. Default is 'XYZ', which means that the
object will first be rotated around its X axis, then its Y axis and finally
its Z axis. Other possibilities are: 'YZX', 'ZXY', 'XZY', 'YXZ' and 'ZYX'.
These must be in upper case.  
  
Three.js uses `intrinsic` Tait-Bryan angles. This means that rotations are
performed with respect to the `local` coordinate system. That is, for order
'XYZ', the rotation is first around the local-X axis (which is the same as the
world-X axis), then around local-Y (which may now be different from the world
Y-axis), then local-Z (which may be different from the world Z-axis).  
  

### x

  
  
```ts  
x: Float;  
```  

The current value of the x component.  
  

### y

  
  
```ts  
y: Float;  
```  

The current value of the y component.  
  

### z

  
  
```ts  
z: Float;  
```  

The current value of the z component.  
  

## Methods

### copy

  
  
```ts  
function copy( euler: Euler ): this;  
```  

Copies value of [euler](en\math\Euler.html) to this euler.

### clone

  
  
```ts  
function clone( ): Euler;  
```  

Returns a new Euler with the same parameters as this one.

### equals

  
  
```ts  
function equals( euler: Euler ): Boolean;  
```  

Checks for strict equality of this euler and [euler](en\math\Euler.html).

### fromArray

  
  
```ts  
function fromArray( array: Array ): this;  
```  

[.rray](#rray) of length 3 or 4. The optional 4th argument corresponds to the
[.order](#order).  
  
Assigns this euler's [.x](#x) angle to `array[0]`.  
Assigns this euler's [.y](#y) angle to `array[1]`.  
Assigns this euler's [.z](#z) angle to `array[2]`.  
Optionally assigns this euler's [.order](#order) to `array[3]`.

### reorder

  
  
```ts  
function reorder( newOrder: String ): this;  
```  

Resets the euler angle with a new order by creating a quaternion from this
euler angle and then setting this euler angle with the quaternion and the new
order.  
  
 _*Warning*: this discards revolution information._

### set

  
  
```ts  
function set( x: Float, y: Float, z: Float, order: String ): this;  
```  

[.x](#x) - the angle of the x axis in radians.  
[.y](#y) - the angle of the y axis in radians.  
[.z](#z) - the angle of the z axis in radians.  
[.order](#order) - (optional) a string representing the order that the
rotations are applied.  
  
Sets the angles of this euler transform and optionally the [.order](#order).

### setFromRotationMatrix

  
  
```ts  
function setFromRotationMatrix( m: Matrix4, order: String ): this;  
```  

[m](en\math\Matrix4.html) - a [Matrix4](en\math\Matrix4.html) of which the
upper 3x3 of matrix is a pure <a
href="https://en.wikipedia.org/wiki/Rotation_matrix">rotation matrix</a> (i.e.
unscaled).  
[.order](#order) - (optional) a string representing the order that the
rotations are applied.  
Sets the angles of this euler transform from a pure rotation matrix based on
the orientation specified by order.

### setFromQuaternion

  
  
```ts  
function setFromQuaternion( q: Quaternion, order: String ): this;  
```  

[q](en\math\Quaternion.html) - a normalized quaternion.  
[.order](#order) - (optional) a string representing the order that the
rotations are applied.  
Sets the angles of this euler transform from a normalized quaternion based on
the orientation specified by [.order](#order).

### setFromVector3

  
  
```ts  
function setFromVector3( vector: Vector3, order: String ): this;  
```  

[vector](en\math\Vector3.html) - [Vector3](en\math\Vector3.html).  
[.order](#order) - (optional) a string representing the order that the
rotations are applied.  
  
Set the [.x](#x), [.y](#y) and [.z](#z), and optionally update the
[.order](#order).

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - (optional) array to store the euler in.  
[offset](#) (optional) offset in the array.  
Returns an array of the form [[.x](#x), [.y](#y), [.z](#z), [.order](#order)].

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Euler.js">src/math/Euler.js</a>

