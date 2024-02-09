# [name]

A point's [link:https://en.wikipedia.org/wiki/Cylindrical_coordinate_system
cylindrical coordinates].

## Constructor

###  [name]( [param:Float radius], [param:Float theta], [param:Float y] )

[page:Float radius] - distance from the origin to a point in the x-z plane.
Default is `1.0`.  
[page:Float theta] - counterclockwise angle in the x-z plane measured in
radians from the positive z-axis. Default is `0`.  
[page:Float y] - height above the x-z plane. Default is `0`.

## Properties

### <br/> Float radius; <br/>

### <br/> Float theta; <br/>

### <br/> Float y; <br/>

## Methods

### [method:Cylindrical clone]()

Returns a new cylindrical with the same [page:.radius radius], [page:.theta
theta] and [page:.y y] properties as this one.

### <br/> function copy( other: Cylindrical ): copy; <br/>

Copies the values of the passed Cylindrical's [page:.radius radius],
[page:.theta theta] and [page:.y y] properties to this cylindrical.

### <br/> function set( radius: Float, theta: Float, y: Float ): set; <br/>

Sets values of this cylindrical's [page:.radius radius], [page:.theta theta]
and [page:.y y] properties.

### <br/> function setFromVector3( vec3: Vector3 ): setFromVector3; <br/>

Sets values of this cylindrical's [page:.radius radius], [page:.theta theta]
and [page:.y y] properties from the [page:Vector3 Vector3].

### <br/> function setFromCartesianCoords( x: Float, y: Float, z: Float ):
setFromCartesianCoords; <br/>

Sets values of this cylindrical's [page:.radius radius], [page:.theta theta]
and [page:.y y] properties from Cartesian coordinates.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

