[Material](en\materials\Material.html) →

# ShadowMaterial

This material can receive shadows, but otherwise is completely transparent.

## Code Example

  
```ts  
const geometry = new THREE.PlaneGeometry( 2000, 2000 ); geometry.rotateX( -
Math.PI / 2 ); const material = new THREE.ShadowMaterial(); material.opacity =
0.2; const plane = new THREE.Mesh( geometry, material ); plane.position.y =
-200; plane.receiveShadow = true; scene.add( plane );  
```  

## Examples

[example:webgl_geometry_spline_editor geometry / spline / editor]

## Constructor

### ShadowMaterial

  
  
```ts  
function ShadowMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.  
  

## Properties

See the base [Material](en\materials\Material.html) classes for common
properties.

### color

  
  
```ts  
color: Color;  
```  

[Color](en\math\Color.html) of the material, by default set to black
(0x000000).

### fog

  
  
```ts  
fog: Boolean;  
```  

Whether the material is affected by fog. Default is `true`.

### transparent

  
  
```ts  
transparent: Boolean;  
```  

Defines whether this material is transparent. Default is `true`.

## Methods

See the base [Material](en\materials\Material.html) classes for common
methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/ShadowMaterial.js">src/materials/ShadowMaterial.js</a>

