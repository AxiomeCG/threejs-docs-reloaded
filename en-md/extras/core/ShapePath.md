# [name]

This class is used to convert a series of shapes to an array of [page:Path]s,
for example an SVG shape to a path (see the example below).

## Constructor

### [name]( )

Creates a new ShapePath. Unlike a [page:Path], no points are passed in as the
ShapePath is designed to be generated after creation.

## Properties

### <br/> Array subPaths; <br/>

Array of [page:Path]s.

### <br/> Array currentPath; <br/>

The current [page:Path] that is being generated.

### <br/> Color color; <br/>

[page:Color] of the shape, by default set to white (0xffffff).

## Methods

### <br/> function moveTo( x: Float, y: Float ): moveTo; <br/>

Starts a new [page:Path] and calls [page:Path.moveTo]( x, y ) on that
[page:Path]. Also points [page:ShapePath.currentPath currentPath] to that
[page:Path].

### <br/> function lineTo( x: Float, y: Float ): lineTo; <br/>

This creates a line from the [page:ShapePath.currentPath currentPath]'s offset
to X and Y and updates the offset to X and Y.

### <br/> function quadraticCurveTo( cpX: Float, cpY: Float, x: Float, y:
Float ): quadraticCurveTo; <br/>

This creates a quadratic curve from the [page:ShapePath.currentPath
currentPath]'s offset to x and y with cpX and cpY as control point and updates
the [page:ShapePath.currentPath currentPath]'s offset to x and y.

### <br/> function bezierCurveTo( cp1X: Float, cp1Y: Float, cp2X: Float, cp2Y:
Float, x: Float, y: Float ): bezierCurveTo; <br/>

This creates a bezier curve from the [page:ShapePath.currentPath
currentPath]'s offset to x and y with cp1X, cp1Y and cp2X, cp2Y as control
points and updates the [page:ShapePath.currentPath currentPath]'s offset to x
and y.

### <br/> function splineThru( points: Array ): splineThru; <br/>

points - An array of [page:Vector2]s

Connects a new [page:SplineCurve] onto the [page:ShapePath.currentPath
currentPath].

### [method:Array toShapes]( [param:Boolean isCCW] )

isCCW -- Changes how solids and holes are generated

Converts the [page:ShapePath.subPaths subPaths] array into an array of Shapes.
By default solid shapes are defined clockwise (CW) and holes are defined
counterclockwise (CCW). If isCCW is set to true, then those are flipped.  

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/extras/core/ShapePath.js
src/extras/core/ShapePath.js]

