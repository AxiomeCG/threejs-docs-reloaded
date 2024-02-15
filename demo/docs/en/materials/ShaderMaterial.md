[Material](en\materials\Material.html) →

# ShaderMaterial

A material rendered with custom shaders. A shader is a small program written
in <a
href="https://www.khronos.org/files/opengles_shading_language.pdf">GLSL</a>
that runs on the GPU. You may want to use a custom shader if you need to:

  * implement an effect not included with any of the built-in [materials](en\materials\Material.html)
  * combine many objects into a single [BufferGeometry](en\core\BufferGeometry.html) in order to improve performance

There are the following notes to bear in mind when using a `ShaderMaterial`:

  * A `ShaderMaterial` will only be rendered properly by [WebGLRenderer](en\renderers\WebGLRenderer.html), since the GLSL code in the <a href="https://en.wikipedia.org/wiki/Shader#Vertex_shaders">vertexShader</a> and <a href="https://en.wikipedia.org/wiki/Shader#Pixel_shaders">fragmentShader</a> properties must be compiled and run on the GPU using WebGL.
  * As of THREE r72, directly assigning attributes in a ShaderMaterial is no longer supported. A [BufferGeometry](en\core\BufferGeometry.html) instance must be used instead, using [BufferAttribute](en\core\BufferAttribute.html) instances to define custom attributes.
  * As of THREE r77, [WebGLRenderTarget](en\renderers\WebGLRenderTarget.html) or [WebGLCubeRenderTarget](en\renderers\WebGLCubeRenderTarget.html) instances are no longer supposed to be used as uniforms. Their [texture](en\textures\Texture.html) property must be used instead.
  * Built in attributes and uniforms are passed to the shaders along with your code. If you don't want the [WebGLProgram](en\renderers\webgl\WebGLProgram.html) to add anything to your shader code, you can use [RawShaderMaterial](en\materials\RawShaderMaterial.html) instead of this class.
  * You can use the directive #pragma unroll_loop_start and #pragma unroll_loop_end in order to unroll a `for` loop in GLSL by the shader preprocessor. The directive has to be placed right above the loop. The loop formatting has to correspond to a defined standard.
    * The loop has to be <a href="https://en.wikipedia.org/wiki/Normalized_loop">normalized</a>.
    * The loop variable has to be *i*.
    * The value `UNROLLED_LOOP_INDEX` will be replaced with the explicitly value of *i* for the given iteration and can be used in preprocessor statements.
  
```ts  
#pragma unroll_loop_start for ( int i = 0; i < 10; i ++ ) { // ... } #pragma
unroll_loop_end  
```  

## Code Example

  
```ts  
const material = new THREE.ShaderMaterial( { uniforms: { time: { value: 1.0 },
resolution: { value: new THREE.Vector2() } }, vertexShader:
document.getElementById( 'vertexShader' ).textContent, fragmentShader:
document.getElementById( 'fragmentShader' ).textContent } );  
```  

## Examples

[example:webgl_buffergeometry_custom_attributes_particles webgl /
buffergeometry / custom / attributes / particles]  
[example:webgl_buffergeometry_selective_draw webgl / buffergeometry /
selective / draw]  
[example:webgl_custom_attributes webgl / custom / attributes]  
[example:webgl_custom_attributes_lines webgl / custom / attributes / lines]  
[example:webgl_custom_attributes_points webgl / custom / attributes / points]  
[example:webgl_custom_attributes_points2 webgl / custom / attributes /
points2]  
[example:webgl_custom_attributes_points3 webgl / custom / attributes /
points3]  
[example:webgl_depth_texture webgl / depth / texture]  
[example:webgl_gpgpu_birds webgl / gpgpu / birds]  
[example:webgl_gpgpu_protoplanet webgl / gpgpu / protoplanet]  
[example:webgl_gpgpu_water webgl / gpgpu / water]  
[example:webgl_interactive_points webgl / interactive / points]  
[example:webgl_video_kinect webgl / video / kinect]  
[example:webgl_lights_hemisphere webgl / lights / hemisphere]  
[example:webgl_marchingcubes webgl / marchingcubes]  
[example:webgl_materials_envmaps webgl / materials / envmaps]  
[example:webgl_materials_lightmap webgl / materials / lightmap]  
[example:webgl_materials_wireframe webgl / materials / wireframe]  
[example:webgl_modifier_tessellation webgl / modifier / tessellation]  
[example:webgl_postprocessing_dof2 webgl / postprocessing / dof2]  
[example:webgl_postprocessing_godrays webgl / postprocessing / godrays]

## Vertex shaders and fragment shaders

You can specify two different types of shaders for each material:

  * The vertex shader runs first; it receives `attributes`, calculates / manipulates the position of each individual vertex, and passes additional data (`varying`s) to the fragment shader.
  * The fragment ( or pixel ) shader runs second; it sets the color of each individual "fragment" (pixel) rendered to the screen.

