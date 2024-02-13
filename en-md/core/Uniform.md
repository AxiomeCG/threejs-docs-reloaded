# Uniform

Uniforms are global GLSL variables. They are passed to shader programs.

## Code Example

When declaring a uniform of a [page:ShaderMaterial], it is declared by value
or by object.

  
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
of either five [page:Vector2] objects or ten `number`s.

Uniform typesGLSL type| JavaScript type  
---|---  
int| [page:Number]  
uint (WebGL 2)| [page:Number]  
float| [page:Number]  
bool| [page:Boolean]  
bool| [page:Number]  
vec2| [page:Vector2 THREE.Vector2]  
vec2| [page:Float32Array Float32Array] (*)  
vec2| [page:Array Array] (*)  
vec3| [page:Vector3 THREE.Vector3]  
vec3| [page:Color THREE.Color]  
vec3| [page:Float32Array Float32Array] (*)  
vec3| [page:Array Array] (*)  
vec4| [page:Vector4 THREE.Vector4]  
vec4| [page:Quaternion THREE.Quaternion]  
vec4| [page:Float32Array Float32Array] (*)  
vec4| [page:Array Array] (*)  
mat2| [page:Float32Array Float32Array] (*)  
mat2| [page:Array Array] (*)  
mat3| [page:Matrix3 THREE.Matrix3]  
mat3| [page:Float32Array Float32Array] (*)  
mat3| [page:Array Array] (*)  
mat4| [page:Matrix4 THREE.Matrix4]  
mat4| [page:Float32Array Float32Array] (*)  
mat4| [page:Array Array] (*)  
ivec2, bvec2| [page:Float32Array Float32Array] (*)  
ivec2, bvec2| [page:Array Array] (*)  
ivec3, bvec3| [page:Int32Array Int32Array] (*)  
ivec3, bvec3| [page:Array Array] (*)  
ivec4, bvec4| [page:Int32Array Int32Array] (*)  
ivec4, bvec4| [page:Array Array] (*)  
sampler2D| [page:Texture THREE.Texture]  
samplerCube| [page:CubeTexture THREE.CubeTexture]  
  
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

###  function Uniform( value: Object ): void;

value -- An object containing the value to set up the uniform. It's type must
be one of the Uniform Types described above.

## Properties

###  Object value;

Current value of the uniform.

## Methods

###  function clone( ): Uniform;

Returns a clone of this uniform.  
If the uniform's value property is an [page:Object] with a clone() method,
this is used, otherwise the value is copied by assignment. Array values are
shared between cloned [page:Uniform]s.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

