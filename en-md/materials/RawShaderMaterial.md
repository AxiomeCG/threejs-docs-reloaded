[page:Material] → [page:ShaderMaterial] →

# [name]

This class works just like [page:ShaderMaterial], except that definitions of
built-in uniforms and attributes are not automatically prepended to the GLSL
shader code.

## Code Example

  
```ts  
const material = new THREE.RawShaderMaterial( {  
  
uniforms: {  
time: { value: 1.0 }  
},  
vertexShader: document.getElementById( 'vertexShader' ).textContent,  
fragmentShader: document.getElementById( 'fragmentShader' ).textContent,  
  
} );  
```  

## Examples

[example:webgl_buffergeometry_rawshader WebGL / buffergeometry / rawshader]  
[example:webgl_buffergeometry_instancing_billboards WebGL / buffergeometry /
instancing / billboards]  
[example:webgl_buffergeometry_instancing WebGL / buffergeometry / instancing]  
[example:webgl_raymarching_reflect WebGL / raymarching / reflect]  
[example:webgl2_volume_cloud WebGL 2 / volume / cloud]  
[example:webgl2_volume_instancing WebGL 2 / volume / instancing]  
[example:webgl2_volume_perlin WebGL 2 / volume / perlin]

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material] and [page:ShaderMaterial]) can be
passed in here.  
  

## Properties

See the base [page:Material] and [page:ShaderMaterial] classes for common
properties.

## Methods

See the base [page:Material] and [page:ShaderMaterial] classes for common
methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

