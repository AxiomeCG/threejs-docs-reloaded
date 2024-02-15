# Buffer Attribute Usage Constants

The usage constants can be used to provide a hint to the API regarding how the
geometry buffer attribute will be used in order to optimize performance.

## Code Example

  
```ts  
const geometry = new THREE.BufferGeometry(); const positionAttribute = new
THREE.BufferAttribute( array, 3 , false ); positionAttribute.setUsage(
THREE.DynamicDrawUsage ); geometry.setAttribute( 'position', positionAttribute
);  
```  

## Examples

[example:webgl_buffergeometry_drawrange materials / buffergeometry / drawrange
]

## Geometry Usage

  
```ts  
THREE.StaticDrawUsage THREE.DynamicDrawUsage THREE.StreamDrawUsage
THREE.StaticReadUsage THREE.DynamicReadUsage THREE.StreamReadUsage
THREE.StaticCopyUsage THREE.DynamicCopyUsage THREE.StreamCopyUsage  
```  
For more detailed information on each of these constants see <a
href="https://www.khronos.org/opengl/wiki/Buffer_Object#Buffer_Object_Usage">this
OpenGL documentation</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/constants.js">src/constants.js</a>

