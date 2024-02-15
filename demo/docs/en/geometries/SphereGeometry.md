[BufferGeometry](en\core\BufferGeometry.html) →

# SphereGeometry

A class for generating sphere geometries.

## Code Example

  
```ts  
const geometry = new THREE.SphereGeometry( 15, 32, 16 ); const material = new
THREE.MeshBasicMaterial( { color: 0xffff00 } ); const sphere = new THREE.Mesh(
geometry, material ); scene.add( sphere );  
```  

## Constructor

### SphereGeometry

  
  
```ts  
function SphereGeometry( radius: Float, widthSegments: Integer,
heightSegments: Integer, phiStart: Float, phiLength: Float, thetaStart: Float,
thetaLength: Float ): void;  
```  

radius — sphere radius. Default is `1`.  
widthSegments — number of horizontal segments. Minimum value is `3`, and the
default is `32`.  
heightSegments — number of vertical segments. Minimum value is `2`, and the
default is `16`.  
phiStart — specify horizontal starting angle. Default is `0`.  
phiLength — specify horizontal sweep angle size. Default is Math.PI * 2.  
thetaStart — specify vertical starting angle. Default is `0`.  
thetaLength — specify vertical sweep angle size. Default is Math.PI.  

The geometry is created by sweeping and calculating vertexes around the Y axis
(horizontal sweep) and the Z axis (vertical sweep). Thus, incomplete spheres
(akin to `'sphere slices'`) can be created through the use of different values
of phiStart, phiLength, thetaStart and thetaLength, in order to define the
points in which we start (or end) calculating those vertices.

## Properties

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
properties.

### parameters

  
  
```ts  
parameters: Object;  
```  

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/SphereGeometry.js">src/geometries/SphereGeometry.js</a>

