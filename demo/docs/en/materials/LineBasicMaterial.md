[Material](en\materials\Material.html) →

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

### LineBasicMaterial

  
  
```ts  
function LineBasicMaterial( parameters: Object ): void;  
```  

[parameters](#) - (optional) an object with one or more properties defining
the material's appearance. Any property of the material (including any
property inherited from [Material](en\materials\Material.html)) can be passed
in here.  
  
The exception is the property [color](#), which can be passed in as a
hexadecimal string and is `0xffffff` (white) by default. [Color.set](#)( color
) is called internally.

## Properties

See the base [Material](en\materials\Material.html) class for common
properties.

### color

  
  
```ts  
color: Color;  
```  

[Color](en\math\Color.html) of the material, by default set to white
(0xffffff).

### fog

  
  
```ts  
fog: Boolean;  
```  

Whether the material is affected by fog. Default is `true`.

### linewidth

  
  
```ts  
linewidth: Float;  
```  

Controls line thickness. Default is `1`.  
  
Due to limitations of the <a
href="https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf">OpenGL
Core Profile</a> with the [WebGL](en\renderers\WebGLRenderer.html) renderer on
most platforms linewidth will always be `1` regardless of the set value.

### linecap

  
  
```ts  
linecap: String;  
```  

Define appearance of line ends. Possible values are 'butt', 'round' and
'square'. Default is 'round'.  
  
This corresponds to the <a
href="https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineCap">2D
Canvas lineCap</a> property and it is ignored by the
[WebGL](en\renderers\WebGLRenderer.html) renderer.

### linejoin

  
  
```ts  
linejoin: String;  
```  

Define appearance of line joints. Possible values are 'round', 'bevel' and
'miter'. Default is 'round'.  
  
This corresponds to the <a
href="https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineJoin">2D
Canvas lineJoin</a> property and it is ignored by the
[WebGL](en\renderers\WebGLRenderer.html) renderer.

### map

  
  
```ts  
map: Texture;  
```  

Sets the color of the lines using data from a
[Texture](en\textures\Texture.html).

## Methods

See the base [Material](en\materials\Material.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/materials/LineBasicMaterial.js">src/materials/LineBasicMaterial.js</a>

