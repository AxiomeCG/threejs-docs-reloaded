[page:Object3D] →

# Mesh

Class representing triangular [link:https://en.wikipedia.org/wiki/Polygon_mesh
polygon mesh] based objects. Also serves as a base for other classes such as
[page:SkinnedMesh].

## Code Example

  
```ts  
const geometry = new THREE.BoxGeometry( 1, 1, 1 ); const material = new
THREE.MeshBasicMaterial( { color: 0xffff00 } ); const mesh = new THREE.Mesh(
geometry, material ); scene.add( mesh );  
```  

## Constructor

###  function Mesh( geometry: BufferGeometry, material: Material ): void;

[page:BufferGeometry geometry] — (optional) an instance of
[page:BufferGeometry]. Default is a new [page:BufferGeometry].  
[page:Material material] — (optional) a single or an array of [page:Material].
Default is a new [page:MeshBasicMaterial]

## Properties

See the base [page:Object3D] class for common properties.

###  BufferGeometry geometry;

An instance of [page:BufferGeometry] (or derived classes), defining the
object's structure.

###  Boolean isMesh;

Read-only flag to check if a given object is of type Mesh.

###  Material material;

An instance of material derived from the [page:Material] base class or an
array of materials, defining the object's appearance. Default is a
[page:MeshBasicMaterial].

###  Array morphTargetInfluences;

An array of weights typically from 0-1 that specify how much of the morph is
applied. Undefined by default, but reset to a blank array by
[page:Mesh.updateMorphTargets updateMorphTargets].

###  Object morphTargetDictionary;

A dictionary of morphTargets based on the morphTarget.name property. Undefined
by default, but rebuilt [page:Mesh.updateMorphTargets updateMorphTargets].

## Methods

See the base [page:Object3D] class for common methods.

###  function clone( ): Mesh;

Returns a clone of this Mesh object and its descendants.

###  function getVertexPosition( index: Integer, target: Vector3 ): Vector3;

Get the local-space position of the vertex at the given index, taking into
account the current animation state of both morph targets and skinning.

###  function raycast( raycaster: Raycaster, intersects: Array ): undefined;

Get intersections between a casted ray and this mesh.
[page:Raycaster.intersectObject] will call this method, but the results are
not ordered.

###  function updateMorphTargets( ): undefined;

Updates the morphTargets to have no influence on the object. Resets the
[page:Mesh.morphTargetInfluences morphTargetInfluences] and
[page:Mesh.morphTargetDictionary morphTargetDictionary] properties.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

