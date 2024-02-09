[page:Object3D] → [page:Line] →

# [name]

The GridHelper is an object to define grids. Grids are two-dimensional arrays
of lines.

## Code Example

  
```ts  
const size = 10;  
const divisions = 10;  
  
const gridHelper = new THREE.GridHelper( size, divisions );  
scene.add( gridHelper );  
```  

## Examples

[example:webgl_helpers WebGL / helpers]

## Constructor

###  [name]( [param:number size], [param:Number divisions], [param:Color
colorCenterLine], [param:Color colorGrid] )

size -- The size of the grid. Default is `10`.  
divisions -- The number of divisions across the grid. Default is `10`.  
colorCenterLine -- The color of the centerline. This can be a [page:Color], a
hexadecimal value and an CSS-Color name. Default is 0x444444  
colorGrid -- The color of the lines of the grid. This can be a [page:Color], a
hexadecimal value and an CSS-Color name. Default is 0x888888

Creates a new [name] of size 'size' and divided into 'divisions' segments per
side. Colors are optional.

## Methods

See the base [page:LineSegments] class for common methods.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

