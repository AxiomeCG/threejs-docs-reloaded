[page:BufferGeometry] →

# [name]

Creates a tube that extrudes along a 3d curve.

## Code Example

  
```ts  
class CustomSinCurve extends THREE.Curve {  
  
constructor( scale = 1 ) {  
super();  
this.scale = scale;  
}  
  
getPoint( t, optionalTarget = new THREE.Vector3() ) {  
  
const tx = t * 3 - 1.5;  
const ty = Math.sin( 2 * Math.PI * t );  
const tz = 0;  
  
return optionalTarget.set( tx, ty, tz ).multiplyScalar( this.scale );  
}  
}  
  
const path = new CustomSinCurve( 10 );  
const geometry = new THREE.TubeGeometry( path, 20, 2, 8, false );  
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );  
const mesh = new THREE.Mesh( geometry, material );  
scene.add( mesh );  
```  

## Constructor

###  [name]([param:Curve path], [param:Integer tubularSegments], [param:Float
radius], [param:Integer radialSegments], [param:Boolean closed])

path — [page:Curve] - A 3D path that inherits from the [page:Curve] base
class. Default is a quadratic bezier curve.  
tubularSegments — [page:Integer] - The number of segments that make up the
tube. Default is `64`.  
radius — [page:Float] - The radius of the tube. Default is `1`.  
radialSegments — [page:Integer] - The number of segments that make up the
cross-section. Default is `8`.  
closed — [page:Boolean] Is the tube open or closed. Default is `false`.  

## Properties

See the base [page:BufferGeometry] class for common properties.

### <br/> Object parameters; <br/>

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

### <br/> Array tangents; <br/>

An array of [page:Vector3] tangents

### <br/> Array normals; <br/>

An array of [page:Vector3] normals

### <br/> Array binormals; <br/>

An array of [page:Vector3] binormals

## Methods

See the base [page:BufferGeometry] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

