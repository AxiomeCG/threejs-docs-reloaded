[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →
[LineSegments](en\objects\LineSegments.html) →

# Box3Helper

Helper object to visualize a [Box3](en\math\Box3.html).

## Code Example

  
```ts  
const box = new THREE.Box3(); box.setFromCenterAndSize( new THREE.Vector3( 1,
1, 1 ), new THREE.Vector3( 2, 1, 3 ) ); const helper = new THREE.Box3Helper(
box, 0xffff00 ); scene.add( helper );  
```  

## Constructor

### Box3Helper

  
  
```ts  
function Box3Helper( box: Box3, color: Color ): void;  
```  

[box](en\math\Box3.html) -- the Box3 to show.  
[color](en\math\Color.html) -- (optional) the box's color. Default is
0xffff00.  
  
Creates a new wireframe box that represents the passed Box3.

## Properties

See the base [LineSegments](en\objects\LineSegments.html) class for common
properties.

### box

  
  
```ts  
box: Box3;  
```  

The Box3 being visualized.

## Methods

See the base [LineSegments](en\objects\LineSegments.html) class for common
methods.

### updateMatrixWorld

  
  
```ts  
function updateMatrixWorld( force: Boolean ): undefined;  
```  

This overrides the method in the base [Object3D](en\core\Object3D.html) class
so that it also updates the wireframe box to the extent of the [.box](#)
property.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/Box3Helper.js">src/helpers/Box3Helper.js</a>

