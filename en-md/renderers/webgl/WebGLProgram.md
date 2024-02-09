# [name]

Constructor for the GLSL program sent to vertex and fragment shaders,
including default uniforms and attributes.

## Built-in uniforms and attributes

### Vertex shader (unconditional):

  
```ts  
// = object.matrixWorld  
uniform mat4 modelMatrix;  
  
// = camera.matrixWorldInverse * object.matrixWorld  
uniform mat4 modelViewMatrix;  
  
// = camera.projectionMatrix  
uniform mat4 projectionMatrix;  
  
// = camera.matrixWorldInverse  
uniform mat4 viewMatrix;  
  
// = inverse transpose of modelViewMatrix  
uniform mat3 normalMatrix;  
  
// = camera position in world space  
uniform vec3 cameraPosition;  
```  
  
```ts  
// default vertex attributes provided by BufferGeometry  
attribute vec3 position;  
attribute vec3 normal;  
attribute vec2 uv;  
```  

Note that you can therefore calculate the position of a vertex in the vertex
shader by:  
```ts  
gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );  
```  
or alternatively  
```ts  
gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4( position,
1.0 );  
```  

### Vertex shader (conditional):

  
```ts  
#ifdef USE_TANGENT  
attribute vec4 tangent;  
#endif  
#if defined( USE_COLOR_ALPHA )  
// vertex color attribute with alpha  
attribute vec4 color;  
#elif defined( USE_COLOR )  
// vertex color attribute  
attribute vec3 color;  
#endif  
```  
  
```ts  
#ifdef USE_MORPHTARGETS  
  
attribute vec3 morphTarget0;  
attribute vec3 morphTarget1;  
attribute vec3 morphTarget2;  
attribute vec3 morphTarget3;  
  
#ifdef USE_MORPHNORMALS  
  
attribute vec3 morphNormal0;  
attribute vec3 morphNormal1;  
attribute vec3 morphNormal2;  
attribute vec3 morphNormal3;  
  
#else  
  
attribute vec3 morphTarget4;  
attribute vec3 morphTarget5;  
attribute vec3 morphTarget6;  
attribute vec3 morphTarget7;  
  
#endif  
#endif  
```  
  
```ts  
#ifdef USE_SKINNING  
attribute vec4 skinIndex;  
attribute vec4 skinWeight;  
#endif  
```  
  
```ts  
#ifdef USE_INSTANCING  
// Note that modelViewMatrix is not set when rendering an instanced model,  
// but can be calculated from viewMatrix * modelMatrix.  
//  
// Basic Usage:  
// gl_Position = projectionMatrix * viewMatrix * modelMatrix * instanceMatrix
* vec4(position, 1.0);  
attribute mat4 instanceMatrix;  
#endif  
```  

### Fragment shader:

  
```ts  
uniform mat4 viewMatrix;  
uniform vec3 cameraPosition;  
```  

## Constructor

### [name]( [param:WebGLRenderer renderer], [param:String cacheKey],
[param:Object parameters] )

For parameters see [page:WebGLRenderer WebGLRenderer].

## Properties

### <br/> String name; <br/>

The name of the respective shader program.

### <br/> String id; <br/>

The identifier of this instance.

### <br/> String cacheKey; <br/>

This key enables the reusability of a single [name] for different materials.

### <br/> Integer usedTimes; <br/>

How many times this instance is used for rendering render items.

### <br/> Object program; <br/>

The actual shader program.

### <br/> WebGLShader vertexShader; <br/>

The vertex shader.

### <br/> WebGLShader fragmentShader; <br/>

The fragment shader.

## Methods

### [method:Object getUniforms]()

Returns a name-value mapping of all active uniform locations.

### [method:Object getAttributes]()

Returns a name-value mapping of all active vertex attribute locations.

### [method:undefined destroy]()

Destroys an instance of [name].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

