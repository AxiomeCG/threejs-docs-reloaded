# Cylindrical

A point's [link:https://en.wikipedia.org/wiki/Cylindrical_coordinate_system
cylindrical coordinates].

## Constructor

###  function Cylindrical( radius: Float, theta: Float, y: Float ): void;

[page:Float radius] - distance from the origin to a point in the x-z plane.
Default is `1.0`.  
[page:Float theta] - counterclockwise angle in the x-z plane measured in
radians from the positive z-axis. Default is `0`.  
[page:Float y] - height above the x-z plane. Default is `0`.

## Properties

###  Float radius;

###  Float theta;

###  Float y;

## Methods

###  function clone( ): Cylindrical;

Returns a new cylindrical with the same [page:.radius radius], [page:.theta
theta] and [page:.y y] properties as this one.

###  function copy( other: Cylindrical ): this;

Copies the values of the passed Cylindrical's [page:.radius radius],
[page:.theta theta] and [page:.y y] properties to this cylindrical.

###  function set( radius: Float, theta: Float, y: Float ): this;

Sets values of this cylindrical's [page:.radius radius], [page:.theta theta]
and [page:.y y] properties.

###  function setFromVector3( vec3: Vector3 ): this;

Sets values of this cylindrical's [page:.radius radius], [page:.theta theta]
and [page:.y y] properties from the [page:Vector3 Vector3].

###  function setFromCartesianCoords( x: Float, y: Float, z: Float ): this;

Sets values of this cylindrical's [page:.radius radius], [page:.theta theta]
and [page:.y y] properties from Cartesian coordinates.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

