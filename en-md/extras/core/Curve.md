# [name]

An abstract base class for creating a [name] object that contains methods for
interpolation. For an array of [name]s see [page:CurvePath].

## Constructor

### [name]()

This constructor creates a new [name].

## Properties

### <br/> Integer arcLengthDivisions; <br/>

This value determines the amount of divisions when calculating the cumulative
segment lengths of a curve via [page:.getLengths]. To ensure precision when
using methods like [page:.getSpacedPoints], it is recommended to increase
[page:.arcLengthDivisions] if the curve is very large. Default is `200`.

## Methods

### [method:Vector getPoint]( [param:Float t], [param:Vector optionalTarget] )

[page:Float t] - A position on the curve. Must be in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns a vector for a given position on the curve.

### [method:Vector getPointAt]( [param:Float u], [param:Vector optionalTarget]
)

[page:Float u] - A position on the curve according to the arc length. Must be
in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns a vector for a given position on the curve according to the arc
length.

### [method:Array getPoints]( [param:Integer divisions] )

divisions -- number of pieces to divide the curve into. Default is `5`.  
  
Returns a set of divisions + 1 points using getPoint( t ).

### [method:Array getSpacedPoints]( [param:Integer divisions] )

divisions -- number of pieces to divide the curve into. Default is `5`.  
  
Returns a set of divisions + 1 equi-spaced points using getPointAt( u ).

### [method:Float getLength]()

Get total curve arc length.

### [method:Array getLengths]( [param:Integer divisions] )

Get list of cumulative segment lengths.

### [method:undefined updateArcLengths]()

Update the cumlative segment distance cache. The method must be called every
time curve parameters are changed. If an updated curve is part of a composed
curve like [page:CurvePath], [page:.updateArcLengths]() must be called on the
composed curve, too.

### [method:Float getUtoTmapping]( [param:Float u], [param:Float distance] )

Given u in the range ( 0 .. 1 ), returns [page:Float t] also in the range ( 0
.. 1 ). u and t can then be used to give you points which are equidistant from
the ends of the curve, using [page:.getPoint].

### [method:Vector getTangent]( [param:Float t], [param:Vector optionalTarget]
)

[page:Float t] - A position on the curve. Must be in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns a unit vector tangent at t. If the derived curve does not implement
its tangent derivation, two points a small delta apart will be used to find
its gradient which seems to give a reasonable approximation.

### [method:Vector getTangentAt]( [param:Float u], [param:Vector
optionalTarget] )

[page:Float u] - A position on the curve according to the arc length. Must be
in the range [ 0, 1 ].  
[page:Vector optionalTarget] — (optional) If specified, the result will be
copied into this Vector, otherwise a new Vector will be created.  
  
Returns tangent at a point which is equidistant to the ends of the curve from
the point given in [page:.getTangent].

### [method:Object computeFrenetFrames]( [param:Integer segments],
[param:Boolean closed] )

Generates the Frenet Frames. Requires a curve definition in 3D space. Used in
geometries like [page:TubeGeometry] or [page:ExtrudeGeometry].

### [method:Curve clone]()

Creates a clone of this instance.

### <br/> function copy( source: Curve ): copy; <br/>

Copies another [name] object to this instance.

### [method:Object toJSON]()

Returns a JSON object representation of this instance.

### <br/> function fromJSON( json: Object ): fromJSON; <br/>

Copies the data from the given JSON object to this instance.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

