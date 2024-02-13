[page:BufferGeometry] →

# CylinderGeometry

A class for generating cylinder geometries.

## Code Example

  
```ts  
const geometry = new THREE.CylinderGeometry( 5, 5, 20, 32 ); const material =
new THREE.MeshBasicMaterial( {color: 0xffff00} ); const cylinder = new
THREE.Mesh( geometry, material ); scene.add( cylinder );  
```  

## Constructor

###  function CylinderGeometry( radiusTop: Float, radiusBottom: Float, height:
Float, radialSegments: Integer, heightSegments: Integer, openEnded: Boolean,
thetaStart: Float, thetaLength: Float ): void;

radiusTop — Radius of the cylinder at the top. Default is `1`.  
radiusBottom — Radius of the cylinder at the bottom. Default is `1`.  
height — Height of the cylinder. Default is `1`.  
radialSegments — Number of segmented faces around the circumference of the
cylinder. Default is `32`  
heightSegments — Number of rows of faces along the height of the cylinder.
Default is `1`.  
openEnded — A Boolean indicating whether the ends of the cylinder are open or
capped. Default is false, meaning capped.  
thetaStart — Start angle for first segment, default = 0 (three o'clock
position).  
thetaLength — The central angle, often called theta, of the circular sector.
The default is `2`*Pi, which makes for a complete cylinder.

## Properties

See the base [page:BufferGeometry] class for common properties.

###  Object parameters;

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [page:BufferGeometry] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

