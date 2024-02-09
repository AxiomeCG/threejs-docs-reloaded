[page:Object3D] → [page:Line] →

# [name]

A series of lines drawn between pairs of vertices.  
  
This is nearly the same as [page:Line]; the only difference is that it is
rendered using [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements gl.LINES] instead of
[link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements gl.LINE_STRIP].

## Constructor

###  [name]( [param:BufferGeometry geometry], [param:Material material] )

[page:BufferGeometry geometry] — Pair(s) of vertices representing each line
segment(s).  
[page:Material material] — Material for the line. Default is
[page:LineBasicMaterial LineBasicMaterial].

## Properties

See the base [page:Line] class for common properties.

### <br/> Boolean isLineSegments; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

See the base [page:Line] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

