[page:Object3D] → [page:Line] →

# PolarGridHelper

The PolarGridHelper is an object to define polar grids. Grids are two-
dimensional arrays of lines.

## Code Example

  
```ts  
const radius = 10; const sectors = 16; const rings = 8; const divisions = 64;
const helper = new THREE.PolarGridHelper( radius, sectors, rings, divisions );
scene.add( helper );  
```  

## Examples

[example:webgl_helpers WebGL / helpers]

## Constructor

###  function PolarGridHelper( radius: Number, sectors: Number, rings: Number,
divisions: Number, color1: Color, color2: Color ): void;

radius -- The radius of the polar grid. This can be any positive number.
Default is `10`.  
sectors -- The number of sectors the grid will be divided into. This can be
any positive integer. Default is `16`.  
rings -- The number of rings. This can be any positive integer. Default is 8.  
divisions -- The number of line segments used for each circle. This can be any
positive integer that is 3 or greater. Default is `64`.  
color1 -- The first color used for grid elements. This can be a [page:Color],
a hexadecimal value and an CSS-Color name. Default is 0x444444  
color2 -- The second color used for grid elements. This can be a [page:Color],
a hexadecimal value and an CSS-Color name. Default is 0x888888

Creates a new PolarGridHelper of radius 'radius' with 'sectors' number of
sectors and 'rings' number of rings, where each circle is smoothed into
'divisions' number of line segments. Colors are optional.

## Methods

See the base [page:LineSegments] class for common methods.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

