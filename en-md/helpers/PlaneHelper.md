[page:Object3D] → [page:Line] → [page:LineSegments] →

# [name]

Helper object to visualize a [page:Plane].

## Code Example

  
```ts  
const plane = new THREE.Plane( new THREE.Vector3( 1, 1, 0.2 ), 3 );  
const helper = new THREE.PlaneHelper( plane, 1, 0xffff00 );  
scene.add( helper );  
```  

## Constructor

###  [name]( [param:Plane plane], [param:Float size], [param:Color hex] )

[page:Plane plane] -- the plane to visualize.  
[page:Float size] -- (optional) side length of plane helper. Default is 1.  
[page:Color color] -- (optional) the color of the helper. Default is 0xffff00.  
  
Creates a new wireframe representation of the passed plane.

## Properties

See the base [page:Line] class for common properties.

### <br/> Plane plane; <br/>

The [page:Plane plane] being visualized.

### <br/> Float size; <br/>

The side lengths of plane helper.

## Methods

See the base [page:LineSegments] class for common methods.

### [method:undefined updateMatrixWorld]( [param:Boolean force] )

This overrides the method in the base [page:Object3D] class so that it also
updates the helper object according to the [page:PlaneHelper.plane .plane] and
[page:PlaneHelper.size .size] properties.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

