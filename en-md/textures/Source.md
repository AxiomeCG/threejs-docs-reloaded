# Source

Represents the data source of a texture.

## Constructor

###  function Source( data: Any ): void;

[page:Any data] -- The data definition of a texture. Default is `null`.

## Properties

###  Any data;

The actual data of a texture. The type of this property depends on the texture
that uses this instance.

###  Boolean isSource;

Read-only flag to check if a given object is of type Source.

###  Boolean needsUpdate;

Set this to `true` to trigger a data upload to the GPU next time the source is
used.

###  String uuid;

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
object instance. This gets automatically assigned, so this shouldn't be
edited.

###  Integer version;

This starts at `0` and counts how many times [page:Source.needsUpdate
.needsUpdate] is set to `true`.

## Methods

###  function toJSON( meta: Object ): Object;

meta -- optional object containing metadata.  
Convert the data source to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

