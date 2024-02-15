[BufferGeometry](en\core\BufferGeometry.html) →

# WireframeGeometry

This can be used as a helper object to view a
[geometry](en\core\BufferGeometry.html) as a wireframe.

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

### WireframeGeometry

  
  
```ts  
function WireframeGeometry( geometry: BufferGeometry ): void;  
```  

geometry — any geometry object.

## Properties

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
properties.

## Methods

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/WireframeGeometry.js">src/geometries/WireframeGeometry.js</a>

