# Fog

This class contains the parameters that define linear fog, i.e., that grows
linearly denser with the distance.

## Code Example

  
```ts  
const scene = new THREE.Scene(); scene.fog = new THREE.Fog( 0xcccccc, 10, 15
);  
```  

## Constructor

### Fog

  
  
```ts  
function Fog( color: Integer, near: Float, far: Float ): void;  
```  

The color parameter is passed to the [Color](en\math\Color.html) constructor
to set the color property. Color can be a hexadecimal integer or a CSS-style
string.

## Properties

### isFog

  
  
```ts  
isFog: Boolean;  
```  

Read-only flag to check if a given object is of type Fog.

### name

  
  
```ts  
name: String;  
```  

Optional name of the object (doesn't need to be unique). Default is an empty
string.

### color

  
  
```ts  
color: Color;  
```  

Fog color. Example: If set to black, far away objects will be rendered black.

### near

  
  
```ts  
near: Float;  
```  

The minimum distance to start applying fog. Objects that are less than 'near'
units from the active camera won't be affected by fog.

Default is `1`.

### far

  
  
```ts  
far: Float;  
```  

The maximum distance at which fog stops being calculated and applied. Objects
that are more than 'far' units away from the active camera won't be affected
by fog.

Default is `1000`.

## Methods

### clone

  
  
```ts  
function clone( ): Fog;  
```  

Returns a new fog instance with the same parameters as this one.

### toJSON

  
  
```ts  
function toJSON( ): Object;  
```  

Return fog data in JSON format.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/scenes/Fog.js">src/scenes/Fog.js</a>

