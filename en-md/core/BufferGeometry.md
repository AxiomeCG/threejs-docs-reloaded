# [name]

A representation of mesh, line, or point geometry. Includes vertex positions,
face indices, normals, colors, UVs, and custom attributes within buffers,
reducing the cost of passing all this data to the GPU.

To read and edit data in BufferGeometry attributes, see [page:BufferAttribute]
documentation.

## Code Example

  
```ts  
const geometry = new THREE.BufferGeometry();  
  
// create a simple square shape. We duplicate the top left and bottom right  
// vertices because each vertex needs to appear once per triangle.  
const vertices = new Float32Array( [  
-1.0, -1.0, 1.0, // v0  
1.0, -1.0, 1.0, // v1  
1.0, 1.0, 1.0, // v2  
  
1.0, 1.0, 1.0, // v3  
-1.0, 1.0, 1.0, // v4  
-1.0, -1.0, 1.0 // v5  
] );  
  
// itemSize = 3 because there are 3 values (components) per vertex  
geometry.setAttribute( 'position', new THREE.BufferAttribute( vertices, 3 ) );  
const material = new THREE.MeshBasicMaterial( { color: 0xff0000 } );  
const mesh = new THREE.Mesh( geometry, material );  
```  

## Code Example (Index)

  
```ts  
const geometry = new THREE.BufferGeometry();  
  
const vertices = new Float32Array( [  
-1.0, -1.0, 1.0, // v0  
1.0, -1.0, 1.0, // v1  
1.0, 1.0, 1.0, // v2  
-1.0, 1.0, 1.0, // v3  
] );  
  
const indices = [  
0, 1, 2,  
2, 3, 0,  
];  
  
geometry.setIndex( indices );  
geometry.setAttribute( 'position', new THREE.BufferAttribute( vertices, 3 ) );  
  
const material = new THREE.MeshBasicMaterial( { color: 0xff0000 } );  
const mesh = new THREE.Mesh( geometry, material );  
```  

## Examples

[example:webgl_buffergeometry Mesh with non-indexed faces]  
[example:webgl_buffergeometry_indexed Mesh with indexed faces]  
[example:webgl_buffergeometry_lines Lines]  
[example:webgl_buffergeometry_lines_indexed Indexed Lines]  
[example:webgl_buffergeometry_custom_attributes_particles Particles]  
[example:webgl_buffergeometry_rawshader Raw Shaders]

## Constructor

### [name]()

This creates a new [name]. It also sets several properties to a default value.

## Properties

### <br/> Object attributes; <br/>

This hashmap has as id the name of the attribute to be set and as value the
[page:BufferAttribute buffer] to set it to. Rather than accessing this
property directly, use [page:.setAttribute] and [page:.getAttribute] to access
attributes of this geometry.

### <br/> Box3 boundingBox; <br/>

Bounding box for the bufferGeometry, which can be calculated with
[page:.computeBoundingBox](). Default is `null`.

### <br/> Sphere boundingSphere; <br/>

Bounding sphere for the bufferGeometry, which can be calculated with
[page:.computeBoundingSphere](). Default is `null`.

### <br/> Object drawRange; <br/>

Determines the part of the geometry to render. This should not be set
directly, instead use [page:.setDrawRange]. Default is  
```ts  
{ start: 0, count: Infinity }  
```  
For non-indexed BufferGeometry, count is the number of vertices to render. For
indexed BufferGeometry, count is the number of indices to render.

### <br/> Array groups; <br/>

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

Note: groups used to be called drawCalls <h3><br/> Array drawcalls; <br/></h3>
<p> For geometries that use indexed triangles, this Array can be used to split
the object into multiple WebGL draw calls. Each draw call will draw some
subset of the vertices in this geometry using the configured [page:Material
shader]. This may be necessary if, for instance, you have more than 65535
vertices in your object. </p>

### <br/> Integer id; <br/>

Unique number for this bufferGeometry instance.

### <br/> BufferAttribute index; <br/>

Allows for vertices to be re-used across multiple triangles; this is called
using "indexed triangles". Each triangle is associated with the indices of
three vertices. This attribute therefore stores the index of each vertex for
each triangular face. If this attribute is not set, the [page:WebGLRenderer
renderer] assumes that each three contiguous positions represent a single
triangle. Default is `null`.

### <br/> Boolean isBufferGeometry; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Object morphAttributes; <br/>

Hashmap of [page:BufferAttribute]s holding details of the geometry's morph
targets.  
Note: Once the geometry has been rendered, the morph attribute data cannot be
changed. You will have to call [page:.dispose](), and create a new instance of
[name].

### <br/> Boolean morphTargetsRelative; <br/>

Used to control the morph target behavior; when set to true, the morph target
data is treated as relative offsets, rather than as absolute
positions/normals. Default is `false`.

### <br/> String name; <br/>

Optional name for this bufferGeometry instance. Default is an empty string.

### <br/> Object userData; <br/>

