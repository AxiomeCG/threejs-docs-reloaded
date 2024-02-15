# Spherical

A point's <a
href="https://en.wikipedia.org/wiki/Spherical_coordinate_system">spherical
coordinates</a>.

## Constructor

### Spherical

  
  
```ts  
function Spherical( radius: Float, phi: Float, theta: Float ): void;  
```  

[radius](#) - the radius, or the <a
href="https://en.wikipedia.org/wiki/Euclidean_distance">Euclidean distance</a>
(straight-line distance) from the point to the origin. Default is `1.0`.  
[phi](#) - polar angle in radians from the y (up) axis. Default is `0`.  
[theta](#) - equator angle in radians around the y (up) axis. Default is `0`.  
  
The poles (phi) are at the positive and negative y axis. The equator (theta)
starts at positive z.

## Properties

### radius

  
  
```ts  
radius: Float;  
```  

### phi

  
  
```ts  
phi: Float;  
```  

### theta

  
  
```ts  
theta: Float;  
```  

## Methods

### clone

  
  
```ts  
function clone( ): Spherical;  
```  

Returns a new spherical with the same [.radius](#radius), [.phi](#phi) and
[.theta](#theta) properties as this one.

### copy

  
  
```ts  
function copy( s: Spherical ): this;  
```  

Copies the values of the passed Spherical's [.radius](#radius), [.phi](#phi)
and [.theta](#theta) properties to this spherical.

### makeSafe

  
  
```ts  
function makeSafe( ): this;  
```  

Restricts the polar angle [.phi](#phi) to be between 0.000001 and pi -
0.000001.

### set

  
  
```ts  
function set( radius: Float, phi: Float, theta: Float ): this;  
```  

Sets values of this spherical's [.radius](#radius), [.phi](#phi) and
[.theta](#theta) properties.

### setFromVector3

  
  
```ts  
function setFromVector3( vec3: Vector3 ): this;  
```  

Sets values of this spherical's [.radius](#radius), [.phi](#phi) and
[.theta](#theta) properties from the [.ector3](#ector3).

### setFromCartesianCoords

  
  
```ts  
function setFromCartesianCoords( x: Float, y: Float, z: Float ): this;  
```  

Sets values of this spherical's [.radius](#radius), [.phi](#phi) and
[.theta](#theta) properties from Cartesian coordinates.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Spherical.js">src/math/Spherical.js</a>

