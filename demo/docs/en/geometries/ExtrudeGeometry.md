[BufferGeometry](en\core\BufferGeometry.html) →

# ExtrudeGeometry

Creates extruded geometry from a path shape.

## Code Example

  
```ts  
const length = 12, width = 8; const shape = new THREE.Shape(); shape.moveTo(
0,0 ); shape.lineTo( 0, width ); shape.lineTo( length, width ); shape.lineTo(
length, 0 ); shape.lineTo( 0, 0 ); const extrudeSettings = { steps: 2, depth:
16, bevelEnabled: true, bevelThickness: 1, bevelSize: 1, bevelOffset: 0,
bevelSegments: 1 }; const geometry = new THREE.ExtrudeGeometry( shape,
extrudeSettings ); const material = new THREE.MeshBasicMaterial( { color:
0x00ff00 } ); const mesh = new THREE.Mesh( geometry, material ) ; scene.add(
mesh );  
```  

## Constructor

### ExtrudeGeometry

  
  
```ts  
function ExtrudeGeometry( shapes: Array, options: Object ): void;  
```  

shapes — Shape or an array of shapes.  
options — Object that can contain the following parameters.

  * curveSegments — int. Number of points on the curves. Default is `12`.
  * steps — int. Number of points used for subdividing segments along the depth of the extruded spline. Default is `1`.
  * depth — float. Depth to extrude the shape. Default is `1`.
  * bevelEnabled — bool. Apply beveling to the shape. Default is true.
  * bevelThickness — float. How deep into the original shape the bevel goes. Default is `0.2`.
  * bevelSize — float. Distance from the shape outline that the bevel extends. Default is bevelThickness - 0.1.
  * bevelOffset — float. Distance from the shape outline that the bevel starts. Default is `0`.
  * bevelSegments — int. Number of bevel layers. Default is `3`.
  * extrudePath — THREE.Curve. A 3D spline path along which the shape should be extruded. Bevels not supported for path extrusion.
  * UVGenerator — Object. object that provides UV generator functions

This object extrudes a 2D shape to a 3D geometry.

When creating a Mesh with this geometry, if you'd like to have a separate
material used for its face and its extruded sides, you can use an array of
materials. The first material will be applied to the face; the second material
will be applied to the sides.

## Properties

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
properties.

### parameters

  
  
```ts  
parameters: Object;  
```  

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [BufferGeometry](en\core\BufferGeometry.html) class for common
methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/ExtrudeGeometry.js">src/geometries/ExtrudeGeometry.js</a>

