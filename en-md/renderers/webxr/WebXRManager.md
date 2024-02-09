# [name]

This class represents an abstraction of the WebXR Device API and is internally
used by [page:WebGLRenderer]. [name] also provides a public interface that
allows users to enable/disable XR and perform XR related tasks like for
instance retrieving controllers.

## Properties

### <br/> Boolean cameraAutoUpdate; <br/>

Whether the manager's XR camera should be automatically updated or not.
Default is `true`.

### <br/> Boolean enabled; <br/>

This flag notifies the renderer to be ready for XR rendering. Default is
`false`. Set it to `true` if you are going to use XR in your app.

### <br/> Boolean isPresenting; <br/>

Whether XR presentation is active or not. Default is `false`. This flag is
read-only and automatically set by [name].

## Methods

### [method:ArrayCamera getCamera]()

Returns an instance of [page:ArrayCamera] which represents the XR camera of
the active XR session. For each view it holds a separate camera object in its
[page:ArrayCamera.cameras cameras] property.

The camera's `fov` is currently not used and does not reflect the fov of the
XR camera. If you need the fov on app level, you have to compute in manually
from the XR camera's projection matrices.

### [method:Group getController]( [param:Integer index] )

[page:Integer index] — The index of the controller.  
  
Returns a [page:Group] representing the so called *target ray* space of the XR
controller. Use this space for visualizing 3D objects that support the user in
pointing tasks like UI interaction.

### [method:Group getControllerGrip]( [param:Integer index] )

[page:Integer index] — The index of the controller.  
  
Returns a [page:Group] representing the so called `grip` space of the XR
controller. Use this space if the user is going to hold other 3D objects like
a lightsaber.

Note: If you want to show something in the user's hand AND offer a pointing
ray at the same time, you'll want to attached the handheld object to the group
returned by [page:.getControllerGrip]() and the ray to the group returned by
[page:.getController](). The idea is to have two different groups in two
different coordinate spaces for the same WebXR controller.

### [method:Float getFoveation]()

Returns the amount of foveation used by the XR compositor for the projection
layer.

### [method:Group getHand]( [param:Integer index] )

[page:Integer index] — The index of the controller.  
  
Returns a [page:Group] representing the so called `hand` or `joint` space of
the XR controller. Use this space for visualizing the user's hands when no
physical controllers are used.

### [method:String getReferenceSpace]()

Returns the reference space.

### [method:XRSession getSession]()

Returns the `XRSession` object which allows a more fine-grained management of
active WebXR sessions on application level.

### [method:undefined setFoveation]( [param:Float foveation] )

[page:Float foveation] — The foveation to set.  
  
Specifies the amount of foveation used by the XR compositor for the layer.
Must be a value between `0` and `1`.

###  [method:undefined setFramebufferScaleFactor]( [param:Float
framebufferScaleFactor] )

[page:Float framebufferScaleFactor] — The framebuffer scale factor to set.  
  
Specifies the scaling factor to use when determining the size of the
framebuffer when rendering to a XR device. The value is relative to the
default XR device display resolution. Default is `1`. A value of `0.5` would
specify a framebuffer with 50% of the display's native resolution.

Note: It is not possible to change the framebuffer scale factor while
presenting XR content.

###  [method:undefined setReferenceSpace]( [param:XRReferenceSpace
referenceSpace] )

[page:XRReferenceSpace referenceSpace] — A custom reference space.  
  
Can be used to configure a custom reference space which overwrites the default
reference space.

###  [method:undefined setReferenceSpaceType]( [param:String
referenceSpaceType] )

[page:String referenceSpaceType] — The reference space type to set.  
  
Can be used to configure a spatial relationship with the user's physical
environment. Depending on how the user moves in 3D space, setting an
appropriate reference space can improve tracking. Default is `local-floor`.
Please check out the [link:https://developer.mozilla.org/en-
US/docs/Web/API/XRReferenceSpaceType MDN] for possible values and their use
cases.

### [method:undefined updateCamera]( [param:PerspectiveCamera camera] )

Updates the state of the XR camera. Use this method on app level if you set
[page:.cameraAutoUpdate] to `false`. The method requires the non-XR camera of
the scene as a parameter. The passed in camera's transformation is
automatically adjusted to the position of the XR camera when calling this
method.

Note: It is not possible to change the reference space type while presenting
XR content.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

