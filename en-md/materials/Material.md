# Material

Abstract base class for materials.  
  
Materials describe the appearance of [page:Object objects]. They are defined
in a (mostly) renderer-independent way, so you don't have to rewrite materials
if you decide to use a different renderer.  
  
The following properties and methods are inherited by all other material types
(although they may have different defaults).

## Constructor

###  function Material( ): void;

This creates a generic material.

## Properties

###  Float alphaTest;

Sets the alpha value to be used when running an alpha test. The material will
not be rendered if the opacity is lower than this value. Default is `0`.

###  Boolean alphaToCoverage;

Enables alpha to coverage. Can only be used with MSAA-enabled contexts
(meaning when the renderer was created with `antialias` parameter set to
`true`). Default is `false`.

###  Integer blendDst;

Blending destination. Default is [page:CustomBlendingEquation
OneMinusSrcAlphaFactor]. See the destination factors
[page:CustomBlendingEquation constants] for all possible values.  
The material's [page:Constant blending] must be set to [page:Materials
CustomBlending] for this to have any effect.

###  Integer blendDstAlpha;

The transparency of the [page:.blendDst]. Uses [page:.blendDst] value if null.
Default is `null`.

###  Integer blendEquation;

Blending equation to use when applying blending. Default is
[page:CustomBlendingEquation AddEquation]. See the blending equation
[page:CustomBlendingEquation constants] for all possible values.  
The material's [page:Constant blending] must be set to [page:Materials
CustomBlending] for this to have any effect.

###  Integer blendEquationAlpha;

The transparency of the [page:.blendEquation]. Uses [page:.blendEquation]
value if null. Default is `null`.

###  Blending blending;

Which blending to use when displaying objects with this material.  
This must be set to [page:Materials CustomBlending] to use custom
[page:Constant blendSrc], [page:Constant blendDst] or [page:Constant
blendEquation].  
See the blending mode [page:Materials constants] for all possible values.
Default is [page:Materials NormalBlending].

###  Integer blendSrc;

Blending source. Default is [page:CustomBlendingEquation SrcAlphaFactor]. See
the source factors [page:CustomBlendingEquation constants] for all possible
values.  
The material's [page:Constant blending] must be set to [page:Materials
CustomBlending] for this to have any effect.

###  Integer blendSrcAlpha;

The transparency of the [page:.blendSrc]. Uses [page:.blendSrc] value if null.
Default is `null`.

###  Boolean clipIntersection;

Changes the behavior of clipping planes so that only their intersection is
clipped, rather than their union. Default is `false`.

###  Array clippingPlanes;

User-defined clipping planes specified as THREE.Plane objects in world space.
These planes apply to the objects this material is attached to. Points in
space whose signed distance to the plane is negative are clipped (not
rendered). This requires [page:WebGLRenderer.localClippingEnabled] to be
`true`. See the [example:webgl_clipping_intersection WebGL / clipping
/intersection] example. Default is `null`.

###  Boolean clipShadows;

Defines whether to clip shadows according to the clipping planes specified on
this material. Default is `false`.

###  Boolean colorWrite;

Whether to render the material's color. This can be used in conjunction with a
mesh's [page:Integer renderOrder] property to create invisible objects that
occlude other objects. Default is `true`.

###  Object defines;

Custom defines to be injected into the shader. These are passed in form of an
object literal, with key/value pairs. `{ MY_CUSTOM_DEFINE: '' , PI2: Math.PI *
2 }`. The pairs are defined in both vertex and fragment shaders. Default is
`undefined`.

###  Integer depthFunc;

Which depth function to use. Default is [page:Materials LessEqualDepth]. See
the depth mode [page:Materials constants] for all possible values.

###  Boolean depthTest;

Whether to have depth test enabled when rendering this material. Default is
`true`.

###  Boolean depthWrite;

Whether rendering this material has any effect on the depth buffer. Default is
`true`.  
  
When drawing 2D overlays it can be useful to disable the depth writing in
order to layer several things together without creating z-index artifacts.

###  Boolean forceSinglePass;

Whether double-sided, transparent objects should be rendered with a single
pass or not. Default is `false`.  
  
The engine renders double-sided, transparent objects with two draw calls (back
faces first, then front faces) to mitigate transparency artifacts. There are
scenarios however where this approach produces no quality gains but still
doubles draw calls e.g. when rendering flat vegetation like grass sprites. In
these cases, set the `forceSinglePass` flag to `true` to disable the two pass
rendering to avoid performance issues.

###  Boolean isMaterial;

Read-only flag to check if a given object is of type Material.

###  Boolean stencilWrite;

Whether stencil operations are performed against the stencil buffer. In order
to perform writes or comparisons against the stencil buffer this value must be
`true`. Default is `false`.

###  Integer stencilWriteMask;

The bit mask to use when writing to the stencil buffer. Default is `0xFF`.

###  Integer stencilFunc;

The stencil comparison function to use. Default is [page:Materials
AlwaysStencilFunc]. See stencil function [page:Materials constants] for all
possible values.

###  Integer stencilRef;

The value to use when performing stencil comparisons or stencil operations.
Default is `0`.

