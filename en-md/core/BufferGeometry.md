# BufferGeometry

A representation of mesh, line, or point geometry. Includes vertex positions,
face indices, normals, colors, UVs, and custom attributes within buffers,
reducing the cost of passing all this data to the GPU.

To read and edit data in BufferGeometry attributes, see [page:BufferAttribute]
documentation.

## Code Example

  
```ts  
const geometry = new THREE.BufferGeometry(); // create a simple square shape.
We duplicate the top left and bottom right // vertices because each vertex
needs to appear once per triangle. const vertices = new Float32Array( [ -1.0,
-1.0, 1.0, // v0 1.0, -1.0, 1.0, // v1 1.0, 1.0, 1.0, // v2 1.0, 1.0, 1.0, //
v3 -1.0, 1.0, 1.0, // v4 -1.0, -1.0, 1.0 // v5 ] ); // itemSize = 3 because
there are 3 values (components) per vertex geometry.setAttribute( 'position',
new THREE.BufferAttribute( vertices, 3 ) ); const material = new
THREE.MeshBasicMaterial( { color: 0xff0000 } ); const mesh = new THREE.Mesh(
geometry, material );  
```  

## Code Example (Index)

  
```ts  
const geometry = new THREE.BufferGeometry(); const vertices = new
Float32Array( [ -1.0, -1.0, 1.0, // v0 1.0, -1.0, 1.0, // v1 1.0, 1.0, 1.0, //
v2 -1.0, 1.0, 1.0, // v3 ] ); const indices = [ 0, 1, 2, 2, 3, 0, ];
geometry.setIndex( indices ); geometry.setAttribute( 'position', new
THREE.BufferAttribute( vertices, 3 ) ); const material = new
THREE.MeshBasicMaterial( { color: 0xff0000 } ); const mesh = new THREE.Mesh(
geometry, material );  
```  

## Examples

[example:webgl_buffergeometry Mesh with non-indexed faces]  
[example:webgl_buffergeometry_indexed Mesh with indexed faces]  
[example:webgl_buffergeometry_lines Lines]  
[example:webgl_buffergeometry_lines_indexed Indexed Lines]  
[example:webgl_buffergeometry_custom_attributes_particles Particles]  
[example:webgl_buffergeometry_rawshader Raw Shaders]

## Constructor

###  function BufferGeometry( ): void;

This creates a new BufferGeometry. It also sets several properties to a
default value.

## Properties

###  Object attributes;

This hashmap has as id the name of the attribute to be set and as value the
[page:BufferAttribute buffer] to set it to. Rather than accessing this
property directly, use [page:.setAttribute] and [page:.getAttribute] to access
attributes of this geometry.

###  Box3 boundingBox;

Bounding box for the bufferGeometry, which can be calculated with
[page:.computeBoundingBox](). Default is `null`.

###  Sphere boundingSphere;

Bounding sphere for the bufferGeometry, which can be calculated with
[page:.computeBoundingSphere](). Default is `null`.

###  Object drawRange;

Determines the part of the geometry to render. This should not be set
directly, instead use [page:.setDrawRange]. Default is  
```ts  
{ start: 0, count: Infinity }  
```  
For non-indexed BufferGeometry, count is the number of vertices to render. For
indexed BufferGeometry, count is the number of indices to render.

###  Array groups;

Split the geometry into groups, each of which will be rendered in a separate
WebGL draw call. This allows an array of materials to be used with the
geometry.  
  
Each group is an object of the form:  
```ts  
{ start: Integer, count: Integer, materialIndex: Integer }  
```  
where start specifies the first element in this draw call – the first vertex
for non-indexed geometry, otherwise the first triangle index. Count specifies
how many vertices (or indices) are included, and materialIndex specifies the
material array index to use.  
  
Use [page:.addGroup] to add groups, rather than modifying this array directly.  
  
Every vertex and index must belong to exactly one group — groups must not
share vertices or indices, and must not leave vertices or indices unused.

Note: groups used to be called drawCalls <h3> Array drawcalls; </h3> <p> For
geometries that use indexed triangles, this Array can be used to split the
object into multiple WebGL draw calls. Each draw call will draw some subset of
the vertices in this geometry using the configured [page:Material shader].
This may be necessary if, for instance, you have more than 65535 vertices in
your object. </p>

###  Integer id;

Unique number for this bufferGeometry instance.

###  BufferAttribute index;

Allows for vertices to be re-used across multiple triangles; this is called
using "indexed triangles". Each triangle is associated with the indices of
three vertices. This attribute therefore stores the index of each vertex for
each triangular face. If this attribute is not set, the [page:WebGLRenderer
renderer] assumes that each three contiguous positions represent a single
triangle. Default is `null`.

###  Boolean isBufferGeometry;

Read-only flag to check if a given object is of type BufferGeometry.

###  Object morphAttributes;

Hashmap of [page:BufferAttribute]s holding details of the geometry's morph
targets.  
Note: Once the geometry has been rendered, the morph attribute data cannot be
changed. You will have to call [page:.dispose](), and create a new instance of
BufferGeometry.

