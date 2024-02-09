[page:Material] →

# [name]

This material can receive shadows, but otherwise is completely transparent.

## Code Example

  
```ts  
const geometry = new THREE.PlaneGeometry( 2000, 2000 );  
geometry.rotateX( - Math.PI / 2 );  
  
const material = new THREE.ShadowMaterial();  
material.opacity = 0.2;  
  
const plane = new THREE.Mesh( geometry, material );  
plane.position.y = -200;  
plane.receiveShadow = true;  
scene.add( plane );  
```  

## Examples

[example:webgl_geometry_spline_editor geometry / spline / editor]

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.  
  

## Properties

See the base [page:Material] classes for common properties.

### <br/> Color color; <br/>

[page:Color] of the material, by default set to black (0x000000).

### <br/> Boolean fog; <br/>

Whether the material is affected by fog. Default is `true`.

### <br/> Boolean transparent; <br/>

Defines whether this material is transparent. Default is `true`.

## Methods

See the base [page:Material] classes for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

