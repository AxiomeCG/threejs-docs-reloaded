[page:Object3D] →

# [name]

This is almost identical to an [page:Object3D Object3D]. Its purpose is to
make working with groups of objects syntactically clearer.

## Code Example

  
```ts  
const geometry = new THREE.BoxGeometry( 1, 1, 1 );  
const material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );  
  
const cubeA = new THREE.Mesh( geometry, material );  
cubeA.position.set( 100, 100, 0 );  
  
const cubeB = new THREE.Mesh( geometry, material );  
cubeB.position.set( -100, -100, 0 );  
  
//create a group and add the two cubes  
//These cubes can now be rotated / scaled etc as a group  
const group = new THREE.Group();  
group.add( cubeA );  
group.add( cubeB );  
  
scene.add( group );  
```  

## Constructor

### [name]( )

## Properties

See the base [page:Object3D] class for common properties.

### <br/> Boolean isGroup; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> String type; <br/>

A string 'Group'. This should not be changed.

## Methods

See the base [page:Object3D] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

