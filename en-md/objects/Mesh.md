[page:Object3D] →

# [name]

Class representing triangular [link:https://en.wikipedia.org/wiki/Polygon_mesh
polygon mesh] based objects. Also serves as a base for other classes such as
[page:SkinnedMesh].

## Code Example

  
```ts  
const geometry = new THREE.BoxGeometry( 1, 1, 1 );  
const material = new THREE.MeshBasicMaterial( { color: 0xffff00 } );  
const mesh = new THREE.Mesh( geometry, material );  
scene.add( mesh );  
```  

## Constructor

###  [name]( [param:BufferGeometry geometry], [param:Material material] )

[page:BufferGeometry geometry] — (optional) an instance of
[page:BufferGeometry]. Default is a new [page:BufferGeometry].  
[page:Material material] — (optional) a single or an array of [page:Material].
Default is a new [page:MeshBasicMaterial]

## Properties

See the base [page:Object3D] class for common properties.

### <br/> BufferGeometry geometry; <br/>

An instance of [page:BufferGeometry] (or derived classes), defining the
object's structure.

### <br/> Boolean isMesh; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Material material; <br/>

An instance of material derived from the [page:Material] base class or an
array of materials, defining the object's appearance. Default is a
[page:MeshBasicMaterial].

### <br/> Array morphTargetInfluences; <br/>

An array of weights typically from 0-1 that specify how much of the morph is
applied. Undefined by default, but reset to a blank array by
[page:Mesh.updateMorphTargets updateMorphTargets].

### <br/> Object morphTargetDictionary; <br/>

A dictionary of morphTargets based on the morphTarget.name property. Undefined
by default, but rebuilt [page:Mesh.updateMorphTargets updateMorphTargets].

## Methods

See the base [page:Object3D] class for common methods.

### [method:Mesh clone]()

Returns a clone of this [name] object and its descendants.

###  [method:Vector3 getVertexPosition]( [param:Integer index], [param:Vector3
target] )

Get the local-space position of the vertex at the given index, taking into
account the current animation state of both morph targets and skinning.

###  [method:undefined raycast]( [param:Raycaster raycaster], [param:Array
intersects] )

Get intersections between a casted ray and this mesh.
[page:Raycaster.intersectObject] will call this method, but the results are
not ordered.

### [method:undefined updateMorphTargets]()

Updates the morphTargets to have no influence on the object. Resets the
[page:Mesh.morphTargetInfluences morphTargetInfluences] and
[page:Mesh.morphTargetDictionary morphTargetDictionary] properties.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

