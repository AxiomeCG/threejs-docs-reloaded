# PropertyBinding

This holds a reference to a real property in the scene graph; used internally.

## Constructor

###  function PropertyBinding( rootNode: Object3D ): void;

\-- [page:Object3D rootNode]: -- path -- parsedPath (optional)

## Properties

###  Number path;

###  Number parsedPath;

###  Number node;

###  Number rootNode;

###  Object BindingType;

###  Object Versioning;

###  Array GetterByBindingType;

###  Array SetterByBindingTypeAndVersioning;

## Methods

###  function getValue( targetArray: Array, offset: Number ): undefined;

###  function setValue( sourceArray: Array, offset: Number ): undefined;

###  function bind( ): undefined;

Create getter / setter pair for a property in the scene graph. Used internally
by [page:PropertyBinding.getValue getValue] and [page:PropertyBinding.setValue
setValue].

###  function unbind( ): undefined;

Unbind getter / setter pair for a property in the scene graph.

###  function Composite( ): Constructor;

Create a new Composite PropertyBinding.

###  function create( ): Constructor;

Create a new Composite PropertyBinding (if root is an
[page:AnimationObjectGroup]) or PropertyBinding.

###  function parseTrackName( ): Constructor;

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

###  function findNode( ): Constructor;

Find a node in a node tree or [page:Skeleton Skeleton].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