There are three types of variables in shaders: uniforms, attributes, and
varyings:

  * `Uniforms` are variables that have the same value for all vertices - lighting, fog, and shadow maps are examples of data that would be stored in uniforms. Uniforms can be accessed by both the vertex shader and the fragment shader.
  * `Attributes` are variables associated with each vertex---for instance, the vertex position, face normal, and vertex color are all examples of data that would be stored in attributes. Attributes can `only` be accessed within the vertex shader.
  * `Varyings` are variables that are passed from the vertex shader to the fragment shader. For each fragment, the value of each varying will be smoothly interpolated from the values of adjacent vertices.

Note that `within` the shader itself, uniforms and attributes act like
constants; you can only modify their values by passing different values to the
buffers from your JavaScript code.

## Built-in attributes and uniforms

The [WebGLRenderer](en\renderers\WebGLRenderer.html) provides many attributes
and uniforms to shaders by default; definitions of these variables are
prepended to your `fragmentShader` and `vertexShader` code by the
[WebGLProgram](en\renderers\webgl\WebGLProgram.html) when the shader is
compiled; you don't need to declare them yourself. See
[WebGLProgram](en\renderers\webgl\WebGLProgram.html) for details of these
variables.

Some of these uniforms or attributes (e.g. those pertaining lighting, fog,
etc.) require properties to be set on the material in order for
[WebGLRenderer](en\renderers\WebGLRenderer.html) to copy the appropriate
values to the GPU - make sure to set these flags if you want to use these
features in your own shader.

If you don't want [WebGLProgram](en\renderers\webgl\WebGLProgram.html) to add
anything to your shader code, you can use
[RawShaderMaterial](en\materials\RawShaderMaterial.html) instead of this
class.

## Custom attributes and uniforms

Both custom attributes and uniforms must be declared in your GLSL shader code
(within `vertexShader` and/or `fragmentShader`). Custom uniforms must be
defined in `both` the `uniforms` property of your `ShaderMaterial`, whereas
any custom attributes must be defined via
[BufferAttribute](en\core\BufferAttribute.html) instances. Note that
`varying`s only need to be declared within the shader code (not within the
material).

To declare a custom attribute, please reference the
[BufferGeometry](en\core\BufferGeometry.html) page for an overview, and the
[BufferAttribute](en\core\BufferAttribute.html) page for a detailed look at
the `BufferAttribute` API.

When creating your attributes, each typed array that you create to hold your
attribute's data must be a multiple of your data type's size. For example, if
your attribute is a [THREE.Vector3](en\math\Vector3.html) type, and you have
3000 vertices in your [BufferGeometry](en\core\BufferGeometry.html), your
typed array value must be created with a length of 3000 * 3, or 9000 (one
value per-component). A table of each data type's size is shown below for
reference:

