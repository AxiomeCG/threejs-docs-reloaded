[page:Object3D] → [page:Line] → [page:LineSegments] →

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

###  function AxesHelper( size: Number ): void;

[page:Number size] -- (optional) size of the lines representing the axes.
Default is `1`.

## Properties

See the base [page:LineSegments] class for common properties.

## Methods

See the base [page:LineSegments] class for common methods.

###  function setColors( xAxisColor: Color, yAxisColor: Color, zAxisColor:
Color ): this;

Sets the axes colors to [page:Color xAxisColor], [page:Color yAxisColor],
[page:Color zAxisColor].

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

