[page:Material] →

# [name]

A material rendered with custom shaders. A shader is a small program written
in [link:https://www.khronos.org/files/opengles_shading_language.pdf GLSL]
that runs on the GPU. You may want to use a custom shader if you need to:

  * implement an effect not included with any of the built-in [page:Material materials] 
  * combine many objects into a single [page:BufferGeometry] in order to improve performance 

There are the following notes to bear in mind when using a `ShaderMaterial`:

  * A `ShaderMaterial` will only be rendered properly by [page:WebGLRenderer], since the GLSL code in the [link:https://en.wikipedia.org/wiki/Shader#Vertex_shaders vertexShader] and [link:https://en.wikipedia.org/wiki/Shader#Pixel_shaders fragmentShader] properties must be compiled and run on the GPU using WebGL. 
  * As of THREE r72, directly assigning attributes in a ShaderMaterial is no longer supported. A [page:BufferGeometry] instance must be used instead, using [page:BufferAttribute] instances to define custom attributes. 
  * As of THREE r77, [page:WebGLRenderTarget] or [page:WebGLCubeRenderTarget] instances are no longer supposed to be used as uniforms. Their [page:Texture texture] property must be used instead. 
  * Built in attributes and uniforms are passed to the shaders along with your code. If you don't want the [page:WebGLProgram] to add anything to your shader code, you can use [page:RawShaderMaterial] instead of this class. 
  * You can use the directive #pragma unroll_loop_start and #pragma unroll_loop_end in order to unroll a `for` loop in GLSL by the shader preprocessor. The directive has to be placed right above the loop. The loop formatting has to correspond to a defined standard. 
    * The loop has to be [link:https://en.wikipedia.org/wiki/Normalized_loop normalized]. 
    * The loop variable has to be *i*.
    * The value `UNROLLED_LOOP_INDEX` will be replaced with the explicitly value of *i* for the given iteration and can be used in preprocessor statements. 
  
```ts  
#pragma unroll_loop_start  
for ( int i = 0; i < 10; i ++ ) {  
// ...  
}  
#pragma unroll_loop_end  
```  

## Code Example

  
```ts  
const material = new THREE.ShaderMaterial( {  
  
uniforms: {  
time: { value: 1.0 },  
resolution: { value: new THREE.Vector2() }  
},  
  
vertexShader: document.getElementById( 'vertexShader' ).textContent,  
fragmentShader: document.getElementById( 'fragmentShader' ).textContent  
  
} );  
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

The [page:WebGLRenderer] provides many attributes and uniforms to shaders by
default; definitions of these variables are prepended to your `fragmentShader`
and `vertexShader` code by the [page:WebGLProgram] when the shader is
compiled; you don't need to declare them yourself. See [page:WebGLProgram] for
details of these variables.

Some of these uniforms or attributes (e.g. those pertaining lighting, fog,
etc.) require properties to be set on the material in order for
[page:WebGLRenderer] to copy the appropriate values to the GPU - make sure to
set these flags if you want to use these features in your own shader.

If you don't want [page:WebGLProgram] to add anything to your shader code, you
can use [page:RawShaderMaterial] instead of this class.

## Custom attributes and uniforms

Both custom attributes and uniforms must be declared in your GLSL shader code
(within `vertexShader` and/or `fragmentShader`). Custom uniforms must be
defined in `both` the `uniforms` property of your `ShaderMaterial`, whereas
any custom attributes must be defined via [page:BufferAttribute] instances.
Note that `varying`s only need to be declared within the shader code (not
within the material).

To declare a custom attribute, please reference the [page:BufferGeometry] page
for an overview, and the [page:BufferAttribute] page for a detailed look at
the `BufferAttribute` API.

When creating your attributes, each typed array that you create to hold your
attribute's data must be a multiple of your data type's size. For example, if
your attribute is a [page:Vector3 THREE.Vector3] type, and you have 3000
vertices in your [page:BufferGeometry], your typed array value must be created
with a length of 3000 * 3, or 9000 (one value per-component). A table of each
data type's size is shown below for reference:

Attribute sizes GLSL type | JavaScript type | Size  
---|---|---  
float | [page:Number] | 1  
vec2 | [page:Vector2 THREE.Vector2] | 2  
vec3 | [page:Vector3 THREE.Vector3] | 3  
vec3 | [page:Color THREE.Color] | 3  
vec4 | [page:Vector4 THREE.Vector4] | 4  
  
Note that attribute buffers are `not` refreshed automatically when their
values change. To update custom attributes, set the `needsUpdate` flag to true
on the [page:BufferAttribute] of the geometry (see [page:BufferGeometry] for
further details).

To declare a custom [page:Uniform], use the `uniforms` property:  
```ts  
uniforms: {  
time: { value: 1.0 },  
resolution: { value: new THREE.Vector2() }  
}  
```  

You're recommended to update custom [page:Uniform] values depending on
[page:Object3D object] and [page:Camera camera] in
[page:Object3D.onBeforeRender] because [page:Material] can be shared among
[page:Mesh meshes], [page:Matrix4 matrixWorld] of [page:Scene] and
[page:Camera] are updated in [page:WebGLRenderer.render], and some effects
render a [page:Scene scene] with their own private [page:Camera cameras].

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.

## Properties

See the base [page:Material] class for common properties.

### <br/> Boolean clipping; <br/>

Defines whether this material supports clipping; true to let the renderer pass
the clippingPlanes uniform. Default is false.

### <br/> Object defaultAttributeValues; <br/>

When the rendered geometry doesn't include these attributes but the material
does, these default values will be passed to the shaders. This avoids errors
when buffer data is missing.  
```ts  
this.defaultAttributeValues = {  
'color': [ 1, 1, 1 ],  
'uv': [ 0, 0 ],  
'uv1': [ 0, 0 ]  
};  
```  

### <br/> Object defines; <br/>

Defines custom constants using `#define` directives within the GLSL code for
both the vertex shader and the fragment shader; each key/value pair yields
another directive:  
```ts  
defines: {  
FOO: 15,  
BAR: true  
}  
```  
yields the lines  
```ts  
#define FOO 15  
#define BAR true  
```  
in the GLSL code.

### <br/> Object extensions; <br/>

An object with the following properties:  
```ts  
this.extensions = {  
derivatives: false, // set to use derivatives  
fragDepth: false, // set to use fragment depth values  
drawBuffers: false, // set to use draw buffers  
shaderTextureLOD: false // set to use  
shader texture LOD  
};  
```  

### <br/> Boolean fog; <br/>

Define whether the material color is affected by global fog settings; true to
pass fog uniforms to the shader. Default is false.

### <br/> String fragmentShader; <br/>

Fragment shader GLSL code. This is the actual code for the shader. In the
example above, the `vertexShader` and `fragmentShader` code is extracted from
the DOM; it could be passed as a string directly or loaded via AJAX instead.

### <br/> String glslVersion; <br/>

Defines the GLSL version of custom shader code. Only relevant for WebGL 2 in
order to define whether to specify GLSL 3.0 or not. Valid values are
`THREE.GLSL1` or `THREE.GLSL3`. Default is `null`.

### <br/> String index0AttributeName; <br/>

If set, this calls [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/bindAttribLocation
gl.bindAttribLocation] to bind a generic vertex index to an attribute
variable. Default is undefined.

### <br/> Boolean isShaderMaterial; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Boolean lights; <br/>

Defines whether this material uses lighting; true to pass uniform data related
to lighting to this shader. Default is false.

### <br/> Float linewidth; <br/>

Controls wireframe thickness. Default is `1`.  
  
Due to limitations of the
[link:https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf
OpenGL Core Profile] with the [page:WebGLRenderer WebGL] renderer on most
platforms linewidth will always be `1` regardless of the set value.

### <br/> Boolean flatShading; <br/>

Define whether the material is rendered with flat shading. Default is false.

### <br/> Object uniforms; <br/>

An object of the form:  
```ts  
{  
"uniform1": { value: 1.0 },  
"uniform2": { value: 2 }  
}  
```  
specifying the uniforms to be passed to the shader code; keys are uniform
names, values are definitions of the form  
```ts  
{  
value: 1.0  
}  
```  
where `value` is the value of the uniform. Names must match the name of the
uniform, as defined in the GLSL code. Note that uniforms are refreshed on
every frame, so updating the value of the uniform will immediately update the
value available to the GLSL code.

### <br/> Boolean uniformsNeedUpdate; <br/>

Can be used to force a uniform update while changing uniforms in
[page:Object3D.onBeforeRender](). Default is `false`.

### <br/> Boolean vertexColors; <br/>

Defines whether vertex coloring is used. Default is `false`.

### <br/> String vertexShader; <br/>

Vertex shader GLSL code. This is the actual code for the shader. In the
example above, the `vertexShader` and `fragmentShader` code is extracted from
the DOM; it could be passed as a string directly or loaded via AJAX instead.

### <br/> Boolean wireframe; <br/>

Render geometry as wireframe (using GL_LINES instead of GL_TRIANGLES). Default
is false (i.e. render as flat polygons).

### <br/> Float wireframeLinewidth; <br/>

Controls wireframe thickness. Default is `1`.  
  
Due to limitations of the
[link:https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf
OpenGL Core Profile] with the [page:WebGLRenderer WebGL] renderer on most
platforms linewidth will always be `1` regardless of the set value.

## Methods

See the base [page:Material] class for common methods.

### [method:ShaderMaterial clone]()

Generates a shallow copy of this material. Note that the vertexShader and
fragmentShader are copied `by reference`, as are the definitions of the
`attributes`; this means that clones of the material will share the same
compiled [page:WebGLProgram]. However, the `uniforms` are copied `by value`,
which allows you to have different sets of uniforms for different copies of
the material.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

