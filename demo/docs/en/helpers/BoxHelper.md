[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →
[LineSegments](en\objects\LineSegments.html) →

# BoxHelper

Helper object to graphically show the world-axis-aligned bounding box around
an object. The actual bounding box is handled with [Box3](en\math\Box3.html),
this is just a visual helper for debugging. It can be automatically resized
with the [BoxHelper.update](#) method when the object it's created from is
transformed. Note that the object must have a
[BufferGeometry](en\core\BufferGeometry.html) for this to work, so it won't
work with [Sprites](en\objects\Sprite.html).

## Code Example

  
```ts  
const sphere = new THREE.SphereGeometry(); const object = new THREE.Mesh(
sphere, new THREE.MeshBasicMaterial( 0xff0000 ) ); const box = new
THREE.BoxHelper( object, 0xffff00 ); scene.add( box );  
```  

## Examples

[example:webgl_helpers WebGL / helpers]  
[example:webgl_loader_nrrd WebGL / loader / nrrd]  
[example:webgl_buffergeometry_drawrange WebGL / buffergeometry / drawrange]

## Constructor

### BoxHelper

  
  
```ts  
function BoxHelper( object: Object3D, color: Color ): void;  
```  

[object](en\core\Object3D.html) -- (optional) the object3D to show the world-
axis-aligned boundingbox.  
[color](en\math\Color.html) -- (optional) hexadecimal value that defines the
box's color. Default is 0xffff00.  
  
Creates a new wireframe box that bounds the passed object. Internally this
uses [Box3.setFromObject](#) to calculate the dimensions. Note that this
includes any children.

## Properties

See the base [LineSegments](en\objects\LineSegments.html) class for common
properties.

## Methods

See the base [LineSegments](en\objects\LineSegments.html) class for common
methods.

### update

  
  
```ts  
function update( ): undefined;  
```  

Updates the helper's geometry to match the dimensions of the object, including
any children. See [Box3.setFromObject](#).

### setFromObject

  
  
```ts  
function setFromObject( object: Object3D ): this;  
```  

[object](en\core\Object3D.html) - [Object3D](en\core\Object3D.html) to create
the helper of.  
  
Updates the wireframe box for the passed object.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/BoxHelper.js">src/helpers/BoxHelper.js</a>

