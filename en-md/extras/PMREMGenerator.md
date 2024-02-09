# [name]

This class generates a Prefiltered, Mipmapped Radiance Environment Map (PMREM)
from a cubeMap environment texture. This allows different levels of blur to be
quickly accessed based on material roughness. Unlike a traditional mipmap
chain, it only goes down to the LOD_MIN level (above), and then creates extra
even more filtered 'mips' at the same LOD_MIN resolution, associated with
higher roughness levels. In this way we maintain resolution to smoothly
interpolate diffuse lighting while limiting sampling computation.  
  
Note: The minimum [page:MeshStandardMaterial]'s roughness depends on the size
of the provided texture. If your render has small dimensions or the shiny
parts have a lot of curvature, you may still be able to get away with a
smaller texture size.

texture size | minimum roughness  
---|---  
16 | 0.21  
32 | 0.15  
64 | 0.11  
128 | 0.076  
256 | 0.054  
512 | 0.038  
1024 | 0.027  
  
## Constructor

### [name]( [param:WebGLRenderer renderer] )

This constructor creates a new [name].

## Methods

###  [method:WebGLRenderTarget fromScene]( [param:Scene scene], [param:Number
sigma], [param:Number near], [param:Number far] )

[page:Scene scene] - The given scene.  
[page:Number sigma] - (optional) Specifies a blur radius in radians to be
applied to the scene before PMREM generation. Default is `0`.  
[page:Number near] - (optional) The near plane value. Default is `0.1`.  
[page:Number far] - (optional) The far plane value. Default is `100`.  
  
Generates a PMREM from a supplied Scene, which can be faster than using an
image if networking bandwidth is low. Optional near and far planes ensure the
scene is rendered in its entirety (the cubeCamera is placed at the origin).

###  [method:WebGLRenderTarget fromEquirectangular]( [param:Texture
equirectangular] )

[page:Texture equirectangular] - The equirectangular texture.  
  
Generates a PMREM from an equirectangular texture.

###  [method:WebGLRenderTarget fromCubemap]( [param:CubeTexture cubemap] )

[page:CubeTexture cubemap] - The cubemap texture.  
  
Generates a PMREM from an cubemap texture.

### [method:undefined compileCubemapShader]()

Pre-compiles the cubemap shader. You can get faster start-up by invoking this
method during your texture's network fetch for increased concurrency.

### [method:undefined compileEquirectangularShader]()

Pre-compiles the equirectangular shader. You can get faster start-up by
invoking this method during your texture's network fetch for increased
concurrency.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

