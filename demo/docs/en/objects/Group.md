[Object3D](en\core\Object3D.html) →

# Group

This is almost identical to an [Object3D](en\core\Object3D.html). Its purpose
is to make working with groups of objects syntactically clearer.

## Code Example

  
```ts  
const geometry = new THREE.BoxGeometry( 1, 1, 1 ); const material = new
THREE.MeshBasicMaterial( {color: 0x00ff00} ); const cubeA = new THREE.Mesh(
geometry, material ); cubeA.position.set( 100, 100, 0 ); const cubeB = new
THREE.Mesh( geometry, material ); cubeB.position.set( -100, -100, 0 );
//create a group and add the two cubes //These cubes can now be rotated /
scaled etc as a group const group = new THREE.Group(); group.add( cubeA );
group.add( cubeB ); scene.add( group );  
```  

## Constructor

### Group

  
  
```ts  
function Group( ): void;  
```  

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### isGroup

  
  
```ts  
isGroup: Boolean;  
```  

Read-only flag to check if a given object is of type Group.

### type

  
  
```ts  
type: String;  
```  

A string 'Group'. This should not be changed.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/Group.js">src/objects/Group.js</a>

