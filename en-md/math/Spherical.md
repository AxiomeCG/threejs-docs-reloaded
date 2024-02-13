# Spherical

A point's [link:https://en.wikipedia.org/wiki/Spherical_coordinate_system
spherical coordinates].

## Constructor

###  function Spherical( radius: Float, phi: Float, theta: Float ): void;

[page:Float radius] - the radius, or the
[link:https://en.wikipedia.org/wiki/Euclidean_distance Euclidean distance]
(straight-line distance) from the point to the origin. Default is `1.0`.  
[page:Float phi] - polar angle in radians from the y (up) axis. Default is
`0`.  
[page:Float theta] - equator angle in radians around the y (up) axis. Default
is `0`.  
  
The poles (phi) are at the positive and negative y axis. The equator (theta)
starts at positive z.

## Properties

###  Float radius;

###  Float phi;

###  Float theta;

## Methods

###  function clone( ): Spherical;

Returns a new spherical with the same [page:.radius radius], [page:.phi phi]
and [page:.theta theta] properties as this one.

###  function copy( s: Spherical ): this;

Copies the values of the passed Spherical's [page:.radius radius], [page:.phi
phi] and [page:.theta theta] properties to this spherical.

###  function makeSafe( ): this;

Restricts the polar angle [page:.phi phi] to be between 0.000001 and pi -
0.000001.

###  function set( radius: Float, phi: Float, theta: Float ): this;

Sets values of this spherical's [page:.radius radius], [page:.phi phi] and
[page:.theta theta] properties.

###  function setFromVector3( vec3: Vector3 ): this;

Sets values of this spherical's [page:.radius radius], [page:.phi phi] and
[page:.theta theta] properties from the [page:Vector3 Vector3].

###  function setFromCartesianCoords( x: Float, y: Float, z: Float ): this;

Sets values of this spherical's [page:.radius radius], [page:.phi phi] and
[page:.theta theta] properties from Cartesian coordinates.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

