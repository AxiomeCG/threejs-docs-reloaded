# Curve

An abstract base class for creating a Curve object that contains methods for
interpolation. For an array of Curves see [page:CurvePath].

## Constructor

###  function Curve( ): void;

This constructor creates a new Curve.

## Properties

###  Integer arcLengthDivisions;

This value determines the amount of divisions when calculating the cumulative
segment lengths of a curve via [page:.getLengths]. To ensure precision when
using methods like [page:.getSpacedPoints], it is recommended to increase
[page:.arcLengthDivisions] if the curve is very large. Default is `200`.

## Methods

###  function getPoint( t: Float, optionalTarget: Vector ): Vector;

[page:Float t] - A position on the curve. Must be in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns a vector for a given position on the curve.

###  function getPointAt( u: Float, optionalTarget: Vector ): Vector;

[page:Float u] - A position on the curve according to the arc length. Must be
in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns a vector for a given position on the curve according to the arc
length.

###  function getPoints( divisions: Integer ): Array;

divisions -- number of pieces to divide the curve into. Default is `5`.  
  
Returns a set of divisions + 1 points using getPoint( t ).

###  function getSpacedPoints( divisions: Integer ): Array;

divisions -- number of pieces to divide the curve into. Default is `5`.  
  
Returns a set of divisions + 1 equi-spaced points using getPointAt( u ).

###  function getLength( ): Float;

Get total curve arc length.

###  function getLengths( divisions: Integer ): Array;

Get list of cumulative segment lengths.

###  function updateArcLengths( ): undefined;

Update the cumlative segment distance cache. The method must be called every
time curve parameters are changed. If an updated curve is part of a composed
curve like [page:CurvePath], [page:.updateArcLengths]() must be called on the
composed curve, too.

###  function getUtoTmapping( u: Float, distance: Float ): Float;

Given u in the range ( 0 .. 1 ), returns [page:Float t] also in the range ( 0
.. 1 ). u and t can then be used to give you points which are equidistant from
the ends of the curve, using [page:.getPoint].

###  function getTangent( t: Float, optionalTarget: Vector ): Vector;

[page:Float t] - A position on the curve. Must be in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns a unit vector tangent at t. If the derived curve does not implement
its tangent derivation, two points a small delta apart will be used to find
its gradient which seems to give a reasonable approximation.

###  function getTangentAt( u: Float, optionalTarget: Vector ): Vector;

[page:Float u] - A position on the curve according to the arc length. Must be
in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns tangent at a point which is equidistant to the ends of the curve from
the point given in [page:.getTangent].

###  function computeFrenetFrames( segments: Integer, closed: Boolean ):
Object;

Generates the Frenet Frames. Requires a curve definition in 3D space. Used in
geometries like [page:TubeGeometry] or [page:ExtrudeGeometry].

###  function clone( ): Curve;

Creates a clone of this instance.

###  function copy( source: Curve ): this;

Copies another Curve object to this instance.

###  function toJSON( ): Object;

Returns a JSON object representation of this instance.

###  function fromJSON( json: Object ): this;

Copies the data from the given JSON object to this instance.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

