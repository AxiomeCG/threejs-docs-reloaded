[page:BufferAttribute] →

# BufferAttribute Types

There are nine types of [page:BufferAttribute] available in three.js. These
correspond to the JavaScript [link:https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray#Syntax Typed
Arrays].

  
```ts  
THREE.Float64BufferAttribute THREE.Float32BufferAttribute
THREE.Float16BufferAttribute THREE.Uint32BufferAttribute
THREE.Int32BufferAttribute THREE.Uint16BufferAttribute
THREE.Int16BufferAttribute THREE.Uint8ClampedBufferAttribute
THREE.Uint8BufferAttribute THREE.Int8BufferAttribute  
```  

## Constructor

All of the above are called in the same way.

### TypedBufferAttribute( [param:Array_or_Integer array], [param:Integer
itemSize], [param:Boolean normalized] )

array -- this can be a typed or untyped (normal) array or an integer length.
An array value will be converted to the Type specified. If a length is given a
new TypedArray will created, initialized with all elements set to zero.  
  
itemSize -- the number of values of the array that should be associated with a
particular vertex.  
  
normalized -- (optional) indicates how the underlying data in the buffer maps
to the values in the GLSL code.

## Properties

See the [page:BufferAttribute] page for inherited properties.

## Methods

See the [page:BufferAttribute] page for inherited methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/core/BufferAttribute.js
src/core/BufferAttribute.js]

