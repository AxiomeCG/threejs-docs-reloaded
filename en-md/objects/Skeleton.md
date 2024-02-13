# Skeleton

Use an array of [page:Bone bones] to create a skeleton that can be used by a
[page:SkinnedMesh].

## Code Example

  
```ts  
// Create a simple "arm" const bones = []; const shoulder = new THREE.Bone();
const elbow = new THREE.Bone(); const hand = new THREE.Bone(); shoulder.add(
elbow ); elbow.add( hand ); bones.push( shoulder ); bones.push( elbow );
bones.push( hand ); shoulder.position.y = -5; elbow.position.y = 0;
hand.position.y = 5; const armSkeleton = new THREE.Skeleton( bones );  
```  

See the [page:SkinnedMesh] page for an example of usage with standard
[page:BufferGeometry].

## Constructor

###  function Skeleton( bones: Array, boneInverses: Array ): void;

[page:Array bones] - The array of [page:Bone bones]. Default is an empty
array.  
[page:Array boneInverses] - (optional) An array of [page:Matrix4 Matrix4s].  
  
Creates a new Skeleton.

## Properties

###  Array bones;

The array of [page:bone bones]. Note this is a copy of the original array, not
a reference, so you can modify the original array without effecting this one.

###  Array boneInverses;

An array of [page:Matrix4 Matrix4s] that represent the inverse of the
[page:Matrix4 matrixWorld] of the individual bones.

###  Float32Array boneMatrices;

The array buffer holding the bone data when using a vertex texture.

###  DataTexture boneTexture;

The [page:DataTexture] holding the bone data when using a vertex texture.

###  Integer boneTextureSize;

The size of the [page:.boneTexture].

## Methods

###  function clone( ): Skeleton;

Returns a clone of this Skeleton object.

###  function calculateInverses( ): undefined;

Generates the [page:.boneInverses boneInverses] array if not provided in the
constructor.

###  function computeBoneTexture( ): this;

Computes an instance of [page:DataTexture] in order to pass the bone data more
efficiently to the shader. The texture is assigned to [page:.boneTexture
boneTexture].

###  function pose( ): undefined;

Returns the skeleton to the base pose.

###  function update( ): undefined;

Updates the [page:Float32Array boneMatrices] and [page:DataTexture
boneTexture] after changing the bones. This is called automatically by the
[page:WebGLRenderer] if the skeleton is used with a [page:SkinnedMesh].

###  function getBoneByName( name: String ): Bone;

name -- String to match to the Bone's .name property.  
  
Searches through the skeleton's bone array and returns the first with a
matching name.  

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

