[page:Object3D] → [page:Line] → [page:LineSegments] →

# PlaneHelper

Helper object to visualize a [page:Plane].

## Code Example

  
```ts  
const plane = new THREE.Plane( new THREE.Vector3( 1, 1, 0.2 ), 3 ); const
helper = new THREE.PlaneHelper( plane, 1, 0xffff00 ); scene.add( helper );  
```  

## Constructor

###  function PlaneHelper( plane: Plane, size: Float, hex: Color ): void;

[page:Plane plane] -- the plane to visualize.  
[page:Float size] -- (optional) side length of plane helper. Default is 1.  
[page:Color color] -- (optional) the color of the helper. Default is 0xffff00.  
  
Creates a new wireframe representation of the passed plane.

## Properties

See the base [page:Line] class for common properties.

###  Plane plane;

The [page:Plane plane] being visualized.

###  Float size;

The side lengths of plane helper.

## Methods

See the base [page:LineSegments] class for common methods.

###  function updateMatrixWorld( force: Boolean ): undefined;

This overrides the method in the base [page:Object3D] class so that it also
updates the helper object according to the [page:PlaneHelper.plane .plane] and
[page:PlaneHelper.size .size] properties.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

