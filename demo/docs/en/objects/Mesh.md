[Object3D](en\core\Object3D.html) →

# Mesh

Class representing triangular <a
href="https://en.wikipedia.org/wiki/Polygon_mesh">polygon mesh</a> based
objects. Also serves as a base for other classes such as
[SkinnedMesh](en\objects\SkinnedMesh.html).

## Code Example

  
```ts  
const geometry = new THREE.BoxGeometry( 1, 1, 1 ); const material = new
THREE.MeshBasicMaterial( { color: 0xffff00 } ); const mesh = new THREE.Mesh(
geometry, material ); scene.add( mesh );  
```  

## Constructor

### Mesh

  
  
```ts  
function Mesh( geometry: BufferGeometry, material: Material ): void;  
```  

[geometry](en\core\BufferGeometry.html) — (optional) an instance of
[BufferGeometry](en\core\BufferGeometry.html). Default is a new
[BufferGeometry](en\core\BufferGeometry.html).  
[material](en\materials\Material.html) — (optional) a single or an array of
[Material](en\materials\Material.html). Default is a new
[MeshBasicMaterial](en\materials\MeshBasicMaterial.html)

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### geometry

  
  
```ts  
geometry: BufferGeometry;  
```  

An instance of [BufferGeometry](en\core\BufferGeometry.html) (or derived
classes), defining the object's structure.

### isMesh

  
  
```ts  
isMesh: Boolean;  
```  

Read-only flag to check if a given object is of type Mesh.

### material

  
  
```ts  
material: Material;  
```  

An instance of material derived from the
[Material](en\materials\Material.html) base class or an array of materials,
defining the object's appearance. Default is a
[MeshBasicMaterial](en\materials\MeshBasicMaterial.html).

### morphTargetInfluences

  
  
```ts  
morphTargetInfluences: Array;  
```  

An array of weights typically from 0-1 that specify how much of the morph is
applied. Undefined by default, but reset to a blank array by
[updateMorphTargets](#).

### morphTargetDictionary

  
  
```ts  
morphTargetDictionary: Object;  
```  

A dictionary of morphTargets based on the morphTarget.name property. Undefined
by default, but rebuilt [updateMorphTargets](#).

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### clone

  
  
```ts  
function clone( ): Mesh;  
```  

Returns a clone of this Mesh object and its descendants.

### getVertexPosition

  
  
```ts  
function getVertexPosition( index: Integer, target: Vector3 ): Vector3;  
```  

Get the local-space position of the vertex at the given index, taking into
account the current animation state of both morph targets and skinning.

### raycast

  
  
```ts  
function raycast( raycaster: Raycaster, intersects: Array ): undefined;  
```  

Get intersections between a casted ray and this mesh.
[Raycaster.intersectObject](#) will call this method, but the results are not
ordered.

### updateMorphTargets

  
  
```ts  
function updateMorphTargets( ): undefined;  
```  

Updates the morphTargets to have no influence on the object. Resets the
[morphTargetInfluences](#) and [morphTargetDictionary](#) properties.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/Mesh.js">src/objects/Mesh.js</a>

