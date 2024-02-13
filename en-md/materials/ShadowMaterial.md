[page:Material] →

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

###  function ShadowMaterial( parameters: Object ): void;

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.  
  

## Properties

See the base [page:Material] classes for common properties.

###  Color color;

[page:Color] of the material, by default set to black (0x000000).

###  Boolean fog;

Whether the material is affected by fog. Default is `true`.

###  Boolean transparent;

Defines whether this material is transparent. Default is `true`.

## Methods

See the base [page:Material] classes for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

