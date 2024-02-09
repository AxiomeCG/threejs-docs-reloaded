# [name]

The WebGL renderer displays your beautifully crafted scenes using
[link:https://en.wikipedia.org/wiki/WebGL WebGL].

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) object with properties defining the
renderer's behaviour. The constructor also accepts no parameters at all. In
all cases, it will assume sane defaults when parameters are missing. The
following are valid parameters:  
  
[page:DOMElement canvas] - A [link:https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/canvas canvas] where the renderer draws its output.
This corresponds to the [page:WebGLRenderer.domElement domElement] property
below. If not passed in here, a new canvas element will be created.  
[page:WebGLRenderingContext context] - This can be used to attach the renderer
to an existing [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext RenderingContext]. Default is null.  
[page:String precision] - Shader precision. Can be `"highp"`, `"mediump"` or
`"lowp"`. Defaults to `"highp"` if supported by the device.  
[page:Boolean alpha] - controls the default clear alpha value. When set to
`true`, the value is `0`. Otherwise it's `1`. Default is `false`.  
[page:Boolean premultipliedAlpha] - whether the renderer will assume that
colors have
[link:https://en.wikipedia.org/wiki/Glossary_of_computer_graphics#Premultiplied_alpha
premultiplied alpha]. Default is `true`.  
[page:Boolean antialias] - whether to perform antialiasing. Default is
`false`.  
[page:Boolean stencil] - whether the drawing buffer has a
[link:https://en.wikipedia.org/wiki/Stencil_buffer stencil buffer] of at least
8 bits. Default is `true`.  
[page:Boolean preserveDrawingBuffer] - whether to preserve the buffers until
manually cleared or overwritten. Default is `false`.  
[page:String powerPreference] - Provides a hint to the user agent indicating
what configuration of GPU is suitable for this WebGL context. Can be `"high-
performance"`, `"low-power"` or `"default"`. Default is `"default"`. See
[link:https://www.khronos.org/registry/webgl/specs/latest/1.0/#5.2 WebGL spec]
for details.  
[page:Boolean failIfMajorPerformanceCaveat] - whether the renderer creation
will fail upon low performance is detected. Default is `false`. See
[link:https://www.khronos.org/registry/webgl/specs/latest/1.0/#5.2 WebGL spec]
for details.  
[page:Boolean depth] - whether the drawing buffer has a
[link:https://en.wikipedia.org/wiki/Z-buffering depth buffer] of at least 16
bits. Default is `true`.  
[page:Boolean logarithmicDepthBuffer] - whether to use a logarithmic depth
buffer. It may be necessary to use this if dealing with huge differences in
scale in a single scene. Note that this setting uses gl_FragDepth if available
which disables the
[link:https://www.khronos.org/opengl/wiki/Early_Fragment_Test Early Fragment
Test] optimization and can cause a decrease in performance. Default is
`false`. See the [example:webgl_camera_logarithmicdepthbuffer camera /
logarithmicdepthbuffer] example.

## Properties

### <br/> Boolean autoClear; <br/>

Defines whether the renderer should automatically clear its output before
rendering a frame.

### <br/> Boolean autoClearColor; <br/>

If [page:.autoClear autoClear] is true, defines whether the renderer should
clear the color buffer. Default is `true`.

### <br/> Boolean autoClearDepth; <br/>

If [page:.autoClear autoClear] is true, defines whether the renderer should
clear the depth buffer. Default is `true`.

### <br/> Boolean autoClearStencil; <br/>

If [page:.autoClear autoClear] is true, defines whether the renderer should
clear the stencil buffer. Default is `true`.

### <br/> Object debug; <br/>

\- [page:Boolean checkShaderErrors]: If it is true, defines whether material
shader programs are checked for errors during compilation and linkage process.
It may be useful to disable this check in production for performance gain. It
is strongly recommended to keep these checks enabled during development. If
the shader does not compile and link - it will not work and associated
material will not render. Default is `true`.  
\- [page:Function onShaderError]( gl, program, glVertexShader,
glFragmentShader ): A callback function that can be used for custom error
reporting. The callback receives the WebGL context, an instance of
WebGLProgram as well two instances of WebGLShader representing the vertex and
fragment shader. Assigning a custom function disables the default error
reporting. Default is `null`.

### <br/> Object capabilities; <br/>

An object containing details about the capabilities of the current
[link:https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext
RenderingContext].  
\- [page:Boolean floatFragmentTextures]: whether the context supports the
[link:https://developer.mozilla.org/en-US/docs/Web/API/OES_texture_float
OES_texture_float] extension.  
\- [page:Boolean floatVertexTextures]: `true` if [page:Boolean
floatFragmentTextures] and [page:Boolean vertexTextures] are both true.  
\- [page:Method getMaxAnisotropy](): Returns the maximum available anisotropy.  
\- [page:Method getMaxPrecision](): Returns the maximum available precision
for vertex and fragment shaders.  
\- [page:Boolean isWebGL2]: `true` if the context in use is a
WebGL2RenderingContext object.  
\- [page:Boolean logarithmicDepthBuffer]: `true` if the [page:parameter
logarithmicDepthBuffer] was set to true in the constructor and the context
supports the [link:https://developer.mozilla.org/en-
US/docs/Web/API/EXT_frag_depth EXT_frag_depth] extension.  
\- [page:Integer maxAttributes]: The value of `gl.MAX_VERTEX_ATTRIBS`.  
\- [page:Integer maxCubemapSize]: The value of `gl.MAX_CUBE_MAP_TEXTURE_SIZE`.
Maximum height * width of cube map textures that a shader can use.  
\- [page:Integer maxFragmentUniforms]: The value of
`gl.MAX_FRAGMENT_UNIFORM_VECTORS`. The number of uniforms that can be used by
a fragment shader.  
\- [page:Integer maxSamples]: The value of `gl.MAX_SAMPLES`. Maximum number of
samples in context of Multisample anti-aliasing (MSAA).  
\- [page:Integer maxTextureSize]: The value of `gl.MAX_TEXTURE_SIZE`. Maximum
height * width of a texture that a shader use.  
\- [page:Integer maxTextures]: The value of `gl.MAX_TEXTURE_IMAGE_UNITS`. The
maximum number of textures that can be used by a shader.  
\- [page:Integer maxVaryings]: The value of `gl.MAX_VARYING_VECTORS`. The
number of varying vectors that can used by shaders.  
\- [page:Integer maxVertexTextures]: The value of
`gl.MAX_VERTEX_TEXTURE_IMAGE_UNITS`. The number of textures that can be used
in a vertex shader.  
\- [page:Integer maxVertexUniforms]: The value of
`gl.MAX_VERTEX_UNIFORM_VECTORS`. The maximum number of uniforms that can be
used in a vertex shader.  
\- [page:String precision]: The shader precision currently being used by the
renderer.  
\- [page:Boolean vertexTextures]: `true` if <br/> Integer maxVertexTextures;
<br/> is greater than 0 (i.e. vertex textures can be used).  

### <br/> Array clippingPlanes; <br/>

User-defined clipping planes specified as THREE.Plane objects in world space.
These planes apply globally. Points in space whose dot product with the plane
is negative are cut away. Default is [].

### <br/> DOMElement domElement; <br/>

A [link:https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas
canvas] where the renderer draws its output.  
This is automatically created by the renderer in the constructor (if not
provided already); you just need to add it to your page like so:  
  
```ts  
document.body.appendChild( renderer.domElement );  
```  

### <br/> Object extensions; <br/>

\- [page:Object get]( [param:String extensionName] ): Used to check whether
various extensions are supported and returns an object with details of the
extension if available. This method can check for the following extensions:  

  * `WEBGL_depth_texture`
  * `EXT_texture_filter_anisotropic`
  * `WEBGL_compressed_texture_s3tc`
  * `WEBGL_compressed_texture_pvrtc`
  * `WEBGL_compressed_texture_etc1`

### <br/> string outputColorSpace; <br/>

Defines the output color space of the renderer. Default is [page:Textures
THREE.SRGBColorSpace].

If a render target has been set using [page:WebGLRenderer.setRenderTarget
.setRenderTarget] then renderTarget.texture.colorSpace will be used instead.

See the [page:Textures texture constants] page for details of other formats.

### <br/> Object info; <br/>

An object with a series of statistical information about the graphics board
memory and the rendering process. Useful for debugging or just for the sake of
curiosity. The object contains the following fields:

  * memory: 
    * geometries
    * textures
  * render: 
    * calls
    * triangles
    * points
    * lines
    * frame
  * programs

By default these data are reset at each render call but when having multiple
render passes per frame (e.g. when using post processing) it can be preferred
to reset with a custom pattern. First, set `autoReset` to `false`.  
```ts renderer.info.autoReset = false; ```  
Call `reset()` whenever you have finished to render a single frame.  
```ts renderer.info.reset(); ```  

### <br/> Boolean localClippingEnabled; <br/>

Defines whether the renderer respects object-level clipping planes. Default is
`false`.

### <br/> Boolean useLegacyLights; <br/>

Whether to use the legacy lighting mode or not. Default is `true`.

### <br/> Object properties; <br/>

Used internally by the renderer to keep track of various sub object
properties.

### <br/> WebGLRenderLists renderLists; <br/>

Used internally to handle ordering of scene object rendering.

### <br/> WebGLShadowMap shadowMap; <br/>

This contains the reference to the shadow map, if used.  
\- [page:Boolean enabled]: If set, use shadow maps in the scene. Default is
`false`.  
\- [page:Boolean autoUpdate]: Enables automatic updates to the shadows in the
scene. Default is `true`.  
If you do not require dynamic lighting / shadows, you may set this to `false`
when the renderer is instantiated.  
\- [page:Boolean needsUpdate]: When set to `true`, shadow maps in the scene
will be updated in the next `render` call. Default is `false`.  
If you have disabled automatic updates to shadow maps (`shadowMap.autoUpdate =
false`), you will need to set this to `true` and then make a render call to
update the shadows in your scene.  
\- [page:Integer type]: Defines shadow map type (unfiltered, percentage close
filtering, percentage close filtering with bilinear filtering in shader).
Options are:

  * THREE.BasicShadowMap
  * THREE.PCFShadowMap (default)
  * THREE.PCFSoftShadowMap
  * THREE.VSMShadowMap

See [page:Renderer Renderer constants] for details.  

### <br/> Boolean sortObjects; <br/>

Defines whether the renderer should sort objects. Default is `true`.  
  
Note: Sorting is used to attempt to properly render objects that have some
degree of transparency. By definition, sorting objects may not work in all
cases. Depending on the needs of application, it may be necessary to turn off
sorting and use other methods to deal with transparency rendering e.g.
manually determining each object's rendering order.

### <br/> Object state; <br/>

Contains functions for setting various properties of the
[page:WebGLRenderer.context] state.

### <br/> Constant toneMapping; <br/>

Default is [page:Renderer NoToneMapping]. See the [page:Renderer Renderer
constants] for other choices.

### <br/> Number toneMappingExposure; <br/>

Exposure level of tone mapping. Default is `1`.

### <br/> WebXRManager xr; <br/>

Provides access to the WebXR related [page:WebXRManager interface] of the
renderer.

## Methods

###  [method:undefined clear]( [param:Boolean color], [param:Boolean depth],
[param:Boolean stencil] )

Tells the renderer to clear its color, depth or stencil drawing buffer(s).
This method initializes the color buffer to the current clear color value.  
Arguments default to `true`.

### [method:undefined clearColor]( )

Clear the color buffer. Equivalent to calling [page:WebGLRenderer.clear
.clear]( true, false, false ).

### [method:undefined clearDepth]( )

Clear the depth buffer. Equivalent to calling [page:WebGLRenderer.clear
.clear]( false, true, false ).

### [method:undefined clearStencil]( )

Clear the stencil buffers. Equivalent to calling [page:WebGLRenderer.clear
.clear]( false, false, true ).

###  [method:undefined compile]( [param:Object3D scene], [param:Camera camera]
)

Compiles all materials in the scene with the camera. This is useful to
precompile shaders before the first rendering.

###  [method:undefined copyFramebufferToTexture]( [param:Vector2 position],
[param:FramebufferTexture texture], [param:Number level] )

Copies pixels from the current WebGLFramebuffer into a 2D texture. Enables
access to [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/copyTexImage2D
WebGLRenderingContext.copyTexImage2D].

###  [method:undefined copyTextureToTexture]( [param:Vector2 position],
[param:Texture srcTexture], [param:Texture dstTexture], [param:Number level] )

