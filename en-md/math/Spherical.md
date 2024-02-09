# [name]

A point's [link:https://en.wikipedia.org/wiki/Spherical_coordinate_system
spherical coordinates].

## Constructor

###  [name]( [param:Float radius], [param:Float phi], [param:Float theta] )

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

### <br/> Float radius; <br/>

### <br/> Float phi; <br/>

### <br/> Float theta; <br/>

## Methods

### [method:Spherical clone]()

Returns a new spherical with the same [page:.radius radius], [page:.phi phi]
and [page:.theta theta] properties as this one.

### <br/> function copy( s: Spherical ): copy; <br/>

Copies the values of the passed Spherical's [page:.radius radius], [page:.phi
phi] and [page:.theta theta] properties to this spherical.

### <br/> function makeSafe( ): makeSafe; <br/>

Restricts the polar angle [page:.phi phi] to be between 0.000001 and pi -
0.000001.

### <br/> function set( radius: Float, phi: Float, theta: Float ): set; <br/>

Sets values of this spherical's [page:.radius radius], [page:.phi phi] and
[page:.theta theta] properties.

### <br/> function setFromVector3( vec3: Vector3 ): setFromVector3; <br/>

Sets values of this spherical's [page:.radius radius], [page:.phi phi] and
[page:.theta theta] properties from the [page:Vector3 Vector3].

### <br/> function setFromCartesianCoords( x: Float, y: Float, z: Float ):
setFromCartesianCoords; <br/>

Sets values of this spherical's [page:.radius radius], [page:.phi phi] and
[page:.theta theta] properties from Cartesian coordinates.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

