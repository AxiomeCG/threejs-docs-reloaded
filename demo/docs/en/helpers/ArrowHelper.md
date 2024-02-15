[Object3D](en\core\Object3D.html) →

# ArrowHelper

An 3D arrow object for visualizing directions.

## Code Example

  
```ts  
const dir = new THREE.Vector3( 1, 2, 0 ); //normalize the direction vector
(convert to vector of length 1) dir.normalize(); const origin = new
THREE.Vector3( 0, 0, 0 ); const length = 1; const hex = 0xffff00; const
arrowHelper = new THREE.ArrowHelper( dir, origin, length, hex ); scene.add(
arrowHelper );  
```  

## Examples

[example:webgl_shadowmesh WebGL / shadowmesh]

## Constructor

### ArrowHelper

  
  
```ts  
function ArrowHelper( dir: Vector3, origin: Vector3, length: Number, hex:
Number, headLength: Number, headWidth: Number ): void;  
```  

[dir](en\math\Vector3.html) -- direction from origin. Must be a unit vector.  
[origin](en\math\Vector3.html) -- Point at which the arrow starts.  
[length](#) -- length of the arrow. Default is `1`.  
[hex](#) -- hexadecimal value to define color. Default is 0xffff00.  
[headLength](#) -- The length of the head of the arrow. Default is `0.2` *
length.  
[headWidth](#) -- The width of the head of the arrow. Default is `0.2` *
headLength.  

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### line

  
  
```ts  
line: Line;  
```  

Contains the line part of the arrowHelper.

### cone

  
  
```ts  
cone: Mesh;  
```  

Contains the cone part of the arrowHelper.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### setColor

  
  
```ts  
function setColor( color: Color ): undefined;  
```  

color -- The desired color.  
  
Sets the color of the arrowHelper.

### setLength

  
  
```ts  
function setLength( length: Number, headLength: Number, headWidth: Number ):
undefined;  
```  

length -- The desired length.  
headLength -- The length of the head of the arrow.  
headWidth -- The width of the head of the arrow.  
  
Sets the length of the arrowhelper.

### setDirection

  
  
```ts  
function setDirection( dir: Vector3 ): undefined;  
```  

dir -- The desired direction. Must be a unit vector.  
  
Sets the direction of the arrowhelper.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/helpers/ArrowHelper.js">src/helpers/ArrowHelper.js</a>