Copies all pixels of a texture to an existing texture starting from the given
position. Enables access to [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/texSubImage2D
WebGLRenderingContext.texSubImage2D].

###  [method:undefined copyTextureToTexture3D]( [param:Box3 sourceBox],
[param:Vector3 position], [param:Texture srcTexture], [param:Texture
dstTexture], [param:Number level] )

Copies the pixels of a texture in the bounds '[page:Box3 sourceBox]' in the
destination texture starting from the given position. Enables access to
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGL2RenderingContext/texSubImage3D
WebGL2RenderingContext.texSubImage3D].

### [method:undefined dispose]( )

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### [method:undefined forceContextLoss]()

Simulate loss of the WebGL context. This requires support for the
[link:https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_lose_context
WEBGL_lose_context] extensions.

### [method:undefined forceContextRestore]( )

Simulate restore of the WebGL context. This requires support for the
[link:https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_lose_context
WEBGL_lose_context] extensions.

### [method:Float getClearAlpha]()

Returns a [page:Float float] with the current clear alpha. Ranges from `0` to
`1`.

### [method:Color getClearColor]( [param:Color target] )

Returns a [page:Color THREE.Color] instance with the current clear color.

### [method:WebGL2RenderingContext getContext]()

Return the current WebGL context.

### [method:WebGLContextAttributes getContextAttributes]()

