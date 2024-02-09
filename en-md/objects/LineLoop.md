[page:Object3D] → [page:Line] →

# [name]

A continuous line that connects back to the start.  
  
This is nearly the same as [page:Line]; the only difference is that it is
rendered using [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements gl.LINE_LOOP] instead of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements gl.LINE_STRIP], which draws
a straight line to the next vertex, and connects the last vertex back to the
first.

## Constructor

###  [name]( [param:BufferGeometry geometry], [param:Material material] )

[page:BufferGeometry geometry] — List of vertices representing points on the
line loop.  
[page:Material material] — Material for the line. Default is
[page:LineBasicMaterial LineBasicMaterial].

## Properties

See the base [page:Line] class for common properties.

### <br/> Boolean isLineLoop; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

See the base [page:Line] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

