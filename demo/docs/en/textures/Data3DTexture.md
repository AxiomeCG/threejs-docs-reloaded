[Texture](en\textures\Texture.html) →

# Data3DTexture

Creates a three-dimensional texture from raw data, with parameters to divide
it into width, height, and depth. This type of texture can only be used with a
WebGL 2 rendering context.

## Constructor

### Data3DTexture

  
  
```ts  
function Data3DTexture( data: TypedArray, width: Number, height: Number,
depth: Number ): void;  
```  

[data](#) -- <a href="https://developer.mozilla.org/en-
US/docs/Web/API/ArrayBufferView">ArrayBufferView</a> of the texture.  
[width](#) -- width of the texture.  
[height](#) -- height of the texture.  
[depth](#) -- depth of the texture.

## Code Example

This creates a Data3DTexture with repeating data, 0 to 255

  
```ts  
// create a buffer with some data const sizeX = 64; const sizeY = 64; const
sizeZ = 64; const data = new Uint8Array( sizeX * sizeY * sizeZ ); let i = 0;
for ( let z = 0; z < sizeZ; z ++ ) { for ( let y = 0; y < sizeY; y ++ ) { for
( let x = 0; x < sizeX; x ++ ) { data[ i ] = i % 256; i ++; } } } // use the
buffer to create the texture const texture = new THREE.Data3DTexture( data,
sizeX, sizeY, sizeZ ); texture.needsUpdate = true;  
```  

## Examples

[example:webgl2_materials_texture3d WebGL2 / materials / texture3d]  
[example:webgl2_materials_texture3d_partialupdate WebGL2 / materials /
texture3d / partialupdate]  
[example:webgl2_volume_cloud WebGL2 / volume / cloud]  
[example:webgl2_volume_perlin WebGL2 / volume / perlin]

## Properties

See the base [Texture](en\textures\Texture.html) class for common properties.

### flipY

  
  
```ts  
flipY: Boolean;  
```  

Whether the texture is flipped along the Y axis when uploaded to the GPU.
Default is `false`.

### generateMipmaps

  
  
```ts  
generateMipmaps: Boolean;  
```  

Whether to generate mipmaps (if possible) for the texture. Default is `false`.

### image

  
  
```ts  
image: Image;  
```  

Overridden with a record type holding data, width and height and depth.

### isData3DTexture

  
  
```ts  
isData3DTexture: Boolean;  
```  

Read-only flag to check if a given object is of type Data3DTexture.

### magFilter

  
  
```ts  
magFilter: number;  
```  

How the texture is sampled when a texel covers more than one pixel. The
default is [THREE.NearestFilter](en\constants\Textures.html), which uses the
value of the closest texel.  
  
See the [texture constants](en\constants\Textures.html) page for details.

### minFilter

  
  
```ts  
minFilter: number;  
```  

How the texture is sampled when a texel covers less than one pixel. The
default is [THREE.NearestFilter](en\constants\Textures.html), which uses the
value of the closest texel.  
  
See the [texture constants](en\constants\Textures.html) page for details.

### unpackAlignment

  
  
```ts  
unpackAlignment: number;  
```  

`1` by default. Specifies the alignment requirements for the start of each
pixel row in memory. The allowable values are 1 (byte-alignment), 2 (rows
aligned to even-numbered bytes), 4 (word-alignment), and 8 (rows start on
double-word boundaries). See <a href="https://registry.khronos.org/OpenGL-
Refpages/es3.0/html/glPixelStorei.xhtml">glPixelStorei</a> for more
information.

### wrapR

  
  
```ts  
wrapR: number;  
```  

This defines how the texture is wrapped in the depth direction.  
The default is [THREE.ClampToEdgeWrapping](en\constants\Textures.html), where
the edge is clamped to the outer edge texels. The other two choices are
[THREE.RepeatWrapping](en\constants\Textures.html) and
[THREE.MirroredRepeatWrapping](en\constants\Textures.html). See the [texture
constants](en\constants\Textures.html) page for details.

## Methods

See the base [Texture](en\textures\Texture.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/Data3DTexture.js">src/textures/Data3DTexture.js</a>

