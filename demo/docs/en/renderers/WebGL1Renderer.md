[WebGLRenderer](en\renderers\WebGLRenderer.html) →

# WebGL1Renderer

Since r118 [WebGLRenderer](en\renderers\WebGLRenderer.html) automatically uses
a WebGL 2 rendering context. When upgrading an existing project to => r118,
applications might break because of two reasons:

  * Custom shader code needs to be GLSL 3.0 conform.
  * WebGL 1 extension checks have to be changed.

If you can't afford the time to upgrade your code but still want to use the
latest version, you can use WebGL1Renderer. This version of the renderer will
enforce a WebGL 1 rendering context.

## Constructor

### WebGL1Renderer

  
  
```ts  
function WebGL1Renderer( parameters: Object ): void;  
```  

Creates a new WebGL1Renderer.

## Properties

See the base [WebGLRenderer](en\renderers\WebGLRenderer.html) class for common
properties.

### isWebGL1Renderer

  
  
```ts  
isWebGL1Renderer: Boolean;  
```  

Read-only flag to check if a given object is of type WebGL1Renderer.

## Methods

See the base [WebGLRenderer](en\renderers\WebGLRenderer.html) class for common
methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/WebGL1Renderer.js">src/renderers/WebGL1Renderer.js</a>

