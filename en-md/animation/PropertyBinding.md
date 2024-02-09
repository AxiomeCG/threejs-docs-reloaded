# [name]

This holds a reference to a real property in the scene graph; used internally.

## Constructor

### [name]( [param:Object3D rootNode], path, parsedPath )

\-- [page:Object3D rootNode]: -- path -- parsedPath (optional)

## Properties

### <br/> Number path; <br/>

### <br/> Number parsedPath; <br/>

### <br/> Number node; <br/>

### <br/> Number rootNode; <br/>

### <br/> Object BindingType; <br/>

### <br/> Object Versioning; <br/>

### <br/> Array GetterByBindingType; <br/>

### <br/> Array SetterByBindingTypeAndVersioning; <br/>

## Methods

### [method:undefined getValue]( [param:Array targetArray], [param:Number
offset] )

### [method:undefined setValue]( [param:Array sourceArray], [param:Number
offset] )

### [method:undefined bind]( )

Create getter / setter pair for a property in the scene graph. Used internally
by [page:PropertyBinding.getValue getValue] and [page:PropertyBinding.setValue
setValue].

### [method:undefined unbind]( )

Unbind getter / setter pair for a property in the scene graph.

### [method:Constructor Composite]( targetGroup, path, optionalParsedPath )

Create a new Composite PropertyBinding.

### [method:Constructor create]( root, path, parsedPath )

Create a new Composite PropertyBinding (if root is an
[page:AnimationObjectGroup]) or PropertyBinding.

### [method:Constructor parseTrackName]( trackName )

Matches strings in the following forms:  
\-- nodeName.property  
\-- nodeName.property[accessor]  
\-- nodeName.material.property[accessor]  
\-- uuid.property[accessor]  
\-- uuid.objectName[objectIndex].propertyName[propertyIndex]  
\-- parentName/nodeName.property  
\-- parentName/parentName/nodeName.property[index]  
\-- .bone[Armature.DEF_cog].position  
\-- scene:helium_balloon_model:helium_balloon_model.position

### [method:Constructor findNode]( root, nodeName )

Find a node in a node tree or [page:Skeleton Skeleton].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

