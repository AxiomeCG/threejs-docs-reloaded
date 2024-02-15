# Texture Constants

## Mapping Modes

  
```ts  
THREE.UVMapping THREE.CubeReflectionMapping THREE.CubeRefractionMapping
THREE.EquirectangularReflectionMapping THREE.EquirectangularRefractionMapping
THREE.CubeUVReflectionMapping  
```  

These define the texture's mapping mode.  
[UVMapping](#) is the default, and maps the texture using the mesh's UV
coordinates.  
  
The rest define environment mapping types.  
  
[CubeReflectionMapping](#) and [CubeRefractionMapping](#) are for use with a
[CubeTexture](en\textures\CubeTexture.html), which is made up of six textures,
one for each face of the cube. [CubeReflectionMapping](#) is the default for a
[CubeTexture](en\textures\CubeTexture.html).  
  
[EquirectangularReflectionMapping](#) and
[EquirectangularRefractionMapping](#) are for use with an equirectangular
environment map. Also called a lat-long map, an equirectangular texture
represents a 360-degree view along the horizontal centerline, and a 180-degree
view along the vertical axis, with the top and bottom edges of the image
corresponding to the north and south poles of a mapped sphere.  
  
See the [example:webgl_materials_envmaps materials / envmaps] example.

## Wrapping Modes

  
```ts  
THREE.RepeatWrapping THREE.ClampToEdgeWrapping THREE.MirroredRepeatWrapping  
```  

These define the texture's [wrapS](#) and [wrapT](#) properties, which define
horizontal and vertical texture wrapping.  
  
With [RepeatWrapping](#) the texture will simply repeat to infinity.  
  
[ClampToEdgeWrapping](#) is the default. The last pixel of the texture
stretches to the edge of the mesh.  
  
With [MirroredRepeatWrapping](#) the texture will repeats to infinity,
mirroring on each repeat.

## Magnification Filters

  
```ts  
THREE.NearestFilter THREE.LinearFilter  
```  

For use with a texture's [magFilter](#) property, these define the texture
magnification function to be used when the pixel being textured maps to an
area less than or equal to one texture element (texel).  
  
[NearestFilter](#) returns the value of the texture element that is nearest
(in Manhattan distance) to the specified texture coordinates.  
  
[LinearFilter](#) is the default and returns the weighted average of the four
texture elements that are closest to the specified texture coordinates, and
can include items wrapped or repeated from other parts of a texture, depending
on the values of [wrapS](#) and [wrapT](#), and on the exact mapping.

## Minification Filters

  
```ts  
THREE.NearestFilter THREE.NearestMipmapNearestFilter
THREE.NearestMipmapLinearFilter THREE.LinearFilter
THREE.LinearMipmapNearestFilter THREE.LinearMipmapLinearFilter  
```  

For use with a texture's [minFilter](#) property, these define the texture
minifying function that is used whenever the pixel being textured maps to an
area greater than one texture element (texel).  
  
In addition to [NearestFilter](#) and [LinearFilter](#), the following four
functions can be used for minification:  
  
[NearestMipmapNearestFilter](#) chooses the mipmap that most closely matches
the size of the pixel being textured and uses the [NearestFilter](#) criterion
(the texel nearest to the center of the pixel) to produce a texture value.  
  
[NearestMipmapLinearFilter](#) chooses the two mipmaps that most closely match
the size of the pixel being textured and uses the [NearestFilter](#) criterion
to produce a texture value from each mipmap. The final texture value is a
weighted average of those two values.  
  
[LinearMipmapNearestFilter](#) chooses the mipmap that most closely matches
the size of the pixel being textured and uses the [LinearFilter](#) criterion
(a weighted average of the four texels that are closest to the center of the
pixel) to produce a texture value.  
  
[LinearMipmapLinearFilter](#) is the default and chooses the two mipmaps that
most closely match the size of the pixel being textured and uses the
[LinearFilter](#) criterion to produce a texture value from each mipmap. The
final texture value is a weighted average of those two values.  
  
See the [example:webgl_materials_texture_filters materials / texture /
filters] example.

## Types

  
```ts  
THREE.UnsignedByteType THREE.ByteType THREE.ShortType THREE.UnsignedShortType
THREE.IntType THREE.UnsignedIntType THREE.FloatType THREE.HalfFloatType
THREE.UnsignedShort4444Type THREE.UnsignedShort5551Type
THREE.UnsignedInt248Type  
```  

For use with a texture's [type](#) property, which must correspond to the
correct format. See below for details.  
  
[UnsignedByteType](#) is the default.

## Formats

  
```ts  
THREE.AlphaFormat THREE.RedFormat THREE.RedIntegerFormat THREE.RGFormat
THREE.RGIntegerFormat THREE.RGBAFormat THREE.RGBAIntegerFormat
THREE.LuminanceFormat THREE.LuminanceAlphaFormat THREE.DepthFormat
THREE.DepthStencilFormat  
```  

For use with a texture's [format](#) property, these define how elements of a
2d texture, or `texels`, are read by shaders.  
  
[AlphaFormat](#) discards the red, green and blue components and reads just
the alpha component.  
  
[RedFormat](#) discards the green and blue components and reads just the red
component. (can only be used with a WebGL 2 rendering context).  
  
[RedIntegerFormat](#) discards the green and blue components and reads just
the red component. The texels are read as integers instead of floating point.
(can only be used with a WebGL 2 rendering context).  
  
[RGFormat](#) discards the alpha, and blue components and reads the red, and
green components. (can only be used with a WebGL 2 rendering context).  
  
[RGIntegerFormat](#) discards the alpha, and blue components and reads the
red, and green components. The texels are read as integers instead of floating
point. (can only be used with a WebGL 2 rendering context).  
  
[RGBAFormat](#) is the default and reads the red, green, blue and alpha
components.  
  
[RGBAIntegerFormat](#) is the default and reads the red, green, blue and alpha
components. The texels are read as integers instead of floating point. (can
only be used with a WebGL 2 rendering context).  
  
[LuminanceFormat](#) reads each element as a single luminance component. This
is then converted to a floating point, clamped to the range [0,1], and then
assembled into an RGBA element by placing the luminance value in the red,
green and blue channels, and attaching 1.0 to the alpha channel.  
  
[LuminanceAlphaFormat](#) reads each element as a luminance/alpha double. The
same process occurs as for the [LuminanceFormat](#), except that the alpha
channel may have values other than `1.0`.  
  
[DepthFormat](#) reads each element as a single depth value, converts it to
floating point, and clamps to the range [0,1]. This is the default for
[DepthTexture](en\textures\DepthTexture.html).  
  
[DepthStencilFormat](#) reads each element is a pair of depth and stencil
values. The depth component of the pair is interpreted as in [DepthFormat](#).
The stencil component is interpreted based on the depth + stencil internal
format.  
  
Note that the texture must have the correct [type](#) set, as described above.
See <a
href="https://developer.mozilla.org/en/docs/Web/API/WebGLRenderingContext/texImage2D">WebGLRenderingContext.texImage2D</a>
for details.

## DDS / ST3C Compressed Texture Formats

  
```ts  
THREE.RGB_S3TC_DXT1_Format THREE.RGBA_S3TC_DXT1_Format
THREE.RGBA_S3TC_DXT3_Format THREE.RGBA_S3TC_DXT5_Format  
```  

For use with a [CompressedTexture](en\textures\CompressedTexture.html)'s
[format](#) property, these require support for the <a
href="https://www.khronos.org/registry/webgl/extensions/WEBGL_compressed_texture_s3tc/">WEBGL_compressed_texture_s3tc</a>
extension.  
  
There are four <a
href="https://en.wikipedia.org/wiki/S3_Texture_Compression">S3TC</a> formats
available via this extension. These are:  
[RGB_S3TC_DXT1_Format](#): A DXT1-compressed image in an RGB image format.  
[RGBA_S3TC_DXT1_Format](#): A DXT1-compressed image in an RGB image format
with a simple on/off alpha value.  
[RGBA_S3TC_DXT3_Format](#): A DXT3-compressed image in an RGBA image format.
Compared to a 32-bit RGBA texture, it offers 4:1 compression.  
[RGBA_S3TC_DXT5_Format](#): A DXT5-compressed image in an RGBA image format.
It also provides a 4:1 compression, but differs to the DXT3 compression in how
the alpha compression is done.  

## PVRTC Compressed Texture Formats

  
```ts  
THREE.RGB_PVRTC_4BPPV1_Format THREE.RGB_PVRTC_2BPPV1_Format
THREE.RGBA_PVRTC_4BPPV1_Format THREE.RGBA_PVRTC_2BPPV1_Format  
```  

For use with a [CompressedTexture](en\textures\CompressedTexture.html)'s
[format](#) property, these require support for the <a
href="https://www.khronos.org/registry/webgl/extensions/WEBGL_compressed_texture_pvrtc/">WEBGL_compressed_texture_pvrtc</a>
extension.  
PVRTC is typically only available on mobile devices with PowerVR chipsets,
which are mainly Apple devices.  
  
There are four <a href="https://en.wikipedia.org/wiki/PVRTC">PVRTC</a> formats
available via this extension. These are:  
[RGB_PVRTC_4BPPV1_Format](#): RGB compression in 4-bit mode. One block for
each 4×4 pixels.  
[RGB_PVRTC_2BPPV1_Format](#): RGB compression in 2-bit mode. One block for
each 8×4 pixels.  
[RGBA_PVRTC_4BPPV1_Format](#): RGBA compression in 4-bit mode. One block for
each 4×4 pixels.  
[RGBA_PVRTC_2BPPV1_Format](#): RGBA compression in 2-bit mode. One block for
each 8×4 pixels.  

## ETC Compressed Texture Format

  
```ts  
THREE.RGB_ETC1_Format THREE.RGB_ETC2_Format THREE.RGBA_ETC2_EAC_Format  
```  

For use with a [CompressedTexture](en\textures\CompressedTexture.html)'s
[format](#) property, these require support for the <a
href="https://www.khronos.org/registry/webgl/extensions/WEBGL_compressed_texture_etc1/">WEBGL_compressed_texture_etc1</a>
(ETC1) or <a
href="https://www.khronos.org/registry/webgl/extensions/WEBGL_compressed_texture_etc/">WEBGL_compressed_texture_etc</a>
(ETC2) extensions.  
  

## ASTC Compressed Texture Format

  
```ts  
THREE.RGBA_ASTC_4x4_Format THREE.RGBA_ASTC_5x4_Format
THREE.RGBA_ASTC_5x5_Format THREE.RGBA_ASTC_6x5_Format
THREE.RGBA_ASTC_6x6_Format THREE.RGBA_ASTC_8x5_Format
THREE.RGBA_ASTC_8x6_Format THREE.RGBA_ASTC_8x8_Format
THREE.RGBA_ASTC_10x5_Format THREE.RGBA_ASTC_10x6_Format
THREE.RGBA_ASTC_10x8_Format THREE.RGBA_ASTC_10x10_Format
THREE.RGBA_ASTC_12x10_Format THREE.RGBA_ASTC_12x12_Format  
```  

For use with a [CompressedTexture](en\textures\CompressedTexture.html)'s
[format](#) property, these require support for the <a
href="https://www.khronos.org/registry/webgl/extensions/WEBGL_compressed_texture_astc/">WEBGL_compressed_texture_astc</a>
extension.  
  

## BPTC Compressed Texture Format

  
```ts  
THREE.RGBA_BPTC_Format  
```  

For use with a [CompressedTexture](en\textures\CompressedTexture.html)'s
[format](#) property, these require support for the <a
href="https://www.khronos.org/registry/webgl/extensions/EXT_texture_compression_bptc/">EXT_texture_compression_bptc</a>
extension.  
  

## Texture Comparison functions

  
```ts  
THREE.NeverCompare THREE.LessCompare THREE.EqualCompare THREE.LessEqualCompare
THREE.GreaterCompare THREE.NotEqualCompare THREE.GreaterEqualCompare
THREE.AlwaysCompare  
```  

## Internal Formats

  
```ts  
'ALPHA' 'RGB' 'RGBA' 'LUMINANCE' 'LUMINANCE_ALPHA' 'RED_INTEGER' 'R8'
'R8_SNORM' 'R8I' 'R8UI' 'R16I' 'R16UI' 'R16F' 'R32I' 'R32UI' 'R32F' 'RG8'
'RG8_SNORM' 'RG8I' 'RG8UI' 'RG16I' 'RG16UI' 'RG16F' 'RG32I' 'RG32UI' 'RG32F'
'RGB565' 'RGB8' 'RGB8_SNORM' 'RGB8I' 'RGB8UI' 'RGB16I' 'RGB16UI' 'RGB16F'
'RGB32I' 'RGB32UI' 'RGB32F' 'RGB9_E5' 'SRGB8' 'R11F_G11F_B10F' 'RGBA4' 'RGBA8'
'RGBA8_SNORM' 'RGBA8I' 'RGBA8UI' 'RGBA16I' 'RGBA16UI' 'RGBA16F' 'RGBA32I'
'RGBA32UI' 'RGBA32F' 'RGB5_A1' 'RGB10_A2' 'RGB10_A2UI' 'SRGB8_ALPHA8'
'DEPTH_COMPONENT16' 'DEPTH_COMPONENT24' 'DEPTH_COMPONENT32F'
'DEPTH24_STENCIL8' 'DEPTH32F_STENCIL8'  
```  

Heads up: changing the internal format of a texture will only affect the
texture when using a WebGL 2 rendering context.  
  
For use with a texture's [internalFormat](#) property, these define how
elements of a texture, or `texels`, are stored on the GPU.  
  
[R8](#) stores the red component on 8 bits.  
  
[R8_SNORM](#) stores the red component on 8 bits. The component is stored as
normalized.  
  
[R8I](#) stores the red component on 8 bits. The component is stored as an
integer.  
  
[R8UI](#) stores the red component on 8 bits. The component is stored as an
unsigned integer.  
  
[R16I](#) stores the red component on 16 bits. The component is stored as an
integer.  
  
[R16UI](#) stores the red component on 16 bits. The component is stored as an
unsigned integer.  
  
[R16F](#) stores the red component on 16 bits. The component is stored as
floating point.  
  
[R32I](#) stores the red component on 32 bits. The component is stored as an
integer.  
  
[R32UI](#) stores the red component on 32 bits. The component is stored as an
unsigned integer.  
  
[R32F](#) stores the red component on 32 bits. The component is stored as
floating point.  
  
[RG8](#) stores the red and green components on 8 bits each.  
  
[RG8_SNORM](#) stores the red and green components on 8 bits each. Every
component is stored as normalized.  
  
[RG8I](#) stores the red and green components on 8 bits each. Every component
is stored as an integer.  
  
[RG8UI](#) stores the red and green components on 8 bits each. Every component
is stored as an unsigned integer.  
  
[RG16I](#) stores the red and green components on 16 bits each. Every
component is stored as an integer.  
  
[RG16UI](#) stores the red and green components on 16 bits each. Every
component is stored as an unsigned integer.  
  
[RG16F](#) stores the red and green components on 16 bits each. Every
component is stored as floating point.  
  
[RG32I](#) stores the red and green components on 32 bits each. Every
component is stored as an integer.  
  
[RG32UI](#) stores the red and green components on 32 bits. Every component is
stored as an unsigned integer.  
  
[RG32F](#) stores the red and green components on 32 bits. Every component is
stored as floating point.  
  
[RGB8](#) stores the red, green, and blue components on 8 bits each.
[RGB8_SNORM](#) stores the red, green, and blue components on 8 bits each.
Every component is stored as normalized.  
  
[RGB8I](#) stores the red, green, and blue components on 8 bits each. Every
component is stored as an integer.  
  
[RGB8UI](#) stores the red, green, and blue components on 8 bits each. Every
component is stored as an unsigned integer.  
  
[RGB16I](#) stores the red, green, and blue components on 16 bits each. Every
component is stored as an integer.  
  
[RGB16UI](#) stores the red, green, and blue components on 16 bits each. Every
component is stored as an unsigned integer.  
  
[RGB16F](#) stores the red, green, and blue components on 16 bits each. Every
component is stored as floating point  
  
[RGB32I](#) stores the red, green, and blue components on 32 bits each. Every
component is stored as an integer.  
  
[RGB32UI](#) stores the red, green, and blue components on 32 bits each. Every
component is stored as an unsigned integer.  
  
[RGB32F](#) stores the red, green, and blue components on 32 bits each. Every
component is stored as floating point  
  
[R11F_G11F_B10F](#) stores the red, green, and blue components respectively on
11 bits, 11 bits, and 10bits. Every component is stored as floating point.  
  
[RGB565](#) stores the red, green, and blue components respectively on 5 bits,
6 bits, and 5 bits.  
  
[RGB9_E5](#) stores the red, green, and blue components on 9 bits each.  
  
[RGBA8](#) stores the red, green, blue, and alpha components on 8 bits each.  
  
[RGBA8_SNORM](#) stores the red, green, blue, and alpha components on 8 bits.
Every component is stored as normalized.  
  
[RGBA8I](#) stores the red, green, blue, and alpha components on 8 bits each.
Every component is stored as an integer.  
  
[RGBA8UI](#) stores the red, green, blue, and alpha components on 8 bits.
Every component is stored as an unsigned integer.  
  
[RGBA16I](#) stores the red, green, blue, and alpha components on 16 bits.
Every component is stored as an integer.  
  
[RGBA16UI](#) stores the red, green, blue, and alpha components on 16 bits.
Every component is stored as an unsigned integer.  
  
[RGBA16F](#) stores the red, green, blue, and alpha components on 16 bits.
Every component is stored as floating point.  
  
[RGBA32I](#) stores the red, green, blue, and alpha components on 32 bits.
Every component is stored as an integer.  
  
[RGBA32UI](#) stores the red, green, blue, and alpha components on 32 bits.
Every component is stored as an unsigned integer.  
  
[RGBA32F](#) stores the red, green, blue, and alpha components on 32 bits.
Every component is stored as floating point.  
  
[RGB5_A1](#) stores the red, green, blue, and alpha components respectively on
5 bits, 5 bits, 5 bits, and 1 bit.  
  
[RGB10_A2](#) stores the red, green, blue, and alpha components respectively
on 10 bits, 10 bits, 10 bits and 2 bits.  
  
[RGB10_A2UI](#) stores the red, green, blue, and alpha components respectively
on 10 bits, 10 bits, 10 bits and 2 bits. Every component is stored as an
unsigned integer.  
  
[SRGB8](#) stores the red, green, and blue components on 8 bits each.  
  
[SRGB8_ALPHA8](#) stores the red, green, blue, and alpha components on 8 bits
each.  
  
[DEPTH_COMPONENT16](#) stores the depth component on 16bits.  
  
[DEPTH_COMPONENT24](#) stores the depth component on 24bits.  
  
[DEPTH_COMPONENT32F](#) stores the depth component on 32bits. The component is
stored as floating point.  
  
[DEPTH24_STENCIL8](#) stores the depth, and stencil components respectively on
24 bits and 8 bits. The stencil component is stored as an unsigned integer.  
  
[DEPTH32F_STENCIL8](#) stores the depth, and stencil components respectively
on 32 bits and 8 bits. The depth component is stored as floating point, and
the stencil component as an unsigned integer.  
  
Note that the texture must have the correct [type](#) set, as well as the
correct [format](#). See <a
href="https://developer.mozilla.org/en/docs/Web/API/WebGLRenderingContext/texImage2D">WebGLRenderingContext.texImage2D</a>,
and <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGL2RenderingContext/texImage3D">WebGL2RenderingContext.texImage3D</a>,
for more details regarding the possible combination of [format](#),
[internalFormat](#), and [type](#).  
  
For more in-depth information regarding internal formats, you can also refer
directly to the <a
href="https://www.khronos.org/registry/webgl/specs/latest/2.0/">WebGL2
Specification</a> and to the <a
href="https://www.khronos.org/registry/OpenGL/specs/es/3.0/es_spec_3.0.pdf">OpenGL
ES 3.0 Specification</a>.

## Depth Packing

  
```ts  
THREE.BasicDepthPacking THREE.RGBADepthPacking  
```  

For use with the [depthPacking](#) property of `MeshDepthMaterial`.

## Color Space

  
```ts  
THREE.NoColorSpace = "" THREE.SRGBColorSpace = "srgb"
THREE.LinearSRGBColorSpace = "srgb-linear"  
```  

Used to define the color space of textures (and the output color space of the
renderer).  
  
If the color space type is changed after the texture has already been used by
a material, you will need to set [Material.needsUpdate](#) to `true` to make
the material recompile.  
  

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/constants.js">src/constants.js</a>

