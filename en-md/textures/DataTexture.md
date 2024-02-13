[page:Texture] →

# DataTexture

Creates a texture directly from raw data, width and height.

## Constructor

###  function DataTexture( ): void;

The data argument must be an [link:https://developer.mozilla.org/en-
US/docs/Web/API/ArrayBufferView ArrayBufferView]. Further parameters
correspond to the properties inherited from [page:Texture], where both
magFilter and minFilter default to THREE.NearestFilter.

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

  
```ts  
// create a buffer with color data const width = 512; const height = 512;
const size = width * height; const data = new Uint8Array( 4 * size ); const
color = new THREE.Color( 0xffffff ); const r = Math.floor( color.r * 255 );
const g = Math.floor( color.g * 255 ); const b = Math.floor( color.b * 255 );
for ( let i = 0; i < size; i ++ ) { const stride = i * 4; data[ stride ] = r;
data[ stride + 1 ] = g; data[ stride + 2 ] = b; data[ stride + 3 ] = 255; } //
used the buffer to create a DataTexture const texture = new THREE.DataTexture(
data, width, height ); texture.needsUpdate = true;  
```  

## Properties

See the base [page:Texture Texture] class for common properties.

###  Boolean flipY;

If set to `true`, the texture is flipped along the vertical axis when uploaded
to the GPU. Default is `false`.

###  Boolean generateMipmaps;

Whether to generate mipmaps (if possible) for a texture. False by default.

###  Object image;

Overridden with a object holding data, width, and height.

###  Boolean isDataTexture;

Read-only flag to check if a given object is of type DataTexture.

###  number unpackAlignment;

`1` by default. Specifies the alignment requirements for the start of each
pixel row in memory. The allowable values are 1 (byte-alignment), 2 (rows
aligned to even-numbered bytes), 4 (word-alignment), and 8 (rows start on
double-word boundaries). See
[link:http://www.khronos.org/opengles/sdk/docs/man/xhtml/glPixelStorei.xml
glPixelStorei] for more information.

## Methods

See the base [page:Texture Texture] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

