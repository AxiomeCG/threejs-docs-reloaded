[page:Object3D] → [page:Line] → [page:LineSegments] →

# Box3Helper

Helper object to visualize a [page:Box3].

## Code Example

  
```ts  
const box = new THREE.Box3(); box.setFromCenterAndSize( new THREE.Vector3( 1,
1, 1 ), new THREE.Vector3( 2, 1, 3 ) ); const helper = new THREE.Box3Helper(
box, 0xffff00 ); scene.add( helper );  
```  

## Constructor

###  function Box3Helper( box: Box3, color: Color ): void;

[page:Box3 box] -- the Box3 to show.  
[page:Color color] -- (optional) the box's color. Default is 0xffff00.  
  
Creates a new wireframe box that represents the passed Box3.

## Properties

See the base [page:LineSegments] class for common properties.

###  Box3 box;

The Box3 being visualized.

## Methods

See the base [page:LineSegments] class for common methods.

###  function updateMatrixWorld( force: Boolean ): undefined;

This overrides the method in the base [page:Object3D] class so that it also
updates the wireframe box to the extent of the [page:Box3Helper.box .box]
property.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

