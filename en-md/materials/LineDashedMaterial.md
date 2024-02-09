[page:Material] → [page:LineBasicMaterial] →

# [name]

A material for drawing wireframe-style geometries with dashed lines.

## Code Example

  
```ts  
const material = new THREE.LineDashedMaterial( {  
color: 0xffffff,  
linewidth: 1,  
scale: 1,  
dashSize: 3,  
gapSize: 1,  
} );  
```  

## Examples

[example:webgl_lines_dashed WebGL / lines / dashed]  

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:LineBasicMaterial]) can be passed in here.

## Properties

See the base [page:LineBasicMaterial] class for common properties.

### <br/> number dashSize; <br/>

The size of the dash. This is both the gap with the stroke. Default is `3`.

### <br/> number gapSize; <br/>

The size of the gap. Default is `1`.

### <br/> Boolean isLineDashedMaterial; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> number scale; <br/>

The scale of the dashed part of a line. Default is `1`.

## Methods

See the base [page:LineBasicMaterial] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

