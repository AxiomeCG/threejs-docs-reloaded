# Material

Abstract base class for materials.  
  
Materials describe the appearance of [objects](#). They are defined in a
(mostly) renderer-independent way, so you don't have to rewrite materials if
you decide to use a different renderer.  
  
The following properties and methods are inherited by all other material types
(although they may have different defaults).

## Constructor

### Material

  
  
```ts  
function Material( ): void;  
```  

This creates a generic material.

## Properties

### alphaTest

  
  
```ts  
alphaTest: Float;  
```  

Sets the alpha value to be used when running an alpha test. The material will
not be rendered if the opacity is lower than this value. Default is `0`.

### alphaToCoverage

  
  
```ts  
alphaToCoverage: Boolean;  
```  

Enables alpha to coverage. Can only be used with MSAA-enabled contexts
(meaning when the renderer was created with `antialias` parameter set to
`true`). Default is `false`.

### blendDst

  
  
```ts  
blendDst: Integer;  
```  

Blending destination. Default is [OneMinusSrcAlphaFactor](#). See the
destination factors [constants](#) for all possible values.  
The material's [blending](#) must be set to
[CustomBlending](en\constants\Materials.html) for this to have any effect.

### blendDstAlpha

  
  
```ts  
blendDstAlpha: Integer;  
```  

The transparency of the [.blendDst](#). Uses [.blendDst](#) value if null.
Default is `null`.

### blendEquation

  
  
```ts  
blendEquation: Integer;  
```  

Blending equation to use when applying blending. Default is [AddEquation](#).
See the blending equation [constants](#) for all possible values.  
The material's [blending](#) must be set to
[CustomBlending](en\constants\Materials.html) for this to have any effect.

### blendEquationAlpha

  
  
```ts  
blendEquationAlpha: Integer;  
```  

The transparency of the [.blendEquation](#). Uses [.blendEquation](#) value if
null. Default is `null`.

### blending

  
  
```ts  
blending: Blending;  
```  

Which blending to use when displaying objects with this material.  
This must be set to [CustomBlending](en\constants\Materials.html) to use
custom [blendSrc](#), [blendDst](#) or [blendEquation](#).  
See the blending mode [constants](en\constants\Materials.html) for all
possible values. Default is [NormalBlending](en\constants\Materials.html).

### blendSrc

  
  
```ts  
blendSrc: Integer;  
```  

Blending source. Default is [SrcAlphaFactor](#). See the source factors
[constants](#) for all possible values.  
The material's [blending](#) must be set to
[CustomBlending](en\constants\Materials.html) for this to have any effect.

### blendSrcAlpha

  
  
```ts  
blendSrcAlpha: Integer;  
```  

The transparency of the [.blendSrc](#). Uses [.blendSrc](#) value if null.
Default is `null`.

### clipIntersection

  
  
```ts  
clipIntersection: Boolean;  
```  

Changes the behavior of clipping planes so that only their intersection is
clipped, rather than their union. Default is `false`.

### clippingPlanes

  
  
```ts  
clippingPlanes: Array;  
```  

User-defined clipping planes specified as THREE.Plane objects in world space.
These planes apply to the objects this material is attached to. Points in
space whose signed distance to the plane is negative are clipped (not
rendered). This requires [WebGLRenderer.localClippingEnabled](#) to be `true`.
See the [example:webgl_clipping_intersection WebGL / clipping /intersection]
example. Default is `null`.

### clipShadows

  
  
```ts  
clipShadows: Boolean;  
```  

Defines whether to clip shadows according to the clipping planes specified on
this material. Default is `false`.

### colorWrite

  
  
```ts  
colorWrite: Boolean;  
```  

Whether to render the material's color. This can be used in conjunction with a
mesh's [renderOrder](#) property to create invisible objects that occlude
other objects. Default is `true`.

### defines

  
  
```ts  
defines: Object;  
```  

Custom defines to be injected into the shader. These are passed in form of an
object literal, with key/value pairs. `{ MY_CUSTOM_DEFINE: '' , PI2: Math.PI *
2 }`. The pairs are defined in both vertex and fragment shaders. Default is
`undefined`.

### depthFunc

  
  
```ts  
depthFunc: Integer;  
```  

Which depth function to use. Default is
[LessEqualDepth](en\constants\Materials.html). See the depth mode
[constants](en\constants\Materials.html) for all possible values.

### depthTest

  
  
```ts  
depthTest: Boolean;  
```  

Whether to have depth test enabled when rendering this material. Default is
`true`.

### depthWrite

  
  
```ts  
depthWrite: Boolean;  
```  

Whether rendering this material has any effect on the depth buffer. Default is
`true`.  
  
When drawing 2D overlays it can be useful to disable the depth writing in
order to layer several things together without creating z-index artifacts.

### forceSinglePass

  
  
```ts  
forceSinglePass: Boolean;  
```  

Whether double-sided, transparent objects should be rendered with a single
pass or not. Default is `false`.  
  
The engine renders double-sided, transparent objects with two draw calls (back
faces first, then front faces) to mitigate transparency artifacts. There are
scenarios however where this approach produces no quality gains but still
doubles draw calls e.g. when rendering flat vegetation like grass sprites. In
these cases, set the `forceSinglePass` flag to `true` to disable the two pass
rendering to avoid performance issues.

### isMaterial

  
  
```ts  
isMaterial: Boolean;  
```  

Read-only flag to check if a given object is of type Material.

### stencilWrite

  
  
```ts  
stencilWrite: Boolean;  
```  

Whether stencil operations are performed against the stencil buffer. In order
to perform writes or comparisons against the stencil buffer this value must be
`true`. Default is `false`.

### stencilWriteMask

  
  
```ts  
stencilWriteMask: Integer;  
```  

The bit mask to use when writing to the stencil buffer. Default is `0xFF`.

### stencilFunc

  
  
```ts  
stencilFunc: Integer;  
```  

The stencil comparison function to use. Default is
[AlwaysStencilFunc](en\constants\Materials.html). See stencil function
[constants](en\constants\Materials.html) for all possible values.

### stencilRef

  
  
```ts  
stencilRef: Integer;  
```  

The value to use when performing stencil comparisons or stencil operations.
Default is `0`.

### stencilFuncMask

  
  
```ts  
stencilFuncMask: Integer;  
```  

The bit mask to use when comparing against the stencil buffer. Default is
`0xFF`.

### stencilFail

  
  
```ts  
stencilFail: Integer;  
```  

Which stencil operation to perform when the comparison function returns false.
Default is [KeepStencilOp](en\constants\Materials.html). See the stencil
operations [constants](en\constants\Materials.html) for all possible values.

### stencilZFail

  
  
```ts  
stencilZFail: Integer;  
```  

Which stencil operation to perform when the comparison function returns true
but the depth test fails. Default is
[KeepStencilOp](en\constants\Materials.html). See the stencil operations
[constants](en\constants\Materials.html) for all possible values.

### stencilZPass

  
  
```ts  
stencilZPass: Integer;  
```  

Which stencil operation to perform when the comparison function returns true
and the depth test passes. Default is
[KeepStencilOp](en\constants\Materials.html). See the stencil operations
[constants](en\constants\Materials.html) for all possible values.

### id

  
  
```ts  
id: Integer;  
```  

Unique number for this material instance.

### name

  
  
```ts  
name: String;  
```  

Optional name of the object (doesn't need to be unique). Default is an empty
string.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

Specifies that the material needs to be recompiled.

### opacity

  
  
```ts  
opacity: Float;  
```  

Float in the range of `0.0` - `1.0` indicating how transparent the material
is. A value of `0.0` indicates fully transparent, `1.0` is fully opaque.  
If the material's [transparent](#) property is not set to `true`, the material
will remain fully opaque and this value will only affect its color.  
Default is `1.0`.

### polygonOffset

  
  
```ts  
polygonOffset: Boolean;  
```  

Whether to use polygon offset. Default is `false`. This corresponds to the
`GL_POLYGON_OFFSET_FILL` WebGL feature.

### polygonOffsetFactor

  
  
```ts  
polygonOffsetFactor: Integer;  
```  

Sets the polygon offset factor. Default is `0`.

### polygonOffsetUnits

  
  
```ts  
polygonOffsetUnits: Integer;  
```  

Sets the polygon offset units. Default is `0`.

### precision

  
  
```ts  
precision: String;  
```  

Override the renderer's default precision for this material. Can be `"highp"`,
`"mediump"` or `"lowp"`. Default is `null`.

### premultipliedAlpha

  
  
```ts  
premultipliedAlpha: Boolean;  
```  

Whether to premultiply the alpha (transparency) value. See
[Example:webgl_materials_physical_transmission WebGL / Materials / Physical /
Transmission] for an example of the difference. Default is `false`.

### dithering

  
  
```ts  
dithering: Boolean;  
```  

Whether to apply dithering to the color to remove the appearance of banding.
Default is `false`.

### shadowSide

  
  
```ts  
shadowSide: Integer;  
```  

Defines which side of faces cast shadows. When set, can be
[THREE.FrontSide](en\constants\Materials.html),
[THREE.BackSide](en\constants\Materials.html), or
[THREE.DoubleSide](en\constants\Materials.html). Default is `null`.  
If `null`, the side casting shadows is determined as follows:  

[Material.side](#)| Side casting shadows  
---|---  
THREE.FrontSide| back side  
THREE.BackSide| front side  
THREE.DoubleSide| both sides  
  
### side

  
  
```ts  
side: Integer;  
```  

Defines which side of faces will be rendered - front, back or both. Default is
[THREE.FrontSide](en\constants\Materials.html). Other options are
[THREE.BackSide](en\constants\Materials.html) or
[THREE.DoubleSide](en\constants\Materials.html).

### toneMapped

  
  
```ts  
toneMapped: Boolean;  
```  

Defines whether this material is tone mapped according to the renderer's
[toneMapping](#) setting. Default is `true`.

### transparent

  
  
```ts  
transparent: Boolean;  
```  

Defines whether this material is transparent. This has an effect on rendering
as transparent objects need special treatment and are rendered after non-
transparent objects.  
When set to true, the extent to which the material is transparent is
controlled by setting its [opacity](#) property.  
Default is `false`.

### type

  
  
```ts  
type: String;  
```  

Value is the string 'Material'. This shouldn't be changed, and can be used to
find all objects of this type in a scene.

### uuid

  
  
```ts  
uuid: String;  
```  

<a href="http://en.wikipedia.org/wiki/Universally_unique_identifier">UUID</a>
of this material instance. This gets automatically assigned, so this shouldn't
be edited.

### version

  
  
```ts  
version: Integer;  
```  

This starts at `0` and counts how many times [.needsUpdate](#) is set to
`true`.

### vertexColors

  
  
```ts  
vertexColors: Boolean;  
```  

Defines whether vertex coloring is used. Default is `false`. The engine
supports RGB and RGBA vertex colors depending on whether a three (RGB) or four
(RGBA) component color buffer attribute is used.

### visible

  
  
```ts  
visible: Boolean;  
```  

Defines whether this material is visible. Default is `true`.

### userData

  
  
```ts  
userData: Object;  
```  

An object that can be used to store custom data about the Material. It should
not hold references to functions as these will not be cloned.

## Methods

[EventDispatcher](en\core\EventDispatcher.html) methods are available on this
class.

### clone

  
  
```ts  
function clone( ): Material;  
```  

Return a new material with the same parameters as this material.

### copy

  
  
```ts  
function copy( material: material ): this;  
```  

Copy the parameters from the passed material into this material.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

Material textures must be be disposed of by the dispose() method of
[Texture](en\textures\Texture.html).

### onBeforeCompile

  
  
```ts  
function onBeforeCompile( shader: Shader, renderer: WebGLRenderer ):
undefined;  
```  

An optional callback that is executed immediately before the shader program is
compiled. This function is called with the shader source code as a parameter.
Useful for the modification of built-in materials.

Unlike properties, the callback is not supported by [.clone](#)(),
[.copy](#)() and [.toJSON](#)().

### customProgramCacheKey

  
  
```ts  
function customProgramCacheKey( ): String;  
```  

In case onBeforeCompile is used, this callback can be used to identify values
of settings used in onBeforeCompile, so three.js can reuse a cached shader or
recompile the shader for this material as needed.

For example, if onBeforeCompile contains a conditional statement like:  
  
```ts  
if ( black ) { shader.fragmentShader =
shader.fragmentShader.replace('gl_FragColor = vec4(1)', 'gl_FragColor =
vec4(0)') }  
```  
then customProgramCacheKey should be set like this:  
  
```ts  
material.customProgramCacheKey = function() { return black ? '1' : '0'; }  
```  

Unlike properties, the callback is not supported by [.clone](#)(),
[.copy](#)() and [.toJSON](#)().

### setValues

  
  
```ts  
function setValues( values: Object ): undefined;  
```  

values -- a container with parameters.  
Sets the properties based on the `values`.

### toJSON

  
  
```ts  
function toJSON( meta: Object ): Object;  
```  

meta -- object containing metadata such as textures or images for the
material.  
Convert the material to three.js <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/Material.js">src/materials/Material.js</a>

