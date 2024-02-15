[BufferGeometry](en\core\BufferGeometry.html) →

# PlaneGeometry

A class for generating plane geometries.

## Code Example

  
```ts  
const geometry = new THREE.PlaneGeometry( 1, 1 );const material = new
THREE.MeshBasicMaterial( {color: 0xffff00, side: THREE.DoubleSide} );const
plane = new THREE.Mesh( geometry, material );scene.add( plane );  
```  

## Constructor

### PlaneGeometry

  
  
```ts  
function PlaneGeometry( width: Float, height: Float, heightSegments: Integer
): void;  
```  

width — Width along the X axis. Default is `1`.  
height — Height along the Y axis. Default is `1`.  
widthSegments — Optional. Default is `1`.  
heightSegments — Optional. Default is `1`.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/PlaneGeometry.js">src/geometries/PlaneGeometry.js</a>

