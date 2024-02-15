# WebGLRenderer Constants

## Cull Face Modes

  
```ts  
THREE.CullFaceNone THREE.CullFaceBack THREE.CullFaceFront
THREE.CullFaceFrontBack  
```  

[CullFaceNone](#) disables face culling.  
[CullFaceBack](#) culls back faces (default).  
[CullFaceFront](#) culls front faces.  
[CullFaceFrontBack](#) culls both front and back faces.

## Shadow Types

  
```ts  
THREE.BasicShadowMap THREE.PCFShadowMap THREE.PCFSoftShadowMap
THREE.VSMShadowMap  
```  

These define the WebGLRenderer's [shadowMap.type](#) property.  
  
[BasicShadowMap](#) gives unfiltered shadow maps - fastest, but lowest
quality.  
[PCFShadowMap](#) filters shadow maps using the Percentage-Closer Filtering
(PCF) algorithm (default).  
[PCFSoftShadowMap](#) filters shadow maps using the Percentage-Closer
Filtering (PCF) algorithm with better soft shadows especially when using low-
resolution shadow maps.  
[VSMShadowMap](#) filters shadow maps using the Variance Shadow Map (VSM)
algorithm. When using VSMShadowMap all shadow receivers will also cast
shadows.

## Tone Mapping

  
```ts  
THREE.NoToneMapping THREE.LinearToneMapping THREE.ReinhardToneMapping
THREE.CineonToneMapping THREE.ACESFilmicToneMapping THREE.CustomToneMapping  
```  

These define the WebGLRenderer's [toneMapping](#) property. This is used to
approximate the appearance of high dynamic range (HDR) on the low dynamic
range medium of a standard computer monitor or mobile device's screen.

THREE.LinearToneMapping, THREE.ReinhardToneMapping, THREE.CineonToneMapping
and THREE.ACESFilmicToneMapping are built-in implementations of tone mapping.
THREE.CustomToneMapping expects a custom implementation by modyfing GLSL code
of the material's fragment shader. See the [example:webgl_tonemapping WebGL /
tonemapping] example.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/constants.js">src/constants.js</a>

