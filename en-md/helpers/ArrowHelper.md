[page:Object3D] →

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

###  function ArrowHelper( dir: Vector3, origin: Vector3, length: Number, hex:
Number, headLength: Number, headWidth: Number ): void;

[page:Vector3 dir] -- direction from origin. Must be a unit vector.  
[page:Vector3 origin] -- Point at which the arrow starts.  
[page:Number length] -- length of the arrow. Default is `1`.  
[page:Number hex] -- hexadecimal value to define color. Default is 0xffff00.  
[page:Number headLength] -- The length of the head of the arrow. Default is
`0.2` * length.  
[page:Number headWidth] -- The width of the head of the arrow. Default is
`0.2` * headLength.  

## Properties

See the base [page:Object3D] class for common properties.

###  Line line;

Contains the line part of the arrowHelper.

###  Mesh cone;

Contains the cone part of the arrowHelper.

## Methods

See the base [page:Object3D] class for common methods.

###  function setColor( color: Color ): undefined;

color -- The desired color.  
  
Sets the color of the arrowHelper.

###  function setLength( length: Number, headLength: Number, headWidth: Number
): undefined;

length -- The desired length.  
headLength -- The length of the head of the arrow.  
headWidth -- The width of the head of the arrow.  
  
Sets the length of the arrowhelper.

###  function setDirection( dir: Vector3 ): undefined;

dir -- The desired direction. Must be a unit vector.  
  
Sets the direction of the arrowhelper.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

