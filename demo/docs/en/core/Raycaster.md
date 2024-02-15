# Raycaster

This class is designed to assist with <a
href="https://en.wikipedia.org/wiki/Ray_casting">raycasting</a>. Raycasting is
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

### Raycaster

  
  
```ts  
function Raycaster( origin: Vector3, direction: Vector3, near: Float, far:
Float ): void;  
```  

[origin](en\math\Vector3.html) — The origin vector where the ray casts from.  
[direction](en\math\Vector3.html) — The direction vector that gives direction
to the ray. Should be normalized.  
[near](#) — All results returned are further away than near. Near can't be
negative. Default value is `0`.  
[far](#) — All results returned are closer than far. Far can't be lower than
near. Default value is Infinity.

This creates a new raycaster object.  

## Properties

### far

  
  
```ts  
far: Float;  
```  

The far factor of the raycaster. This value indicates which objects can be
discarded based on the distance. This value shouldn't be negative and should
be larger than the near property.

### near

  
  
```ts  
near: Float;  
```  

The near factor of the raycaster. This value indicates which objects can be
discarded based on the distance. This value shouldn't be negative and should
be smaller than the far property.

### camera

  
  
```ts  
camera: Camera;  
```  

The camera to use when raycasting against view-dependent objects such as
billboarded objects like [Sprites](#). This field can be set manually or is
set when calling "setFromCamera". Defaults to null.

### layers

  
  
```ts  
layers: Layers;  
```  

Used by Raycaster to selectively ignore 3D objects when performing
intersection tests. The following code example ensures that only 3D objects on
layer `1` will be honored by the instance of Raycaster.  
```ts  
raycaster.layers.set( 1 ); object.layers.enable( 1 );  
```  

### params

  
  
```ts  
params: Object;  
```  

An object with the following properties:  
```ts  
{ Mesh: {}, Line: { threshold: 1 }, LOD: {}, Points: { threshold: 1 }, Sprite:
{} }  
```  
Where threshold is the precision of the raycaster when intersecting objects,
in world units.

### ray

  
  
```ts  
ray: Ray;  
```  

The [Page:Ray] used for the raycasting.

## Methods

### set

  
  
```ts  
function set( origin: Vector3, direction: Vector3 ): undefined;  
```  

[origin](en\math\Vector3.html) — The origin vector where the ray casts from.  
[direction](en\math\Vector3.html) — The normalized direction vector that gives
direction to the ray.

Updates the ray with a new origin and direction. Please note that this method
only copies the values from the arguments.

### setFromCamera

  
  
```ts  
function setFromCamera( coords: Vector2, camera: Camera ): undefined;  
```  

[coords](en\math\Vector2.html) — 2D coordinates of the mouse, in normalized
device coordinates (NDC)---X and Y components should be between `-1` and `1`.  
[camera](en\cameras\Camera.html) — camera from which the ray should originate

Updates the ray with a new origin and direction.

### intersectObject

  
  
```ts  
function intersectObject( object: Object3D, recursive: Boolean,
optionalTarget: Array ): Array;  
```  

[object](en\core\Object3D.html) — The object to check for intersection with
the ray.  
[recursive](#) — If true, it also checks all descendants. Otherwise it only
checks intersection with the object. Default is true.  
[optionalTarget](#) — (optional) target to set the result. Otherwise a new
[Array](#) is instantiated. If set, you must clear this array prior to each
call (i.e., array.length = 0;).

Checks all intersection between the ray and the object with or without the
descendants. Intersections are returned sorted by distance, closest first. An
array of intersections is returned...

  
```ts  
[ { distance, point, face, faceIndex, object }, ... ]  
```  

[distance](#) – distance between the origin of the ray and the intersection  
[point](en\math\Vector3.html) – point of intersection, in world coordinates  
[face](#) – intersected face  
[faceIndex](#) – index of the intersected face  
[object](en\core\Object3D.html) – the intersected object  
[uv](en\math\Vector2.html) - U,V coordinates at point of intersection  
[uv1](en\math\Vector2.html) - Second set of U,V coordinates at point of
intersection  
[normal](en\math\Vector3.html) - interpolated normal vector at point of
intersection  
[instanceId](#) – The index number of the instance where the ray intersects
the InstancedMesh

`Raycaster` delegates to the [raycast](#) method of the passed object, when
evaluating whether the ray intersects the object or not. This allows
[meshes](en\objects\Mesh.html) to respond differently to ray casting than
[lines](en\objects\Line.html) and [pointclouds](en\objects\Points.html).

*Note* that for meshes, faces must be pointed towards the origin of the [.ray](#ray) in order to be detected; intersections of the ray passing through the back of a face will not be detected. To raycast against both faces of an object, you'll want to set the [material](#)'s [side](#) property to `THREE.DoubleSide`.

### intersectObjects

  
  
```ts  
function intersectObjects( objects: Array, recursive: Boolean, optionalTarget:
Array ): Array;  
```  

[objects](#) — The objects to check for intersection with the ray.  
[recursive](#) — If true, it also checks all descendants of the objects.
Otherwise it only checks intersection with the objects. Default is true.  
[optionalTarget](#) — (optional) target to set the result. Otherwise a new
[Array](#) is instantiated. If set, you must clear this array prior to each
call (i.e., array.length = 0;).

Checks all intersection between the ray and the objects with or without the
descendants. Intersections are returned sorted by distance, closest first.
Intersections are of the same form as those returned by [.intersectObject](#).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/Raycaster.js">src/core/Raycaster.js</a>

