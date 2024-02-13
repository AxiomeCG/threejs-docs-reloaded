[page:Material] →

# SpriteMaterial

A material for a use with a [page:Sprite].

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

###  function SpriteMaterial( parameters: Object ): void;

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.  
  
The exception is the property [page:Hexadecimal color], which can be passed in
as a hexadecimal string and is `0xffffff` (white) by default.
[page:Color.set]( color ) is called internally. SpriteMaterials are not
clipped by using [page:Material.clippingPlanes].

## Properties

See the base [page:Material] class for common properties.

###  Texture alphaMap;

The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Default is null.  
  
Only the color of the texture is used, ignoring the alpha channel if one
exists. For RGB and RGBA textures, the [page:WebGLRenderer WebGL] renderer
will use the green channel when sampling this texture due to the extra bit of
precision provided for green in DXT-compressed and uncompressed RGB 565
formats. Luminance-only and luminance/alpha textures will also still work as
expected.

###  Color color;

[page:Color] of the material, by default set to white (0xffffff). The
[page:.map] is multiplied by the color.

###  Boolean fog;

Whether the material is affected by fog. Default is `true`.

###  Boolean isSpriteMaterial;

Read-only flag to check if a given object is of type SpriteMaterial.

###  Texture map;

The color map. May optionally include an alpha channel, typically combined
with [page:Material.transparent .transparent] or [page:Material.alphaTest
.alphaTest]. Default is null.

###  Radians rotation;

The rotation of the sprite in radians. Default is `0`.

###  Boolean sizeAttenuation;

Whether the size of the sprite is attenuated by the camera depth. (Perspective
camera only.) Default is `true`.

###  Boolean transparent;

Defines whether this material is transparent. Default is `true`.

## Methods

See the base [page:Material] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

