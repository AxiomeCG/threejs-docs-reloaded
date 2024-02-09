# [name]

This is the base class for most objects in three.js and provides a set of
properties and methods for manipulating objects in 3D space.  
  
Note that this can be used for grouping objects via the [page:.add]( object )
method which adds the object as a child, however it is better to use
[page:Group] for this.

## Constructor

### [name]()

The constructor takes no arguments.

## Properties

### <br/> AnimationClip animations; <br/>

Array with object's animation clips.

### <br/> Boolean castShadow; <br/>

Whether the object gets rendered into shadow map. Default is `false`.

### <br/> Array children; <br/>

Array with object's children. See [page:Group] for info on manually grouping
objects.

### <br/> Material customDepthMaterial; <br/>

Custom depth material to be used when rendering to the depth map. Can only be
used in context of meshes. When shadow-casting with a [page:DirectionalLight]
or [page:SpotLight], if you are modifying vertex positions in the vertex
shader you must specify a customDepthMaterial for proper shadows. Default is
`undefined`.

### <br/> Material customDistanceMaterial; <br/>

Same as [page:.customDepthMaterial customDepthMaterial], but used with
[page:PointLight]. Default is `undefined`.

### <br/> Boolean frustumCulled; <br/>

When this is set, it checks every frame if the object is in the frustum of the
camera before rendering the object. If set to `false` the object gets rendered
every frame even if it is not in the frustum of the camera. Default is `true`.

### <br/> Integer id; <br/>

readonly – Unique number for this object instance.

### <br/> Boolean isObject3D; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Layers layers; <br/>

The layer membership of the object. The object is only visible if it has at
least one layer in common with the [page:Camera] in use. This property can
also be used to filter out unwanted objects in ray-intersection tests when
using [page:Raycaster].

### <br/> Matrix4 matrix; <br/>

The local transform matrix.

### <br/> Boolean matrixAutoUpdate; <br/>

When this is set, it calculates the matrix of position, (rotation or
quaternion) and scale every frame and also recalculates the matrixWorld
property. Default is [page:Object3D.DEFAULT_MATRIX_AUTO_UPDATE] (true).

### <br/> Matrix4 matrixWorld; <br/>

The global transform of the object. If the Object3D has no parent, then it's
identical to the local transform [page:.matrix].

### <br/> Boolean matrixWorldAutoUpdate; <br/>

If set, then the renderer checks every frame if the object and its children
need matrix updates. When it isn't, then you have to maintain all matrices in
the object and its children yourself. Default is
[page:Object3D.DEFAULT_MATRIX_WORLD_AUTO_UPDATE] (true).

### <br/> Boolean matrixWorldNeedsUpdate; <br/>

When this is set, it calculates the matrixWorld in that frame and resets this
property to false. Default is `false`.

### <br/> Matrix4 modelViewMatrix; <br/>

This is passed to the shader and used to calculate the position of the object.

### <br/> String name; <br/>

Optional name of the object (doesn't need to be unique). Default is an empty
string.

### <br/> Matrix3 normalMatrix; <br/>

This is passed to the shader and used to calculate lighting for the object. It
is the transpose of the inverse of the upper left 3x3 sub-matrix of this
object's modelViewMatrix.  
  
The reason for this special matrix is that simply using the modelViewMatrix
could result in a non-unit length of normals (on scaling) or in a non-
perpendicular direction (on non-uniform scaling).  
  
On the other hand the translation part of the modelViewMatrix is not relevant
for the calculation of normals. Thus a Matrix3 is sufficient.

### <br/> Function onAfterRender; <br/>

An optional callback that is executed immediately after a 3D object is
rendered. This function is called with the following parameters: renderer,
scene, camera, geometry, material, group.

Please notice that this callback is only executed for `renderable` 3D objects.
Meaning 3D objects which define their visual appearance with geometries and
materials like instances of [page:Mesh], [page:Line], [page:Points] or
[page:Sprite]. Instances of [page:Object3D], [page:Group] or [page:Bone] are
not renderable and thus this callback is not executed for such objects.

### <br/> Function onBeforeRender; <br/>

An optional callback that is executed immediately before a 3D object is
rendered. This function is called with the following parameters: renderer,
scene, camera, geometry, material, group.

Please notice that this callback is only executed for `renderable` 3D objects.
Meaning 3D objects which define their visual appearance with geometries and
materials like instances of [page:Mesh], [page:Line], [page:Points] or
[page:Sprite]. Instances of [page:Object3D], [page:Group] or [page:Bone] are
not renderable and thus this callback is not executed for such objects.

### <br/> Object3D parent; <br/>

Object's parent in the [link:https://en.wikipedia.org/wiki/Scene_graph scene
graph]. An object can have at most one parent.

