[page:BufferGeometry] →

# [name]

Creates a torus knot, the particular shape of which is defined by a pair of
coprime integers, p and q. If p and q are not coprime, the result will be a
torus link.

## Code Example

  
```ts  
const geometry = new THREE.TorusKnotGeometry( 10, 3, 100, 16 );  
const material = new THREE.MeshBasicMaterial( { color: 0xffff00 } );  
const torusKnot = new THREE.Mesh( geometry, material ); scene.add( torusKnot
);  
```  

## Constructor

###  [name]([param:Float radius], [param:Float tube], [param:Integer
tubularSegments], [param:Integer radialSegments], [param:Integer p],
[param:Integer q])

  * radius - Radius of the torus. Default is `1`.
  * tube — Radius of the tube. Default is `0.4`.
  * tubularSegments — Default is `64`.
  * radialSegments — Default is `8`.
  * p — This value determines, how many times the geometry winds around its axis of rotational symmetry. Default is `2`. 
  * q — This value determines, how many times the geometry winds around a circle in the interior of the torus. Default is `3`. 

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