###  Integer stencilFuncMask;

The bit mask to use when comparing against the stencil buffer. Default is
`0xFF`.

###  Integer stencilFail;

Which stencil operation to perform when the comparison function returns false.
Default is [page:Materials KeepStencilOp]. See the stencil operations
[page:Materials constants] for all possible values.

###  Integer stencilZFail;

Which stencil operation to perform when the comparison function returns true
but the depth test fails. Default is [page:Materials KeepStencilOp]. See the
stencil operations [page:Materials constants] for all possible values.

###  Integer stencilZPass;

Which stencil operation to perform when the comparison function returns true
and the depth test passes. Default is [page:Materials KeepStencilOp]. See the
stencil operations [page:Materials constants] for all possible values.

###  Integer id;

Unique number for this material instance.

###  String name;

Optional name of the object (doesn't need to be unique). Default is an empty
string.

###  Boolean needsUpdate;

Specifies that the material needs to be recompiled.

###  Float opacity;

Float in the range of `0.0` - `1.0` indicating how transparent the material
is. A value of `0.0` indicates fully transparent, `1.0` is fully opaque.  
If the material's [page:Boolean transparent] property is not set to `true`,
the material will remain fully opaque and this value will only affect its
color.  
Default is `1.0`.

###  Boolean polygonOffset;

Whether to use polygon offset. Default is `false`. This corresponds to the
`GL_POLYGON_OFFSET_FILL` WebGL feature.

###  Integer polygonOffsetFactor;

Sets the polygon offset factor. Default is `0`.

###  Integer polygonOffsetUnits;

Sets the polygon offset units. Default is `0`.

###  String precision;

Override the renderer's default precision for this material. Can be `"highp"`,
`"mediump"` or `"lowp"`. Default is `null`.

###  Boolean premultipliedAlpha;

Whether to premultiply the alpha (transparency) value. See
[Example:webgl_materials_physical_transmission WebGL / Materials / Physical /
Transmission] for an example of the difference. Default is `false`.

###  Boolean dithering;

Whether to apply dithering to the color to remove the appearance of banding.
Default is `false`.

###  Integer shadowSide;

Defines which side of faces cast shadows. When set, can be [page:Materials
THREE.FrontSide], [page:Materials THREE.BackSide], or [page:Materials
THREE.DoubleSide]. Default is `null`.  
If `null`, the side casting shadows is determined as follows:  

[page:Material.side]| Side casting shadows  
---|---  
THREE.FrontSide| back side  
THREE.BackSide| front side  
THREE.DoubleSide| both sides  
  
###  Integer side;

Defines which side of faces will be rendered - front, back or both. Default is
[page:Materials THREE.FrontSide]. Other options are [page:Materials
THREE.BackSide] or [page:Materials THREE.DoubleSide].

###  Boolean toneMapped;

Defines whether this material is tone mapped according to the renderer's
[page:WebGLRenderer.toneMapping toneMapping] setting. Default is `true`.

###  Boolean transparent;

Defines whether this material is transparent. This has an effect on rendering
as transparent objects need special treatment and are rendered after non-
transparent objects.  
When set to true, the extent to which the material is transparent is
controlled by setting its [page:Float opacity] property.  
Default is `false`.

###  String type;

Value is the string 'Material'. This shouldn't be changed, and can be used to
find all objects of this type in a scene.

###  String uuid;

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
material instance. This gets automatically assigned, so this shouldn't be
edited.

###  Integer version;

This starts at `0` and counts how many times [page:Material.needsUpdate
.needsUpdate] is set to `true`.

###  Boolean vertexColors;

Defines whether vertex coloring is used. Default is `false`. The engine
supports RGB and RGBA vertex colors depending on whether a three (RGB) or four
(RGBA) component color buffer attribute is used.

###  Boolean visible;

Defines whether this material is visible. Default is `true`.

###  Object userData;

An object that can be used to store custom data about the Material. It should
not hold references to functions as these will not be cloned.

## Methods

[page:EventDispatcher EventDispatcher] methods are available on this class.

###  function clone( ): Material;

Return a new material with the same parameters as this material.

###  function copy( material: material ): this;

Copy the parameters from the passed material into this material.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

Material textures must be be disposed of by the dispose() method of
[page:Texture Texture].

###  function onBeforeCompile( shader: Shader, renderer: WebGLRenderer ):
undefined;

An optional callback that is executed immediately before the shader program is
compiled. This function is called with the shader source code as a parameter.
Useful for the modification of built-in materials.

Unlike properties, the callback is not supported by [page:Material.clone
.clone](), [page:Material.copy .copy]() and [page:Material.toJSON .toJSON]().

###  function customProgramCacheKey( ): String;

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

Unlike properties, the callback is not supported by [page:Material.clone
.clone](), [page:Material.copy .copy]() and [page:Material.toJSON .toJSON]().

###  function setValues( values: Object ): undefined;

values -- a container with parameters.  
Sets the properties based on the `values`.

###  function toJSON( meta: Object ): Object;

meta -- object containing metadata such as textures or images for the
material.  
Convert the material to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

