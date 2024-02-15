# Material Constants

These constants define properties common to all material types, with the
exception of Texture Combine Operations which only apply to
[MeshBasicMaterial](#), [MeshLambertMaterial](#) and [MeshPhongMaterial](#).  

## Side

  
```ts  
THREE.FrontSide THREE.BackSide THREE.DoubleSide  
```  

Defines which side of faces will be rendered - front, back or both. Default is
[FrontSide](#).

## Blending Mode

  
```ts  
THREE.NoBlending THREE.NormalBlending THREE.AdditiveBlending
THREE.SubtractiveBlending THREE.MultiplyBlending THREE.CustomBlending  
```  

These control the source and destination blending equations for the material's
RGB and Alpha sent to the WebGLRenderer for use by WebGL.  
[NormalBlending](#) is the default.  
Note that [CustomBlending](#) must be set to use [Custom Blending
Equations](#).  
See the [example:webgl_materials_blending materials / blending] example.  

## Depth Mode

  
```ts  
THREE.NeverDepth THREE.AlwaysDepth THREE.EqualDepth THREE.LessDepth
THREE.LessEqualDepth THREE.GreaterEqualDepth THREE.GreaterDepth
THREE.NotEqualDepth  
```  

Which depth function the material uses to compare incoming pixels Z-depth
against the current Z-depth buffer value. If the result of the comparison is
true, the pixel will be drawn.  
[NeverDepth](en\constants\Materials.html) will never return true.  
[AlwaysDepth](en\constants\Materials.html) will always return true.  
[EqualDepth](en\constants\Materials.html) will return true if the incoming
pixel Z-depth is equal to the current buffer Z-depth.  
[LessDepth](en\constants\Materials.html) will return true if the incoming
pixel Z-depth is less than the current buffer Z-depth.  
[LessEqualDepth](en\constants\Materials.html) is the default and will return
true if the incoming pixel Z-depth is less than or equal to the current buffer
Z-depth.  
[GreaterEqualDepth](en\constants\Materials.html) will return true if the
incoming pixel Z-depth is greater than or equal to the current buffer Z-depth.  
[GreaterDepth](en\constants\Materials.html) will return true if the incoming
pixel Z-depth is greater than the current buffer Z-depth.  
[NotEqualDepth](en\constants\Materials.html) will return true if the incoming
pixel Z-depth is not equal to the current buffer Z-depth.  

## Texture Combine Operations

  
```ts  
THREE.MultiplyOperation THREE.MixOperation THREE.AddOperation  
```  

These define how the result of the surface's color is combined with the
environment map (if present), for [MeshBasicMaterial](#),
[MeshLambertMaterial](#) and [MeshPhongMaterial](#).  
[MultiplyOperation](#) is the default and multiplies the environment map color
with the surface color.  
[MixOperation](#) uses reflectivity to blend between the two colors.  
[AddOperation](#) adds the two colors.

## Stencil Functions

  
```ts  
THREE.NeverStencilFunc THREE.LessStencilFunc THREE.EqualStencilFunc
THREE.LessEqualStencilFunc THREE.GreaterStencilFunc THREE.NotEqualStencilFunc
THREE.GreaterEqualStencilFunc THREE.AlwaysStencilFunc  
```  

Which stencil function the material uses to determine whether or not to
perform a stencil operation.  
[NeverStencilFunc](en\constants\Materials.html) will never return true.  
[LessStencilFunc](en\constants\Materials.html) will return true if the stencil
reference value is less than the current stencil value.  
[EqualStencilFunc](en\constants\Materials.html) will return true if the
stencil reference value is equal to the current stencil value.  
[LessEqualStencilFunc](en\constants\Materials.html) will return true if the
stencil reference value is less than or equal to the current stencil value.  
[GreaterStencilFunc](en\constants\Materials.html) will return true if the
stencil reference value is greater than the current stencil value.  
[NotEqualStencilFunc](en\constants\Materials.html) will return true if the
stencil reference value is not equal to the current stencil value.  
[GreaterEqualStencilFunc](en\constants\Materials.html) will return true if the
stencil reference value is greater than or equal to the current stencil value.  
[AlwaysStencilFunc](en\constants\Materials.html) will always return true.  

## Stencil Operations

  
```ts  
THREE.ZeroStencilOp THREE.KeepStencilOp THREE.ReplaceStencilOp
THREE.IncrementStencilOp THREE.DecrementStencilOp THREE.IncrementWrapStencilOp
THREE.DecrementWrapStencilOp THREE.InvertStencilOp  
```  

Which stencil operation the material will perform on the stencil buffer pixel
if the provided stencil function passes.  
[ZeroStencilOp](en\constants\Materials.html) will set the stencil value to
`0`.  
[KeepStencilOp](en\constants\Materials.html) will not change the current
stencil value.  
[ReplaceStencilOp](en\constants\Materials.html) will replace the stencil value
with the specified stencil reference value.  
[IncrementStencilOp](en\constants\Materials.html) will increment the current
stencil value by `1`.  
[DecrementStencilOp](en\constants\Materials.html) will decrement the current
stencil value by `1`.  
[IncrementWrapStencilOp](en\constants\Materials.html) will increment the
current stencil value by `1`. If the value increments past `255` it will be
set to `0`.  
[DecrementWrapStencilOp](en\constants\Materials.html) will increment the
current stencil value by `1`. If the value decrements below `0` it will be set
to `255`.  
[InvertStencilOp](en\constants\Materials.html) will perform a bitwise
inversion of the current stencil value.  

## Normal map type

  
```ts  
THREE.TangentSpaceNormalMap THREE.ObjectSpaceNormalMap  
```  

Defines the type of the normal map. For TangentSpaceNormalMap, the information
is relative to the underlying surface. For ObjectSpaceNormalMap, the
information is relative to the object orientation. Default is
[TangentSpaceNormalMap](#).

## GLSL Version

  
```ts  
THREE.GLSL1 THREE.GLSL3  
```  

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/constants.js">src/constants.js</a>

