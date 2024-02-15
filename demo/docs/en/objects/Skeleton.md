# Skeleton

Use an array of [bones](en\objects\Bone.html) to create a skeleton that can be
used by a [SkinnedMesh](en\objects\SkinnedMesh.html).

## Code Example

  
```ts  
// Create a simple "arm" const bones = []; const shoulder = new THREE.Bone();
const elbow = new THREE.Bone(); const hand = new THREE.Bone(); shoulder.add(
elbow ); elbow.add( hand ); bones.push( shoulder ); bones.push( elbow );
bones.push( hand ); shoulder.position.y = -5; elbow.position.y = 0;
hand.position.y = 5; const armSkeleton = new THREE.Skeleton( bones );  
```  

See the [SkinnedMesh](en\objects\SkinnedMesh.html) page for an example of
usage with standard [BufferGeometry](en\core\BufferGeometry.html).

## Constructor

### Skeleton

  
  
```ts  
function Skeleton( bones: Array, boneInverses: Array ): void;  
```  

[bones](#) - The array of [bones](en\objects\Bone.html). Default is an empty
array.  
[boneInverses](#) - (optional) An array of [Matrix4s](en\math\Matrix4.html).  
  
Creates a new Skeleton.

## Properties

### bones

  
  
```ts  
bones: Array;  
```  

The array of [bones](#). Note this is a copy of the original array, not a
reference, so you can modify the original array without effecting this one.

### boneInverses

  
  
```ts  
boneInverses: Array;  
```  

An array of [Matrix4s](en\math\Matrix4.html) that represent the inverse of the
[matrixWorld](en\math\Matrix4.html) of the individual bones.

### boneMatrices

  
  
```ts  
boneMatrices: Float32Array;  
```  

The array buffer holding the bone data when using a vertex texture.

### boneTexture

  
  
```ts  
boneTexture: DataTexture;  
```  

The [DataTexture](en\textures\DataTexture.html) holding the bone data when
using a vertex texture.

### boneTextureSize

  
  
```ts  
boneTextureSize: Integer;  
```  

The size of the [.boneTexture](#).

## Methods

### clone

  
  
```ts  
function clone( ): Skeleton;  
```  

Returns a clone of this Skeleton object.

### calculateInverses

  
  
```ts  
function calculateInverses( ): undefined;  
```  

Generates the [.boneInverses](#boneInverses) array if not provided in the
constructor.

### computeBoneTexture

  
  
```ts  
function computeBoneTexture( ): this;  
```  

Computes an instance of [DataTexture](en\textures\DataTexture.html) in order
to pass the bone data more efficiently to the shader. The texture is assigned
to [.boneTexture](#boneTexture).

### pose

  
  
```ts  
function pose( ): undefined;  
```  

Returns the skeleton to the base pose.

### update

  
  
```ts  
function update( ): undefined;  
```  

Updates the [boneMatrices](#) and [boneTexture](en\textures\DataTexture.html)
after changing the bones. This is called automatically by the
[WebGLRenderer](en\renderers\WebGLRenderer.html) if the skeleton is used with
a [SkinnedMesh](en\objects\SkinnedMesh.html).

### getBoneByName

  
  
```ts  
function getBoneByName( name: String ): Bone;  
```  

name -- String to match to the Bone's .name property.  
  
Searches through the skeleton's bone array and returns the first with a
matching name.  

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/Skeleton.js">src/objects/Skeleton.js</a>

