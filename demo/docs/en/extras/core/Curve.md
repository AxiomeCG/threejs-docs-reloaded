# Curve

An abstract base class for creating a Curve object that contains methods for
interpolation. For an array of Curves see
[CurvePath](en\extras\core\CurvePath.html).

## Constructor

### Curve

  
  
```ts  
function Curve( ): void;  
```  

This constructor creates a new Curve.

## Properties

### arcLengthDivisions

  
  
```ts  
arcLengthDivisions: Integer;  
```  

This value determines the amount of divisions when calculating the cumulative
segment lengths of a curve via [.getLengths](#). To ensure precision when
using methods like [.getSpacedPoints](#), it is recommended to increase
[.arcLengthDivisions](#) if the curve is very large. Default is `200`.

## Methods

### getPoint

  
  
```ts  
function getPoint( t: Float, optionalTarget: Vector ): Vector;  
```  

[t](#) - A position on the curve. Must be in the range [ 0, 1 ].  
[optionalTarget](#) — (optional) If specified, the result will be copied into
this Vector, otherwise a new Vector will be created.  
  
Returns a vector for a given position on the curve.

### getPointAt

  
  
```ts  
function getPointAt( u: Float, optionalTarget: Vector ): Vector;  
```  

[u](#) - A position on the curve according to the arc length. Must be in the
range [ 0, 1 ].  
[optionalTarget](#) — (optional) If specified, the result will be copied into
this Vector, otherwise a new Vector will be created.  
  
Returns a vector for a given position on the curve according to the arc
length.

### getPoints

  
  
```ts  
function getPoints( divisions: Integer ): Array;  
```  

divisions -- number of pieces to divide the curve into. Default is `5`.  
  
Returns a set of divisions + 1 points using getPoint( t ).

### getSpacedPoints

  
  
```ts  
function getSpacedPoints( divisions: Integer ): Array;  
```  

divisions -- number of pieces to divide the curve into. Default is `5`.  
  
Returns a set of divisions + 1 equi-spaced points using getPointAt( u ).

### getLength

  
  
```ts  
function getLength( ): Float;  
```  

Get total curve arc length.

### getLengths

  
  
```ts  
function getLengths( divisions: Integer ): Array;  
```  

Get list of cumulative segment lengths.

### updateArcLengths

  
  
```ts  
function updateArcLengths( ): undefined;  
```  

Update the cumlative segment distance cache. The method must be called every
time curve parameters are changed. If an updated curve is part of a composed
curve like [CurvePath](en\extras\core\CurvePath.html),
[.updateArcLengths](#)() must be called on the composed curve, too.

### getUtoTmapping

  
  
```ts  
function getUtoTmapping( u: Float, distance: Float ): Float;  
```  

Given u in the range ( 0 .. 1 ), returns [.loat](#loat) also in the range ( 0
.. 1 ). u and t can then be used to give you points which are equidistant from
the ends of the curve, using [.getPoint](#).

### getTangent

  
  
```ts  
function getTangent( t: Float, optionalTarget: Vector ): Vector;  
```  

[t](#) - A position on the curve. Must be in the range [ 0, 1 ].  
[optionalTarget](#) — (optional) If specified, the result will be copied into
this Vector, otherwise a new Vector will be created.  
  
Returns a unit vector tangent at t. If the derived curve does not implement
its tangent derivation, two points a small delta apart will be used to find
its gradient which seems to give a reasonable approximation.

### getTangentAt

  
  
```ts  
function getTangentAt( u: Float, optionalTarget: Vector ): Vector;  
```  

[u](#) - A position on the curve according to the arc length. Must be in the
range [ 0, 1 ].  
[optionalTarget](#) — (optional) If specified, the result will be copied into
this Vector, otherwise a new Vector will be created.  
  
Returns tangent at a point which is equidistant to the ends of the curve from
the point given in [.getTangent](#).

### computeFrenetFrames

  
  
```ts  
function computeFrenetFrames( segments: Integer, closed: Boolean ): Object;  
```  

Generates the Frenet Frames. Requires a curve definition in 3D space. Used in
geometries like [TubeGeometry](en\geometries\TubeGeometry.html) or
[ExtrudeGeometry](en\geometries\ExtrudeGeometry.html).

### clone

  
  
```ts  
function clone( ): Curve;  
```  

Creates a clone of this instance.

### copy

  
  
```ts  
function copy( source: Curve ): this;  
```  

Copies another Curve object to this instance.

### toJSON

  
  
```ts  
function toJSON( ): Object;  
```  

Returns a JSON object representation of this instance.

### fromJSON

  
  
```ts  
function fromJSON( json: Object ): this;  
```  

Copies the data from the given JSON object to this instance.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/core/Curve.js">src/extras/core/Curve.js</a>

