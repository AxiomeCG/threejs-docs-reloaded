# Fog

This class contains the parameters that define linear fog, i.e., that grows
linearly denser with the distance.

## Code Example

  
```ts  
const scene = new THREE.Scene(); scene.fog = new THREE.Fog( 0xcccccc, 10, 15
);  
```  

## Constructor

###  function Fog( color: Integer, near: Float, far: Float ): void;

The color parameter is passed to the [page:Color] constructor to set the color
property. Color can be a hexadecimal integer or a CSS-style string.

## Properties

###  Boolean isFog;

Read-only flag to check if a given object is of type Fog.

###  String name;

Optional name of the object (doesn't need to be unique). Default is an empty
string.

###  Color color;

Fog color. Example: If set to black, far away objects will be rendered black.

###  Float near;

The minimum distance to start applying fog. Objects that are less than 'near'
units from the active camera won't be affected by fog.

Default is `1`.

###  Float far;

The maximum distance at which fog stops being calculated and applied. Objects
that are more than 'far' units away from the active camera won't be affected
by fog.

Default is `1000`.

## Methods

###  function clone( ): Fog;

Returns a new fog instance with the same parameters as this one.

###  function toJSON( ): Object;

Return fog data in JSON format.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

