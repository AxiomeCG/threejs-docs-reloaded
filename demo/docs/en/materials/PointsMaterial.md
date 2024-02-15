[Material](en\materials\Material.html) →

# PointsMaterial

The default material used by [Points](en\objects\Points.html).

## Code Example

  
```ts  
const vertices = []; for ( let i = 0; i < 10000; i ++ ) { const x =
THREE.MathUtils.randFloatSpread( 2000 ); const y =
THREE.MathUtils.randFloatSpread( 2000 ); const z =
THREE.MathUtils.randFloatSpread( 2000 ); vertices.push( x, y, z ); } const
geometry = new THREE.BufferGeometry(); geometry.setAttribute( 'position', new
THREE.Float32BufferAttribute( vertices, 3 ) ); const material = new
THREE.PointsMaterial( { color: 0x888888 } ); const points = new THREE.Points(
geometry, material ); scene.add( points );  
```  

## Examples

[example:misc_controls_fly misc / controls / fly]  
[example:webgl_buffergeometry_drawrange WebGL / BufferGeometry / drawrange]  
[example:webgl_buffergeometry_points WebGL / BufferGeometry / points]  
[example:webgl_buffergeometry_points_interleaved WebGL / BufferGeometry /
points / interleaved]  
[example:webgl_camera WebGL / camera ]  
[example:webgl_geometry_convex WebGL / geometry / convex]  
[example:webgl_geometry_shapes WebGL / geometry / shapes]  
[example:webgl_interactive_raycasting_points WebGL / interactive / raycasting
/ points]  
[example:webgl_multiple_elements_text WebGL / multiple / elements / text]  
[example:webgl_points_billboards WebGL / points / billboards]  
[example:webgl_points_dynamic WebGL / points / dynamic]  
[example:webgl_points_sprites WebGL / points / sprites]

## Constructor

### PointsMaterial

  
  
```ts  
function PointsMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.  
  
The exception is the property [color](#), which can be passed in as a
hexadecimal string and is `0xffffff` (white) by default. [Color.set](#)( color
) is called internally.

## Properties

See the base [Material](en\materials\Material.html) class for common
properties.

### alphaMap

  
  
```ts  
alphaMap: Texture;  
```  

The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Default is null.  
  
Only the color of the texture is used, ignoring the alpha channel if one
exists. For RGB and RGBA textures, the
[WebGL](en\renderers\WebGLRenderer.html) renderer will use the green channel
when sampling this texture due to the extra bit of precision provided for
green in DXT-compressed and uncompressed RGB 565 formats. Luminance-only and
luminance/alpha textures will also still work as expected.

### color

  
  
```ts  
color: Color;  
```  

[Color](en\math\Color.html) of the material, by default set to white
(0xffffff).

### fog

  
  
```ts  
fog: Boolean;  
```  

Whether the material is affected by fog. Default is `true`.

### map

  
  
```ts  
map: Texture;  
```  

Sets the color of the points using data from a
[Texture](en\textures\Texture.html). May optionally include an alpha channel,
typically combined with [.transparent](#) or [.alphaTest](#).

### size

  
  
```ts  
size: Number;  
```  

Defines the size of the points in pixels. Default is `1.0`.  
Will be capped if it exceeds the hardware dependent parameter <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/getParameter">gl.ALIASED_POINT_SIZE_RANGE</a>.

### sizeAttenuation

  
  
```ts  
sizeAttenuation: Boolean;  
```  

Specify whether points' size is attenuated by the camera depth. (Perspective
camera only.) Default is true.

## Methods

See the base [Material](en\materials\Material.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/PointsMaterial.js">src/materials/PointsMaterial.js</a>

