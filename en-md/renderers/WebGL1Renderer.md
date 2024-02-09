[page:WebGLRenderer] →

# [name]

Since r118 [page:WebGLRenderer] automatically uses a WebGL 2 rendering
context. When upgrading an existing project to => r118, applications might
break because of two reasons:

  * Custom shader code needs to be GLSL 3.0 conform.
  * WebGL 1 extension checks have to be changed.

If you can't afford the time to upgrade your code but still want to use the
latest version, you can use [name]. This version of the renderer will enforce
a WebGL 1 rendering context.

## Constructor

### [name]( [param:Object parameters] )

Creates a new [name].

## Properties

See the base [page:WebGLRenderer] class for common properties.

### <br/> Boolean isWebGL1Renderer; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

See the base [page:WebGLRenderer] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

