# Custom Blending Equation Constants

These work with all material types. First set the material's blending mode to
THREE.CustomBlending, then set the desired Blending Equation, Source Factor
and Destination Factor.

## Code Example

  
```ts  
const material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
material.blending = THREE.CustomBlending; material.blendEquation =
THREE.AddEquation; //default material.blendSrc = THREE.SrcAlphaFactor;
//default material.blendDst = THREE.OneMinusSrcAlphaFactor; //default  
```  

## Examples

[example:webgl_materials_blending_custom materials / blending / custom ]

## Blending Equations

  
```ts  
THREE.AddEquation THREE.SubtractEquation THREE.ReverseSubtractEquation
THREE.MinEquation THREE.MaxEquation  
```  

## Source Factors

  
```ts  
THREE.ZeroFactor THREE.OneFactor THREE.SrcColorFactor
THREE.OneMinusSrcColorFactor THREE.SrcAlphaFactor THREE.OneMinusSrcAlphaFactor
THREE.DstAlphaFactor THREE.OneMinusDstAlphaFactor THREE.DstColorFactor
THREE.OneMinusDstColorFactor THREE.SrcAlphaSaturateFactor  
```  

## Destination Factors

All of the Source Factors are valid as Destination Factors, except for  
```ts  
THREE.SrcAlphaSaturateFactor  
```  

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/constants.js
src/constants.js]

