[page:BufferGeometry] → [page:PolyhedronGeometry] →

# IcosahedronGeometry

A class for generating an icosahedron geometry.

## Constructor

###  function IcosahedronGeometry( radius: Float, detail: Integer ): void;

radius — Default is `1`.  
detail — Default is `0`. Setting this to a value greater than `0` adds more
vertices making it no longer an icosahedron. When detail is greater than 1,
it's effectively a sphere.

## Properties

See the base [page:PolyhedronGeometry] class for common properties.

###  Object parameters;

An object with a property for each of the constructor parameters. Any
modification after instantiation does not change the geometry.

## Methods

See the base [page:PolyhedronGeometry] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