Attribute sizesGLSL type| JavaScript type| Size  
---|---|---  
float| [Number](#)| 1  
vec2| [THREE.Vector2](en\math\Vector2.html)| 2  
vec3| [THREE.Vector3](en\math\Vector3.html)| 3  
vec3| [THREE.Color](en\math\Color.html)| 3  
vec4| [THREE.Vector4](en\math\Vector4.html)| 4  
  
Note that attribute buffers are `not` refreshed automatically when their
values change. To update custom attributes, set the `needsUpdate` flag to true
on the [BufferAttribute](en\core\BufferAttribute.html) of the geometry (see
[BufferGeometry](en\core\BufferGeometry.html) for further details).

To declare a custom [Uniform](en\core\Uniform.html), use the `uniforms`
property:  
```ts  
uniforms: { time: { value: 1.0 }, resolution: { value: new THREE.Vector2() } }  
```  

You're recommended to update custom [Uniform](en\core\Uniform.html) values
depending on [object](en\core\Object3D.html) and
[camera](en\cameras\Camera.html) in [Object3D.onBeforeRender](#) because
[Material](en\materials\Material.html) can be shared among
[meshes](en\objects\Mesh.html), [matrixWorld](en\math\Matrix4.html) of
[Scene](en\scenes\Scene.html) and [Camera](en\cameras\Camera.html) are updated
in [WebGLRenderer.render](#), and some effects render a
[scene](en\scenes\Scene.html) with their own private
[cameras](en\cameras\Camera.html).

## Constructor

### ShaderMaterial

  
  
```ts  
function ShaderMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.

## Properties

See the base [Material](en\materials\Material.html) class for common
properties.

### clipping

  
  
```ts  
clipping: Boolean;  
```  

Defines whether this material supports clipping; true to let the renderer pass
the clippingPlanes uniform. Default is false.

### defaultAttributeValues

  
  
```ts  
defaultAttributeValues: Object;  
```  

When the rendered geometry doesn't include these attributes but the material
does, these default values will be passed to the shaders. This avoids errors
when buffer data is missing.  
```ts  
this.defaultAttributeValues = { 'color': [ 1, 1, 1 ], 'uv': [ 0, 0 ], 'uv1': [
0, 0 ] };  
```  

### defines

  
  
```ts  
defines: Object;  
```  

Defines custom constants using `#define` directives within the GLSL code for
both the vertex shader and the fragment shader; each key/value pair yields
another directive:  
```ts  
defines: { FOO: 15, BAR: true }  
```  
yields the lines  
```ts  
#define FOO 15 #define BAR true  
```  
in the GLSL code.

### extensions

  
  
```ts  
extensions: Object;  
```  

An object with the following properties:  
```ts  
this.extensions = { derivatives: false, // set to use derivatives fragDepth:
false, // set to use fragment depth values drawBuffers: false, // set to use
draw buffers shaderTextureLOD: false // set to use shader texture LOD };  
```  

### fog

  
  
```ts  
fog: Boolean;  
```  

Define whether the material color is affected by global fog settings; true to
pass fog uniforms to the shader. Default is false.

### fragmentShader

  
  
```ts  
fragmentShader: String;  
```  

Fragment shader GLSL code. This is the actual code for the shader. In the
example above, the `vertexShader` and `fragmentShader` code is extracted from
the DOM; it could be passed as a string directly or loaded via AJAX instead.

### glslVersion

  
  
```ts  
glslVersion: String;  
```  

Defines the GLSL version of custom shader code. Only relevant for WebGL 2 in
order to define whether to specify GLSL 3.0 or not. Valid values are
`THREE.GLSL1` or `THREE.GLSL3`. Default is `null`.

### index0AttributeName

  
  
```ts  
index0AttributeName: String;  
```  

If set, this calls <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bindAttribLocation">gl.bindAttribLocation</a>
to bind a generic vertex index to an attribute variable. Default is undefined.

### isShaderMaterial

  
  
```ts  
isShaderMaterial: Boolean;  
```  

Read-only flag to check if a given object is of type ShaderMaterial.

### lights

  
  
```ts  
lights: Boolean;  
```  

Defines whether this material uses lighting; true to pass uniform data related
to lighting to this shader. Default is false.

### linewidth

  
  
```ts  
linewidth: Float;  
```  

Controls wireframe thickness. Default is `1`.  
  
Due to limitations of the <a
href="https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf">OpenGL
Core Profile</a> with the [WebGL](en\renderers\WebGLRenderer.html) renderer on
most platforms linewidth will always be `1` regardless of the set value.

### flatShading

  
  
```ts  
flatShading: Boolean;  
```  

Define whether the material is rendered with flat shading. Default is false.

### uniforms

  
  
```ts  
uniforms: Object;  
```  

An object of the form:  
```ts  
{ "uniform1": { value: 1.0 }, "uniform2": { value: 2 } }  
```  
specifying the uniforms to be passed to the shader code; keys are uniform
names, values are definitions of the form  
```ts  
{ value: 1.0 }  
```  
where `value` is the value of the uniform. Names must match the name of the
uniform, as defined in the GLSL code. Note that uniforms are refreshed on
every frame, so updating the value of the uniform will immediately update the
value available to the GLSL code.

### uniformsNeedUpdate

  
  
```ts  
uniformsNeedUpdate: Boolean;  
```  

Can be used to force a uniform update while changing uniforms in
[Object3D.onBeforeRender](#)(). Default is `false`.

### vertexColors

  
  
```ts  
vertexColors: Boolean;  
```  

Defines whether vertex coloring is used. Default is `false`.

### vertexShader

  
  
```ts  
vertexShader: String;  
```  

Vertex shader GLSL code. This is the actual code for the shader. In the
example above, the `vertexShader` and `fragmentShader` code is extracted from
the DOM; it could be passed as a string directly or loaded via AJAX instead.

### wireframe

  
  
```ts  
wireframe: Boolean;  
```  

Render geometry as wireframe (using GL_LINES instead of GL_TRIANGLES). Default
is false (i.e. render as flat polygons).

### wireframeLinewidth

  
  
```ts  
wireframeLinewidth: Float;  
```  

Controls wireframe thickness. Default is `1`.  
  
Due to limitations of the <a
href="https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf">OpenGL
Core Profile</a> with the [WebGL](en\renderers\WebGLRenderer.html) renderer on
most platforms linewidth will always be `1` regardless of the set value.

## Methods

See the base [Material](en\materials\Material.html) class for common methods.

### clone

  
  
```ts  
function clone( ): ShaderMaterial;  
```  

Generates a shallow copy of this material. Note that the vertexShader and
fragmentShader are copied `by reference`, as are the definitions of the
`attributes`; this means that clones of the material will share the same
compiled [WebGLProgram](en\renderers\webgl\WebGLProgram.html). However, the
`uniforms` are copied `by value`, which allows you to have different sets of
uniforms for different copies of the material.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/ShaderMaterial.js">src/materials/ShaderMaterial.js</a>

