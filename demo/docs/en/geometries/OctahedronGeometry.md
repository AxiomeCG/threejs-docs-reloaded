[BufferGeometry](en\core\BufferGeometry.html) →
[PolyhedronGeometry](en\geometries\PolyhedronGeometry.html) →

# OctahedronGeometry

A class for generating an octahedron geometry.

## Constructor

### OctahedronGeometry

  
  
```ts  
function OctahedronGeometry( radius: Float, detail: Integer ): void;  
```  

radius — Radius of the octahedron. Default is `1`.  
detail — Default is `0`. Setting this to a value greater than zero add
vertices making it no longer an octahedron.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/OctahedronGeometry.js">src/geometries/OctahedronGeometry.js</a>

