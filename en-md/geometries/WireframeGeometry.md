[page:BufferGeometry] →

# WireframeGeometry

This can be used as a helper object to view a [page:BufferGeometry geometry]
as a wireframe.

## Code Example

  
```ts  
const geometry = new THREE.SphereGeometry( 100, 100, 100 ); const wireframe =
new THREE.WireframeGeometry( geometry ); const line = new THREE.LineSegments(
wireframe ); line.material.depthTest = false; line.material.opacity = 0.25;
line.material.transparent = true; scene.add( line );  
```  

## Examples

[example:webgl_helpers helpers]

## Constructor

###  function WireframeGeometry( geometry: BufferGeometry ): void;

geometry — any geometry object.

## Properties

See the base [page:BufferGeometry] class for common properties.

## Methods

See the base [page:BufferGeometry] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

