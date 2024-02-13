# LightShadow

Serves as a base class for the other shadow classes.

## Constructor

###  function LightShadow( camera: Camera ): void;

[page:Camera camera] - the light's view of the world.  
  
Create a new LightShadow. This is not intended to be called directly - it is
used as a base class by other light shadows.

## Properties

###  Boolean autoUpdate;

Enables automatic updates of the light's shadow. Default is `true`. If you do
not require dynamic lighting / shadows, you may set this to `false`.

###  Camera camera;

The light's view of the world. This is used to generate a depth map of the
scene; objects behind other objects from the light's perspective will be in
shadow.

###  Float bias;

Shadow map bias, how much to add or subtract from the normalized depth when
deciding whether a surface is in shadow.  
The default is `0`. Very tiny adjustments here (in the order of `0.0001`) may
help reduce artifacts in shadows

###  Integer blurSamples;

The amount of samples to use when blurring a VSM shadow map.

###  WebGLRenderTarget map;

The depth map generated using the internal camera; a location beyond a pixel's
depth is in shadow. Computed internally during rendering.

###  WebGLRenderTarget mapPass;

The distribution map generated using the internal camera; an occlusion is
calculated based on the distribution of depths. Computed internally during
rendering.

###  Vector2 mapSize;

A [Page:Vector2] defining the width and height of the shadow map.  
  
Higher values give better quality shadows at the cost of computation time.
Values must be powers of 2, up to the
[page:WebGLRenderer.capabilities].maxTextureSize for a given device, although
the width and height don't have to be the same (so, for example, (512, 1024)
is valid). The default is `( 512, 512 )`.

###  Matrix4 matrix;

Model to shadow camera space, to compute location and depth in shadow map.
Stored in a [page:Matrix4 Matrix4]. This is computed internally during
rendering.

###  Boolean needsUpdate;

When set to `true`, shadow maps will be updated in the next `render` call.
Default is `false`. If you have set [page:.autoUpdate] to `false`, you will
need to set this property to `true` and then make a render call to update the
light's shadow.

###  Float normalBias;

Defines how much the position used to query the shadow map is offset along the
object normal. The default is `0`. Increasing this value can be used to reduce
shadow acne especially in large scenes where light shines onto geometry at a
shallow angle. The cost is that shadows may appear distorted.

###  Float radius;

Setting this to values greater than 1 will blur the edges of the shadow.  
High values will cause unwanted banding effects in the shadows - a greater
[page:.mapSize mapSize] will allow for a higher value to be used here before
these effects become visible.  
If [page:WebGLRenderer.shadowMap.type] is set to [page:Renderer
PCFSoftShadowMap], radius has no effect and it is recommended to increase
softness by decreasing [page:.mapSize mapSize] instead.  
  
Note that this has no effect if the [page:WebGLRenderer.shadowMap.type] is set
to [page:Renderer BasicShadowMap].

## Methods

###  function getFrameExtents( ): Vector2;

Used internally by the renderer to extend the shadow map to contain all
viewports

###  function updateMatrices( light: Light ): undefined;

Update the matrices for the camera and shadow, used internally by the
renderer.  
  
light -- the light for which the shadow is being rendered.

###  function getFrustum( ): Frustum;

Gets the shadow cameras frustum. Used internally by the renderer to cull
objects.

###  function getViewportCount( ): number;

Used internally by the renderer to get the number of viewports that need to be
rendered for this shadow.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function copy( source: LightShadow ): this;

Copies value of all the properties from the [page:LightShadow source] to this
Light.

###  function clone( ): LightShadow;

Creates a new LightShadow with the same properties as this one.

###  function toJSON( ): Object;

Serialize this LightShadow.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/lights/LightShadow.js
src/lights/LightShadow.js]

