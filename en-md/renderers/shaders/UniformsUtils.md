# [name]

Provides utility functions for managing uniforms.

## Methods

### [method:Object clone]( [param:Object src] )

src -- An object representing uniform definitions.  
  
Clones the given uniform definitions by performing a deep-copy. That means if
the [page:Uniform.value value] of a uniform refers to an object like a
[page:Vector3] or [page:Texture], the cloned uniform will refer to a new
object reference.

### [method:Object merge]( [param:Array uniforms] )

uniforms -- An array of objects containing uniform definitions.  
  
Merges the given uniform definitions into a single object. Since the method
internally uses [page:.clone](), it performs a deep-copy when producing the
merged uniform definitions.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

