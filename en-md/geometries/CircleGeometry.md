[page:BufferGeometry] →

# [name]

[name] is a simple shape of Euclidean geometry. It is constructed from a
number of triangular segments that are oriented around a central point and
extend as far out as a given radius. It is built counter-clockwise from a
start angle and a given central angle. It can also be used to create regular
polygons, where the number of segments determines the number of sides.

## Code Example

  
```ts  
const geometry = new THREE.CircleGeometry( 5, 32 );  
const material = new THREE.MeshBasicMaterial( { color: 0xffff00 } );  
const circle = new THREE.Mesh( geometry, material ); scene.add( circle );  
```  

## Constructor

###  [name]([param:Float radius], [param:Integer segments], [param:Float
thetaStart], [param:Float thetaLength])

radius — Radius of the circle, default = 1.  
segments — Number of segments (triangles), minimum = `3`, default = `32`.  
thetaStart — Start angle for first segment, default = `0` (three o'clock
position).  
thetaLength — The central angle, often called theta, of the circular sector.
The default is `2`*Pi, which makes for a complete circle.

## Properties

See the base [page:BufferGeometry] class for common properties.

### <br/> Object parameters; <br/>

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [page:BufferGeometry] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

