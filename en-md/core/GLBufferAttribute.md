# [name]

This buffer attribute class does not construct a VBO. Instead, it uses
whatever VBO is passed in constructor and can later be altered via the
`buffer` property.  
  
It is required to pass additional params alongside the VBO. Those are: the GL
context, the GL data type, the number of components per vertex, the number of
bytes per component, and the number of vertices.  
  
The most common use case for this class is when some kind of GPGPU calculation
interferes or even produces the VBOs in question.

## Constructor

### [name]( [param:WebGLBuffer buffer], [param:GLenum type], [param:Integer
itemSize], [param:Integer elementSize], [param:Integer count] )

`buffer` — Must be a [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLBuffer WebGLBuffer].  
`type` — One of [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGL_API/Constants#Data_types WebGL Data Types].  
`itemSize` — The number of values of the array that should be associated with
a particular vertex. For instance, if this attribute is storing a 3-component
vector (such as a position, normal, or color), then itemSize should be 3.  
`elementSize` — 1, 2 or 4. The corresponding size (in bytes) for the given
"type" param.

  * gl.FLOAT: 4
  * gl.UNSIGNED_SHORT: 2
  * gl.SHORT: 2
  * gl.UNSIGNED_INT: 4
  * gl.INT: 4
  * gl.BYTE: 1
  * gl.UNSIGNED_BYTE: 1

`count` — The expected number of vertices in VBO.

## Properties

### <br/> WebGLBuffer buffer; <br/>

The current [link:https://developer.mozilla.org/en-US/docs/Web/API/WebGLBuffer
WebGLBuffer] instance.

### <br/> Integer count; <br/>

The expected number of vertices in VBO.

### <br/> Boolean isGLBufferAttribute; <br/>

Read-only. Always `true`.

### <br/> Integer itemSize; <br/>

How many values make up each item (vertex).

### <br/> Integer elementSize; <br/>

Stores the corresponding size in bytes for the current `type` property value.

See above (constructor) for a list of known type sizes.

### <br/> String name; <br/>

Optional name for this attribute instance. Default is an empty string.

### <br/> GLenum type; <br/>

A [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGL_API/Constants#Data_types WebGL Data Type] describing the
underlying VBO contents.

Set this property together with `elementSize`. The recommended way is using
the `setType` method.

## Methods

### <br/> function setBuffer( ): setBuffer; <br/>

Sets the `buffer` property.

### <br/> function setType( ): setType; <br/>

Sets the both `type` and `elementSize` properties.

### <br/> function setItemSize( ): setItemSize; <br/>

Sets the `itemSize` property.

### <br/> function setCount( ): setCount; <br/>

Sets the `count` property.

### <br/> Integer version; <br/>

A version number, incremented every time the needsUpdate property is set to
true.

### <br/> Boolean needsUpdate; <br/>

Default is `false`. Setting this to true increments
[page:GLBufferAttribute.version version].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