Returns an object that describes the attributes set on the WebGL context when
it was created.

### [method:Integer getActiveCubeFace]()

Returns the current active cube face.

### [method:Integer getActiveMipmapLevel]()

Returns the current active mipmap level.

### [method:RenderTarget getRenderTarget]()

Returns the current [page:RenderTarget RenderTarget] if there are; returns
`null` otherwise.

### [method:Vector4 getCurrentViewport]( [param:Vector4 target] )

[page:Vector4 target] — the result will be copied into this Vector4.  
  
Returns the current viewport.

### [method:Vector2 getDrawingBufferSize]( [param:Vector2 target] )

[page:Vector2 target] — the result will be copied into this Vector2.  
  
Returns the width and height of the renderer's drawing buffer, in pixels.

### [method:number getPixelRatio]()

Returns current device pixel ratio used.

### [method:Vector4 getScissor]( [param:Vector4 target] )

[page:Vector4 target] — the result will be copied into this Vector4.  
  
Returns the scissor region.

### [method:Boolean getScissorTest]()

Returns `true` if scissor test is enabled; returns `false` otherwise.

### [method:Vector2 getSize]( [param:Vector2 target] )

[page:Vector2 target] — the result will be copied into this Vector2.  
  
Returns the width and height of the renderer's output canvas, in pixels.

