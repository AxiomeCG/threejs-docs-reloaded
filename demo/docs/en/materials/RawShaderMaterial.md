[Material](en\materials\Material.html) →
[ShaderMaterial](en\materials\ShaderMaterial.html) →

# RawShaderMaterial

This class works just like [ShaderMaterial](en\materials\ShaderMaterial.html),
except that definitions of built-in uniforms and attributes are not
automatically prepended to the GLSL shader code.

## Code Example

  
```ts  
const material = new THREE.RawShaderMaterial( { uniforms: { time: { value: 1.0
} }, vertexShader: document.getElementById( 'vertexShader' ).textContent,
fragmentShader: document.getElementById( 'fragmentShader' ).textContent, } );  
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

### RawShaderMaterial

  
  
```ts  
function RawShaderMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html) and
[ShaderMaterial](en\materials\ShaderMaterial.html)) can be passed in here.  
  

## Properties

See the base [Material](en\materials\Material.html) and
[ShaderMaterial](en\materials\ShaderMaterial.html) classes for common
properties.

## Methods

See the base [Material](en\materials\Material.html) and
[ShaderMaterial](en\materials\ShaderMaterial.html) classes for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/RawShaderMaterial.js">src/materials/RawShaderMaterial.js</a>

