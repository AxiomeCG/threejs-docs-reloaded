[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →

# GridHelper

The GridHelper is an object to define grids. Grids are two-dimensional arrays
of lines.

## Code Example

  
```ts  
const size = 10; const divisions = 10; const gridHelper = new
THREE.GridHelper( size, divisions ); scene.add( gridHelper );  
```  

## Examples

[example:webgl_helpers WebGL / helpers]

## Constructor

### GridHelper

  
  
```ts  
function GridHelper( size: number, divisions: Number, colorCenterLine: Color,
colorGrid: Color ): void;  
```  

size -- The size of the grid. Default is `10`.  
divisions -- The number of divisions across the grid. Default is `10`.  
colorCenterLine -- The color of the centerline. This can be a
[Color](en\math\Color.html), a hexadecimal value and an CSS-Color name.
Default is 0x444444  
colorGrid -- The color of the lines of the grid. This can be a
[Color](en\math\Color.html), a hexadecimal value and an CSS-Color name.
Default is 0x888888

Creates a new GridHelper of size 'size' and divided into 'divisions' segments
per side. Colors are optional.

## Methods

See the base [LineSegments](en\objects\LineSegments.html) class for common
methods.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/GridHelper.js">src/helpers/GridHelper.js</a>

