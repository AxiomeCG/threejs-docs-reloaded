# Texture

Create a texture to apply to a surface or as a reflection or refraction map.

Note: After the initial use of a texture, its dimensions, format, and type
cannot be changed. Instead, call [page:.dispose]() on the texture and
instantiate a new one.

## Code Example

  
```ts  
// load a texture, set wrap mode to repeat const texture = new
THREE.TextureLoader().load( "textures/water.jpg" ); texture.wrapS =
THREE.RepeatWrapping; texture.wrapT = THREE.RepeatWrapping;
texture.repeat.set( 4, 4 );  
```  

## Constructor

###  function Texture( ): void;

## Properties

###  Integer id;

Readonly - unique number for this texture instance.

###  Boolean isTexture;

Read-only flag to check if a given object is of type Texture.

###  String uuid;

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
object instance. This gets automatically assigned, so this shouldn't be
edited.

###  String name;

Optional name of the object (doesn't need to be unique). Default is an empty
string.

###  Image image;

An image object, typically created using the [page:TextureLoader.load] method.
This can be any image (e.g., PNG, JPG, GIF, DDS) or video (e.g., MP4, OGG/OGV)
type supported by three.js.  
  
To use video as a texture you need to have a playing HTML5 video element as a
source for your texture image and continuously update this texture as long as
video is playing - the [page:VideoTexture VideoTexture] class handles this
automatically.

###  Array mipmaps;

Array of user-specified mipmaps (optional).

###  number mapping;

How the image is applied to the object. An object type of [page:Textures
THREE.UVMapping] is the default, where the U,V coordinates are used to apply
the map.  
See the [page:Textures texture constants] page for other mapping types.

###  Integer channel;

Lets you select the uv attribute to map the texture to. `0` for `uv`, `1` for
`uv1`, `2` for `uv2` and `3` for `uv3`.

###  number wrapS;

This defines how the texture is wrapped horizontally and corresponds to *U* in
UV mapping.  
The default is [page:Textures THREE.ClampToEdgeWrapping], where the edge is
clamped to the outer edge texels. The other two choices are [page:Textures
THREE.RepeatWrapping] and [page:Textures THREE.MirroredRepeatWrapping]. See
the [page:Textures texture constants] page for details.

###  number wrapT;

This defines how the texture is wrapped vertically and corresponds to *V* in
UV mapping.  
The same choices are available as for number wrapS; .  
  
NOTE: tiling of images in textures only functions if image dimensions are
powers of two (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, ...) in terms
of pixels. Individual dimensions need not be equal, but each must be a power
of two. This is a limitation of WebGL, not three.js.

###  number magFilter;

How the texture is sampled when a texel covers more than one pixel. The
default is [page:Textures THREE.LinearFilter], which takes the four closest
texels and bilinearly interpolates among them. The other option is
[page:Textures THREE.NearestFilter], which uses the value of the closest
texel.  
See the [page:Textures texture constants] page for details.

###  number minFilter;

How the texture is sampled when a texel covers less than one pixel. The
default is [page:Textures THREE.LinearMipmapLinearFilter], which uses
mipmapping and a trilinear filter.  
  
See the [page:Textures texture constants] page for all possible choices.

###  number anisotropy;

The number of samples taken along the axis through the pixel that has the
highest density of texels. By default, this value is `1`. A higher value gives
a less blurry result than a basic mipmap, at the cost of more texture samples
being used. Use [page:WebGLRenderer.capabilities
renderer.capabilities.getMaxAnisotropy]() to find the maximum valid anisotropy
value for the GPU; this value is usually a power of 2.

###  number format;

The default is [page:Textures THREE.RGBAFormat].  
  
See the [page:Textures texture constants] page for details of other formats.

###  String internalFormat;

The default value is obtained using a combination of [page:Texture.format
.format] and [page:Texture.type .type].  
The GPU format allows the developer to specify how the data is going to be
stored on the GPU.  
  
See the [page:Textures texture constants] page for details regarding all
supported internal formats.

###  number type;

This must correspond to the [page:Texture.format .format]. The default is
[page:Textures THREE.UnsignedByteType], which will be used for most texture
formats.  
  
See the [page:Textures texture constants] page for details of other formats.

###  Vector2 offset;

How much a single repetition of the texture is offset from the beginning, in
each direction U and V. Typical range is `0.0` to `1.0`.

###  Vector2 repeat;

How many times the texture is repeated across the surface, in each direction U
and V. If repeat is set greater than 1 in either direction, the corresponding
Wrap parameter should also be set to [page:Textures THREE.RepeatWrapping] or
[page:Textures THREE.MirroredRepeatWrapping] to achieve the desired tiling
effect.

###  number rotation;

How much the texture is rotated around the center point, in radians. Positive
values are counter-clockwise. Default is `0`.

###  Vector2 center;

The point around which rotation occurs. A value of (0.5, 0.5) corresponds to
the center of the texture. Default is (0, 0), the lower left.

###  Boolean matrixAutoUpdate;

Whether to update the texture's uv-transform [page:Texture.matrix .matrix]
from the texture properties [page:Texture.offset .offset],
[page:Texture.repeat .repeat], [page:Texture.rotation .rotation], and
[page:Texture.center .center]. True by default. Set this to false if you are
specifying the uv-transform matrix directly.

###  Matrix3 matrix;

The uv-transform matrix for the texture. Updated by the renderer from the
texture properties [page:Texture.offset .offset], [page:Texture.repeat
.repeat], [page:Texture.rotation .rotation], and [page:Texture.center .center]
when the texture's [page:Texture.matrixAutoUpdate .matrixAutoUpdate] property
is true. When [page:Texture.matrixAutoUpdate .matrixAutoUpdate] property is
false, this matrix may be set manually. Default is the identity matrix.

###  Boolean generateMipmaps;

Whether to generate mipmaps (if possible) for a texture. True by default. Set
this to false if you are creating mipmaps manually.

###  Boolean premultiplyAlpha;

If set to `true`, the alpha channel, if present, is multiplied into the color
channels when the texture is uploaded to the GPU. Default is `false`.  
  
Note that this property has no effect for
[link:https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap
ImageBitmap]. You need to configure on bitmap creation instead. See
[page:ImageBitmapLoader].

###  Boolean flipY;

If set to `true`, the texture is flipped along the vertical axis when uploaded
to the GPU. Default is `true`.  
  
Note that this property has no effect for
[link:https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap
ImageBitmap]. You need to configure on bitmap creation instead. See
[page:ImageBitmapLoader].

###  number unpackAlignment;

4 by default. Specifies the alignment requirements for the start of each pixel
row in memory. The allowable values are 1 (byte-alignment), 2 (rows aligned to
even-numbered bytes), 4 (word-alignment), and 8 (rows start on double-word
boundaries). See
[link:http://www.khronos.org/opengles/sdk/docs/man/xhtml/glPixelStorei.xml
glPixelStorei] for more information.

###  string colorSpace;

[page:Textures THREE.NoColorSpace] is the default. Textures containing color
data should be annotated with [page:Textures THREE.SRGBColorSpace] or
[page:Textures THREE.LinearSRGBColorSpace].

###  Integer version;

This starts at `0` and counts how many times [page:Texture.needsUpdate
.needsUpdate] is set to `true`.

###  Function onUpdate;

A callback function, called when the texture is updated (e.g., when
needsUpdate has been set to true and then the texture is used).

###  Boolean needsUpdate;

Set this to `true` to trigger an update next time the texture is used.
Particularly important for setting the wrap mode.

###  Object userData;

An object that can be used to store custom data about the texture. It should
not hold references to functions as these will not be cloned.

###  Source source;

The data definition of a texture. A reference to the data source can be shared
across textures. This is often useful in context of spritesheets where
multiple textures render the same data but with different texture
transformations.

## Methods

[page:EventDispatcher EventDispatcher] methods are available on this class.

###  function updateMatrix( ): undefined;

Update the texture's uv-transform [page:Texture.matrix .matrix] from the
texture properties [page:Texture.offset .offset], [page:Texture.repeat
.repeat], [page:Texture.rotation .rotation], and [page:Texture.center
.center].

###  function clone( ): Texture;

Make copy of the texture. Note this is not a "deep copy", the image is shared.
Besides, cloning a texture does not automatically mark it for a texture
upload. You have to set [page:Texture.needsUpdate .needsUpdate] to true as
soon as its image property (the data source) is fully loaded or ready.

###  function toJSON( meta: Object ): Object;

meta -- optional object containing metadata.  
Convert the texture to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function transformUv( uv: Vector2 ): Vector2;

Transform the uv based on the value of this texture's [page:Texture.offset
.offset], [page:Texture.repeat .repeat], [page:Texture.wrapS .wrapS],
[page:Texture.wrapT .wrapT] and [page:Texture.flipY .flipY] properties.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