### [method:Vector4 getViewport]( [param:Vector4 target] )

[page:Vector4 target] — the result will be copied into this Vector4.  
  
Returns the viewport.

### [method:undefined initTexture]( [param:Texture texture] )

Initializes the given texture. Useful for preloading a texture rather than
waiting until first render (which can cause noticeable lags due to decode and
GPU upload overhead).

### [method:undefined resetGLState]( )

Reset the GL state to default. Called internally if the WebGL context is lost.

###  [method:undefined readRenderTargetPixels]( [param:WebGLRenderTarget
renderTarget], [param:Float x], [param:Float y], [param:Float width],
[param:Float height], [param:TypedArray buffer], [param:Integer
activeCubeFaceIndex] )

buffer - Uint8Array is the only destination type supported in all cases, other
types are renderTarget and platform dependent. See
[link:https://www.khronos.org/registry/webgl/specs/latest/1.0/#5.14.12 WebGL
spec] for details.

Reads the pixel data from the renderTarget into the buffer you pass in. This
is a wrapper around [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/readPixels
WebGLRenderingContext.readPixels]().

See the [example:webgl_interactive_cubes_gpu interactive / cubes / gpu]
example.

For reading out a [page:WebGLCubeRenderTarget WebGLCubeRenderTarget] use the
optional parameter activeCubeFaceIndex to determine which face should be read.

