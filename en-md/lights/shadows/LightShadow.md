# [name]

Serves as a base class for the other shadow classes.

## Constructor

### [name]( [param:Camera camera] )

[page:Camera camera] - the light's view of the world.  
  
Create a new [name]. This is not intended to be called directly - it is used
as a base class by other light shadows.

## Properties

### <br/> Boolean autoUpdate; <br/>

Enables automatic updates of the light's shadow. Default is `true`. If you do
not require dynamic lighting / shadows, you may set this to `false`.

### <br/> Camera camera; <br/>

The light's view of the world. This is used to generate a depth map of the
scene; objects behind other objects from the light's perspective will be in
shadow.

### <br/> Float bias; <br/>

Shadow map bias, how much to add or subtract from the normalized depth when
deciding whether a surface is in shadow.  
The default is `0`. Very tiny adjustments here (in the order of `0.0001`) may
help reduce artifacts in shadows

### <br/> Integer blurSamples; <br/>

The amount of samples to use when blurring a VSM shadow map.

### <br/> WebGLRenderTarget map; <br/>

The depth map generated using the internal camera; a location beyond a pixel's
depth is in shadow. Computed internally during rendering.

### <br/> WebGLRenderTarget mapPass; <br/>

The distribution map generated using the internal camera; an occlusion is
calculated based on the distribution of depths. Computed internally during
rendering.

### <br/> Vector2 mapSize; <br/>

A [Page:Vector2] defining the width and height of the shadow map.  
  
Higher values give better quality shadows at the cost of computation time.
Values must be powers of 2, up to the
[page:WebGLRenderer.capabilities].maxTextureSize for a given device, although
the width and height don't have to be the same (so, for example, (512, 1024)
is valid). The default is `( 512, 512 )`.

### <br/> Matrix4 matrix; <br/>

Model to shadow camera space, to compute location and depth in shadow map.
Stored in a [page:Matrix4 Matrix4]. This is computed internally during
rendering.

### <br/> Boolean needsUpdate; <br/>

When set to `true`, shadow maps will be updated in the next `render` call.
Default is `false`. If you have set [page:.autoUpdate] to `false`, you will
need to set this property to `true` and then make a render call to update the
light's shadow.

### <br/> Float normalBias; <br/>

Defines how much the position used to query the shadow map is offset along the
object normal. The default is `0`. Increasing this value can be used to reduce
shadow acne especially in large scenes where light shines onto geometry at a
shallow angle. The cost is that shadows may appear distorted.

### <br/> Float radius; <br/>

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

### [method:Vector2 getFrameExtents]()

Used internally by the renderer to extend the shadow map to contain all
viewports

### [method:undefined updateMatrices]( [param:Light light] )

Update the matrices for the camera and shadow, used internally by the
renderer.  
  
light -- the light for which the shadow is being rendered.

### [method:Frustum getFrustum]()

Gets the shadow cameras frustum. Used internally by the renderer to cull
objects.

### [method:number getViewportCount]()

Used internally by the renderer to get the number of viewports that need to be
rendered for this shadow.

### [method:undefined dispose]()

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### <br/> function copy( source: LightShadow ): copy; <br/>

Copies value of all the properties from the [page:LightShadow source] to this
Light.

### [method:LightShadow clone]()

Creates a new LightShadow with the same properties as this one.

### [method:Object toJSON]()

Serialize this LightShadow.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/lights/[name].js
src/lights/[name].js]

