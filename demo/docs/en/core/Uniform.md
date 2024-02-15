# Uniform

Uniforms are global GLSL variables. They are passed to shader programs.

## Code Example

When declaring a uniform of a
[ShaderMaterial](en\materials\ShaderMaterial.html), it is declared by value or
by object.

  
```ts  
uniforms: { time: { value: 1.0 }, resolution: new Uniform( new Vector2() ) };  
```  

## Uniform types

Each uniform must have a `value` property. The type of the value must
correspond to the type of the uniform variable in the GLSL code as specified
for the primitive GLSL types in the table below. Uniform structures and arrays
are also supported. GLSL arrays of primitive type must either be specified as
an array of the corresponding THREE objects or as a flat array containing the
data of all the objects. In other words; GLSL primitives in arrays must not be
represented by arrays. This rule does not apply transitively. An array of
`vec2` arrays, each with a length of five vectors, must be an array of arrays,
of either five [Vector2](en\math\Vector2.html) objects or ten `number`s.

Uniform typesGLSL type| JavaScript type  
---|---  
int| [Number](#)  
uint (WebGL 2)| [Number](#)  
float| [Number](#)  
bool| [Boolean](#)  
bool| [Number](#)  
vec2| [THREE.Vector2](en\math\Vector2.html)  
vec2| [Float32Array](#) (*)  
vec2| [Array](#) (*)  
vec3| [THREE.Vector3](en\math\Vector3.html)  
vec3| [THREE.Color](en\math\Color.html)  
vec3| [Float32Array](#) (*)  
vec3| [Array](#) (*)  
vec4| [THREE.Vector4](en\math\Vector4.html)  
vec4| [THREE.Quaternion](en\math\Quaternion.html)  
vec4| [Float32Array](#) (*)  
vec4| [Array](#) (*)  
mat2| [Float32Array](#) (*)  
mat2| [Array](#) (*)  
mat3| [THREE.Matrix3](en\math\Matrix3.html)  
mat3| [Float32Array](#) (*)  
mat3| [Array](#) (*)  
mat4| [THREE.Matrix4](en\math\Matrix4.html)  
mat4| [Float32Array](#) (*)  
mat4| [Array](#) (*)  
ivec2, bvec2| [Float32Array](#) (*)  
ivec2, bvec2| [Array](#) (*)  
ivec3, bvec3| [Int32Array](#) (*)  
ivec3, bvec3| [Array](#) (*)  
ivec4, bvec4| [Int32Array](#) (*)  
ivec4, bvec4| [Array](#) (*)  
sampler2D| [THREE.Texture](en\textures\Texture.html)  
samplerCube| [THREE.CubeTexture](en\textures\CubeTexture.html)  
  
(*) Same for an (innermost) array (dimension) of the same GLSL type,
containing the components of all vectors or matrices in the array.

## Structured Uniforms

Sometimes you want to organize uniforms as `structs` in your shader code. The
following style must be used so `three.js` is able to process structured
uniform data.

  
```ts  
uniforms = { data: { value: { position: new Vector3(), direction: new Vector3(
0, 0, 1 ) } } };  
```  
This definition can be mapped on the following GLSL code:  
```ts  
struct Data { vec3 position; vec3 direction; }; uniform Data data;  
```  

## Structured Uniforms with Arrays

It's also possible to manage `structs` in arrays. The syntax for this use case
looks like so:

  
```ts  
const entry1 = { position: new Vector3(), direction: new Vector3( 0, 0, 1 ) };
const entry2 = { position: new Vector3( 1, 1, 1 ), direction: new Vector3( 0,
1, 0 ) }; uniforms = { data: { value: [ entry1, entry2 ] } };  
```  
This definition can be mapped on the following GLSL code:  
```ts  
struct Data { vec3 position; vec3 direction; }; uniform Data data[ 2 ];  
```  

## Constructor

### Uniform

  
  
```ts  
function Uniform( value: Object ): void;  
```  

value -- An object containing the value to set up the uniform. It's type must
be one of the Uniform Types described above.

## Properties

### value

  
  
```ts  
value: Object;  
```  

Current value of the uniform.

## Methods

### clone

  
  
```ts  
function clone( ): Uniform;  
```  

Returns a clone of this uniform.  
If the uniform's value property is an [Object](#) with a clone() method, this
is used, otherwise the value is copied by assignment. Array values are shared
between cloned [Uniform](en\core\Uniform.html)s.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/Uniform.js">src/core/Uniform.js</a>

