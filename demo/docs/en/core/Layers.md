# Layers

A [Layers](en\core\Layers.html) object assigns an
[Object3D](en\core\Object3D.html) to 1 or more of 32 layers numbered `0` to
`31` - internally the layers are stored as a <a
href="https://en.wikipedia.org/wiki/Mask_(computing)">bit mask</a>, and by
default all Object3Ds are a member of layer 0.  
  
This can be used to control visibility - an object must share a layer with a
[camera](en\cameras\Camera.html) to be visible when that camera's view is
rendered.  
  
All classes that inherit from [Object3D](en\core\Object3D.html) have an
[Object3D.layers](#) property which is an instance of this class.

## Examples

[example:webgl_layers WebGL / layers]

## Constructor

### Layers

  
  
```ts  
function Layers( ): void;  
```  

Create a new Layers object, with membership initially set to layer 0.

## Properties

### mask

  
  
```ts  
mask: Integer;  
```  

A bit mask storing which of the 32 layers this layers object is currently a
member of.

## Methods

### disable

  
  
```ts  
function disable( layer: Integer ): undefined;  
```  

layer - an integer from 0 to 31.  
  
Remove membership of this `layer`.

### enable

  
  
```ts  
function enable( layer: Integer ): undefined;  
```  

layer - an integer from 0 to 31.  
  
Add membership of this `layer`.

### set

  
  
```ts  
function set( layer: Integer ): undefined;  
```  

layer - an integer from 0 to 31.  
  
Set membership to `layer`, and remove membership all other layers.

### test

  
  
```ts  
function test( layers: Layers ): Boolean;  
```  

layers - a Layers object  
  
Returns true if this and the passed `layers` object have at least one layer in
common.

### isEnabled

  
  
```ts  
function isEnabled( layer: Integer ): Boolean;  
```  

layer - an integer from 0 to 31.  
  
Returns true if the given layer is enabled.

### toggle

  
  
```ts  
function toggle( layer: Integer ): undefined;  
```  

layer - an integer from 0 to 31.  
  
Toggle membership of `layer`.

### enableAll

  
  
```ts  
function enableAll( ): undefined;  
```  

Add membership to all layers.

### disableAll

  
  
```ts  
function disableAll( ): undefined;  
```  

Remove membership from all layers.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/Layers.js">src/core/Layers.js</a>

