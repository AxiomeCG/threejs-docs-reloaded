[page:BufferGeometry] →

# [name]

A class for generating a two-dimensional ring geometry.

## Code Example

  
```ts  
const geometry = new THREE.RingGeometry( 1, 5, 32 );  
const material = new THREE.MeshBasicMaterial( { color: 0xffff00, side:
THREE.DoubleSide } );  
const mesh = new THREE.Mesh( geometry, material ); scene.add( mesh );  
```  

## Constructor

###  [name]([param:Float innerRadius], [param:Float outerRadius],
[param:Integer thetaSegments], [param:Integer phiSegments], [param:Float
thetaStart], [param:Float thetaLength])

innerRadius — Default is `0.5`.  
outerRadius — Default is `1`.  
thetaSegments — Number of segments. A higher number means the ring will be
more round. Minimum is `3`. Default is `32`.  
phiSegments — Minimum is `1`. Default is `1`.  
thetaStart — Starting angle. Default is `0`.  
thetaLength — Central angle. Default is Math.PI * 2.

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

