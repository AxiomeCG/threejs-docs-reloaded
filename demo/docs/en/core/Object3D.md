# Object3D

This is the base class for most objects in three.js and provides a set of
properties and methods for manipulating objects in 3D space.  
  
Note that this can be used for grouping objects via the [.add](#)( object )
method which adds the object as a child, however it is better to use
[Group](en\objects\Group.html) for this.

## Constructor

### Object3D

  
  
```ts  
function Object3D( ): void;  
```  

The constructor takes no arguments.

## Properties

### animations

  
  
```ts  
animations: AnimationClip;  
```  

Array with object's animation clips.

### castShadow

  
  
```ts  
castShadow: Boolean;  
```  

Whether the object gets rendered into shadow map. Default is `false`.

### children

  
  
```ts  
children: Array;  
```  

Array with object's children. See [Group](en\objects\Group.html) for info on
manually grouping objects.

### customDepthMaterial

  
  
```ts  
customDepthMaterial: Material;  
```  

Custom depth material to be used when rendering to the depth map. Can only be
used in context of meshes. When shadow-casting with a
[DirectionalLight](en\lights\DirectionalLight.html) or
[SpotLight](en\lights\SpotLight.html), if you are modifying vertex positions
in the vertex shader you must specify a customDepthMaterial for proper
shadows. Default is `undefined`.

### customDistanceMaterial

  
  
```ts  
customDistanceMaterial: Material;  
```  

Same as [.customDepthMaterial](#customDepthMaterial), but used with
[PointLight](en\lights\PointLight.html). Default is `undefined`.

### frustumCulled

  
  
```ts  
frustumCulled: Boolean;  
```  

When this is set, it checks every frame if the object is in the frustum of the
camera before rendering the object. If set to `false` the object gets rendered
every frame even if it is not in the frustum of the camera. Default is `true`.

### id

  
  
```ts  
id: Integer;  
```  

readonly – Unique number for this object instance.

### isObject3D

  
  
```ts  
isObject3D: Boolean;  
```  

Read-only flag to check if a given object is of type Object3D.

### layers

  
  
```ts  
layers: Layers;  
```  

The layer membership of the object. The object is only visible if it has at
least one layer in common with the [Camera](en\cameras\Camera.html) in use.
This property can also be used to filter out unwanted objects in ray-
intersection tests when using [Raycaster](en\core\Raycaster.html).

### matrix

  
  
```ts  
matrix: Matrix4;  
```  

The local transform matrix.

### matrixAutoUpdate

  
  
```ts  
matrixAutoUpdate: Boolean;  
```  

When this is set, it calculates the matrix of position, (rotation or
quaternion) and scale every frame and also recalculates the matrixWorld
property. Default is [Object3D.DEFAULT_MATRIX_AUTO_UPDATE](#) (true).

### matrixWorld

  
  
```ts  
matrixWorld: Matrix4;  
```  

The global transform of the object. If the Object3D has no parent, then it's
identical to the local transform [.matrix](#).

### matrixWorldAutoUpdate

  
  
```ts  
matrixWorldAutoUpdate: Boolean;  
```  

If set, then the renderer checks every frame if the object and its children
need matrix updates. When it isn't, then you have to maintain all matrices in
the object and its children yourself. Default is
[Object3D.DEFAULT_MATRIX_WORLD_AUTO_UPDATE](#) (true).

### matrixWorldNeedsUpdate

  
  
```ts  
matrixWorldNeedsUpdate: Boolean;  
```  

When this is set, it calculates the matrixWorld in that frame and resets this
property to false. Default is `false`.

### modelViewMatrix

  
  
```ts  
modelViewMatrix: Matrix4;  
```  

This is passed to the shader and used to calculate the position of the object.

### name

  
  
```ts  
name: String;  
```  

Optional name of the object (doesn't need to be unique). Default is an empty
string.

### normalMatrix

  
  
```ts  
normalMatrix: Matrix3;  
```  

This is passed to the shader and used to calculate lighting for the object. It
is the transpose of the inverse of the upper left 3x3 sub-matrix of this
object's modelViewMatrix.  
  
The reason for this special matrix is that simply using the modelViewMatrix
could result in a non-unit length of normals (on scaling) or in a non-
perpendicular direction (on non-uniform scaling).  
  
On the other hand the translation part of the modelViewMatrix is not relevant
for the calculation of normals. Thus a Matrix3 is sufficient.

### onAfterRender

  
  
```ts  
onAfterRender: Function;  
```  

An optional callback that is executed immediately after a 3D object is
rendered. This function is called with the following parameters: renderer,
scene, camera, geometry, material, group.

Please notice that this callback is only executed for `renderable` 3D objects.
Meaning 3D objects which define their visual appearance with geometries and
materials like instances of [Mesh](en\objects\Mesh.html),
[Line](en\objects\Line.html), [Points](en\objects\Points.html) or
[Sprite](en\objects\Sprite.html). Instances of
[Object3D](en\core\Object3D.html), [Group](en\objects\Group.html) or
[Bone](en\objects\Bone.html) are not renderable and thus this callback is not
executed for such objects.

### onBeforeRender

  
  
```ts  
onBeforeRender: Function;  
```  

An optional callback that is executed immediately before a 3D object is
rendered. This function is called with the following parameters: renderer,
scene, camera, geometry, material, group.

Please notice that this callback is only executed for `renderable` 3D objects.
Meaning 3D objects which define their visual appearance with geometries and
materials like instances of [Mesh](en\objects\Mesh.html),
[Line](en\objects\Line.html), [Points](en\objects\Points.html) or
[Sprite](en\objects\Sprite.html). Instances of
[Object3D](en\core\Object3D.html), [Group](en\objects\Group.html) or
[Bone](en\objects\Bone.html) are not renderable and thus this callback is not
executed for such objects.

### parent

  
  
```ts  
parent: Object3D;  
```  

Object's parent in the <a
href="https://en.wikipedia.org/wiki/Scene_graph">scene graph</a>. An object
can have at most one parent.

### position

  
  
```ts  
position: Vector3;  
```  

A [Vector3](en\math\Vector3.html) representing the object's local position.
Default is `(0, 0, 0)`.

### quaternion

  
  
```ts  
quaternion: Quaternion;  
```  

Object's local rotation as a [Quaternion](en\math\Quaternion.html).

### receiveShadow

  
  
```ts  
receiveShadow: Boolean;  
```  

Whether the material receives shadows. Default is `false`.

### renderOrder

  
  
```ts  
renderOrder: Number;  
```  

This value allows the default rendering order of <a
href="https://en.wikipedia.org/wiki/Scene_graph">scene graph</a> objects to be
overridden although opaque and transparent objects remain sorted
independently. When this property is set for an instance of
[Group](en\objects\Group.html), all descendants objects will be sorted and
rendered together. Sorting is from lowest to highest renderOrder. Default
value is `0`.

### rotation

  
  
```ts  
rotation: Euler;  
```  

Object's local rotation (see <a
href="https://en.wikipedia.org/wiki/Euler_angles">Euler angles</a>), in
radians.

### scale

  
  
```ts  
scale: Vector3;  
```  

The object's local scale. Default is [Vector3](en\math\Vector3.html)( 1, 1, 1
).

### up

  
  
```ts  
up: Vector3;  
```  

This is used by the [.lookAt](#lookAt) method, for example, to determine the
orientation of the result.  
Default is [Object3D.DEFAULT_UP](#) - that is, `( 0, 1, 0 )`.

### userData

  
  
```ts  
userData: Object;  
```  

An object that can be used to store custom data about the Object3D. It should
not hold references to functions as these will not be cloned.

### uuid

  
  
```ts  
uuid: String;  
```  

<a href="http://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a>
of this object instance. This gets automatically assigned, so this shouldn't
be edited.

### visible

  
  
```ts  
visible: Boolean;  
```  

Object gets rendered if `true`. Default is `true`.

## Static Properties

Static properties and methods are defined per class rather than per instance
of that class. This means that changing [Object3D.DEFAULT_UP](#) or
[Object3D.DEFAULT_MATRIX_AUTO_UPDATE](#) will change the values of [.up](#up)
and [.matrixAutoUpdate](#matrixAutoUpdate) for `every` instance of Object3D
(or derived classes) created after the change has been made (already created
Object3Ds will not be affected).

### DEFAULT_UP

  
  
```ts  
DEFAULT_UP: Vector3;  
```  

The default [.up](#up) direction for objects, also used as the default
position for [DirectionalLight](en\lights\DirectionalLight.html),
[HemisphereLight](en\lights\HemisphereLight.html) and [Spotlight](#) (which
creates lights shining from the top down).  
Set to ( 0, 1, 0 ) by default.

### DEFAULT_MATRIX_AUTO_UPDATE

  
  
```ts  
DEFAULT_MATRIX_AUTO_UPDATE: Boolean;  
```  

The default setting for [.matrixAutoUpdate](#matrixAutoUpdate) for newly
created Object3Ds.  

### DEFAULT_MATRIX_WORLD_AUTO_UPDATE

  
  
```ts  
DEFAULT_MATRIX_WORLD_AUTO_UPDATE: Boolean;  
```  

The default setting for [.matrixWorldAutoUpdate](#matrixWorldAutoUpdate) for
newly created Object3Ds.  

## Methods

[EventDispatcher](en\core\EventDispatcher.html) methods are available on this
class.

### add

  
  
```ts  
function add( object: Object3D ): this;  
```  

Adds `object` as child of this object. An arbitrary number of objects may be
added. Any current parent on an object passed in here will be removed, since
an object can have at most one parent.  
  
See [Group](en\objects\Group.html) for info on manually grouping objects.

### applyMatrix4

  
  
```ts  
function applyMatrix4( matrix: Matrix4 ): undefined;  
```  

Applies the matrix transform to the object and updates the object's position,
rotation and scale.

### applyQuaternion

  
  
```ts  
function applyQuaternion( quaternion: Quaternion ): this;  
```  

Applies the rotation represented by the quaternion to the object.

### attach

  
  
```ts  
function attach( object: Object3D ): this;  
```  

Adds `object` as a child of this, while maintaining the object's world
transform.  
  
Note: This method does not support scene graphs having non-uniformly-scaled
nodes(s).

### clone

  
  
```ts  
function clone( recursive: Boolean ): Object3D;  
```  

recursive -- if true, descendants of the object are also cloned. Default is
true.  
  
Returns a clone of this object and optionally all descendants.

### copy

  
  
```ts  
function copy( object: Object3D, recursive: Boolean ): this;  
```  

recursive -- if true, descendants of the object are also copied. Default is
true.  
  
Copy the given object into this object. Note: event listeners and user-defined
callbacks ([.onAfterRender](#) and [.onBeforeRender](#)) are not copied.

### getObjectById

  
  
```ts  
function getObjectById( id: Integer ): Object3D;  
```  

id -- Unique number of the object instance  
  
Searches through an object and its children, starting with the object itself,
and returns the first with a matching id.  
Note that ids are assigned in chronological order: 1, 2, 3, ..., incrementing
by one for each new object.

### getObjectByName

  
  
```ts  
function getObjectByName( name: String ): Object3D;  
```  

name -- String to match to the children's Object3D.name property.  
  
Searches through an object and its children, starting with the object itself,
and returns the first with a matching name.  
Note that for most objects the name is an empty string by default. You will
have to set it manually to make use of this method.

### getObjectByProperty

  
  
```ts  
function getObjectByProperty( name: String, value: Any ): Object3D;  
```  

name -- the property name to search for.  
value -- value of the given property.  
  
Searches through an object and its children, starting with the object itself,
and returns the first with a property that matches the value given.

### getObjectsByProperty

  
  
```ts  
function getObjectsByProperty( name: String, value: Any ): Object3D;  
```  

name -- the property name to search for.  
value -- value of the given property.  
  
Searches through an object and its children, starting with the object itself,
and returns all the objects with a property that matches the value given.

### getWorldPosition

  
  
```ts  
function getWorldPosition( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns a vector representing the position of the object in world space.

### getWorldQuaternion

  
  
```ts  
function getWorldQuaternion( target: Quaternion ): Quaternion;  
```  

[target](en\math\Quaternion.html) — the result will be copied into this
Quaternion.  
  
Returns a quaternion representing the rotation of the object in world space.

### getWorldScale

  
  
```ts  
function getWorldScale( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns a vector of the scaling factors applied to the object for each axis in
world space.

### getWorldDirection

  
  
```ts  
function getWorldDirection( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns a vector representing the direction of object's positive z-axis in
world space.

### localToWorld

  
  
```ts  
function localToWorld( vector: Vector3 ): Vector3;  
```  

vector - A vector representing a position in this object's local space.  
  
Converts the vector from this object's local space to world space.

### lookAt

  
  
```ts  
function lookAt( vector: Vector3, x: Float, y: Float, z: Float ): undefined;  
```  

vector - A vector representing a position in world space.  
  
Optionally, the [.x](#x), [.y](#y) and [.z](#z) components of the world space
position.  
  
Rotates the object to face a point in world space.  
  
This method does not support objects having non-uniformly-scaled parent(s).

### raycast

  
  
```ts  
function raycast( raycaster: Raycaster, intersects: Array ): undefined;  
```  

Abstract (empty) method to get intersections between a casted ray and this
object. Subclasses such as [Mesh](en\objects\Mesh.html),
[Line](en\objects\Line.html), and [Points](en\objects\Points.html) implement
this method in order to use raycasting.

### remove

  
  
```ts  
function remove( object: Object3D ): this;  
```  

Removes `object` as child of this object. An arbitrary number of objects may
be removed.

### removeFromParent

  
  
```ts  
function removeFromParent( ): this;  
```  

Removes this object from its current parent.

### clear

  
  
```ts  
function clear( ): this;  
```  

Removes all child objects.

### rotateOnAxis

  
  
```ts  
function rotateOnAxis( axis: Vector3, angle: Float ): this;  
```  

axis -- A normalized vector in object space.  
angle -- The angle in radians.  
  
Rotate an object along an axis in object space. The axis is assumed to be
normalized.

### rotateOnWorldAxis

  
  
```ts  
function rotateOnWorldAxis( axis: Vector3, angle: Float ): this;  
```  

axis -- A normalized vector in world space.  
angle -- The angle in radians.  
  
Rotate an object along an axis in world space. The axis is assumed to be
normalized. Method Assumes no rotated parent.

### rotateX

  
  
```ts  
function rotateX( rad: Float ): this;  
```  

rad - the angle to rotate in radians.  
  
Rotates the object around x axis in local space.

### rotateY

  
  
```ts  
function rotateY( rad: Float ): this;  
```  

rad - the angle to rotate in radians.  
  
Rotates the object around y axis in local space.

### rotateZ

  
  
```ts  
function rotateZ( rad: Float ): this;  
```  

rad - the angle to rotate in radians.  
  
Rotates the object around z axis in local space.

### setRotationFromAxisAngle

  
  
```ts  
function setRotationFromAxisAngle( axis: Vector3, angle: Float ): undefined;  
```  

axis -- A normalized vector in object space.  
angle -- angle in radians  
  
Calls [setFromAxisAngle](#)( [.loat](#loat), [.loat](#loat) ) on the
[.quaternion](#).

### setRotationFromEuler

  
  
```ts  
function setRotationFromEuler( euler: Euler ): undefined;  
```  

euler -- Euler angle specifying rotation amount.  
Calls [setRotationFromEuler](#)( [.uler](#uler)) on the [.quaternion](#).

### setRotationFromMatrix

  
  
```ts  
function setRotationFromMatrix( m: Matrix4 ): undefined;  
```  

m -- rotate the quaternion by the rotation component of the matrix.  
Calls [setFromRotationMatrix](#)( [.atrix4](#atrix4)) on the [.quaternion](#).  
  
Note that this assumes that the upper 3x3 of m is a pure rotation matrix (i.e,
unscaled).

### setRotationFromQuaternion

  
  
```ts  
function setRotationFromQuaternion( q: Quaternion ): undefined;  
```  

q -- normalized Quaternion.  
  
Copy the given quaternion into [.quaternion](#).

### toJSON

  
  
```ts  
function toJSON( meta: Object ): Object;  
```  

meta -- object containing metadata such as materials, textures or images for
the object.  
Convert the object to three.js <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.

### translateOnAxis

  
  
```ts  
function translateOnAxis( axis: Vector3, distance: Float ): this;  
```  

axis -- A normalized vector in object space.  
distance -- The distance to translate.  
  
Translate an object by distance along an axis in object space. The axis is
assumed to be normalized.

### translateX

  
  
```ts  
function translateX( distance: Float ): this;  
```  

Translates object along x axis in object space by `distance` units.

### translateY

  
  
```ts  
function translateY( distance: Float ): this;  
```  

Translates object along y axis in object space by `distance` units.

### translateZ

  
  
```ts  
function translateZ( distance: Float ): this;  
```  

Translates object along z axis in object space by `distance` units.

### traverse

  
  
```ts  
function traverse( callback: Function ): undefined;  
```  

callback - A function with as first argument an object3D object.  
  
Executes the callback on this object and all descendants.  
Note: Modifying the scene graph inside the callback is discouraged.

### traverseVisible

  
  
```ts  
function traverseVisible( callback: Function ): undefined;  
```  

callback - A function with as first argument an object3D object.  
  
Like traverse, but the callback will only be executed for visible objects.
Descendants of invisible objects are not traversed.  
Note: Modifying the scene graph inside the callback is discouraged.

### traverseAncestors

  
  
```ts  
function traverseAncestors( callback: Function ): undefined;  
```  

callback - A function with as first argument an object3D object.  
  
Executes the callback on all ancestors.  
Note: Modifying the scene graph inside the callback is discouraged.

### updateMatrix

  
  
```ts  
function updateMatrix( ): undefined;  
```  

Updates the local transform.

### updateMatrixWorld

  
  
```ts  
function updateMatrixWorld( force: Boolean ): undefined;  
```  

force - A boolean that can be used to bypass [.matrixWorldAutoUpdate](#), to
recalculate the world matrix of the object and descendants on the current
frame. Useful if you cannot wait for the renderer to update it on the next
frame (assuming [.matrixWorldAutoUpdate](#) set to `true`).  
  
Updates the global transform of the object and its descendants if the world
matrix needs update ([.matrixWorldNeedsUpdate](#) set to true) or if the
`force` parameter is set to `true`.

### updateWorldMatrix

  
  
```ts  
function updateWorldMatrix( updateParents: Boolean, updateChildren: Boolean ):
undefined;  
```  

updateParents - recursively updates global transform of ancestors.  
updateChildren - recursively updates global transform of descendants.  
  
Updates the global transform of the object.

### worldToLocal

  
  
```ts  
function worldToLocal( vector: Vector3 ): Vector3;  
```  

vector - A vector representing a position in world space.  
  
Converts the vector from world space to this object's local space.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/Object3D.js">src/core/Object3D.js</a>

