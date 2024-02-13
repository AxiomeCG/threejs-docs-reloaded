[page:BufferGeometry] →

# TorusKnotGeometry

Creates a torus knot, the particular shape of which is defined by a pair of
coprime integers, p and q. If p and q are not coprime, the result will be a
torus link.

## Code Example

  
```ts  
const geometry = new THREE.TorusKnotGeometry( 10, 3, 100, 16 ); const material
= new THREE.MeshBasicMaterial( { color: 0xffff00 } ); const torusKnot = new
THREE.Mesh( geometry, material ); scene.add( torusKnot );  
```  

## Constructor

###  function TorusKnotGeometry( radius: Float, tube: Float, tubularSegments:
Integer, radialSegments: Integer, p: Integer, q: Integer ): void;

  * radius - Radius of the torus. Default is `1`.
  * tube — Radius of the tube. Default is `0.4`.
  * tubularSegments — Default is `64`.
  * radialSegments — Default is `8`.
  * p — This value determines, how many times the geometry winds around its axis of rotational symmetry. Default is `2`.
  * q — This value determines, how many times the geometry winds around a circle in the interior of the torus. Default is `3`.

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

