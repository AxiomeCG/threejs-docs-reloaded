# WebXRManager

This class represents an abstraction of the WebXR Device API and is internally
used by [WebGLRenderer](en\renderers\WebGLRenderer.html). WebXRManager also
provides a public interface that allows users to enable/disable XR and perform
XR related tasks like for instance retrieving controllers.

## Properties

### cameraAutoUpdate

  
  
```ts  
cameraAutoUpdate: Boolean;  
```  

Whether the manager's XR camera should be automatically updated or not.
Default is `true`.

### enabled

  
  
```ts  
enabled: Boolean;  
```  

This flag notifies the renderer to be ready for XR rendering. Default is
`false`. Set it to `true` if you are going to use XR in your app.

### isPresenting

  
  
```ts  
isPresenting: Boolean;  
```  

Whether XR presentation is active or not. Default is `false`. This flag is
read-only and automatically set by WebXRManager.

## Methods

### getCamera

  
  
```ts  
function getCamera( ): ArrayCamera;  
```  

Returns an instance of [ArrayCamera](en\cameras\ArrayCamera.html) which
represents the XR camera of the active XR session. For each view it holds a
separate camera object in its [cameras](#) property.

The camera's `fov` is currently not used and does not reflect the fov of the
XR camera. If you need the fov on app level, you have to compute in manually
from the XR camera's projection matrices.

### getController

  
  
```ts  
function getController( index: Integer ): Group;  
```  

[index](#) — The index of the controller.  
  
Returns a [Group](en\objects\Group.html) representing the so called *target
ray* space of the XR controller. Use this space for visualizing 3D objects
that support the user in pointing tasks like UI interaction.

### getControllerGrip

  
  
```ts  
function getControllerGrip( index: Integer ): Group;  
```  

[index](#) — The index of the controller.  
  
Returns a [Group](en\objects\Group.html) representing the so called `grip`
space of the XR controller. Use this space if the user is going to hold other
3D objects like a lightsaber.

Note: If you want to show something in the user's hand AND offer a pointing
ray at the same time, you'll want to attached the handheld object to the group
returned by [.getControllerGrip](#)() and the ray to the group returned by
[.getController](#)(). The idea is to have two different groups in two
different coordinate spaces for the same WebXR controller.

### getFoveation

  
  
```ts  
function getFoveation( ): Float;  
```  

Returns the amount of foveation used by the XR compositor for the projection
layer.

### getHand

  
  
```ts  
function getHand( index: Integer ): Group;  
```  

[index](#) — The index of the controller.  
  
Returns a [Group](en\objects\Group.html) representing the so called `hand` or
`joint` space of the XR controller. Use this space for visualizing the user's
hands when no physical controllers are used.

### getReferenceSpace

  
  
```ts  
function getReferenceSpace( ): String;  
```  

Returns the reference space.

### getSession

  
  
```ts  
function getSession( ): XRSession;  
```  

Returns the `XRSession` object which allows a more fine-grained management of
active WebXR sessions on application level.

### setFoveation

  
  
```ts  
function setFoveation( foveation: Float ): undefined;  
```  

[foveation](#) — The foveation to set.  
  
Specifies the amount of foveation used by the XR compositor for the layer.
Must be a value between `0` and `1`.

### setFramebufferScaleFactor

  
  
```ts  
function setFramebufferScaleFactor( framebufferScaleFactor: Float ):
undefined;  
```  

[framebufferScaleFactor](#) — The framebuffer scale factor to set.  
  
Specifies the scaling factor to use when determining the size of the
framebuffer when rendering to a XR device. The value is relative to the
default XR device display resolution. Default is `1`. A value of `0.5` would
specify a framebuffer with 50% of the display's native resolution.

Note: It is not possible to change the framebuffer scale factor while
presenting XR content.

### setReferenceSpace

  
  
```ts  
function setReferenceSpace( referenceSpace: XRReferenceSpace ): undefined;  
```  

[referenceSpace](#) — A custom reference space.  
  
Can be used to configure a custom reference space which overwrites the default
reference space.

### setReferenceSpaceType

  
  
```ts  
function setReferenceSpaceType( referenceSpaceType: String ): undefined;  
```  

[referenceSpaceType](#) — The reference space type to set.  
  
Can be used to configure a spatial relationship with the user's physical
environment. Depending on how the user moves in 3D space, setting an
appropriate reference space can improve tracking. Default is `local-floor`.
Please check out the <a href="https://developer.mozilla.org/en-
US/docs/Web/API/XRReferenceSpaceType">MDN</a> for possible values and their
use cases.

### updateCamera

  
  
```ts  
function updateCamera( camera: PerspectiveCamera ): undefined;  
```  

Updates the state of the XR camera. Use this method on app level if you set
[.cameraAutoUpdate](#) to `false`. The method requires the non-XR camera of
the scene as a parameter. The passed in camera's transformation is
automatically adjusted to the position of the XR camera when calling this
method.

Note: It is not possible to change the reference space type while presenting
XR content.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/webxr/WebXRManager.js">src/renderers/webxr/WebXRManager.js</a>

