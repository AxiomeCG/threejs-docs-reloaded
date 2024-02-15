# ImageUtils

A class containing utility functions for images.

## Methods

### getDataURL

  
  
```ts  
function getDataURL( image: HTMLCanvasElement, image: HTMLImageElement, image:
ImageBitmap ): String;  
```  

image -- The image object.  
  
Returns a data URI containing a representation of the given image.

### sRGBToLinear

  
  
```ts  
function sRGBToLinear( image: HTMLCanvasElement, image: HTMLImageElement,
image: ImageBitmap ): Object;  
```  

image -- The image object.  
  
Converts the given sRGB image data to linear color space.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/ImageUtils.js">src/extras/ImageUtils.js</a>

