# ShapePath

This class is used to convert a series of shapes to an array of
[Path](en\extras\core\Path.html)s, for example an SVG shape to a path (see the
example below).

## Constructor

### ShapePath

  
  
```ts  
function ShapePath( ): void;  
```  

Creates a new ShapePath. Unlike a [Path](en\extras\core\Path.html), no points
are passed in as the ShapePath is designed to be generated after creation.

## Properties

### subPaths

  
  
```ts  
subPaths: Array;  
```  

Array of [Path](en\extras\core\Path.html)s.

### currentPath

  
  
```ts  
currentPath: Array;  
```  

The current [Path](en\extras\core\Path.html) that is being generated.

### color

  
  
```ts  
color: Color;  
```  

[Color](en\math\Color.html) of the shape, by default set to white (0xffffff).

## Methods

### moveTo

  
  
```ts  
function moveTo( x: Float, y: Float ): this;  
```  

Starts a new [Path](en\extras\core\Path.html) and calls [Path.moveTo](#)( x, y
) on that [Path](en\extras\core\Path.html). Also points [currentPath](#) to
that [Path](en\extras\core\Path.html).

### lineTo

  
  
```ts  
function lineTo( x: Float, y: Float ): this;  
```  

This creates a line from the [currentPath](#)'s offset to X and Y and updates
the offset to X and Y.

### quadraticCurveTo

  
  
```ts  
function quadraticCurveTo( cpX: Float, cpY: Float, x: Float, y: Float ): this;  
```  

This creates a quadratic curve from the [currentPath](#)'s offset to x and y
with cpX and cpY as control point and updates the [currentPath](#)'s offset to
x and y.

### bezierCurveTo

  
  
```ts  
function bezierCurveTo( cp1X: Float, cp1Y: Float, cp2X: Float, cp2Y: Float, x:
Float, y: Float ): this;  
```  

This creates a bezier curve from the [currentPath](#)'s offset to x and y with
cp1X, cp1Y and cp2X, cp2Y as control points and updates the [currentPath](#)'s
offset to x and y.

### splineThru

  
  
```ts  
function splineThru( points: Array ): this;  
```  

points - An array of [Vector2](en\math\Vector2.html)s

Connects a new [SplineCurve](en\extras\curves\SplineCurve.html) onto the
[currentPath](#).

### toShapes

  
  
```ts  
function toShapes( isCCW: Boolean ): Array;  
```  

isCCW -- Changes how solids and holes are generated

Converts the [subPaths](#) array into an array of Shapes. By default solid
shapes are defined clockwise (CW) and holes are defined counterclockwise
(CCW). If isCCW is set to true, then those are flipped.  

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/extras/core/ShapePath.js">src/extras/core/ShapePath.js</a>

