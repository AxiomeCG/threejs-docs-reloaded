# Raycaster

This class is designed to assist with
[link:https://en.wikipedia.org/wiki/Ray_casting raycasting]. Raycasting is
used for mouse picking (working out what objects in the 3d space the mouse is
over) amongst other things.

## Code Example

  
```ts  
const raycaster = new THREE.Raycaster(); const pointer = new THREE.Vector2();
function onPointerMove( event ) { // calculate pointer position in normalized
device coordinates // (-1 to +1) for both components pointer.x = (
event.clientX / window.innerWidth ) * 2 - 1; pointer.y = - ( event.clientY /
window.innerHeight ) * 2 + 1; } function render() { // update the picking ray
with the camera and pointer position raycaster.setFromCamera( pointer, camera
); // calculate objects intersecting the picking ray const intersects =
raycaster.intersectObjects( scene.children ); for ( let i = 0; i <
intersects.length; i ++ ) { intersects[ i ].object.material.color.set(
0xff0000 ); } renderer.render( scene, camera ); } window.addEventListener(
'pointermove', onPointerMove ); window.requestAnimationFrame(render);  
```  

## Examples

[example:webgl_interactive_cubes Raycasting to a Mesh]  
[example:webgl_interactive_cubes_ortho Raycasting to a Mesh in using an
OrthographicCamera]  
[example:webgl_interactive_buffergeometry Raycasting to a Mesh with
BufferGeometry]  
[example:webgl_instancing_raycast Raycasting to a InstancedMesh]  
[example:webgl_interactive_lines Raycasting to a Line]  
[example:webgl_interactive_raycasting_points Raycasting to Points]  
[example:webgl_geometry_terrain_raycast Terrain raycasting]  
[example:webgl_interactive_voxelpainter Raycasting to paint voxels]  
[example:webgl_raycaster_texture Raycast to a Texture]

## Constructor

###  function Raycaster( origin: Vector3, direction: Vector3, near: Float,
far: Float ): void;

[page:Vector3 origin] — The origin vector where the ray casts from.  
[page:Vector3 direction] — The direction vector that gives direction to the
ray. Should be normalized.  
[page:Float near] — All results returned are further away than near. Near
can't be negative. Default value is `0`.  
[page:Float far] — All results returned are closer than far. Far can't be
lower than near. Default value is Infinity.

This creates a new raycaster object.  

## Properties

###  Float far;

The far factor of the raycaster. This value indicates which objects can be
discarded based on the distance. This value shouldn't be negative and should
be larger than the near property.

###  Float near;

The near factor of the raycaster. This value indicates which objects can be
discarded based on the distance. This value shouldn't be negative and should
be smaller than the far property.

###  Camera camera;

The camera to use when raycasting against view-dependent objects such as
billboarded objects like [page:Sprites]. This field can be set manually or is
set when calling "setFromCamera". Defaults to null.

###  Layers layers;

Used by Raycaster to selectively ignore 3D objects when performing
intersection tests. The following code example ensures that only 3D objects on
layer `1` will be honored by the instance of Raycaster.  
```ts  
raycaster.layers.set( 1 ); object.layers.enable( 1 );  
```  

###  Object params;

An object with the following properties:  
```ts  
{ Mesh: {}, Line: { threshold: 1 }, LOD: {}, Points: { threshold: 1 }, Sprite:
{} }  
```  
Where threshold is the precision of the raycaster when intersecting objects,
in world units.

###  Ray ray;

The [Page:Ray] used for the raycasting.

## Methods

###  function set( origin: Vector3, direction: Vector3 ): undefined;

[page:Vector3 origin] — The origin vector where the ray casts from.  
[page:Vector3 direction] — The normalized direction vector that gives
direction to the ray.

Updates the ray with a new origin and direction. Please note that this method
only copies the values from the arguments.

###  function setFromCamera( coords: Vector2, camera: Camera ): undefined;

[page:Vector2 coords] — 2D coordinates of the mouse, in normalized device
coordinates (NDC)---X and Y components should be between `-1` and `1`.  
[page:Camera camera] — camera from which the ray should originate

Updates the ray with a new origin and direction.

###  function intersectObject( object: Object3D, recursive: Boolean,
optionalTarget: Array ): Array;

[page:Object3D object] — The object to check for intersection with the ray.  
[page:Boolean recursive] — If true, it also checks all descendants. Otherwise
it only checks intersection with the object. Default is true.  
[page:Array optionalTarget] — (optional) target to set the result. Otherwise a
new [page:Array] is instantiated. If set, you must clear this array prior to
each call (i.e., array.length = 0;).

Checks all intersection between the ray and the object with or without the
descendants. Intersections are returned sorted by distance, closest first. An
array of intersections is returned...

  
```ts  
[ { distance, point, face, faceIndex, object }, ... ]  
```  

[page:Float distance] – distance between the origin of the ray and the
intersection  
[page:Vector3 point] – point of intersection, in world coordinates  
[page:Object face] – intersected face  
[page:Integer faceIndex] – index of the intersected face  
[page:Object3D object] – the intersected object  
[page:Vector2 uv] - U,V coordinates at point of intersection  
[page:Vector2 uv1] - Second set of U,V coordinates at point of intersection  
[page:Vector3 normal] - interpolated normal vector at point of intersection  
[page:Integer instanceId] – The index number of the instance where the ray
intersects the InstancedMesh

`Raycaster` delegates to the [page:Object3D.raycast raycast] method of the
passed object, when evaluating whether the ray intersects the object or not.
This allows [page:Mesh meshes] to respond differently to ray casting than
[page:Line lines] and [page:Points pointclouds].

*Note* that for meshes, faces must be pointed towards the origin of the [page:.ray ray] in order to be detected; intersections of the ray passing through the back of a face will not be detected. To raycast against both faces of an object, you'll want to set the [page:Mesh.material material]'s [page:Material.side side] property to `THREE.DoubleSide`.

###  function intersectObjects( objects: Array, recursive: Boolean,
optionalTarget: Array ): Array;

[page:Array objects] — The objects to check for intersection with the ray.  
[page:Boolean recursive] — If true, it also checks all descendants of the
objects. Otherwise it only checks intersection with the objects. Default is
true.  
[page:Array optionalTarget] — (optional) target to set the result. Otherwise a
new [page:Array] is instantiated. If set, you must clear this array prior to
each call (i.e., array.length = 0;).

Checks all intersection between the ray and the objects with or without the
descendants. Intersections are returned sorted by distance, closest first.
Intersections are of the same form as those returned by
[page:.intersectObject].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

