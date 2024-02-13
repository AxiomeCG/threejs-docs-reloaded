# PMREMGenerator

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

texture size| minimum roughness  
---|---  
16| 0.21  
32| 0.15  
64| 0.11  
128| 0.076  
256| 0.054  
512| 0.038  
1024| 0.027  
  
## Constructor

###  function PMREMGenerator( renderer: WebGLRenderer ): void;

This constructor creates a new PMREMGenerator.

## Methods

###  function fromScene( scene: Scene, sigma: Number, near: Number, far:
Number ): WebGLRenderTarget;

[page:Scene scene] - The given scene.  
[page:Number sigma] - (optional) Specifies a blur radius in radians to be
applied to the scene before PMREM generation. Default is `0`.  
[page:Number near] - (optional) The near plane value. Default is `0.1`.  
[page:Number far] - (optional) The far plane value. Default is `100`.  
  
Generates a PMREM from a supplied Scene, which can be faster than using an
image if networking bandwidth is low. Optional near and far planes ensure the
scene is rendered in its entirety (the cubeCamera is placed at the origin).

###  function fromEquirectangular( equirectangular: Texture ):
WebGLRenderTarget;

[page:Texture equirectangular] - The equirectangular texture.  
  
Generates a PMREM from an equirectangular texture.

###  function fromCubemap( cubemap: CubeTexture ): WebGLRenderTarget;

[page:CubeTexture cubemap] - The cubemap texture.  
  
Generates a PMREM from an cubemap texture.

###  function compileCubemapShader( ): undefined;

Pre-compiles the cubemap shader. You can get faster start-up by invoking this
method during your texture's network fetch for increased concurrency.

###  function compileEquirectangularShader( ): undefined;

Pre-compiles the equirectangular shader. You can get faster start-up by
invoking this method during your texture's network fetch for increased
concurrency.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

