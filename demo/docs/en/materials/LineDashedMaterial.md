[Material](en\materials\Material.html) →
[LineBasicMaterial](en\materials\LineBasicMaterial.html) →

# LineDashedMaterial

A material for drawing wireframe-style geometries with dashed lines.

## Code Example

  
```ts  
const material = new THREE.LineDashedMaterial( { color: 0xffffff, linewidth:
1, scale: 1, dashSize: 3, gapSize: 1, } );  
```  

## Examples

[example:webgl_lines_dashed WebGL / lines / dashed]  

## Constructor

### LineDashedMaterial

  
  
```ts  
function LineDashedMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from
[LineBasicMaterial](en\materials\LineBasicMaterial.html)) can be passed in
here.

## Properties

See the base [LineBasicMaterial](en\materials\LineBasicMaterial.html) class
for common properties.

### dashSize

  
  
```ts  
dashSize: number;  
```  

The size of the dash. This is both the gap with the stroke. Default is `3`.

### gapSize

  
  
```ts  
gapSize: number;  
```  

The size of the gap. Default is `1`.

### isLineDashedMaterial

  
  
```ts  
isLineDashedMaterial: Boolean;  
```  

Read-only flag to check if a given object is of type LineDashedMaterial.

### scale

  
  
```ts  
scale: number;  
```  

The scale of the dashed part of a line. Default is `1`.

## Methods

See the base [LineBasicMaterial](en\materials\LineBasicMaterial.html) class
for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/LineDashedMaterial.js">src/materials/LineDashedMaterial.js</a>

