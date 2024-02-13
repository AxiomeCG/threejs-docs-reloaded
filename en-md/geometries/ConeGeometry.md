[page:BufferGeometry] → [page:CylinderGeometry] →

# ConeGeometry

A class for generating cone geometries.

## Code Example

  
```ts  
const geometry = new THREE.ConeGeometry( 5, 20, 32 ); const material = new
THREE.MeshBasicMaterial( {color: 0xffff00} );const cone = new
THREE.Mesh(geometry, material ); scene.add( cone );  
```  

## Constructor

###  function ConeGeometry( radius: Float, height: Float, radialSegments:
Integer, heightSegments: Integer, openEnded: Boolean, thetaStart: Float,
thetaLength: Float ): void;

radius — Radius of the cone base. Default is `1`.  
height — Height of the cone. Default is `1`.  
radialSegments — Number of segmented faces around the circumference of the
cone. Default is `32`  
heightSegments — Number of rows of faces along the height of the cone. Default
is `1`.  
openEnded — A Boolean indicating whether the base of the cone is open or
capped. Default is false, meaning capped.  
thetaStart — Start angle for first segment, default = 0 (three o'clock
position).  
thetaLength — The central angle, often called theta, of the circular sector.
The default is `2`*Pi, which makes for a complete cone.

## Properties

See the base [page:CylinderGeometry] class for common properties.

###  Object parameters;

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [page:CylinderGeometry] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

