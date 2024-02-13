[page:BufferAttribute] →

# InstancedBufferAttribute

An instanced version of [page:BufferAttribute].

## Constructor

###  function InstancedBufferAttribute( array: TypedArray, itemSize: Integer,
normalized: Boolean, meshPerAttribute: Number ): void;

## Properties

See [page:BufferAttribute] for inherited properties.

###  Number meshPerAttribute;

Defines how often a value of this buffer attribute should be repeated. A value
of one means that each value of the instanced attribute is used for a single
instance. A value of two means that each value is used for two consecutive
instances (and so on). Default is `1`.

## Methods

See [page:BufferAttribute] for inherited methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

