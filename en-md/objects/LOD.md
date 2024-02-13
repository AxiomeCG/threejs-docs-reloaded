[page:Object3D] →

# LOD

Level of Detail - show meshes with more or less geometry based on distance
from the camera.  
  
Every level is associated with an object, and rendering can be switched
between them at the distances specified. Typically you would create, say,
three meshes, one for far away (low detail), one for mid range (medium detail)
and one for close up (high detail).

## Code Example

  
```ts  
const lod = new THREE.LOD(); //Create spheres with 3 levels of detail and
create new LOD levels for them for( let i = 0; i < 3; i++ ) { const geometry =
new THREE.IcosahedronGeometry( 10, 3 - i ) const mesh = new THREE.Mesh(
geometry, material ); lod.addLevel( mesh, i * 75 ); } scene.add( lod );  
```  

## Examples

[example:webgl_lod webgl / lod ]

## Constructor

###  function LOD( ): void;

Creates a new LOD.

## Properties

See the base [page:Object3D] class for common properties.

###  Boolean autoUpdate;

Whether the LOD object is updated automatically by the renderer per frame or
not. If set to false, you have to call [page:LOD.update]() in the render loop
by yourself. Default is true.

###  Boolean isLOD;

Read-only flag to check if a given object is of type LOD.

###  Array levels;

An array of [page:Object level] objects  
  
Each level is an object with the following properties:  
[page:Object3D object] - The [page:Object3D] to display at this level.  
[page:Float distance] - The distance at which to display this level of detail.  
[page:Float hysteresis] - Threshold used to avoid flickering at LOD
boundaries, as a fraction of distance.

## Methods

See the base [page:Object3D] class for common methods.

###  function addLevel( object: Object3D, distance: Float, hysteresis: Float
): this;

[page:Object3D object] - The [page:Object3D] to display at this level.  
[page:Float distance] - The distance at which to display this level of detail.
Default `0.0`.  
[page:Float hysteresis] - Threshold used to avoid flickering at LOD
boundaries, as a fraction of distance. Default `0.0`.  
  
Adds a mesh that will display at a certain distance and greater. Typically the
further away the distance, the lower the detail on the mesh.

###  function clone( ): LOD;

Returns a clone of this LOD object with its associated levels.

###  function getCurrentLevel( ): Integer;

Get the currently active LOD level. As index of the levels array.

###  function getObjectForDistance( distance: Float ): Object3D;

Get a reference to the first [page:Object3D] (mesh) that is greater than
[page:Float distance].

###  function raycast( raycaster: Raycaster, intersects: Array ): undefined;

Get intersections between a casted [page:Ray] and this LOD.
[page:Raycaster.intersectObject] will call this method.

###  function toJSON( ): Object;

Create a JSON structure with details of this LOD object.

###  function update( camera: Camera ): undefined;

Set the visibility of each [page:levels level]'s [page:Object3D object] based
on distance from the [page:Camera camera].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