An object that can be used to store custom data about the BufferGeometry. It
should not hold references to functions as these will not be cloned.

### <br/> String uuid; <br/>

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
object instance. This gets automatically assigned and shouldn't be edited.

## Methods

[page:EventDispatcher EventDispatcher] methods are available on this class.

### [method:undefined addGroup]( [param:Integer start], [param:Integer count],
[param:Integer materialIndex] )

Adds a group to this geometry; see the [page:BufferGeometry.groups groups]
property for details.

### <br/> function applyMatrix4( matrix: Matrix4 ): applyMatrix4; <br/>

Applies the matrix transform to the geometry.

### <br/> function applyQuaternion( quaternion: Quaternion ): applyQuaternion;
<br/>

Applies the rotation represented by the quaternion to the geometry.

### <br/> function center( ): center; <br/>

Center the geometry based on the bounding box.

### [method:undefined clearGroups]( )

Clears all groups.

### [method:BufferGeometry clone]()

Creates a clone of this BufferGeometry.

### [method:undefined computeBoundingBox]()

Computes bounding box of the geometry, updating [page:.boundingBox] attribute.  
Bounding boxes aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

### [method:undefined computeBoundingSphere]()

Computes bounding sphere of the geometry, updating [page:.boundingSphere]
attribute.  
Bounding spheres aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

### [method:undefined computeTangents]()

Calculates and adds a tangent attribute to this geometry.  
The computation is only supported for indexed geometries and if position,
normal, and uv attributes are defined. When using a tangent space normal map,
prefer the MikkTSpace algorithm provided by
[page:BufferGeometryUtils.computeMikkTSpaceTangents] instead.

### [method:undefined computeVertexNormals]()

Computes vertex normals for the given vertex data. For indexed geometries, the
method sets each vertex normal to be the average of the face normals of the
faces that share that vertex. For non-indexed geometries, vertices are not
shared, and the method sets each vertex normal to be the same as the face
normal.

### <br/> function copy( bufferGeometry: BufferGeometry ): copy; <br/>

Copies another BufferGeometry to this BufferGeometry.

### [method:BufferAttribute deleteAttribute]( [param:String name] )

Deletes the [page:BufferAttribute attribute] with the specified name.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### [method:BufferAttribute getAttribute]( [param:String name] )

Returns the [page:BufferAttribute attribute] with the specified name.

### [method:BufferAttribute getIndex] ()

Return the [page:.index] buffer.

### [method:Boolean hasAttribute]( [param:String name] )

Returns `true` if the attribute with the specified name exists.

### <br/> function lookAt( vector: Vector3 ): lookAt; <br/>

vector - A world vector to look at.  
  
Rotates the geometry to face a point in space. This is typically done as a one
time operation, and not during a loop. Use [page:Object3D.lookAt] for typical
real-time mesh usage.

### [method:undefined normalizeNormals]()

Every normal vector in a geometry will have a magnitude of `1`. This will
correct lighting on the geometry surfaces.

### <br/> function rotateX( radians: Float ): rotateX; <br/>

Rotate the geometry about the X axis. This is typically done as a one time
operation, and not during a loop. Use [page:Object3D.rotation] for typical
real-time mesh rotation.

### <br/> function rotateY( radians: Float ): rotateY; <br/>

Rotate the geometry about the Y axis. This is typically done as a one time
operation, and not during a loop. Use [page:Object3D.rotation] for typical
real-time mesh rotation.

### <br/> function rotateZ( radians: Float ): rotateZ; <br/>

Rotate the geometry about the Z axis. This is typically done as a one time
operation, and not during a loop. Use [page:Object3D.rotation] for typical
real-time mesh rotation.

### <br/> function scale( x: Float, y: Float, z: Float ): scale; <br/>

Scale the geometry data. This is typically done as a one time operation, and
not during a loop. Use [page:Object3D.scale] for typical real-time mesh
scaling.

### <br/> function setAttribute( name: String, attribute: BufferAttribute ):
setAttribute; <br/>

Sets an attribute to this geometry. Use this rather than the attributes
property, because an internal hashmap of [page:.attributes] is maintained to
speed up iterating over attributes.

### [method:undefined setDrawRange] ( [param:Integer start], [param:Integer
count] )

Set the [page:.drawRange] property. For non-indexed BufferGeometry, count is
the number of vertices to render. For indexed BufferGeometry, count is the
number of indices to render.

### <br/> function setFromPoints( points: Array ): setFromPoints; <br/>

Sets the attributes for this BufferGeometry from an array of points.

### <br/> function setIndex( index: BufferAttribute ): setIndex; <br/>

Set the [page:.index] buffer.

### [method:Object toJSON]()

Convert the buffer geometry to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

### [method:BufferGeometry toNonIndexed]()

Return a non-index version of an indexed BufferGeometry.

### <br/> function translate( x: Float, y: Float, z: Float ): translate; <br/>

Translate the geometry. This is typically done as a one time operation, and
not during a loop. Use [page:Object3D.position] for typical real-time mesh
translation.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

