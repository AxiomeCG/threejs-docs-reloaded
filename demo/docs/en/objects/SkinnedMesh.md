[Object3D](en\core\Object3D.html) → [Mesh](en\objects\Mesh.html) →

# SkinnedMesh

A mesh that has a [Skeleton](en\objects\Skeleton.html) with
[bones](en\objects\Bone.html) that can then be used to animate the vertices of
the geometry.  
  
SkinnedMesh can only be used with WebGL 2. With WebGL 1 `OES_texture_float`
and vertex textures support is required.

## Code Example

  
```ts  
const geometry = new THREE.CylinderGeometry( 5, 5, 5, 5, 15, 5, 30 ); //
create the skin indices and skin weights manually // (typically a loader would
read this data from a 3D model for you) const position =
geometry.attributes.position; const vertex = new THREE.Vector3(); const
skinIndices = []; const skinWeights = []; for ( let i = 0; i < position.count;
i ++ ) { vertex.fromBufferAttribute( position, i ); // compute skinIndex and
skinWeight based on some configuration data const y = ( vertex.y +
sizing.halfHeight ); const skinIndex = Math.floor( y / sizing.segmentHeight );
const skinWeight = ( y % sizing.segmentHeight ) / sizing.segmentHeight;
skinIndices.push( skinIndex, skinIndex + 1, 0, 0 ); skinWeights.push( 1 -
skinWeight, skinWeight, 0, 0 ); } geometry.setAttribute( 'skinIndex', new
THREE.Uint16BufferAttribute( skinIndices, 4 ) ); geometry.setAttribute(
'skinWeight', new THREE.Float32BufferAttribute( skinWeights, 4 ) ); // create
skinned mesh and skeleton const mesh = new THREE.SkinnedMesh( geometry,
material ); const skeleton = new THREE.Skeleton( bones ); // see example from
THREE.Skeleton const rootBone = skeleton.bones[ 0 ]; mesh.add( rootBone ); //
bind the skeleton to the mesh mesh.bind( skeleton ); // move the bones and
manipulate the model skeleton.bones[ 0 ].rotation.x = -0.1; skeleton.bones[ 1
].rotation.x = 0.2;  
```  

## Constructor

### SkinnedMesh

  
  
```ts  
function SkinnedMesh( geometry: BufferGeometry, material: Material ): void;  
```  

[geometry](en\core\BufferGeometry.html) - an instance of
[BufferGeometry](en\core\BufferGeometry.html).  
[material](en\materials\Material.html) - (optional) an instance of
[Material](en\materials\Material.html). Default is a new
[MeshBasicMaterial](en\materials\MeshBasicMaterial.html).

## Properties

See the base [Mesh](en\objects\Mesh.html) class for common properties.

### bindMode

  
  
```ts  
bindMode: String;  
```  

Either "attached" or "detached". "attached" uses the
[SkinnedMesh.matrixWorld](#) property for the base transform matrix of the
bones. "detached" uses the [SkinnedMesh.bindMatrix](#). Default is "attached".

### bindMatrix

  
  
```ts  
bindMatrix: Matrix4;  
```  

The base matrix that is used for the bound bone transforms.

### bindMatrixInverse

  
  
```ts  
bindMatrixInverse: Matrix4;  
```  

The base matrix that is used for resetting the bound bone transforms.

### boundingBox

  
  
```ts  
boundingBox: Box3;  
```  

The bounding box of the SkinnedMesh. Can be calculated with
[.computeBoundingBox](#)(). Default is `null`.

### boundingSphere

  
  
```ts  
boundingSphere: Sphere;  
```  

The bounding sphere of the SkinnedMesh. Can be calculated with
[.computeBoundingSphere](#)(). Default is `null`.

### isSkinnedMesh

  
  
```ts  
isSkinnedMesh: Boolean;  
```  

Read-only flag to check if a given object is of type SkinnedMesh.

### skeleton

  
  
```ts  
skeleton: Skeleton;  
```  

[Skeleton](en\objects\Skeleton.html) representing the bone hierarchy of the
skinned mesh.

## Methods

See the base [Mesh](en\objects\Mesh.html) class for common methods.

### bind

  
  
```ts  
function bind( skeleton: Skeleton, bindMatrix: Matrix4 ): undefined;  
```  

[skeleton](en\objects\Skeleton.html) - [Skeleton](en\objects\Skeleton.html)
created from a [Bones](en\objects\Bone.html) tree.  
[bindMatrix](en\math\Matrix4.html) - [Matrix4](en\math\Matrix4.html) that
represents the base transform of the skeleton.  
  
Bind a skeleton to the skinned mesh. The bindMatrix gets saved to .bindMatrix
property and the .bindMatrixInverse gets calculated.

### clone

  
  
```ts  
function clone( ): SkinnedMesh;  
```  

This method does currently not clone an instance of SkinnedMesh correctly.
Please use [SkeletonUtils.clone](#)() in the meanwhile.

### computeBoundingBox

  
  
```ts  
function computeBoundingBox( ): undefined;  
```  

Computes the bounding box, updating [.boundingBox](#) attribute.  
Bounding boxes aren't computed by default. They need to be explicitly
computed, otherwise they are `null`. If an instance of SkinnedMesh is
animated, this method should be called per frame to compute a correct bounding
box.

### computeBoundingSphere

  
  
```ts  
function computeBoundingSphere( ): undefined;  
```  

Computes the bounding sphere, updating [.boundingSphere](#) attribute.  
Bounding spheres aren't computed by default. They need to be explicitly
computed, otherwise they are `null`. If an instance of SkinnedMesh is
animated, this method should be called per frame to compute a correct bounding
sphere.

### normalizeSkinWeights

  
  
```ts  
function normalizeSkinWeights( ): undefined;  
```  

Normalizes the skin weights.

### pose

  
  
```ts  
function pose( ): undefined;  
```  

This method sets the skinned mesh in the rest pose (resets the pose).

### applyBoneTransform

  
  
```ts  
function applyBoneTransform( index: Integer, vector: Vector3 ): Vector3;  
```  

Applies the bone transform associated with the given index to the given
position vector. Returns the updated vector.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/SkinnedMesh.js">src/objects/SkinnedMesh.js</a>

