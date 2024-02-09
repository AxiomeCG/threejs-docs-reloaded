# [name]

A class representing [link:http://en.wikipedia.org/wiki/Euler_angles Euler
Angles].  
  
Euler angles describe a rotational transformation by rotating an object on its
various axes in specified amounts per axis, and a specified axis order.

Iterating through a [name] instance will yield its components (x, y, z, order)
in the corresponding order.

## Code Example

  
```ts  
const a = new THREE.Euler( 0, 1, 1.57, 'XYZ' );  
const b = new THREE.Vector3( 1, 0, 1 );  
b.applyEuler(a);  
```  

## Constructor

###  [name]( [param:Float x], [param:Float y], [param:Float z], [param:String
order] )

[page:Float x] - (optional) the angle of the x axis in radians. Default is
`0`.  
[page:Float y] - (optional) the angle of the y axis in radians. Default is
`0`.  
[page:Float z] - (optional) the angle of the z axis in radians. Default is
`0`.  
[page:String order] - (optional) a string representing the order that the
rotations are applied, defaults to 'XYZ' (must be upper case).  
  

## Properties

### <br/> Boolean isEuler; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> String order; <br/>

The order in which to apply rotations. Default is 'XYZ', which means that the
object will first be rotated around its X axis, then its Y axis and finally
its Z axis. Other possibilities are: 'YZX', 'ZXY', 'XZY', 'YXZ' and 'ZYX'.
These must be in upper case.  
  
Three.js uses `intrinsic` Tait-Bryan angles. This means that rotations are
performed with respect to the `local` coordinate system. That is, for order
'XYZ', the rotation is first around the local-X axis (which is the same as the
world-X axis), then around local-Y (which may now be different from the world
Y-axis), then local-Z (which may be different from the world Z-axis).  
  

### <br/> Float x; <br/>

The current value of the x component.  
  

### <br/> Float y; <br/>

The current value of the y component.  
  

### <br/> Float z; <br/>

The current value of the z component.  
  

## Methods

### <br/> function copy( euler: Euler ): copy; <br/>

Copies value of [page:Euler euler] to this euler.

### [method:Euler clone]()

Returns a new Euler with the same parameters as this one.

### [method:Boolean equals]( [param:Euler euler] )

Checks for strict equality of this euler and [page:Euler euler].

### <br/> function fromArray( array: Array ): fromArray; <br/>

[page:Array array] of length 3 or 4. The optional 4th argument corresponds to
the [page:.order order].  
  
Assigns this euler's [page:.x x] angle to `array[0]`.  
Assigns this euler's [page:.y y] angle to `array[1]`.  
Assigns this euler's [page:.z z] angle to `array[2]`.  
Optionally assigns this euler's [page:.order order] to `array[3]`.

### <br/> function reorder( newOrder: String ): reorder; <br/>

Resets the euler angle with a new order by creating a quaternion from this
euler angle and then setting this euler angle with the quaternion and the new
order.  
  
_*Warning*: this discards revolution information._

### <br/> function set( x: Float, y: Float, z: Float, order: String ): set;
<br/>

[page:.x x] - the angle of the x axis in radians.  
[page:.y y] - the angle of the y axis in radians.  
[page:.z z] - the angle of the z axis in radians.  
[page:.order order] - (optional) a string representing the order that the
rotations are applied.  
  
Sets the angles of this euler transform and optionally the [page:.order
order].

### <br/> function setFromRotationMatrix( m: Matrix4, order: String ):
setFromRotationMatrix; <br/>

[page:Matrix4 m] - a [page:Matrix4] of which the upper 3x3 of matrix is a pure
[link:https://en.wikipedia.org/wiki/Rotation_matrix rotation matrix] (i.e.
unscaled).  
[page:.order order] - (optional) a string representing the order that the
rotations are applied.  
Sets the angles of this euler transform from a pure rotation matrix based on
the orientation specified by order.

### <br/> function setFromQuaternion( q: Quaternion, order: String ):
setFromQuaternion; <br/>

[page:Quaternion q] - a normalized quaternion.  
[page:.order order] - (optional) a string representing the order that the
rotations are applied.  
Sets the angles of this euler transform from a normalized quaternion based on
the orientation specified by [page:.order order].

### <br/> function setFromVector3( vector: Vector3, order: String ):
setFromVector3; <br/>

[page:Vector3 vector] - [page:Vector3].  
[page:.order order] - (optional) a string representing the order that the
rotations are applied.  
  
Set the [page:.x x], [page:.y y] and [page:.z z], and optionally update the
[page:.order order].

###  [method:Array toArray]( [param:Array array], [param:Integer offset] )

[page:Array array] - (optional) array to store the euler in.  
[page:Integer offset] (optional) offset in the array.  
Returns an array of the form [[page:.x x], [page:.y y], [page:.z z],
[page:.order order ]].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

