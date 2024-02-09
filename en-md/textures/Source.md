# [name]

Represents the data source of a texture.

## Constructor

### [name]( [param:Any data] )

[page:Any data] -- The data definition of a texture. Default is `null`.

## Properties

### <br/> Any data; <br/>

The actual data of a texture. The type of this property depends on the texture
that uses this instance.

### <br/> Boolean isSource; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Boolean needsUpdate; <br/>

Set this to `true` to trigger a data upload to the GPU next time the source is
used.

### <br/> String uuid; <br/>

[link:http://en.wikipedia.org/wiki/Universally_unique_identifier UUID] of this
object instance. This gets automatically assigned, so this shouldn't be
edited.

### <br/> Integer version; <br/>

This starts at `0` and counts how many times [page:Source.needsUpdate
.needsUpdate] is set to `true`.

## Methods

### [method:Object toJSON]( [param:Object meta] )

meta -- optional object containing metadata.  
Convert the data source to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

