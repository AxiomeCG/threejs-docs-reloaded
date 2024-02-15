[Texture](en\textures\Texture.html) →

# DepthTexture

This class can be used to automatically save the depth information of a
rendering into a texture. When using a WebGL 1 rendering context, DepthTexture
requires support for the <a
href="https://www.khronos.org/registry/webgl/extensions/WEBGL_depth_texture/">WEBGL_depth_texture</a>
extension.

## Examples

[example:webgl_depth_texture depth / texture]

## Constructor

### DepthTexture

  
  
```ts  
function DepthTexture( width: Number, height: Number, type: Constant, mapping:
Constant, wrapS: Constant, wrapT: Constant, magFilter: Constant, minFilter:
Constant, anisotropy: Number, format: Constant ): void;  
```  

[width](#) -- width of the texture.  
[height](#) -- height of the texture.  
[type](#) -- Default is [THREE.UnsignedIntType](en\constants\Textures.html)
when using [DepthFormat](en\constants\Textures.html) and
[THREE.UnsignedInt248Type](en\constants\Textures.html) when using
[DepthStencilFormat](en\constants\Textures.html). See [type
constants](en\constants\Textures.html) for other choices.  
[mapping](#) -- See [mapping mode constants](en\constants\Textures.html) for
details.  
[wrapS](#) -- The default is
[THREE.ClampToEdgeWrapping](en\constants\Textures.html). See [wrap mode
constants](en\constants\Textures.html) for other choices.  
[wrapT](#) -- The default is
[THREE.ClampToEdgeWrapping](en\constants\Textures.html). See [wrap mode
constants](en\constants\Textures.html) for other choices.  
[magFilter](#) -- How the texture is sampled when a texel covers more than one
pixel. The default is [THREE.NearestFilter](en\constants\Textures.html). See
[magnification filter constants](en\constants\Textures.html) for other
choices.  
[minFilter](#) -- How the texture is sampled when a texel covers less than one
pixel. The default is [THREE.NearestFilter](en\constants\Textures.html). See
[minification filter constants](en\constants\Textures.html) for other choices.  
[anisotropy](#) -- The number of samples taken along the axis through the
pixel that has the highest density of texels. By default, this value is `1`. A
higher value gives a less blurry result than a basic mipmap, at the cost of
more texture samples being used. Use [renderer.getMaxAnisotropy](#)() to find
the maximum valid anisotropy value for the GPU; this value is usually a power
of 2.  
[format](#) -- must be either [DepthFormat](en\constants\Textures.html)
(default) or [DepthStencilFormat](en\constants\Textures.html). See [format
constants](en\constants\Textures.html) for details.  

## Properties

See the base [Texture](en\textures\Texture.html) class for common properties -
the following are also part of the texture class, but have different defaults
here.

### [format](#)

Either [DepthFormat](en\constants\Textures.html) (default) or
[DepthStencilFormat](en\constants\Textures.html). See [format
constants](en\constants\Textures.html) for details.  

### [type](#)

Default is [THREE.UnsignedIntType](en\constants\Textures.html) when using
[DepthFormat](en\constants\Textures.html) and
[THREE.UnsignedInt248Type](en\constants\Textures.html) when using
[DepthStencilFormat](en\constants\Textures.html). See [format
constants](en\constants\Textures.html) for details.  

### [magFilter](#)

How the texture is sampled when a texel covers more than one pixel. The
default is [THREE.NearestFilter](en\constants\Textures.html). See
[magnification filter constants](en\constants\Textures.html) for other
choices.

### [minFilter](#)

How the texture is sampled when a texel covers less than one pixel. The
default is [THREE.NearestFilter](en\constants\Textures.html). See
[magnification filter constants](en\constants\Textures.html) for other
choices.

### [flipY](#)

Depth textures do not need to be flipped so this is `false` by default.

### [.generateMipmaps](#)

Depth textures do not use mipmaps.

### isDepthTexture

  
  
```ts  
isDepthTexture: Boolean;  
```  

Read-only flag to check if a given object is of type DepthTexture.

### compareFunction

  
  
```ts  
compareFunction: number;  
```  

This is used to define the comparison function used when comparing texels in
the depth texture to the value in the depth buffer. Default is `null` which
means comparison is disabled.  
  
See the [texture constants](en\constants\Textures.html) page for details of
other functions.

## Methods

See the base [Texture](en\textures\Texture.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/textures/DepthTexture.js">src/textures/DepthTexture.js</a>

