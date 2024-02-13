[page:Mesh] →

# InstancedMesh

A special version of [page:Mesh] with instanced rendering support. Use
InstancedMesh if you have to render a large number of objects with the same
geometry and material but with different world transformations. The usage of
InstancedMesh will help you to reduce the number of draw calls and thus
improve the overall rendering performance in your application.

## Examples

[example:webgl_instancing_dynamic WebGL / instancing / dynamic]  
[example:webgl_instancing_performance WebGL / instancing / performance]  
[example:webgl_instancing_scatter WebGL / instancing / scatter]  
[example:webgl_instancing_raycast WebGL / instancing / raycast]

## Constructor

###  function InstancedMesh( geometry: BufferGeometry, material: Material,
count: Integer ): void;

[page:BufferGeometry geometry] - an instance of [page:BufferGeometry].  
[page:Material material] - an instance of [page:Material]. Default is a new
[page:MeshBasicMaterial].  
[page:Integer count] - the number of instances.  

## Properties

See the base [page:Mesh] class for common properties.

###  Box3 boundingBox;

This bounding box encloses all instances of the InstancedMesh. Can be
calculated with [page:.computeBoundingBox](). Default is `null`.

###  Sphere boundingSphere;

This bounding sphere encloses all instances of the InstancedMesh. Can be
calculated with [page:.computeBoundingSphere](). Default is `null`.

###  Integer count;

The number of instances. The `count` value passed into the constructor
represents the maximum number of instances of this mesh. You can change the
number of instances at runtime to an integer value in the range [0, count].

If you need more instances than the original count value, you have to create a
new InstancedMesh.

###  InstancedBufferAttribute instanceColor;

Represents the colors of all instances. `null` by default. You have to set its
[page:BufferAttribute.needsUpdate needsUpdate] flag to true if you modify
instanced data via [page:.setColorAt]().

###  InstancedBufferAttribute instanceMatrix;

Represents the local transformation of all instances. You have to set its
[page:BufferAttribute.needsUpdate needsUpdate] flag to true if you modify
instanced data via [page:.setMatrixAt]().

###  Boolean isInstancedMesh;

Read-only flag to check if a given object is of type InstancedMesh.

## Methods

See the base [page:Mesh] class for common methods.

###  function computeBoundingBox( ): undefined;

Computes the bounding box, updating [page:.boundingBox] attribute.  
Bounding boxes aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

###  function computeBoundingSphere( ): undefined;

Computes the bounding sphere, updating [page:.boundingSphere] attribute.  
Bounding spheres aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function getColorAt( index: Integer, color: Color ): undefined;

[page:Integer index]: The index of an instance. Values have to be in the range
[0, count].

[page:Color color]: This color object will be set to the color of the defined
instance.

Get the color of the defined instance.

###  function getMatrixAt( index: Integer, matrix: Matrix4 ): undefined;

[page:Integer index]: The index of an instance. Values have to be in the range
[0, count].

[page:Matrix4 matrix]: This 4x4 matrix will be set to the local transformation
matrix of the defined instance.

Get the local transformation matrix of the defined instance.

###  function setColorAt( index: Integer, color: Color ): undefined;

[page:Integer index]: The index of an instance. Values have to be in the range
[0, count].

[page:Color color]: The color of a single instance.

Sets the given color to the defined instance. Make sure you set
[page:.instanceColor][page:BufferAttribute.needsUpdate .needsUpdate] to true
after updating all the colors.

###  function setMatrixAt( index: Integer, matrix: Matrix4 ): undefined;

[page:Integer index]: The index of an instance. Values have to be in the range
[0, count].

[page:Matrix4 matrix]: A 4x4 matrix representing the local transformation of a
single instance.

Sets the given local transformation matrix to the defined instance. Make sure
you set [page:.instanceMatrix][page:BufferAttribute.needsUpdate .needsUpdate]
to true after updating all the matrices.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

