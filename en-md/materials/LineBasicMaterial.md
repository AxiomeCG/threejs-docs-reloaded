[page:Material] →

# LineBasicMaterial

A material for drawing wireframe-style geometries.

## Code Example

  
```ts  
const material = new THREE.LineBasicMaterial( { color: 0xffffff, linewidth: 1,
linecap: 'round', //ignored by WebGLRenderer linejoin: 'round' //ignored by
WebGLRenderer } );  
```  

## Examples

[example:webgl_buffergeometry_drawrange WebGL / buffergeometry / drawrange]  
[example:webgl_buffergeometry_lines WebGL / buffergeometry / lines]  
[example:webgl_buffergeometry_lines_indexed WebGL / buffergeometry / lines /
indexed]  
[example:webgl_decals WebGL / decals]  
[example:webgl_geometry_nurbs WebGL / geometry / nurbs]  
[example:webgl_geometry_shapes WebGL / geometry / shapes]  
[example:webgl_geometry_spline_editor WebGL / geometry / spline / editor]  
[example:webgl_interactive_buffergeometry WebGL / interactive /
buffergeometry]  
[example:webgl_interactive_voxelpainter WebGL / interactive / voxelpainter]  
[example:webgl_lines_colors WebGL / lines / colors]  
[example:webgl_lines_dashed WebGL / lines / dashed]  
[example:physics_ammo_rope physics / ammo / rope]

## Constructor

###  function LineBasicMaterial( parameters: Object ): void;

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.  
  
The exception is the property [page:Hexadecimal color], which can be passed in
as a hexadecimal string and is `0xffffff` (white) by default.
[page:Color.set]( color ) is called internally.

## Properties

See the base [page:Material] class for common properties.

###  Color color;

[page:Color] of the material, by default set to white (0xffffff).

###  Boolean fog;

Whether the material is affected by fog. Default is `true`.

###  Float linewidth;

Controls line thickness. Default is `1`.  
  
Due to limitations of the
[link:https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf
OpenGL Core Profile] with the [page:WebGLRenderer WebGL] renderer on most
platforms linewidth will always be `1` regardless of the set value.

###  String linecap;

Define appearance of line ends. Possible values are 'butt', 'round' and
'square'. Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineCap
2D Canvas lineCap] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

###  String linejoin;

Define appearance of line joints. Possible values are 'round', 'bevel' and
'miter'. Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineJoin
2D Canvas lineJoin] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

###  Texture map;

Sets the color of the lines using data from a [page:Texture].

## Methods

See the base [page:Material] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