###  Boolean morphTargetsRelative;

Used to control the morph target behavior; when set to true, the morph target
data is treated as relative offsets, rather than as absolute
positions/normals. Default is `false`.

###  String name;

Optional name for this bufferGeometry instance. Default is an empty string.

###  Object userData;

An object that can be used to store custom data about the BufferGeometry. It
should not hold references to functions as these will not be cloned.

###  String uuid;

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
object instance. This gets automatically assigned and shouldn't be edited.

## Methods

[page:EventDispatcher EventDispatcher] methods are available on this class.

###  function addGroup( start: Integer, count: Integer, materialIndex: Integer
): undefined;

Adds a group to this geometry; see the [page:BufferGeometry.groups groups]
property for details.

###  function applyMatrix4( matrix: Matrix4 ): this;

Applies the matrix transform to the geometry.

###  function applyQuaternion( quaternion: Quaternion ): this;

Applies the rotation represented by the quaternion to the geometry.

###  function center( ): this;

Center the geometry based on the bounding box.

###  function clearGroups( ): undefined;

Clears all groups.

###  function clone( ): BufferGeometry;

Creates a clone of this BufferGeometry.

###  function computeBoundingBox( ): undefined;

Computes bounding box of the geometry, updating [page:.boundingBox] attribute.  
Bounding boxes aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

###  function computeBoundingSphere( ): undefined;

Computes bounding sphere of the geometry, updating [page:.boundingSphere]
attribute.  
Bounding spheres aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

###  function computeTangents( ): undefined;

Calculates and adds a tangent attribute to this geometry.  
The computation is only supported for indexed geometries and if position,
normal, and uv attributes are defined. When using a tangent space normal map,
prefer the MikkTSpace algorithm provided by
[page:BufferGeometryUtils.computeMikkTSpaceTangents] instead.

###  function computeVertexNormals( ): undefined;

Computes vertex normals for the given vertex data. For indexed geometries, the
method sets each vertex normal to be the average of the face normals of the
faces that share that vertex. For non-indexed geometries, vertices are not
shared, and the method sets each vertex normal to be the same as the face
normal.

###  function copy( bufferGeometry: BufferGeometry ): this;

Copies another BufferGeometry to this BufferGeometry.

###  function deleteAttribute( name: String ): BufferAttribute;

Deletes the [page:BufferAttribute attribute] with the specified name.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function getAttribute( name: String ): BufferAttribute;

Returns the [page:BufferAttribute attribute] with the specified name.

###  function getIndex( ): BufferAttribute;

Return the [page:.index] buffer.

###  function hasAttribute( name: String ): Boolean;

Returns `true` if the attribute with the specified name exists.

###  function lookAt( vector: Vector3 ): this;

vector - A world vector to look at.  
  
Rotates the geometry to face a point in space. This is typically done as a one
time operation, and not during a loop. Use [page:Object3D.lookAt] for typical
real-time mesh usage.

###  function normalizeNormals( ): undefined;

Every normal vector in a geometry will have a magnitude of `1`. This will
correct lighting on the geometry surfaces.

###  function rotateX( radians: Float ): this;

Rotate the geometry about the X axis. This is typically done as a one time
operation, and not during a loop. Use [page:Object3D.rotation] for typical
real-time mesh rotation.

###  function rotateY( radians: Float ): this;

Rotate the geometry about the Y axis. This is typically done as a one time
operation, and not during a loop. Use [page:Object3D.rotation] for typical
real-time mesh rotation.

###  function rotateZ( radians: Float ): this;

Rotate the geometry about the Z axis. This is typically done as a one time
operation, and not during a loop. Use [page:Object3D.rotation] for typical
real-time mesh rotation.

###  function scale( x: Float, y: Float, z: Float ): this;

Scale the geometry data. This is typically done as a one time operation, and
not during a loop. Use [page:Object3D.scale] for typical real-time mesh
scaling.

###  function setAttribute( name: String, attribute: BufferAttribute ): this;

Sets an attribute to this geometry. Use this rather than the attributes
property, because an internal hashmap of [page:.attributes] is maintained to
speed up iterating over attributes.

###  function setDrawRange( start: Integer, count: Integer ): undefined;

Set the [page:.drawRange] property. For non-indexed BufferGeometry, count is
the number of vertices to render. For indexed BufferGeometry, count is the
number of indices to render.

###  function setFromPoints( points: Array ): this;

Sets the attributes for this BufferGeometry from an array of points.

###  function setIndex( index: BufferAttribute ): this;

Set the [page:.index] buffer.

###  function toJSON( ): Object;

Convert the buffer geometry to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

###  function toNonIndexed( ): BufferGeometry;

Return a non-index version of an indexed BufferGeometry.

###  function translate( x: Float, y: Float, z: Float ): this;

Translate the geometry. This is typically done as a one time operation, and
not during a loop. Use [page:Object3D.position] for typical real-time mesh
translation.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

