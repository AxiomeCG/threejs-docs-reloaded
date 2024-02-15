[Object3D](en\core\Object3D.html) → [Line](en\objects\Line.html) →

# LineSegments

A series of lines drawn between pairs of vertices.  
  
This is nearly the same as [Line](en\objects\Line.html); the only difference
is that it is rendered using <a href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements">gl.LINES</a> instead of <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements">gl.LINE_STRIP</a>.

## Constructor

### LineSegments

  
  
```ts  
function LineSegments( geometry: BufferGeometry, material: Material ): void;  
```  

[geometry](en\core\BufferGeometry.html) — Pair(s) of vertices representing
each line segment(s).  
[material](en\materials\Material.html) — Material for the line. Default is
[LineBasicMaterial](en\materials\LineBasicMaterial.html).

## Properties

See the base [Line](en\objects\Line.html) class for common properties.

### isLineSegments

  
  
```ts  
isLineSegments: Boolean;  
```  

Read-only flag to check if a given object is of type LineSegments.

## Methods

See the base [Line](en\objects\Line.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/LineSegments.js">src/objects/LineSegments.js</a>

