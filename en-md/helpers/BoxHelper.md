[page:Object3D] → [page:Line] → [page:LineSegments] →

# [name]

Helper object to graphically show the world-axis-aligned bounding box around
an object. The actual bounding box is handled with [page:Box3], this is just a
visual helper for debugging. It can be automatically resized with the
[page:BoxHelper.update] method when the object it's created from is
transformed. Note that the object must have a [page:BufferGeometry] for this
to work, so it won't work with [page:Sprite Sprites].

## Code Example

  
```ts  
const sphere = new THREE.SphereGeometry();  
const object = new THREE.Mesh( sphere, new THREE.MeshBasicMaterial( 0xff0000 )
);  
const box = new THREE.BoxHelper( object, 0xffff00 );  
scene.add( box );  
```  

## Examples

[example:webgl_helpers WebGL / helpers]  
[example:webgl_loader_nrrd WebGL / loader / nrrd]  
[example:webgl_buffergeometry_drawrange WebGL / buffergeometry / drawrange]

## Constructor

### [name]( [param:Object3D object], [param:Color color] )

[page:Object3D object] -- (optional) the object3D to show the world-axis-
aligned boundingbox.  
[page:Color color] -- (optional) hexadecimal value that defines the box's
color. Default is 0xffff00.  
  
Creates a new wireframe box that bounds the passed object. Internally this
uses [page:Box3.setFromObject] to calculate the dimensions. Note that this
includes any children.

## Properties

See the base [page:LineSegments] class for common properties.

## Methods

See the base [page:LineSegments] class for common methods.

### [method:undefined update]()

Updates the helper's geometry to match the dimensions of the object, including
any children. See [page:Box3.setFromObject].

### <br/> function setFromObject( object: Object3D ): setFromObject; <br/>

[page:Object3D object] - [page:Object3D] to create the helper of.  
  
Updates the wireframe box for the passed object.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

