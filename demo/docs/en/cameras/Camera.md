[Object3D](en\core\Object3D.html) →

# Camera

Abstract base class for cameras. This class should always be inherited when
you build a new camera.

## Constructor

### Camera

  
  
```ts  
function Camera( ): void;  
```  

Creates a new Camera. Note that this class is not intended to be called
directly; you probably want a
[PerspectiveCamera](en\cameras\PerspectiveCamera.html) or
[OrthographicCamera](en\cameras\OrthographicCamera.html) instead.

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### isCamera

  
  
```ts  
isCamera: Boolean;  
```  

Read-only flag to check if a given object is of type Camera.

### layers

  
  
```ts  
layers: Layers;  
```  

The [layers](en\core\Layers.html) that the camera is a member of. This is an
inherited property from [Object3D](en\core\Object3D.html).  
  
Objects must share at least one layer with the camera to be seen when the
camera's viewpoint is rendered.

### matrixWorldInverse

  
  
```ts  
matrixWorldInverse: Matrix4;  
```  

This is the inverse of matrixWorld. MatrixWorld contains the Matrix which has
the world transform of the Camera.

### projectionMatrix

  
  
```ts  
projectionMatrix: Matrix4;  
```  

This is the matrix which contains the projection.

### projectionMatrixInverse

  
  
```ts  
projectionMatrixInverse: Matrix4;  
```  

The inverse of projectionMatrix.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### clone

  
  
```ts  
function clone( ): Camera;  
```  

Return a new camera with the same properties as this one.

### copy

  
  
```ts  
function copy( source: Camera, recursive: Boolean ): this;  
```  

Copy the properties from the source camera into this one.

### getWorldDirection

  
  
```ts  
function getWorldDirection( target: Vector3 ): Vector3;  
```  

[target](en\math\Vector3.html) — the result will be copied into this Vector3.  
  
Returns a [Vector3](en\math\Vector3.html) representing the world space
direction in which the camera is looking. (Note: A camera looks down its
local, negative z-axis).  
  

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/cameras/Camera.js">src/cameras/Camera.js</a>

