[Object3D](en\core\Object3D.html) →

# LOD

Level of Detail - show meshes with more or less geometry based on distance
from the camera.  
  
Every level is associated with an object, and rendering can be switched
between them at the distances specified. Typically you would create, say,
three meshes, one for far away (low detail), one for mid range (medium detail)
and one for close up (high detail).

## Code Example

  
```ts  
const lod = new THREE.LOD(); //Create spheres with 3 levels of detail and
create new LOD levels for them for( let i = 0; i < 3; i++ ) { const geometry =
new THREE.IcosahedronGeometry( 10, 3 - i ) const mesh = new THREE.Mesh(
geometry, material ); lod.addLevel( mesh, i * 75 ); } scene.add( lod );  
```  

## Examples

[example:webgl_lod webgl / lod ]

## Constructor

### LOD

  
  
```ts  
function LOD( ): void;  
```  

Creates a new LOD.

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### autoUpdate

  
  
```ts  
autoUpdate: Boolean;  
```  

Whether the LOD object is updated automatically by the renderer per frame or
not. If set to false, you have to call [LOD.update](#)() in the render loop by
yourself. Default is true.

### isLOD

  
  
```ts  
isLOD: Boolean;  
```  

Read-only flag to check if a given object is of type LOD.

### levels

  
  
```ts  
levels: Array;  
```  

An array of [level](#) objects  
  
Each level is an object with the following properties:  
[object](en\core\Object3D.html) - The [Object3D](en\core\Object3D.html) to
display at this level.  
[distance](#) - The distance at which to display this level of detail.  
[hysteresis](#) - Threshold used to avoid flickering at LOD boundaries, as a
fraction of distance.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### addLevel

  
  
```ts  
function addLevel( object: Object3D, distance: Float, hysteresis: Float ):
this;  
```  

[object](en\core\Object3D.html) - The [Object3D](en\core\Object3D.html) to
display at this level.  
[distance](#) - The distance at which to display this level of detail. Default
`0.0`.  
[hysteresis](#) - Threshold used to avoid flickering at LOD boundaries, as a
fraction of distance. Default `0.0`.  
  
Adds a mesh that will display at a certain distance and greater. Typically the
further away the distance, the lower the detail on the mesh.

### clone

  
  
```ts  
function clone( ): LOD;  
```  

Returns a clone of this LOD object with its associated levels.

### getCurrentLevel

  
  
```ts  
function getCurrentLevel( ): Integer;  
```  

Get the currently active LOD level. As index of the levels array.

### getObjectForDistance

  
  
```ts  
function getObjectForDistance( distance: Float ): Object3D;  
```  

Get a reference to the first [Object3D](en\core\Object3D.html) (mesh) that is
greater than [distance](#).

### raycast

  
  
```ts  
function raycast( raycaster: Raycaster, intersects: Array ): undefined;  
```  

Get intersections between a casted [Ray](en\math\Ray.html) and this LOD.
[Raycaster.intersectObject](#) will call this method.

### toJSON

  
  
```ts  
function toJSON( ): Object;  
```  

Create a JSON structure with details of this LOD object.

### update

  
  
```ts  
function update( camera: Camera ): undefined;  
```  

Set the visibility of each [level](#)'s [object](en\core\Object3D.html) based
on distance from the [camera](en\cameras\Camera.html).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/LOD.js">src/objects/LOD.js</a>

