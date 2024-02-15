# Cylindrical

A point's <a
href="https://en.wikipedia.org/wiki/Cylindrical_coordinate_system">cylindrical
coordinates</a>.

## Constructor

### Cylindrical

  
  
```ts  
function Cylindrical( radius: Float, theta: Float, y: Float ): void;  
```  

[radius](#) - distance from the origin to a point in the x-z plane. Default is
`1.0`.  
[theta](#) - counterclockwise angle in the x-z plane measured in radians from
the positive z-axis. Default is `0`.  
[y](#) - height above the x-z plane. Default is `0`.

## Properties

### radius

  
  
```ts  
radius: Float;  
```  

### theta

  
  
```ts  
theta: Float;  
```  

### y

  
  
```ts  
y: Float;  
```  

## Methods

### clone

  
  
```ts  
function clone( ): Cylindrical;  
```  

Returns a new cylindrical with the same [.radius](#radius), [.theta](#theta)
and [.y](#y) properties as this one.

### copy

  
  
```ts  
function copy( other: Cylindrical ): this;  
```  

Copies the values of the passed Cylindrical's [.radius](#radius),
[.theta](#theta) and [.y](#y) properties to this cylindrical.

### set

  
  
```ts  
function set( radius: Float, theta: Float, y: Float ): this;  
```  

Sets values of this cylindrical's [.radius](#radius), [.theta](#theta) and
[.y](#y) properties.

### setFromVector3

  
  
```ts  
function setFromVector3( vec3: Vector3 ): this;  
```  

Sets values of this cylindrical's [.radius](#radius), [.theta](#theta) and
[.y](#y) properties from the [.ector3](#ector3).

### setFromCartesianCoords

  
  
```ts  
function setFromCartesianCoords( x: Float, y: Float, z: Float ): this;  
```  

Sets values of this cylindrical's [.radius](#radius), [.theta](#theta) and
[.y](#y) properties from Cartesian coordinates.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Cylindrical.js">src/math/Cylindrical.js</a>