###  [method:undefined render]( [param:Object3D scene], [param:Camera camera]
)

Render a [page:Scene scene] or another type of [page:Object3D object] using a
[page:Camera camera].  
The render is done to a previously specified [page:WebGLRenderTarget
renderTarget] set by calling [page:WebGLRenderer.setRenderTarget
.setRenderTarget] or to the canvas as usual.  
By default render buffers are cleared before rendering but you can prevent
this by setting the property [page:WebGLRenderer.autoClear autoClear] to
false. If you want to prevent only certain buffers being cleared you can set
either the [page:WebGLRenderer.autoClearColor autoClearColor],
[page:WebGLRenderer.autoClearStencil autoClearStencil] or
[page:WebGLRenderer.autoClearDepth autoClearDepth] properties to false. To
forcibly clear one or more buffers call [page:WebGLRenderer.clear .clear].

### [method:undefined resetState]()

Can be used to reset the internal WebGL state. This method is mostly relevant
for applications which share a single WebGL context across multiple WebGL
libraries.

### [method:undefined setAnimationLoop]( [param:Function callback] )

[page:Function callback] — The function will be called every available frame.
If `null` is passed it will stop any already ongoing animation.

A built in function that can be used instead of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/window/requestAnimationFrame requestAnimationFrame]. For WebXR
projects this function must be used.

### [method:undefined setClearAlpha]( [param:Float alpha] )

Sets the clear alpha. Valid input is a float between `0.0` and `1.0`.

###  [method:undefined setClearColor]( [param:Color color], [param:Float
alpha] )

Sets the clear color and opacity.

### [method:undefined setPixelRatio]( [param:number value] )

Sets device pixel ratio. This is usually used for HiDPI device to prevent
blurring output canvas.

###  [method:undefined setRenderTarget]( [param:WebGLRenderTarget
renderTarget], [param:Integer activeCubeFace], [param:Integer
activeMipmapLevel] )

renderTarget -- The [page:WebGLRenderTarget renderTarget] that needs to be
activated. When `null` is given, the canvas is set as the active render target
instead.  
activeCubeFace -- Specifies the active cube side (PX 0, NX 1, PY 2, NY 3, PZ
4, NZ 5) of [page:WebGLCubeRenderTarget]. When passing a
[page:WebGLArrayRenderTarget] or [page:WebGL3DRenderTarget] this indicates the
z layer to render in to (optional).  
activeMipmapLevel -- Specifies the active mipmap level (optional).  
  
This method sets the active rendertarget.

###  [method:undefined setScissor]( [param:Integer x], [param:Integer y],
[param:Integer width], [param:Integer height] )  
[method:undefined setScissor]( [param:Vector4 vector] )

The x, y, width, and height parameters of the scissor region.  
Optionally, a 4-component vector specifying the parameters of the region.  
  
Sets the scissor region from (x, y) to (x + width, y + height).  
(x, y) is the lower-left corner of the scissor region.

### [method:undefined setScissorTest]( [param:Boolean boolean] )

Enable or disable the scissor test. When this is enabled, only the pixels
within the defined scissor area will be affected by further renderer actions.

### [method:undefined setOpaqueSort]( [param:Function method] )

Sets the custom opaque sort function for the WebGLRenderLists. Pass null to
use the default painterSortStable function.

### [method:undefined setTransparentSort]( [param:Function method] )

Sets the custom transparent sort function for the WebGLRenderLists. Pass null
to use the default reversePainterSortStable function.

###  [method:undefined setSize]( [param:Integer width], [param:Integer
height], [param:Boolean updateStyle] )

Resizes the output canvas to (width, height) with device pixel ratio taken
into account, and also sets the viewport to fit that size, starting in (0, 0).
Setting [page:Boolean updateStyle] to false prevents any style changes to the
output canvas.

###  [method:undefined setViewport]( [param:Integer x], [param:Integer y],
[param:Integer width], [param:Integer height] )  
[method:undefined setViewport]( [param:Vector4 vector] )

The x, y, width, and height parameters of the viewport.  
Optionally, a 4-component vector specifying the parameters of a viewport.  
  
Sets the viewport to render from (x, y) to (x + width, y + height).  
(x, y) is the lower-left corner of the region.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]
