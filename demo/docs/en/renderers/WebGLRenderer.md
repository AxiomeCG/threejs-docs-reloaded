# WebGLRenderer

The WebGL renderer displays your beautifully crafted scenes using <a
href="https://en.wikipedia.org/wiki/WebGL">WebGL</a>.

## Constructor

### WebGLRenderer

  
  
```ts  
function WebGLRenderer( parameters: Object ): void;  
```  

[parameters](#) - (optional) object with properties defining the renderer's
behaviour. The constructor also accepts no parameters at all. In all cases, it
will assume sane defaults when parameters are missing. The following are valid
parameters:  
  
[canvas](#) - A <a href="https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/canvas">canvas</a> where the renderer draws its
output. This corresponds to the [domElement](#) property below. If not passed
in here, a new canvas element will be created.  
[context](#) - This can be used to attach the renderer to an existing <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext">RenderingContext</a>. Default is null.  
[precision](#) - Shader precision. Can be `"highp"`, `"mediump"` or `"lowp"`.
Defaults to `"highp"` if supported by the device.  
[alpha](#) - controls the default clear alpha value. When set to `true`, the
value is `0`. Otherwise it's `1`. Default is `false`.  
[premultipliedAlpha](#) - whether the renderer will assume that colors have <a
href="https://en.wikipedia.org/wiki/Glossary_of_computer_graphics#Premultiplied_alpha">premultiplied
alpha</a>. Default is `true`.  
[antialias](#) - whether to perform antialiasing. Default is `false`.  
[stencil](#) - whether the drawing buffer has a <a
href="https://en.wikipedia.org/wiki/Stencil_buffer">stencil buffer</a> of at
least 8 bits. Default is `true`.  
[preserveDrawingBuffer](#) - whether to preserve the buffers until manually
cleared or overwritten. Default is `false`.  
[powerPreference](#) - Provides a hint to the user agent indicating what
configuration of GPU is suitable for this WebGL context. Can be `"high-
performance"`, `"low-power"` or `"default"`. Default is `"default"`. See <a
href="https://www.khronos.org/registry/webgl/specs/latest/1.0/#5.2">WebGL
spec</a> for details.  
[failIfMajorPerformanceCaveat](#) - whether the renderer creation will fail
upon low performance is detected. Default is `false`. See <a
href="https://www.khronos.org/registry/webgl/specs/latest/1.0/#5.2">WebGL
spec</a> for details.  
[depth](#) - whether the drawing buffer has a <a
href="https://en.wikipedia.org/wiki/Z-buffering">depth buffer</a> of at least
16 bits. Default is `true`.  
[logarithmicDepthBuffer](#) - whether to use a logarithmic depth buffer. It
may be necessary to use this if dealing with huge differences in scale in a
single scene. Note that this setting uses gl_FragDepth if available which
disables the <a
href="https://www.khronos.org/opengl/wiki/Early_Fragment_Test">Early Fragment
Test</a> optimization and can cause a decrease in performance. Default is
`false`. See the [example:webgl_camera_logarithmicdepthbuffer camera /
logarithmicdepthbuffer] example.

## Properties

### autoClear

  
  
```ts  
autoClear: Boolean;  
```  

Defines whether the renderer should automatically clear its output before
rendering a frame.

### autoClearColor

  
  
```ts  
autoClearColor: Boolean;  
```  

If [.autoClear](#autoClear) is true, defines whether the renderer should clear
the color buffer. Default is `true`.

### autoClearDepth

  
  
```ts  
autoClearDepth: Boolean;  
```  

If [.autoClear](#autoClear) is true, defines whether the renderer should clear
the depth buffer. Default is `true`.

### autoClearStencil

  
  
```ts  
autoClearStencil: Boolean;  
```  

If [.autoClear](#autoClear) is true, defines whether the renderer should clear
the stencil buffer. Default is `true`.

### debug

  
  
```ts  
debug: Object;  
```  

\- [checkShaderErrors](#): If it is true, defines whether material shader
programs are checked for errors during compilation and linkage process. It may
be useful to disable this check in production for performance gain. It is
strongly recommended to keep these checks enabled during development. If the
shader does not compile and link - it will not work and associated material
will not render. Default is `true`.  
\- [onShaderError](#)( gl, program, glVertexShader, glFragmentShader ): A
callback function that can be used for custom error reporting. The callback
receives the WebGL context, an instance of WebGLProgram as well two instances
of WebGLShader representing the vertex and fragment shader. Assigning a custom
function disables the default error reporting. Default is `null`.

### capabilities

  
  
```ts  
capabilities: Object;  
```  

An object containing details about the capabilities of the current <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext">RenderingContext</a>.  
\- [floatFragmentTextures](#): whether the context supports the <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/OES_texture_float">OES_texture_float</a> extension.  
\- [floatVertexTextures](#): `true` if [floatFragmentTextures](#) and
[vertexTextures](#) are both true.  
\- [getMaxAnisotropy](#)(): Returns the maximum available anisotropy.  
\- [getMaxPrecision](#)(): Returns the maximum available precision for vertex
and fragment shaders.  
\- [isWebGL2](#): `true` if the context in use is a WebGL2RenderingContext
object.  
\- [logarithmicDepthBuffer](#): `true` if the [logarithmicDepthBuffer](#) was
set to true in the constructor and the context supports the <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/EXT_frag_depth">EXT_frag_depth</a> extension.  
\- [maxAttributes](#): The value of `gl.MAX_VERTEX_ATTRIBS`.  
\- [maxCubemapSize](#): The value of `gl.MAX_CUBE_MAP_TEXTURE_SIZE`. Maximum
height * width of cube map textures that a shader can use.  
\- [maxFragmentUniforms](#): The value of `gl.MAX_FRAGMENT_UNIFORM_VECTORS`.
The number of uniforms that can be used by a fragment shader.  
\- [maxSamples](#): The value of `gl.MAX_SAMPLES`. Maximum number of samples
in context of Multisample anti-aliasing (MSAA).  
\- [maxTextureSize](#): The value of `gl.MAX_TEXTURE_SIZE`. Maximum height *
width of a texture that a shader use.  
\- [maxTextures](#): The value of `gl.MAX_TEXTURE_IMAGE_UNITS`. The maximum
number of textures that can be used by a shader.  
\- [maxVaryings](#): The value of `gl.MAX_VARYING_VECTORS`. The number of
varying vectors that can used by shaders.  
\- [maxVertexTextures](#): The value of `gl.MAX_VERTEX_TEXTURE_IMAGE_UNITS`.
The number of textures that can be used in a vertex shader.  
\- [maxVertexUniforms](#): The value of `gl.MAX_VERTEX_UNIFORM_VECTORS`. The
maximum number of uniforms that can be used in a vertex shader.  
\- [precision](#): The shader precision currently being used by the renderer.  
\- [vertexTextures](#): `true` if [property:Integer maxVertexTextures] is
greater than 0 (i.e. vertex textures can be used).  

### clippingPlanes

  
  
```ts  
clippingPlanes: Array;  
```  

User-defined clipping planes specified as THREE.Plane objects in world space.
These planes apply globally. Points in space whose dot product with the plane
is negative are cut away. Default is [].

### domElement

  
  
```ts  
domElement: DOMElement;  
```  

A <a href="https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/canvas">canvas</a> where the renderer draws its
output.  
This is automatically created by the renderer in the constructor (if not
provided already); you just need to add it to your page like so:  
  
```ts  
document.body.appendChild( renderer.domElement );  
```  

### extensions

  
  
```ts  
extensions: Object;  
```  

\- [get](#)( [param:String extensionName] ): Used to check whether various
extensions are supported and returns an object with details of the extension
if available. This method can check for the following extensions:  

  * `WEBGL_depth_texture`
  * `EXT_texture_filter_anisotropic`
  * `WEBGL_compressed_texture_s3tc`
  * `WEBGL_compressed_texture_pvrtc`
  * `WEBGL_compressed_texture_etc1`

### outputColorSpace

  
  
```ts  
outputColorSpace: string;  
```  

Defines the output color space of the renderer. Default is
[THREE.SRGBColorSpace](en\constants\Textures.html).

If a render target has been set using [.setRenderTarget](#) then
renderTarget.texture.colorSpace will be used instead.

See the [texture constants](en\constants\Textures.html) page for details of
other formats.

### info

  
  
```ts  
info: Object;  
```  

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
```ts  
renderer.info.autoReset = false;  
```  
Call `reset()` whenever you have finished to render a single frame.  
```ts  
renderer.info.reset();  
```  

### localClippingEnabled

  
  
```ts  
localClippingEnabled: Boolean;  
```  

Defines whether the renderer respects object-level clipping planes. Default is
`false`.

### useLegacyLights

  
  
```ts  
useLegacyLights: Boolean;  
```  

Whether to use the legacy lighting mode or not. Default is `true`.

### properties

  
  
```ts  
properties: Object;  
```  

Used internally by the renderer to keep track of various sub object
properties.

### renderLists

  
  
```ts  
renderLists: WebGLRenderLists;  
```  

Used internally to handle ordering of scene object rendering.

### shadowMap

  
  
```ts  
shadowMap: WebGLShadowMap;  
```  

This contains the reference to the shadow map, if used.  
\- [enabled](#): If set, use shadow maps in the scene. Default is `false`.  
\- [autoUpdate](#): Enables automatic updates to the shadows in the scene.
Default is `true`.  
If you do not require dynamic lighting / shadows, you may set this to `false`
when the renderer is instantiated.  
\- [needsUpdate](#): When set to `true`, shadow maps in the scene will be
updated in the next `render` call. Default is `false`.  
If you have disabled automatic updates to shadow maps (`shadowMap.autoUpdate =
false`), you will need to set this to `true` and then make a render call to
update the shadows in your scene.  
\- [type](#): Defines shadow map type (unfiltered, percentage close filtering,
percentage close filtering with bilinear filtering in shader). Options are:

  * THREE.BasicShadowMap
  * THREE.PCFShadowMap (default)
  * THREE.PCFSoftShadowMap
  * THREE.VSMShadowMap

See [Renderer constants](en\constants\Renderer.html) for details.  

### sortObjects

  
  
```ts  
sortObjects: Boolean;  
```  

Defines whether the renderer should sort objects. Default is `true`.  
  
Note: Sorting is used to attempt to properly render objects that have some
degree of transparency. By definition, sorting objects may not work in all
cases. Depending on the needs of application, it may be necessary to turn off
sorting and use other methods to deal with transparency rendering e.g.
manually determining each object's rendering order.

### state

  
  
```ts  
state: Object;  
```  

Contains functions for setting various properties of the
[WebGLRenderer.context](#) state.

### toneMapping

  
  
```ts  
toneMapping: Constant;  
```  

Default is [NoToneMapping](en\constants\Renderer.html). See the [Renderer
constants](en\constants\Renderer.html) for other choices.

### toneMappingExposure

  
  
```ts  
toneMappingExposure: Number;  
```  

Exposure level of tone mapping. Default is `1`.

### xr

  
  
```ts  
xr: WebXRManager;  
```  

Provides access to the WebXR related
[interface](en\renderers\webxr\WebXRManager.html) of the renderer.

## Methods

### clear

  
  
```ts  
function clear( color: Boolean, depth: Boolean, stencil: Boolean ): undefined;  
```  

Tells the renderer to clear its color, depth or stencil drawing buffer(s).
This method initializes the color buffer to the current clear color value.  
Arguments default to `true`.

### clearColor

  
  
```ts  
function clearColor( ): undefined;  
```  

Clear the color buffer. Equivalent to calling [.clear](#)( true, false, false
).

### clearDepth

  
  
```ts  
function clearDepth( ): undefined;  
```  

Clear the depth buffer. Equivalent to calling [.clear](#)( false, true, false
).

### clearStencil

  
  
```ts  
function clearStencil( ): undefined;  
```  

Clear the stencil buffers. Equivalent to calling [.clear](#)( false, false,
true ).

### compile

  
  
```ts  
function compile( scene: Object3D, camera: Camera ): undefined;  
```  

Compiles all materials in the scene with the camera. This is useful to
precompile shaders before the first rendering.

### copyFramebufferToTexture

  
  
```ts  
function copyFramebufferToTexture( position: Vector2, texture:
FramebufferTexture, level: Number ): undefined;  
```  

Copies pixels from the current WebGLFramebuffer into a 2D texture. Enables
access to <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/copyTexImage2D">WebGLRenderingContext.copyTexImage2D</a>.

### copyTextureToTexture

  
  
```ts  
function copyTextureToTexture( position: Vector2, srcTexture: Texture,
dstTexture: Texture, level: Number ): undefined;  
```  

Copies all pixels of a texture to an existing texture starting from the given
position. Enables access to <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/texSubImage2D">WebGLRenderingContext.texSubImage2D</a>.

### copyTextureToTexture3D

  
  
```ts  
function copyTextureToTexture3D( sourceBox: Box3, position: Vector3,
srcTexture: Texture, dstTexture: Texture, level: Number ): undefined;  
```  

Copies the pixels of a texture in the bounds '[sourceBox](en\math\Box3.html)'
in the destination texture starting from the given position. Enables access to
<a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGL2RenderingContext/texSubImage3D">WebGL2RenderingContext.texSubImage3D</a>.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### forceContextLoss

  
  
```ts  
function forceContextLoss( ): undefined;  
```  

Simulate loss of the WebGL context. This requires support for the <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WEBGL_lose_context">WEBGL_lose_context</a> extensions.

### forceContextRestore

  
  
```ts  
function forceContextRestore( ): undefined;  
```  

Simulate restore of the WebGL context. This requires support for the <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WEBGL_lose_context">WEBGL_lose_context</a> extensions.

### getClearAlpha

  
  
```ts  
function getClearAlpha( ): Float;  
```  

Returns a [float](#) with the current clear alpha. Ranges from `0` to `1`.

### getClearColor

  
  
```ts  
function getClearColor( target: Color ): Color;  
```  

Returns a [THREE.Color](en\math\Color.html) instance with the current clear
color.

### getContext

  
  
```ts  
function getContext( ): WebGL2RenderingContext;  
```  

Return the current WebGL context.

### getContextAttributes

  
  
```ts  
function getContextAttributes( ): WebGLContextAttributes;  
```  

Returns an object that describes the attributes set on the WebGL context when
it was created.

### getActiveCubeFace

  
  
```ts  
function getActiveCubeFace( ): Integer;  
```  

Returns the current active cube face.

### getActiveMipmapLevel

  
  
```ts  
function getActiveMipmapLevel( ): Integer;  
```  

Returns the current active mipmap level.

### getRenderTarget

  
  
```ts  
function getRenderTarget( ): RenderTarget;  
```  

Returns the current [RenderTarget](#) if there are; returns `null` otherwise.

### getCurrentViewport

  
  
```ts  
function getCurrentViewport( target: Vector4 ): Vector4;  
```  

[target](en\math\Vector4.html) — the result will be copied into this Vector4.  
  
Returns the current viewport.

### getDrawingBufferSize

  
  
```ts  
function getDrawingBufferSize( target: Vector2 ): Vector2;  
```  

[target](en\math\Vector2.html) — the result will be copied into this Vector2.  
  
Returns the width and height of the renderer's drawing buffer, in pixels.

### getPixelRatio

  
  
```ts  
function getPixelRatio( ): number;  
```  

Returns current device pixel ratio used.

### getScissor

  
  
```ts  
function getScissor( target: Vector4 ): Vector4;  
```  

[target](en\math\Vector4.html) — the result will be copied into this Vector4.  
  
Returns the scissor region.

### getScissorTest

  
  
```ts  
function getScissorTest( ): Boolean;  
```  

Returns `true` if scissor test is enabled; returns `false` otherwise.

### getSize

  
  
```ts  
function getSize( target: Vector2 ): Vector2;  
```  

[target](en\math\Vector2.html) — the result will be copied into this Vector2.  
  
Returns the width and height of the renderer's output canvas, in pixels.

### getViewport

  
  
```ts  
function getViewport( target: Vector4 ): Vector4;  
```  

[target](en\math\Vector4.html) — the result will be copied into this Vector4.  
  
Returns the viewport.

### initTexture

  
  
```ts  
function initTexture( texture: Texture ): undefined;  
```  

Initializes the given texture. Useful for preloading a texture rather than
waiting until first render (which can cause noticeable lags due to decode and
GPU upload overhead).

### resetGLState

  
  
```ts  
function resetGLState( ): undefined;  
```  

Reset the GL state to default. Called internally if the WebGL context is lost.

### readRenderTargetPixels

  
  
```ts  
function readRenderTargetPixels( renderTarget: WebGLRenderTarget, x: Float, y:
Float, width: Float, height: Float, buffer: TypedArray, activeCubeFaceIndex:
Integer ): undefined;  
```  

buffer - Uint8Array is the only destination type supported in all cases, other
types are renderTarget and platform dependent. See <a
href="https://www.khronos.org/registry/webgl/specs/latest/1.0/#5.14.12">WebGL
spec</a> for details.

Reads the pixel data from the renderTarget into the buffer you pass in. This
is a wrapper around <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/readPixels">WebGLRenderingContext.readPixels</a>().

See the [example:webgl_interactive_cubes_gpu interactive / cubes / gpu]
example.

For reading out a
[WebGLCubeRenderTarget](en\renderers\WebGLCubeRenderTarget.html) use the
optional parameter activeCubeFaceIndex to determine which face should be read.

### render

  
  
```ts  
function render( scene: Object3D, camera: Camera ): undefined;  
```  

Render a [scene](en\scenes\Scene.html) or another type of
[object](en\core\Object3D.html) using a [camera](en\cameras\Camera.html).  
The render is done to a previously specified
[renderTarget](en\renderers\WebGLRenderTarget.html) set by calling
[.setRenderTarget](#) or to the canvas as usual.  
By default render buffers are cleared before rendering but you can prevent
this by setting the property [autoClear](#) to false. If you want to prevent
only certain buffers being cleared you can set either the [autoClearColor](#),
[autoClearStencil](#) or [autoClearDepth](#) properties to false. To forcibly
clear one or more buffers call [.clear](#).

### resetState

  
  
```ts  
function resetState( ): undefined;  
```  

Can be used to reset the internal WebGL state. This method is mostly relevant
for applications which share a single WebGL context across multiple WebGL
libraries.

### setAnimationLoop

  
  
```ts  
function setAnimationLoop( callback: Function ): undefined;  
```  

[callback](#) — The function will be called every available frame. If `null`
is passed it will stop any already ongoing animation.

A built in function that can be used instead of <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/window/requestAnimationFrame">requestAnimationFrame</a>. For
WebXR projects this function must be used.

### setClearAlpha

  
  
```ts  
function setClearAlpha( alpha: Float ): undefined;  
```  

Sets the clear alpha. Valid input is a float between `0.0` and `1.0`.

### setClearColor

  
  
```ts  
function setClearColor( color: Color, alpha: Float ): undefined;  
```  

Sets the clear color and opacity.

### setPixelRatio

  
  
```ts  
function setPixelRatio( value: number ): undefined;  
```  

Sets device pixel ratio. This is usually used for HiDPI device to prevent
blurring output canvas.

### setRenderTarget

  
  
```ts  
function setRenderTarget( renderTarget: WebGLRenderTarget, activeCubeFace:
Integer, activeMipmapLevel: Integer ): undefined;  
```  

renderTarget -- The [renderTarget](en\renderers\WebGLRenderTarget.html) that
needs to be activated. When `null` is given, the canvas is set as the active
render target instead.  
activeCubeFace -- Specifies the active cube side (PX 0, NX 1, PY 2, NY 3, PZ
4, NZ 5) of [WebGLCubeRenderTarget](en\renderers\WebGLCubeRenderTarget.html).
When passing a
[WebGLArrayRenderTarget](en\renderers\WebGLArrayRenderTarget.html) or
[WebGL3DRenderTarget](en\renderers\WebGL3DRenderTarget.html) this indicates
the z layer to render in to (optional).  
activeMipmapLevel -- Specifies the active mipmap level (optional).  
  
This method sets the active rendertarget.

### setScissor

  
  
```ts  
function setScissor( x: Integer, y: Integer, width: Integer, height: Integer,
vector: Vector4 ): undefined;  
```  

The x, y, width, and height parameters of the scissor region.  
Optionally, a 4-component vector specifying the parameters of the region.  
  
Sets the scissor region from (x, y) to (x + width, y + height).  
(x, y) is the lower-left corner of the scissor region.

### setScissorTest

  
  
```ts  
function setScissorTest( boolean: Boolean ): undefined;  
```  

Enable or disable the scissor test. When this is enabled, only the pixels
within the defined scissor area will be affected by further renderer actions.

### setOpaqueSort

  
  
```ts  
function setOpaqueSort( method: Function ): undefined;  
```  

Sets the custom opaque sort function for the WebGLRenderLists. Pass null to
use the default painterSortStable function.

### setTransparentSort

  
  
```ts  
function setTransparentSort( method: Function ): undefined;  
```  

Sets the custom transparent sort function for the WebGLRenderLists. Pass null
to use the default reversePainterSortStable function.

### setSize

  
  
```ts  
function setSize( width: Integer, height: Integer, updateStyle: Boolean ):
undefined;  
```  

Resizes the output canvas to (width, height) with device pixel ratio taken
into account, and also sets the viewport to fit that size, starting in (0, 0).
Setting [updateStyle](#) to false prevents any style changes to the output
canvas.

### setViewport

  
  
```ts  
function setViewport( x: Integer, y: Integer, width: Integer, height: Integer,
vector: Vector4 ): undefined;  
```  

The x, y, width, and height parameters of the viewport.  
Optionally, a 4-component vector specifying the parameters of a viewport.  
  
Sets the viewport to render from (x, y) to (x + width, y + height).  
(x, y) is the lower-left corner of the region.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/WebGLRenderer.js">src/renderers/WebGLRenderer.js</a>

