[Texture](en\textures\Texture.html) →

# DataArrayTexture

Creates an array of textures directly from raw data, width and height and
depth. This type of texture can only be used with a WebGL 2 rendering context.

## Constructor

### DataArrayTexture

  
  
```ts  
function DataArrayTexture( ): void;  
```  

The data argument must be an <a href="https://developer.mozilla.org/en-
US/docs/Web/API/ArrayBufferView">ArrayBufferView</a>. The properties inherited
from [Texture](en\textures\Texture.html) are the default, except magFilter and
minFilter default to THREE.NearestFilter. The properties flipY and
generateMipmaps are initially set to false.

The interpretation of the data depends on type and format: If the type is
THREE.UnsignedByteType, a Uint8Array will be useful for addressing the texel
data. If the format is THREE.RGBAFormat, data needs four values for one texel;
Red, Green, Blue and Alpha (typically the opacity).  
For the packed types, THREE.UnsignedShort4444Type and
THREE.UnsignedShort5551Type all color components of one texel can be addressed
as bitfields within an integer element of a Uint16Array.  
In order to use the types THREE.FloatType and THREE.HalfFloatType, the WebGL
implementation must support the respective extensions OES_texture_float and
OES_texture_half_float. In order to use THREE.LinearFilter for component-wise,
bilinear interpolation of the texels based on these types, the WebGL
extensions OES_texture_float_linear or OES_texture_half_float_linear must also
be present.

## Code Example

This creates a DataArrayTexture where each texture has a different color.

  
```ts  
// create a buffer with color data const width = 512; const height = 512;
const depth = 100; const size = width * height; const data = new Uint8Array( 4
* size * depth ); for ( let i = 0; i < depth; i ++ ) { const color = new
THREE.Color( Math.random(), Math.random(), Math.random() ); const r =
Math.floor( color.r * 255 ); const g = Math.floor( color.g * 255 ); const b =
Math.floor( color.b * 255 ); for ( let j = 0; j < size; j ++ ) { const stride
= ( i * size + j ) * 4; data[ stride ] = r; data[ stride + 1 ] = g; data[
stride + 2 ] = b; data[ stride + 3 ] = 255; } } // used the buffer to create a
DataArrayTexture const texture = new THREE.DataArrayTexture( data, width,
height, depth ); texture.needsUpdate = true;  
```  

## Examples

[example:webgl2_materials_texture2darray WebGL2 / materials / texture2darray]
[example:webgl2_rendertarget_texture2darray WebGL2 / rendertarget /
texture2darray]

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
image: Object;  
```  

Overridden with a object holding data, width, height, and depth.

### isDataArrayTexture

  
  
```ts  
isDataArrayTexture: Boolean;  
```  

Read-only flag to check if a given object is of type DataArrayTexture.

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
href="https://github.com/mrdoob/three.js/blob/master/src/textures/DataArrayTexture.js">src/textures/DataArrayTexture.js</a>

