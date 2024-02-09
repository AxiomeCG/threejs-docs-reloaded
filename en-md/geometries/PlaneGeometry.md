[page:BufferGeometry] →

# [name]

A class for generating plane geometries.

## Code Example

  
```ts  
const geometry = new THREE.PlaneGeometry( 1, 1 );  
const material = new THREE.MeshBasicMaterial( {color: 0xffff00, side:
THREE.DoubleSide} );  
const plane = new THREE.Mesh( geometry, material );  
scene.add( plane );  
```  

## Constructor

###  [name]([param:Float width], [param:Float height], [param:Integer
widthSegments], [param:Integer heightSegments])

width — Width along the X axis. Default is `1`.  
height — Height along the Y axis. Default is `1`.  
widthSegments — Optional. Default is `1`.  
heightSegments — Optional. Default is `1`.

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
