# Texture

Create a texture to apply to a surface or as a reflection or refraction map.

Note: After the initial use of a texture, its dimensions, format, and type
cannot be changed. Instead, call [.dispose](#)() on the texture and
instantiate a new one.

## Code Example

  
```ts  
// load a texture, set wrap mode to repeat const texture = new
THREE.TextureLoader().load( "textures/water.jpg" ); texture.wrapS =
THREE.RepeatWrapping; texture.wrapT = THREE.RepeatWrapping;
texture.repeat.set( 4, 4 );  
```  

## Constructor

### Texture

  
  
```ts  
function Texture( ): void;  
```  

## Properties

### id

  
  
```ts  
id: Integer;  
```  

Readonly - unique number for this texture instance.

### isTexture

  
  
```ts  
isTexture: Boolean;  
```  

Read-only flag to check if a given object is of type Texture.

### uuid

  
  
```ts  
uuid: String;  
```  

<a href="http://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a>
of this object instance. This gets automatically assigned, so this shouldn't
be edited.

### name

  
  
```ts  
name: String;  
```  

Optional name of the object (doesn't need to be unique). Default is an empty
string.

### image

  
  
```ts  
image: Image;  
```  

An image object, typically created using the [TextureLoader.load](#) method.
This can be any image (e.g., PNG, JPG, GIF, DDS) or video (e.g., MP4, OGG/OGV)
type supported by three.js.  
  
To use video as a texture you need to have a playing HTML5 video element as a
source for your texture image and continuously update this texture as long as
video is playing - the [VideoTexture](en\textures\VideoTexture.html) class
handles this automatically.

### mipmaps

  
  
```ts  
mipmaps: Array;  
```  

Array of user-specified mipmaps (optional).

### mapping

  
  
```ts  
mapping: number;  
```  

How the image is applied to the object. An object type of
[THREE.UVMapping](en\constants\Textures.html) is the default, where the U,V
coordinates are used to apply the map.  
See the [texture constants](en\constants\Textures.html) page for other mapping
types.

### channel

  
  
```ts  
channel: Integer;  
```  

Lets you select the uv attribute to map the texture to. `0` for `uv`, `1` for
`uv1`, `2` for `uv2` and `3` for `uv3`.

### wrapS

  
  
```ts  
wrapS: number;  
```  

This defines how the texture is wrapped horizontally and corresponds to *U* in
UV mapping.  
The default is [THREE.ClampToEdgeWrapping](en\constants\Textures.html), where
the edge is clamped to the outer edge texels. The other two choices are
[THREE.RepeatWrapping](en\constants\Textures.html) and
[THREE.MirroredRepeatWrapping](en\constants\Textures.html). See the [texture
constants](en\constants\Textures.html) page for details.

### wrapT

  
  
```ts  
wrapT: number;  
```  

This defines how the texture is wrapped vertically and corresponds to *V* in
UV mapping.  
The same choices are available as for [property:number wrapS].  
  
NOTE: tiling of images in textures only functions if image dimensions are
powers of two (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, ...) in terms
of pixels. Individual dimensions need not be equal, but each must be a power
of two. This is a limitation of WebGL, not three.js.

### magFilter

  
  
```ts  
magFilter: number;  
```  

How the texture is sampled when a texel covers more than one pixel. The
default is [THREE.LinearFilter](en\constants\Textures.html), which takes the
four closest texels and bilinearly interpolates among them. The other option
is [THREE.NearestFilter](en\constants\Textures.html), which uses the value of
the closest texel.  
See the [texture constants](en\constants\Textures.html) page for details.

### minFilter

  
  
```ts  
minFilter: number;  
```  

How the texture is sampled when a texel covers less than one pixel. The
default is [THREE.LinearMipmapLinearFilter](en\constants\Textures.html), which
uses mipmapping and a trilinear filter.  
  
See the [texture constants](en\constants\Textures.html) page for all possible
choices.

### anisotropy

  
  
```ts  
anisotropy: number;  
```  

The number of samples taken along the axis through the pixel that has the
highest density of texels. By default, this value is `1`. A higher value gives
a less blurry result than a basic mipmap, at the cost of more texture samples
being used. Use [renderer.capabilities.getMaxAnisotropy](#)() to find the
maximum valid anisotropy value for the GPU; this value is usually a power of
2.

### format

  
  
```ts  
format: number;  
```  

The default is [THREE.RGBAFormat](en\constants\Textures.html).  
  
See the [texture constants](en\constants\Textures.html) page for details of
other formats.

### internalFormat

  
  
```ts  
internalFormat: String;  
```  

The default value is obtained using a combination of [.format](#) and
[.type](#).  
The GPU format allows the developer to specify how the data is going to be
stored on the GPU.  
  
See the [texture constants](en\constants\Textures.html) page for details
regarding all supported internal formats.

### type

  
  
```ts  
type: number;  
```  

This must correspond to the [.format](#). The default is
[THREE.UnsignedByteType](en\constants\Textures.html), which will be used for
most texture formats.  
  
See the [texture constants](en\constants\Textures.html) page for details of
other formats.

### offset

  
  
```ts  
offset: Vector2;  
```  

How much a single repetition of the texture is offset from the beginning, in
each direction U and V. Typical range is `0.0` to `1.0`.

### repeat

  
  
```ts  
repeat: Vector2;  
```  

How many times the texture is repeated across the surface, in each direction U
and V. If repeat is set greater than 1 in either direction, the corresponding
Wrap parameter should also be set to
[THREE.RepeatWrapping](en\constants\Textures.html) or
[THREE.MirroredRepeatWrapping](en\constants\Textures.html) to achieve the
desired tiling effect.

### rotation

  
  
```ts  
rotation: number;  
```  

How much the texture is rotated around the center point, in radians. Positive
values are counter-clockwise. Default is `0`.

### center

  
  
```ts  
center: Vector2;  
```  

The point around which rotation occurs. A value of (0.5, 0.5) corresponds to
the center of the texture. Default is (0, 0), the lower left.

### matrixAutoUpdate

  
  
```ts  
matrixAutoUpdate: Boolean;  
```  

Whether to update the texture's uv-transform [.matrix](#) from the texture
properties [.offset](#), [.repeat](#), [.rotation](#), and [.center](#). True
by default. Set this to false if you are specifying the uv-transform matrix
directly.

### matrix

  
  
```ts  
matrix: Matrix3;  
```  

The uv-transform matrix for the texture. Updated by the renderer from the
texture properties [.offset](#), [.repeat](#), [.rotation](#), and
[.center](#) when the texture's [.matrixAutoUpdate](#) property is true. When
[.matrixAutoUpdate](#) property is false, this matrix may be set manually.
Default is the identity matrix.

### generateMipmaps

  
  
```ts  
generateMipmaps: Boolean;  
```  

Whether to generate mipmaps (if possible) for a texture. True by default. Set
this to false if you are creating mipmaps manually.

### premultiplyAlpha

  
  
```ts  
premultiplyAlpha: Boolean;  
```  

If set to `true`, the alpha channel, if present, is multiplied into the color
channels when the texture is uploaded to the GPU. Default is `false`.  
  
Note that this property has no effect for <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/ImageBitmap">ImageBitmap</a>. You need to configure on bitmap
creation instead. See [ImageBitmapLoader](en\loaders\ImageBitmapLoader.html).

### flipY

  
  
```ts  
flipY: Boolean;  
```  

If set to `true`, the texture is flipped along the vertical axis when uploaded
to the GPU. Default is `true`.  
  
Note that this property has no effect for <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/ImageBitmap">ImageBitmap</a>. You need to configure on bitmap
creation instead. See [ImageBitmapLoader](en\loaders\ImageBitmapLoader.html).

### unpackAlignment

  
  
```ts  
unpackAlignment: number;  
```  

4 by default. Specifies the alignment requirements for the start of each pixel
row in memory. The allowable values are 1 (byte-alignment), 2 (rows aligned to
even-numbered bytes), 4 (word-alignment), and 8 (rows start on double-word
boundaries). See <a
href="http://www.khronos.org/opengles/sdk/docs/man/xhtml/glPixelStorei.xml">glPixelStorei</a>
for more information.

### colorSpace

  
  
```ts  
colorSpace: string;  
```  

[THREE.NoColorSpace](en\constants\Textures.html) is the default. Textures
containing color data should be annotated with
[THREE.SRGBColorSpace](en\constants\Textures.html) or
[THREE.LinearSRGBColorSpace](en\constants\Textures.html).

### version

  
  
```ts  
version: Integer;  
```  

This starts at `0` and counts how many times [.needsUpdate](#) is set to
`true`.

### onUpdate

  
  
```ts  
onUpdate: Function;  
```  

A callback function, called when the texture is updated (e.g., when
needsUpdate has been set to true and then the texture is used).

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

Set this to `true` to trigger an update next time the texture is used.
Particularly important for setting the wrap mode.

### userData

  
  
```ts  
userData: Object;  
```  

An object that can be used to store custom data about the texture. It should
not hold references to functions as these will not be cloned.

### source

  
  
```ts  
source: Source;  
```  

The data definition of a texture. A reference to the data source can be shared
across textures. This is often useful in context of spritesheets where
multiple textures render the same data but with different texture
transformations.

## Methods

[EventDispatcher](en\core\EventDispatcher.html) methods are available on this
class.

### updateMatrix

  
  
```ts  
function updateMatrix( ): undefined;  
```  

Update the texture's uv-transform [.matrix](#) from the texture properties
[.offset](#), [.repeat](#), [.rotation](#), and [.center](#).

### clone

  
  
```ts  
function clone( ): Texture;  
```  

Make copy of the texture. Note this is not a "deep copy", the image is shared.
Besides, cloning a texture does not automatically mark it for a texture
upload. You have to set [.needsUpdate](#) to true as soon as its image
property (the data source) is fully loaded or ready.

### toJSON

  
  
```ts  
function toJSON( meta: Object ): Object;  
```  

meta -- optional object containing metadata.  
Convert the texture to three.js <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### transformUv

  
  
```ts  
function transformUv( uv: Vector2 ): Vector2;  
```  

Transform the uv based on the value of this texture's [.offset](#),
[.repeat](#), [.wrapS](#), [.wrapT](#) and [.flipY](#) properties.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/Texture.js">src/textures/Texture.js</a>

