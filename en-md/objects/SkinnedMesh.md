[page:Object3D] → [page:Mesh] →

# SkinnedMesh

A mesh that has a [page:Skeleton] with [page:Bone bones] that can then be used
to animate the vertices of the geometry.  
  
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

###  function SkinnedMesh( geometry: BufferGeometry, material: Material ):
void;

[page:BufferGeometry geometry] - an instance of [page:BufferGeometry].  
[page:Material material] - (optional) an instance of [page:Material]. Default
is a new [page:MeshBasicMaterial].

## Properties

See the base [page:Mesh] class for common properties.

###  String bindMode;

Either "attached" or "detached". "attached" uses the
[page:SkinnedMesh.matrixWorld] property for the base transform matrix of the
bones. "detached" uses the [page:SkinnedMesh.bindMatrix]. Default is
"attached".

###  Matrix4 bindMatrix;

The base matrix that is used for the bound bone transforms.

###  Matrix4 bindMatrixInverse;

The base matrix that is used for resetting the bound bone transforms.

###  Box3 boundingBox;

The bounding box of the SkinnedMesh. Can be calculated with
[page:.computeBoundingBox](). Default is `null`.

###  Sphere boundingSphere;

The bounding sphere of the SkinnedMesh. Can be calculated with
[page:.computeBoundingSphere](). Default is `null`.

###  Boolean isSkinnedMesh;

Read-only flag to check if a given object is of type SkinnedMesh.

###  Skeleton skeleton;

[page:Skeleton] representing the bone hierarchy of the skinned mesh.

## Methods

See the base [page:Mesh] class for common methods.

###  function bind( skeleton: Skeleton, bindMatrix: Matrix4 ): undefined;

[page:Skeleton skeleton] - [page:Skeleton] created from a [page:Bone Bones]
tree.  
[page:Matrix4 bindMatrix] - [page:Matrix4] that represents the base transform
of the skeleton.  
  
Bind a skeleton to the skinned mesh. The bindMatrix gets saved to .bindMatrix
property and the .bindMatrixInverse gets calculated.

###  function clone( ): SkinnedMesh;

This method does currently not clone an instance of SkinnedMesh correctly.
Please use [page:SkeletonUtils.clone]() in the meanwhile.

###  function computeBoundingBox( ): undefined;

Computes the bounding box, updating [page:.boundingBox] attribute.  
Bounding boxes aren't computed by default. They need to be explicitly
computed, otherwise they are `null`. If an instance of SkinnedMesh is
animated, this method should be called per frame to compute a correct bounding
box.

###  function computeBoundingSphere( ): undefined;

Computes the bounding sphere, updating [page:.boundingSphere] attribute.  
Bounding spheres aren't computed by default. They need to be explicitly
computed, otherwise they are `null`. If an instance of SkinnedMesh is
animated, this method should be called per frame to compute a correct bounding
sphere.

###  function normalizeSkinWeights( ): undefined;

Normalizes the skin weights.

###  function pose( ): undefined;

This method sets the skinned mesh in the rest pose (resets the pose).

###  function applyBoneTransform( index: Integer, vector: Vector3 ): Vector3;

Applies the bone transform associated with the given index to the given
position vector. Returns the updated vector.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

