[Material](en\materials\Material.html) →

# SpriteMaterial

A material for a use with a [Sprite](en\objects\Sprite.html).

## Code Example

  
```ts  
const map = new THREE.TextureLoader().load( 'textures/sprite.png' ); const
material = new THREE.SpriteMaterial( { map: map, color: 0xffffff } ); const
sprite = new THREE.Sprite( material ); sprite.scale.set(200, 200, 1)
scene.add( sprite );  
```  

## Examples

[example:webgl_raycaster_sprite WebGL / raycast / sprite]  
[example:webgl_sprites WebGL / sprites]  
[example:svg_sandbox SVG / sandbox]

## Constructor

### SpriteMaterial

  
  
```ts  
function SpriteMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.  
  
The exception is the property [color](#), which can be passed in as a
hexadecimal string and is `0xffffff` (white) by default. [Color.set](#)( color
) is called internally. SpriteMaterials are not clipped by using
[Material.clippingPlanes](#).

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
(0xffffff). The [.map](#) is multiplied by the color.

### fog

  
  
```ts  
fog: Boolean;  
```  

Whether the material is affected by fog. Default is `true`.

### isSpriteMaterial

  
  
```ts  
isSpriteMaterial: Boolean;  
```  

Read-only flag to check if a given object is of type SpriteMaterial.

### map

  
  
```ts  
map: Texture;  
```  

The color map. May optionally include an alpha channel, typically combined
with [.transparent](#) or [.alphaTest](#). Default is null.

### rotation

  
  
```ts  
rotation: Radians;  
```  

The rotation of the sprite in radians. Default is `0`.

### sizeAttenuation

  
  
```ts  
sizeAttenuation: Boolean;  
```  

Whether the size of the sprite is attenuated by the camera depth. (Perspective
camera only.) Default is `true`.

### transparent

  
  
```ts  
transparent: Boolean;  
```  

Defines whether this material is transparent. Default is `true`.

## Methods

See the base [Material](en\materials\Material.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/SpriteMaterial.js">src/materials/SpriteMaterial.js</a>

