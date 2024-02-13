[page:Texture] →

# VideoTexture

Creates a texture for use with a video.

Note: After the initial use of a texture, the video cannot be changed.
Instead, call [page:.dispose]() on the texture and instantiate a new one.

## Code Example

  
```ts  
// assuming you have created a HTML video element with id="video" const video
= document.getElementById( 'video' ); const texture = new THREE.VideoTexture(
video );  
```  

## Examples

[example:webgl_materials_video materials / video]  
[example:webgl_materials_video_webcam materials / video / webcam]  
[example:webgl_video_kinect video / kinect]  
[example:webgl_video_panorama_equirectangular video / panorama /
equirectangular]  
[example:webxr_vr_video vr / video]

## Constructor

###  function VideoTexture( video: Video, mapping: Constant, wrapS: Constant,
wrapT: Constant, magFilter: Constant, minFilter: Constant, format: Constant,
type: Constant, anisotropy: Number ): void;

[page:Video video] -- The video element to use as the texture.  
[page:Constant mapping] -- How the image is applied to the object. An object
type of [page:Textures THREE.UVMapping]. See [page:Textures mapping constants]
for other choices.  
[page:Constant wrapS] -- The default is [page:Textures
THREE.ClampToEdgeWrapping]. See [page:Textures wrap mode constants] for other
choices.  
[page:Constant wrapT] -- The default is [page:Textures
THREE.ClampToEdgeWrapping]. See [page:Textures wrap mode constants] for other
choices.  
[page:Constant magFilter] -- How the texture is sampled when a texel covers
more than one pixel. The default is [page:Textures THREE.LinearFilter]. See
[page:Textures magnification filter constants] for other choices.  
[page:Constant minFilter] -- How the texture is sampled when a texel covers
less than one pixel. The default is [page:Textures THREE.LinearFilter]. See
[page:Textures minification filter constants] for other choices.  
[page:Constant format] -- The default is [page:Textures THREE.RGBAFormat]. See
[page:Textures format constants] for other choices.  
[page:Constant type] -- Default is [page:Textures THREE.UnsignedByteType]. See
[page:Textures type constants] for other choices.  
[page:Number anisotropy] -- The number of samples taken along the axis through
the pixel that has the highest density of texels. By default, this value is
`1`. A higher value gives a less blurry result than a basic mipmap, at the
cost of more texture samples being used. Use
[page:WebGLrenderer.getMaxAnisotropy renderer.getMaxAnisotropy]() to find the
maximum valid anisotropy value for the GPU; this value is usually a power of
2.  
  

## Properties

See the base [page:Texture Texture] class for common properties.

###  Boolean generateMipmaps;

Whether to generate mipmaps. `false` by default.

###  Boolean isVideoTexture;

Read-only flag to check if a given object is of type VideoTexture.

###  Boolean needsUpdate;

You will not need to set this manually here as it is handled by the
[page:VideoTexture.update update]() method.

## Methods

See the base [page:Texture Texture] class for common methods.

###  function update( ): undefined;

This is called automatically and sets [page:VideoTexture.needsUpdate
.needsUpdate] to `true` every time a new frame is available.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

