# PropertyBinding

This holds a reference to a real property in the scene graph; used internally.

## Constructor

### PropertyBinding

  
  
```ts  
function PropertyBinding( rootNode: Object3D ): void;  
```  

\-- [rootNode](en\core\Object3D.html): -- path -- parsedPath (optional)

## Properties

### path

  
  
```ts  
path: Number;  
```  

### parsedPath

  
  
```ts  
parsedPath: Number;  
```  

### node

  
  
```ts  
node: Number;  
```  

### rootNode

  
  
```ts  
rootNode: Number;  
```  

### BindingType

  
  
```ts  
BindingType: Object;  
```  

### Versioning

  
  
```ts  
Versioning: Object;  
```  

### GetterByBindingType

  
  
```ts  
GetterByBindingType: Array;  
```  

### SetterByBindingTypeAndVersioning

  
  
```ts  
SetterByBindingTypeAndVersioning: Array;  
```  

## Methods

### getValue

  
  
```ts  
function getValue( targetArray: Array, offset: Number ): undefined;  
```  

### setValue

  
  
```ts  
function setValue( sourceArray: Array, offset: Number ): undefined;  
```  

### bind

  
  
```ts  
function bind( ): undefined;  
```  

Create getter / setter pair for a property in the scene graph. Used internally
by [getValue](#) and [setValue](#).

### unbind

  
  
```ts  
function unbind( ): undefined;  
```  

Unbind getter / setter pair for a property in the scene graph.

### Composite

  
  
```ts  
function Composite( ): Constructor;  
```  

Create a new Composite PropertyBinding.

### create

  
  
```ts  
function create( ): Constructor;  
```  

Create a new Composite PropertyBinding (if root is an
[AnimationObjectGroup](en\animation\AnimationObjectGroup.html)) or
PropertyBinding.

### parseTrackName

  
  
```ts  
function parseTrackName( ): Constructor;  
```  

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

### findNode

  
  
```ts  
function findNode( ): Constructor;  
```  

Find a node in a node tree or [Skeleton](en\objects\Skeleton.html).

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/PropertyBinding.js">src/animation/PropertyBinding.js</a>

