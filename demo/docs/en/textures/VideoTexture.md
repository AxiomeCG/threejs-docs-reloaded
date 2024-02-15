[Texture](en\textures\Texture.html) →

# VideoTexture

Creates a texture for use with a video.

Note: After the initial use of a texture, the video cannot be changed.
Instead, call [.dispose](#)() on the texture and instantiate a new one.

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

### VideoTexture

  
  
```ts  
function VideoTexture( video: Video, mapping: Constant, wrapS: Constant,
wrapT: Constant, magFilter: Constant, minFilter: Constant, format: Constant,
type: Constant, anisotropy: Number ): void;  
```  

[video](#) -- The video element to use as the texture.  
[mapping](#) -- How the image is applied to the object. An object type of
[THREE.UVMapping](en\constants\Textures.html). See [mapping
constants](en\constants\Textures.html) for other choices.  
[wrapS](#) -- The default is
[THREE.ClampToEdgeWrapping](en\constants\Textures.html). See [wrap mode
constants](en\constants\Textures.html) for other choices.  
[wrapT](#) -- The default is
[THREE.ClampToEdgeWrapping](en\constants\Textures.html). See [wrap mode
constants](en\constants\Textures.html) for other choices.  
[magFilter](#) -- How the texture is sampled when a texel covers more than one
pixel. The default is [THREE.LinearFilter](en\constants\Textures.html). See
[magnification filter constants](en\constants\Textures.html) for other
choices.  
[minFilter](#) -- How the texture is sampled when a texel covers less than one
pixel. The default is [THREE.LinearFilter](en\constants\Textures.html). See
[minification filter constants](en\constants\Textures.html) for other choices.  
[format](#) -- The default is [THREE.RGBAFormat](en\constants\Textures.html).
See [format constants](en\constants\Textures.html) for other choices.  
[type](#) -- Default is [THREE.UnsignedByteType](en\constants\Textures.html).
See [type constants](en\constants\Textures.html) for other choices.  
[anisotropy](#) -- The number of samples taken along the axis through the
pixel that has the highest density of texels. By default, this value is `1`. A
higher value gives a less blurry result than a basic mipmap, at the cost of
more texture samples being used. Use [renderer.getMaxAnisotropy](#)() to find
the maximum valid anisotropy value for the GPU; this value is usually a power
of 2.  
  

## Properties

See the base [Texture](en\textures\Texture.html) class for common properties.

### generateMipmaps

  
  
```ts  
generateMipmaps: Boolean;  
```  

Whether to generate mipmaps. `false` by default.

### isVideoTexture

  
  
```ts  
isVideoTexture: Boolean;  
```  

Read-only flag to check if a given object is of type VideoTexture.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

You will not need to set this manually here as it is handled by the
[update](#)() method.

## Methods

See the base [Texture](en\textures\Texture.html) class for common methods.

### update

  
  
```ts  
function update( ): undefined;  
```  

This is called automatically and sets [.needsUpdate](#) to `true` every time a
new frame is available.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/VideoTexture.js">src/textures/VideoTexture.js</a>

