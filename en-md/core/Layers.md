# Layers

A [page:Layers] object assigns an [page:Object3D] to 1 or more of 32 layers
numbered `0` to `31` - internally the layers are stored as a
[link:https://en.wikipedia.org/wiki/Mask_(computing) bit mask], and by default
all Object3Ds are a member of layer 0.  
  
This can be used to control visibility - an object must share a layer with a
[page:Camera camera] to be visible when that camera's view is rendered.  
  
All classes that inherit from [page:Object3D] have an [page:Object3D.layers]
property which is an instance of this class.

## Examples

[example:webgl_layers WebGL / layers]

## Constructor

###  function Layers( ): void;

Create a new Layers object, with membership initially set to layer 0.

## Properties

###  Integer mask;

A bit mask storing which of the 32 layers this layers object is currently a
member of.

## Methods

###  function disable( layer: Integer ): undefined;

layer - an integer from 0 to 31.  
  
Remove membership of this `layer`.

###  function enable( layer: Integer ): undefined;

layer - an integer from 0 to 31.  
  
Add membership of this `layer`.

###  function set( layer: Integer ): undefined;

layer - an integer from 0 to 31.  
  
Set membership to `layer`, and remove membership all other layers.

###  function test( layers: Layers ): Boolean;

layers - a Layers object  
  
Returns true if this and the passed `layers` object have at least one layer in
common.

###  function isEnabled( layer: Integer ): Boolean;

layer - an integer from 0 to 31.  
  
Returns true if the given layer is enabled.

###  function toggle( layer: Integer ): undefined;

layer - an integer from 0 to 31.  
  
Toggle membership of `layer`.

###  function enableAll( ): undefined;

Add membership to all layers.

###  function disableAll( ): undefined;

Remove membership from all layers.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

