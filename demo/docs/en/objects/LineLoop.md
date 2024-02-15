[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →

# LineLoop

A continuous line that connects back to the start.  
  
This is nearly the same as [Line](en\objects\Line.html); the only difference
is that it is rendered using <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements">gl.LINE_LOOP</a> instead
of <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements">gl.LINE_STRIP</a>, which
draws a straight line to the next vertex, and connects the last vertex back to
the first.

## Constructor

### LineLoop

  
  
```ts  
function LineLoop( geometry: BufferGeometry, material: Material ): void;  
```  

[geometry](en\core\BufferGeometry.html) — List of vertices representing points
on the line loop.  
[material](en\materials\Material.html) — Material for the line. Default is
[LineBasicMaterial](en\materials\LineBasicMaterial.html).

## Properties

See the base [Line](en\objects\Line.html) class for common properties.

### isLineLoop

  
  
```ts  
isLineLoop: Boolean;  
```  

Read-only flag to check if a given object is of type LineLoop.

## Methods

See the base [Line](en\objects\Line.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/LineLoop.js">src/objects/LineLoop.js</a>

