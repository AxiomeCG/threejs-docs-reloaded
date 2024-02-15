[BufferAttribute](en\core\BufferAttribute.html) →

# InstancedBufferAttribute

An instanced version of [BufferAttribute](en\core\BufferAttribute.html).

## Constructor

### InstancedBufferAttribute

  
  
```ts  
function InstancedBufferAttribute( array: TypedArray, itemSize: Integer,
normalized: Boolean, meshPerAttribute: Number ): void;  
```  

## Properties

See [BufferAttribute](en\core\BufferAttribute.html) for inherited properties.

### meshPerAttribute

  
  
```ts  
meshPerAttribute: Number;  
```  

Defines how often a value of this buffer attribute should be repeated. A value
of one means that each value of the instanced attribute is used for a single
instance. A value of two means that each value is used for two consecutive
instances (and so on). Default is `1`.

## Methods

See [BufferAttribute](en\core\BufferAttribute.html) for inherited methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/InstancedBufferAttribute.js">src/core/InstancedBufferAttribute.js</a>

