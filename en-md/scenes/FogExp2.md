# [name]

This class contains the parameters that define exponential squared fog, which
gives a clear view near the camera and a faster than exponentially densening
fog farther from the camera.

## Code Example

  
```ts  
const scene = new THREE.Scene();  
scene.fog = new THREE.FogExp2( 0xcccccc, 0.002 );  
```  

## Constructor

### [name]( [param:Integer color], [param:Float density] )

The color parameter is passed to the [page:Color] constructor to set the color
property. Color can be a hexadecimal integer or a CSS-style string.

## Properties

### <br/> Boolean isFogExp2; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> String name; <br/>

Optional name of the object (doesn't need to be unique). Default is an empty
string.

### <br/> Color color; <br/>

Fog color. Example: If set to black, far away objects will be rendered black.

### <br/> Float density; <br/>

Defines how fast the fog will grow dense.

Default is `0.00025`.

## Methods

### [method:FogExp2 clone]()

Returns a new FogExp2 instance with the same parameters as this one.

### [method:Object toJSON]()

Return FogExp2 data in JSON format.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

