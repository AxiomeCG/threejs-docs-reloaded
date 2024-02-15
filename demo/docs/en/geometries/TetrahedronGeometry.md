[BufferGeometry](en\core\BufferGeometry.html) →
[PolyhedronGeometry](en\geometries\PolyhedronGeometry.html) →

# TetrahedronGeometry

A class for generating a tetrahedron geometries.

## Constructor

### TetrahedronGeometry

  
  
```ts  
function TetrahedronGeometry( radius: Float, detail: Integer ): void;  
```  

radius — Radius of the tetrahedron. Default is `1`.  
detail — Default is `0`. Setting this to a value greater than `0` adds
vertices making it no longer a tetrahedron.

## Properties

See the base [PolyhedronGeometry](en\geometries\PolyhedronGeometry.html) class
for common properties.

### parameters

  
  
```ts  
parameters: Object;  
```  

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [PolyhedronGeometry](en\geometries\PolyhedronGeometry.html) class
for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/TetrahedronGeometry.js">src/geometries/TetrahedronGeometry.js</a>

