[BufferGeometry](en\core\BufferGeometry.html) →
[PolyhedronGeometry](en\geometries\PolyhedronGeometry.html) →

# IcosahedronGeometry

A class for generating an icosahedron geometry.

## Constructor

### IcosahedronGeometry

  
  
```ts  
function IcosahedronGeometry( radius: Float, detail: Integer ): void;  
```  

radius — Default is `1`.  
detail — Default is `0`. Setting this to a value greater than `0` adds more
vertices making it no longer an icosahedron. When detail is greater than 1,
it's effectively a sphere.

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
href="https://github.com/mrdoob/three.js/blob/master/src/geometries/IcosahedronGeometry.js">src/geometries/IcosahedronGeometry.js</a>

