# Core Constants

## Revision Number

  
```ts  
THREE.REVISION  
```  

The current three.js [link:https://github.com/mrdoob/three.js/releases
revision number].

## Color Spaces

  
```ts  
THREE.NoColorSpace = ""THREE.SRGBColorSpace = "srgb"THREE.LinearSRGBColorSpace
= "srgb-linear"  
```  

[page:NoColorSpace] defines no specific color space. It is commonly used for
textures including normal maps, roughness maps, metalness maps, ambient
occlusion maps, and other non-color data.

[page:SRGBColorSpace] (“srgb”) refers to the color space defined by the Rec.
709 primaries, D65 white point, and nonlinear sRGB transfer functions. sRGB is
the default color space in CSS, and is often found in color palettes and color
pickers. Colors expressed in hexadecimal or CSS notation are typically in the
sRGB color space.

[page:LinearSRGBColorSpace] (“srgb-linear”) refers to the sRGB color space
(above) with linear transfer functions. Linear-sRGB is the working color space
in three.js, used throughout most of the rendering process. RGB components
found in three.js materials and shaders are in the Linear-sRGB color space.

For further background and usage, see _Color management_.

## Mouse Buttons

  
```ts  
THREE.MOUSE.LEFT THREE.MOUSE.MIDDLE THREE.MOUSE.RIGHT
THREE.MOUSE.ROTATETHREE.MOUSE.DOLLY THREE.MOUSE.PAN  
```  

The constants LEFT and ROTATE have the same underlying value. The constants
MIDDLE and DOLLY have the same underlying value. The constants RIGHT and PAN
have the same underlying value.

## Touch Actions

  
```ts  
THREE.TOUCH.ROTATE THREE.TOUCH.PAN
THREE.TOUCH.DOLLY_PANTHREE.TOUCH.DOLLY_ROTATE  
```  

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/constants.js
src/constants.js]

