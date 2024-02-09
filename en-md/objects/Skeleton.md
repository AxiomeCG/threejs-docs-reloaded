# [name]

Use an array of [page:Bone bones] to create a skeleton that can be used by a
[page:SkinnedMesh].

## Code Example

  
```ts  
// Create a simple "arm"  
  
const bones = [];  
  
const shoulder = new THREE.Bone();  
const elbow = new THREE.Bone();  
const hand = new THREE.Bone();  
  
shoulder.add( elbow );  
elbow.add( hand );  
  
bones.push( shoulder );  
bones.push( elbow );  
bones.push( hand );  
  
shoulder.position.y = -5;  
elbow.position.y = 0;  
hand.position.y = 5;  
  
const armSkeleton = new THREE.Skeleton( bones );  
```  

See the [page:SkinnedMesh] page for an example of usage with standard
[page:BufferGeometry].

## Constructor

### [name]( [param:Array bones], [param:Array boneInverses] )

[page:Array bones] - The array of [page:Bone bones]. Default is an empty
array.  
[page:Array boneInverses] - (optional) An array of [page:Matrix4 Matrix4s].  
  
Creates a new [name].

## Properties

### <br/> Array bones; <br/>

The array of [page:bone bones]. Note this is a copy of the original array, not
a reference, so you can modify the original array without effecting this one.

### <br/> Array boneInverses; <br/>

An array of [page:Matrix4 Matrix4s] that represent the inverse of the
[page:Matrix4 matrixWorld] of the individual bones.

### <br/> Float32Array boneMatrices; <br/>

The array buffer holding the bone data when using a vertex texture.

### <br/> DataTexture boneTexture; <br/>

The [page:DataTexture] holding the bone data when using a vertex texture.

### <br/> Integer boneTextureSize; <br/>

The size of the [page:.boneTexture].

## Methods

### [method:Skeleton clone]()

Returns a clone of this Skeleton object.

### [method:undefined calculateInverses]()

Generates the [page:.boneInverses boneInverses] array if not provided in the
constructor.

### <br/> function computeBoneTexture( ): computeBoneTexture; <br/>

Computes an instance of [page:DataTexture] in order to pass the bone data more
efficiently to the shader. The texture is assigned to [page:.boneTexture
boneTexture].

### [method:undefined pose]()

Returns the skeleton to the base pose.

### [method:undefined update]()

Updates the [page:Float32Array boneMatrices] and [page:DataTexture
boneTexture] after changing the bones. This is called automatically by the
[page:WebGLRenderer] if the skeleton is used with a [page:SkinnedMesh].

### [method:Bone getBoneByName]( [param:String name] )

name -- String to match to the Bone's .name property.  
  
Searches through the skeleton's bone array and returns the first with a
matching name.  

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

