[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →
[LineSegments](en\objects\LineSegments.html) →

# AxesHelper

An axis object to visualize the 3 axes in a simple way.  
The X axis is red. The Y axis is green. The Z axis is blue.

## Code Example

  
```ts  
const axesHelper = new THREE.AxesHelper( 5 );scene.add( axesHelper );  
```  

## Examples

[example:webgl_buffergeometry_compression WebGL / buffergeometry /
compression]  
[example:webgl_geometry_convex WebGL / geometry / convex]  
[example:webgl_loader_nrrd WebGL / loader / nrrd]

## Constructor

### AxesHelper

  
  
```ts  
function AxesHelper( size: Number ): void;  
```  

[size](#) -- (optional) size of the lines representing the axes. Default is
`1`.

## Properties

See the base [LineSegments](en\objects\LineSegments.html) class for common
properties.

## Methods

See the base [LineSegments](en\objects\LineSegments.html) class for common
methods.

### setColors

  
  
```ts  
function setColors( xAxisColor: Color, yAxisColor: Color, zAxisColor: Color ):
this;  
```  

Sets the axes colors to [xAxisColor](en\math\Color.html),
[yAxisColor](en\math\Color.html), [zAxisColor](en\math\Color.html).

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/AxesHelper.js">src/helpers/AxesHelper.js</a>

