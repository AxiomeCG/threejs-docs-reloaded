# ShapePath

This class is used to convert a series of shapes to an array of [page:Path]s,
for example an SVG shape to a path (see the example below).

## Constructor

###  function ShapePath( ): void;

Creates a new ShapePath. Unlike a [page:Path], no points are passed in as the
ShapePath is designed to be generated after creation.

## Properties

###  Array subPaths;

Array of [page:Path]s.

###  Array currentPath;

The current [page:Path] that is being generated.

###  Color color;

[page:Color] of the shape, by default set to white (0xffffff).

## Methods

###  function moveTo( x: Float, y: Float ): this;

Starts a new [page:Path] and calls [page:Path.moveTo]( x, y ) on that
[page:Path]. Also points [page:ShapePath.currentPath currentPath] to that
[page:Path].

###  function lineTo( x: Float, y: Float ): this;

This creates a line from the [page:ShapePath.currentPath currentPath]'s offset
to X and Y and updates the offset to X and Y.

###  function quadraticCurveTo( cpX: Float, cpY: Float, x: Float, y: Float ):
this;

This creates a quadratic curve from the [page:ShapePath.currentPath
currentPath]'s offset to x and y with cpX and cpY as control point and updates
the [page:ShapePath.currentPath currentPath]'s offset to x and y.

###  function bezierCurveTo( cp1X: Float, cp1Y: Float, cp2X: Float, cp2Y:
Float, x: Float, y: Float ): this;

This creates a bezier curve from the [page:ShapePath.currentPath
currentPath]'s offset to x and y with cp1X, cp1Y and cp2X, cp2Y as control
points and updates the [page:ShapePath.currentPath currentPath]'s offset to x
and y.

###  function splineThru( points: Array ): this;

points - An array of [page:Vector2]s

Connects a new [page:SplineCurve] onto the [page:ShapePath.currentPath
currentPath].

###  function toShapes( isCCW: Boolean ): Array;

isCCW -- Changes how solids and holes are generated

Converts the [page:ShapePath.subPaths subPaths] array into an array of Shapes.
By default solid shapes are defined clockwise (CW) and holes are defined
counterclockwise (CCW). If isCCW is set to true, then those are flipped.  

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/extras/core/ShapePath.js
src/extras/core/ShapePath.js]

