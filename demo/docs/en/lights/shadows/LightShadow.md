# LightShadow

Serves as a base class for the other shadow classes.

## Constructor

### LightShadow

  
  
```ts  
function LightShadow( camera: Camera ): void;  
```  

[camera](en\cameras\Camera.html) - the light's view of the world.  
  
Create a new LightShadow. This is not intended to be called directly - it is
used as a base class by other light shadows.

## Properties

### autoUpdate

  
  
```ts  
autoUpdate: Boolean;  
```  

Enables automatic updates of the light's shadow. Default is `true`. If you do
not require dynamic lighting / shadows, you may set this to `false`.

### camera

  
  
```ts  
camera: Camera;  
```  

The light's view of the world. This is used to generate a depth map of the
scene; objects behind other objects from the light's perspective will be in
shadow.

### bias

  
  
```ts  
bias: Float;  
```  

Shadow map bias, how much to add or subtract from the normalized depth when
deciding whether a surface is in shadow.  
The default is `0`. Very tiny adjustments here (in the order of `0.0001`) may
help reduce artifacts in shadows

### blurSamples

  
  
```ts  
blurSamples: Integer;  
```  

The amount of samples to use when blurring a VSM shadow map.

### map

  
  
```ts  
map: WebGLRenderTarget;  
```  

The depth map generated using the internal camera; a location beyond a pixel's
depth is in shadow. Computed internally during rendering.

### mapPass

  
  
```ts  
mapPass: WebGLRenderTarget;  
```  

The distribution map generated using the internal camera; an occlusion is
calculated based on the distribution of depths. Computed internally during
rendering.

### mapSize

  
  
```ts  
mapSize: Vector2;  
```  

A [Page:Vector2] defining the width and height of the shadow map.  
  
Higher values give better quality shadows at the cost of computation time.
Values must be powers of 2, up to the
[WebGLRenderer.capabilities](#).maxTextureSize for a given device, although
the width and height don't have to be the same (so, for example, (512, 1024)
is valid). The default is `( 512, 512 )`.

### matrix

  
  
```ts  
matrix: Matrix4;  
```  

Model to shadow camera space, to compute location and depth in shadow map.
Stored in a [Matrix4](en\math\Matrix4.html). This is computed internally
during rendering.

### needsUpdate

  
  
```ts  
needsUpdate: Boolean;  
```  

When set to `true`, shadow maps will be updated in the next `render` call.
Default is `false`. If you have set [.autoUpdate](#) to `false`, you will need
to set this property to `true` and then make a render call to update the
light's shadow.

### normalBias

  
  
```ts  
normalBias: Float;  
```  

Defines how much the position used to query the shadow map is offset along the
object normal. The default is `0`. Increasing this value can be used to reduce
shadow acne especially in large scenes where light shines onto geometry at a
shallow angle. The cost is that shadows may appear distorted.

### radius

  
  
```ts  
radius: Float;  
```  

Setting this to values greater than 1 will blur the edges of the shadow.  
High values will cause unwanted banding effects in the shadows - a greater
[.mapSize](#mapSize) will allow for a higher value to be used here before
these effects become visible.  
If [WebGLRenderer.shadowMap.type](#) is set to [.enderer](#enderer), radius
has no effect and it is recommended to increase softness by decreasing
[.mapSize](#mapSize) instead.  
  
Note that this has no effect if the [WebGLRenderer.shadowMap.type](#) is set
to [BasicShadowMap](en\constants\Renderer.html).

## Methods

### getFrameExtents

  
  
```ts  
function getFrameExtents( ): Vector2;  
```  

Used internally by the renderer to extend the shadow map to contain all
viewports

### updateMatrices

  
  
```ts  
function updateMatrices( light: Light ): undefined;  
```  

Update the matrices for the camera and shadow, used internally by the
renderer.  
  
light -- the light for which the shadow is being rendered.

### getFrustum

  
  
```ts  
function getFrustum( ): Frustum;  
```  

Gets the shadow cameras frustum. Used internally by the renderer to cull
objects.

### getViewportCount

  
  
```ts  
function getViewportCount( ): number;  
```  

Used internally by the renderer to get the number of viewports that need to be
rendered for this shadow.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

### copy

  
  
```ts  
function copy( source: LightShadow ): this;  
```  

Copies value of all the properties from the
[source](en\lights\shadows\LightShadow.html) to this Light.

### clone

  
  
```ts  
function clone( ): LightShadow;  
```  

Creates a new LightShadow with the same properties as this one.

### toJSON

  
  
```ts  
function toJSON( ): Object;  
```  

Serialize this LightShadow.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/LightShadow.js">src/lights/LightShadow.js</a>

