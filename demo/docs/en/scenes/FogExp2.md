# FogExp2

This class contains the parameters that define exponential squared fog, which
gives a clear view near the camera and a faster than exponentially densening
fog farther from the camera.

## Code Example

  
```ts  
const scene = new THREE.Scene();scene.fog = new THREE.FogExp2( 0xcccccc, 0.002
);  
```  

## Constructor

### FogExp2

  
  
```ts  
function FogExp2( color: Integer, density: Float ): void;  
```  

The color parameter is passed to the [Color](en\math\Color.html) constructor
to set the color property. Color can be a hexadecimal integer or a CSS-style
string.

## Properties

### isFogExp2

  
  
```ts  
isFogExp2: Boolean;  
```  

Read-only flag to check if a given object is of type FogExp2.

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

### density

  
  
```ts  
density: Float;  
```  

Defines how fast the fog will grow dense.

Default is `0.00025`.

## Methods

### clone

  
  
```ts  
function clone( ): FogExp2;  
```  

Returns a new FogExp2 instance with the same parameters as this one.

### toJSON

  
  
```ts  
function toJSON( ): Object;  
```  

Return FogExp2 data in JSON format.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/scenes/FogExp2.js">src/scenes/FogExp2.js</a>

