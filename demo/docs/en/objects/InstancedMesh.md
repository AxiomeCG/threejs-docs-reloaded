[Mesh](en\objects\Mesh.html) →

# InstancedMesh

A special version of [Mesh](en\objects\Mesh.html) with instanced rendering
support. Use InstancedMesh if you have to render a large number of objects
with the same geometry and material but with different world transformations.
The usage of InstancedMesh will help you to reduce the number of draw calls
and thus improve the overall rendering performance in your application.

## Examples

[example:webgl_instancing_dynamic WebGL / instancing / dynamic]  
[example:webgl_instancing_performance WebGL / instancing / performance]  
[example:webgl_instancing_scatter WebGL / instancing / scatter]  
[example:webgl_instancing_raycast WebGL / instancing / raycast]

## Constructor

### InstancedMesh

  
  
```ts  
function InstancedMesh( geometry: BufferGeometry, material: Material, count:
Integer ): void;  
```  

[geometry](en\core\BufferGeometry.html) - an instance of
[BufferGeometry](en\core\BufferGeometry.html).  
[material](en\materials\Material.html) - an instance of
[Material](en\materials\Material.html). Default is a new
[MeshBasicMaterial](en\materials\MeshBasicMaterial.html).  
[count](#) - the number of instances.  

## Properties

See the base [Mesh](en\objects\Mesh.html) class for common properties.

### boundingBox

  
  
```ts  
boundingBox: Box3;  
```  

This bounding box encloses all instances of the InstancedMesh. Can be
calculated with [.computeBoundingBox](#)(). Default is `null`.

### boundingSphere

  
  
```ts  
boundingSphere: Sphere;  
```  

This bounding sphere encloses all instances of the InstancedMesh. Can be
calculated with [.computeBoundingSphere](#)(). Default is `null`.

### count

  
  
```ts  
count: Integer;  
```  

The number of instances. The `count` value passed into the constructor
represents the maximum number of instances of this mesh. You can change the
number of instances at runtime to an integer value in the range [0, count].

If you need more instances than the original count value, you have to create a
new InstancedMesh.

### instanceColor

  
  
```ts  
instanceColor: InstancedBufferAttribute;  
```  

Represents the colors of all instances. `null` by default. You have to set its
[needsUpdate](#) flag to true if you modify instanced data via
[.setColorAt](#)().

### instanceMatrix

  
  
```ts  
instanceMatrix: InstancedBufferAttribute;  
```  

Represents the local transformation of all instances. You have to set its
[needsUpdate](#) flag to true if you modify instanced data via
[.setMatrixAt](#)().

### isInstancedMesh

  
  
```ts  
isInstancedMesh: Boolean;  
```  

Read-only flag to check if a given object is of type InstancedMesh.

## Methods

See the base [Mesh](en\objects\Mesh.html) class for common methods.

### computeBoundingBox

  
  
```ts  
function computeBoundingBox( ): undefined;  
```  

Computes the bounding box, updating [.boundingBox](#) attribute.  
Bounding boxes aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

### computeBoundingSphere

  
  
```ts  
function computeBoundingSphere( ): undefined;  
```  

Computes the bounding sphere, updating [.boundingSphere](#) attribute.  
Bounding spheres aren't computed by default. They need to be explicitly
computed, otherwise they are `null`.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### getColorAt

  
  
```ts  
function getColorAt( index: Integer, color: Color ): undefined;  
```  

[index](#): The index of an instance. Values have to be in the range [0,
count].

[color](en\math\Color.html): This color object will be set to the color of the
defined instance.

Get the color of the defined instance.

### getMatrixAt

  
  
```ts  
function getMatrixAt( index: Integer, matrix: Matrix4 ): undefined;  
```  

[index](#): The index of an instance. Values have to be in the range [0,
count].

[matrix](en\math\Matrix4.html): This 4x4 matrix will be set to the local
transformation matrix of the defined instance.

Get the local transformation matrix of the defined instance.

### setColorAt

  
  
```ts  
function setColorAt( index: Integer, color: Color ): undefined;  
```  

[index](#): The index of an instance. Values have to be in the range [0,
count].

[color](en\math\Color.html): The color of a single instance.

Sets the given color to the defined instance. Make sure you set
[.instanceColor](#)[.needsUpdate](#) to true after updating all the colors.

### setMatrixAt

  
  
```ts  
function setMatrixAt( index: Integer, matrix: Matrix4 ): undefined;  
```  

[index](#): The index of an instance. Values have to be in the range [0,
count].

[matrix](en\math\Matrix4.html): A 4x4 matrix representing the local
transformation of a single instance.

Sets the given local transformation matrix to the defined instance. Make sure
you set [.instanceMatrix](#)[.needsUpdate](#) to true after updating all the
matrices.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/InstancedMesh.js">src/objects/InstancedMesh.js</a>