### <br/> Vector3 position; <br/>

A [page:Vector3] representing the object's local position. Default is `(0, 0,
0)`.

### <br/> Quaternion quaternion; <br/>

Object's local rotation as a [page:Quaternion Quaternion].

### <br/> Boolean receiveShadow; <br/>

Whether the material receives shadows. Default is `false`.

### <br/> Number renderOrder; <br/>

This value allows the default rendering order of
[link:https://en.wikipedia.org/wiki/Scene_graph scene graph] objects to be
overridden although opaque and transparent objects remain sorted
independently. When this property is set for an instance of [page:Group
Group], all descendants objects will be sorted and rendered together. Sorting
is from lowest to highest renderOrder. Default value is `0`.

### <br/> Euler rotation; <br/>

Object's local rotation (see [link:https://en.wikipedia.org/wiki/Euler_angles
Euler angles]), in radians.

### <br/> Vector3 scale; <br/>

The object's local scale. Default is [page:Vector3]( 1, 1, 1 ).

### <br/> Vector3 up; <br/>

This is used by the [page:.lookAt lookAt] method, for example, to determine
the orientation of the result.  
Default is [page:Object3D.DEFAULT_UP] - that is, `( 0, 1, 0 )`.

### <br/> Object userData; <br/>

An object that can be used to store custom data about the Object3D. It should
not hold references to functions as these will not be cloned.

### <br/> String uuid; <br/>

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
object instance. This gets automatically assigned, so this shouldn't be
edited.

### <br/> Boolean visible; <br/>

Object gets rendered if `true`. Default is `true`.

## Static Properties

Static properties and methods are defined per class rather than per instance
of that class. This means that changing [page:Object3D.DEFAULT_UP] or
[page:Object3D.DEFAULT_MATRIX_AUTO_UPDATE] will change the values of [page:.up
up] and [page:.matrixAutoUpdate matrixAutoUpdate] for `every` instance of
Object3D (or derived classes) created after the change has been made (already
created Object3Ds will not be affected).

### <br/> Vector3 DEFAULT_UP; <br/>

The default [page:.up up] direction for objects, also used as the default
position for [page:DirectionalLight], [page:HemisphereLight] and
[page:Spotlight] (which creates lights shining from the top down).  
Set to ( 0, 1, 0 ) by default.

### <br/> Boolean DEFAULT_MATRIX_AUTO_UPDATE; <br/>

The default setting for [page:.matrixAutoUpdate matrixAutoUpdate] for newly
created Object3Ds.  

### <br/> Boolean DEFAULT_MATRIX_WORLD_AUTO_UPDATE; <br/>

The default setting for [page:.matrixWorldAutoUpdate matrixWorldAutoUpdate]
for newly created Object3Ds.  

## Methods

[page:EventDispatcher EventDispatcher] methods are available on this class.

### <br/> function add( object: Object3D ): add; <br/>

Adds `object` as child of this object. An arbitrary number of objects may be
added. Any current parent on an object passed in here will be removed, since
an object can have at most one parent.  
  
See [page:Group] for info on manually grouping objects.

### [method:undefined applyMatrix4]( [param:Matrix4 matrix] )

Applies the matrix transform to the object and updates the object's position,
rotation and scale.

### <br/> function applyQuaternion( quaternion: Quaternion ): applyQuaternion;
<br/>

Applies the rotation represented by the quaternion to the object.

### <br/> function attach( object: Object3D ): attach; <br/>

Adds `object` as a child of this, while maintaining the object's world
transform.  
  
Note: This method does not support scene graphs having non-uniformly-scaled
nodes(s).

### [method:Object3D clone]( [param:Boolean recursive] )

recursive -- if true, descendants of the object are also cloned. Default is
true.  
  
Returns a clone of this object and optionally all descendants.

### <br/> function copy( object: Object3D, recursive: Boolean? ): copy; <br/>

recursive -- if true, descendants of the object are also copied. Default is
true.  
  
Copy the given object into this object. Note: event listeners and user-defined
callbacks ([page:.onAfterRender] and [page:.onBeforeRender]) are not copied.

### [method:Object3D getObjectById]( [param:Integer id] )

id -- Unique number of the object instance  
  
Searches through an object and its children, starting with the object itself,
and returns the first with a matching id.  
Note that ids are assigned in chronological order: 1, 2, 3, ..., incrementing
by one for each new object.

### [method:Object3D getObjectByName]( [param:String name] )

name -- String to match to the children's Object3D.name property.  
  
Searches through an object and its children, starting with the object itself,
and returns the first with a matching name.  
Note that for most objects the name is an empty string by default. You will
have to set it manually to make use of this method.

### [method:Object3D getObjectByProperty]( [param:String name], [param:Any
value] )

name -- the property name to search for.  
value -- value of the given property.  
  
Searches through an object and its children, starting with the object itself,
and returns the first with a property that matches the value given.

### [method:Object3D getObjectsByProperty]( [param:String name], [param:Any
value] )

name -- the property name to search for.  
value -- value of the given property.  
  
Searches through an object and its children, starting with the object itself,
and returns all the objects with a property that matches the value given.

### [method:Vector3 getWorldPosition]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a vector representing the position of the object in world space.

### [method:Quaternion getWorldQuaternion]( [param:Quaternion target] )

[page:Quaternion target] — the result will be copied into this Quaternion.  
  
Returns a quaternion representing the rotation of the object in world space.

### [method:Vector3 getWorldScale]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a vector of the scaling factors applied to the object for each axis in
world space.

### [method:Vector3 getWorldDirection]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a vector representing the direction of object's positive z-axis in
world space.

### [method:Vector3 localToWorld]( [param:Vector3 vector] )

vector - A vector representing a position in this object's local space.  
  
Converts the vector from this object's local space to world space.

### [method:undefined lookAt]( [param:Vector3 vector] )  
[method:undefined lookAt]( [param:Float x], [param:Float y], [param:Float z] )

vector - A vector representing a position in world space.  
  
Optionally, the [page:.x x], [page:.y y] and [page:.z z] components of the
world space position.  
  
Rotates the object to face a point in world space.  
  
This method does not support objects having non-uniformly-scaled parent(s).

### [method:undefined raycast]( [param:Raycaster raycaster], [param:Array
intersects] )

Abstract (empty) method to get intersections between a casted ray and this
object. Subclasses such as [page:Mesh], [page:Line], and [page:Points]
implement this method in order to use raycasting.

### <br/> function remove( object: Object3D ): remove; <br/>

Removes `object` as child of this object. An arbitrary number of objects may
be removed.

### <br/> function removeFromParent( ): removeFromParent; <br/>

Removes this object from its current parent.

### <br/> function clear( ): clear; <br/>

Removes all child objects.

### <br/> function rotateOnAxis( axis: Vector3, angle: Float ): rotateOnAxis;
<br/>

axis -- A normalized vector in object space.  
angle -- The angle in radians.  
  
Rotate an object along an axis in object space. The axis is assumed to be
normalized.

### <br/> function rotateOnWorldAxis( axis: Vector3, angle: Float ):
rotateOnWorldAxis; <br/>

axis -- A normalized vector in world space.  
angle -- The angle in radians.  
  
Rotate an object along an axis in world space. The axis is assumed to be
normalized. Method Assumes no rotated parent.

### <br/> function rotateX( rad: Float ): rotateX; <br/>

rad - the angle to rotate in radians.  
  
Rotates the object around x axis in local space.

### <br/> function rotateY( rad: Float ): rotateY; <br/>

rad - the angle to rotate in radians.  
  
Rotates the object around y axis in local space.

### <br/> function rotateZ( rad: Float ): rotateZ; <br/>

rad - the angle to rotate in radians.  
  
Rotates the object around z axis in local space.

### [method:undefined setRotationFromAxisAngle]( [param:Vector3 axis],
[param:Float angle] )

axis -- A normalized vector in object space.  
angle -- angle in radians  
  
Calls [page:Quaternion.setFromAxisAngle setFromAxisAngle]( [page:Float axis],
[page:Float angle] ) on the [page:.quaternion].

### [method:undefined setRotationFromEuler]( [param:Euler euler] )

euler -- Euler angle specifying rotation amount.  
Calls [page:Quaternion.setRotationFromEuler setRotationFromEuler]( [page:Euler
euler]) on the [page:.quaternion].

### [method:undefined setRotationFromMatrix]( [param:Matrix4 m] )

m -- rotate the quaternion by the rotation component of the matrix.  
Calls [page:Quaternion.setFromRotationMatrix setFromRotationMatrix](
[page:Matrix4 m]) on the [page:.quaternion].  
  
Note that this assumes that the upper 3x3 of m is a pure rotation matrix (i.e,
unscaled).

### [method:undefined setRotationFromQuaternion]( [param:Quaternion q] )

q -- normalized Quaternion.  
  
Copy the given quaternion into [page:.quaternion].

### [method:Object toJSON]( [param:Object meta] )

meta -- object containing metadata such as materials, textures or images for
the object.  
Convert the object to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

### <br/> function translateOnAxis( axis: Vector3, distance: Float ):
translateOnAxis; <br/>

axis -- A normalized vector in object space.  
distance -- The distance to translate.  
  
Translate an object by distance along an axis in object space. The axis is
assumed to be normalized.

### <br/> function translateX( distance: Float ): translateX; <br/>

Translates object along x axis in object space by `distance` units.

### <br/> function translateY( distance: Float ): translateY; <br/>

Translates object along y axis in object space by `distance` units.

### <br/> function translateZ( distance: Float ): translateZ; <br/>

Translates object along z axis in object space by `distance` units.

### [method:undefined traverse]( [param:Function callback] )

callback - A function with as first argument an object3D object.  
  
Executes the callback on this object and all descendants.  
Note: Modifying the scene graph inside the callback is discouraged.

### [method:undefined traverseVisible]( [param:Function callback] )

callback - A function with as first argument an object3D object.  
  
Like traverse, but the callback will only be executed for visible objects.
Descendants of invisible objects are not traversed.  
Note: Modifying the scene graph inside the callback is discouraged.

### [method:undefined traverseAncestors]( [param:Function callback] )

callback - A function with as first argument an object3D object.  
  
Executes the callback on all ancestors.  
Note: Modifying the scene graph inside the callback is discouraged.

### [method:undefined updateMatrix]()

Updates the local transform.

### [method:undefined updateMatrixWorld]( [param:Boolean force] )

force - A boolean that can be used to bypass [page:.matrixWorldAutoUpdate], to
recalculate the world matrix of the object and descendants on the current
frame. Useful if you cannot wait for the renderer to update it on the next
frame (assuming [page:.matrixWorldAutoUpdate] set to `true`).  
  
Updates the global transform of the object and its descendants if the world
matrix needs update ([page:.matrixWorldNeedsUpdate] set to true) or if the
`force` parameter is set to `true`.

### [method:undefined updateWorldMatrix]( [param:Boolean updateParents],
[param:Boolean updateChildren] )

updateParents - recursively updates global transform of ancestors.  
updateChildren - recursively updates global transform of descendants.  
  
Updates the global transform of the object.

### [method:Vector3 worldToLocal]( [param:Vector3 vector] )

vector - A vector representing a position in world space.  
  
Converts the vector from world space to this object's local space.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

