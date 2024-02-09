[page:Texture] →

# [name]

Creates a three-dimensional texture from raw data, with parameters to divide
it into width, height, and depth. This type of texture can only be used with a
WebGL 2 rendering context.

## Constructor

###  [name]( [param:TypedArray data], [param:Number width], [param:Number
height], [param:Number depth] )

[page:Object data] -- [link:https://developer.mozilla.org/en-
US/docs/Web/API/ArrayBufferView ArrayBufferView] of the texture.  
[page:Number width] -- width of the texture.  
[page:Number height] -- height of the texture.  
[page:Number depth] -- depth of the texture.

## Code Example

This creates a [name] with repeating data, 0 to 255

  
```ts  
// create a buffer with some data  
const sizeX = 64;  
const sizeY = 64;  
const sizeZ = 64;  
  
const data = new Uint8Array( sizeX * sizeY * sizeZ );  
let i = 0;  
  
for ( let z = 0; z < sizeZ; z ++ ) {  
for ( let y = 0; y < sizeY; y ++ ) {  
for ( let x = 0; x < sizeX; x ++ ) {  
data[ i ] = i % 256;  
i ++;  
}  
}  
}  
  
// use the buffer to create the texture  
const texture = new THREE.Data3DTexture( data, sizeX, sizeY, sizeZ );  
texture.needsUpdate = true;  
```  

## Examples

[example:webgl2_materials_texture3d WebGL2 / materials / texture3d]  
[example:webgl2_materials_texture3d_partialupdate WebGL2 / materials /
texture3d / partialupdate]  
[example:webgl2_volume_cloud WebGL2 / volume / cloud]  
[example:webgl2_volume_perlin WebGL2 / volume / perlin]

## Properties

See the base [page:Texture Texture] class for common properties.

### <br/> Boolean flipY; <br/>

Whether the texture is flipped along the Y axis when uploaded to the GPU.
Default is `false`.

### <br/> Boolean generateMipmaps; <br/>

Whether to generate mipmaps (if possible) for the texture. Default is `false`.

### <br/> Image image; <br/>

Overridden with a record type holding data, width and height and depth.

### <br/> Boolean isData3DTexture; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> number magFilter; <br/>

How the texture is sampled when a texel covers more than one pixel. The
default is [page:Textures THREE.NearestFilter], which uses the value of the
closest texel.  
  
See the [page:Textures texture constants] page for details.

### <br/> number minFilter; <br/>

How the texture is sampled when a texel covers less than one pixel. The
default is [page:Textures THREE.NearestFilter], which uses the value of the
closest texel.  
  
See the [page:Textures texture constants] page for details.

### <br/> number unpackAlignment; <br/>

`1` by default. Specifies the alignment requirements for the start of each
pixel row in memory. The allowable values are 1 (byte-alignment), 2 (rows
aligned to even-numbered bytes), 4 (word-alignment), and 8 (rows start on
double-word boundaries). See [link:https://registry.khronos.org/OpenGL-
Refpages/es3.0/html/glPixelStorei.xhtml glPixelStorei] for more information.

### <br/> number wrapR; <br/>

This defines how the texture is wrapped in the depth direction.  
The default is [page:Textures THREE.ClampToEdgeWrapping], where the edge is
clamped to the outer edge texels. The other two choices are [page:Textures
THREE.RepeatWrapping] and [page:Textures THREE.MirroredRepeatWrapping]. See
the [page:Textures texture constants] page for details.

## Methods

See the base [page:Texture Texture] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

