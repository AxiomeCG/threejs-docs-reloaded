[page:Object3D] →

# [name]

Abstract base class for cameras. This class should always be inherited when
you build a new camera.

## Constructor

### [name]()

Creates a new [name]. Note that this class is not intended to be called
directly; you probably want a [page:PerspectiveCamera] or
[page:OrthographicCamera] instead.

## Properties

See the base [page:Object3D] class for common properties.

### <br/> Boolean isCamera; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Layers layers; <br/>

The [page:Layers layers] that the camera is a member of. This is an inherited
property from [page:Object3D].  
  
Objects must share at least one layer with the camera to be seen when the
camera's viewpoint is rendered.

### <br/> Matrix4 matrixWorldInverse; <br/>

This is the inverse of matrixWorld. MatrixWorld contains the Matrix which has
the world transform of the Camera.

### <br/> Matrix4 projectionMatrix; <br/>

This is the matrix which contains the projection.

### <br/> Matrix4 projectionMatrixInverse; <br/>

The inverse of projectionMatrix.

## Methods

See the base [page:Object3D] class for common methods.

### [method:Camera clone]( )

Return a new camera with the same properties as this one.

### <br/> function copy( source: Camera, recursive: Boolean? ): copy; <br/>

Copy the properties from the source camera into this one.

### [method:Vector3 getWorldDirection]( [param:Vector3 target] )

[page:Vector3 target] — the result will be copied into this Vector3.  
  
Returns a [page:Vector3] representing the world space direction in which the
camera is looking. (Note: A camera looks down its local, negative z-axis).  
  

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

