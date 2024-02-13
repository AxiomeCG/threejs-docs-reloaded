[page:BufferGeometry] →

# TorusGeometry

A class for generating torus geometries.

## Code Example

  
```ts  
const geometry = new THREE.TorusGeometry( 10, 3, 16, 100 ); const material =
new THREE.MeshBasicMaterial( { color: 0xffff00 } ); const torus = new
THREE.Mesh( geometry, material ); scene.add( torus );  
```  

## Constructor

###  function TorusGeometry( radius: Float, tube: Float, radialSegments:
Integer, tubularSegments: Integer, arc: Float ): void;

radius - Radius of the torus, from the center of the torus to the center of
the tube. Default is `1`.  
tube — Radius of the tube. Default is `0.4`.  
radialSegments — Default is `12`  
tubularSegments — Default is `48`.  
arc — Central angle. Default is Math.PI * 2.

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

