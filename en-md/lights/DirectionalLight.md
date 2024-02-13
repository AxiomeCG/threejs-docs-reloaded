[page:Object3D] → [page:Light] →

# DirectionalLight

A light that gets emitted in a specific direction. This light will behave as
though it is infinitely far away and the rays produced from it are all
parallel. The common use case for this is to simulate daylight; the sun is far
enough away that its position can be considered to be infinite, and all light
rays coming from it are parallel.  
  
This light can cast shadows - see the [page:DirectionalLightShadow] page for
details.

## A Note about Position, Target and rotation

A common point of confusion for directional lights is that setting the
rotation has no effect. This is because three.js's DirectionalLight is the
equivalent to what is often called a 'Target Direct Light' in other
applications.  
  
This means that its direction is calculated as pointing from the light's
[page:Object3D.position position] to the [page:.target target]'s position (as
opposed to a 'Free Direct Light' that just has a rotation component).  
  
The reason for this is to allow the light to cast shadows - the [page:.shadow
shadow] camera needs a position to calculate shadows from.  
  
See the [page:.target target] property below for details on updating the
target.

## Code Example

  
```ts  
// White directional light at half intensity shining from the top. const
directionalLight = new THREE.DirectionalLight( 0xffffff, 0.5 ); scene.add(
directionalLight );  
```  

## Examples

[example:misc_controls_fly controls / fly ]  
[example:webgl_effects_parallaxbarrier effects / parallaxbarrier ]  
[example:webgl_effects_stereo effects / stereo ]  
[example:webgl_geometry_extrude_splines geometry / extrude / splines ]  
[example:webgl_materials_bumpmap materials / bumpmap ]

## Constructor

###  function DirectionalLight( color: Integer, intensity: Float ): void;

[page:Integer color] - (optional) hexadecimal color of the light. Default is
0xffffff (white).  
[page:Float intensity] - (optional) numeric value of the light's
strength/intensity. Default is `1`.  
  
Creates a new DirectionalLight.

## Properties

See the base [page:Light Light] class for common properties.

###  Boolean castShadow;

If set to `true` light will cast dynamic shadows. *Warning*: This is expensive
and requires tweaking to get shadows looking right. See the
[page:DirectionalLightShadow] for details. The default is `false`.

###  Boolean isDirectionalLight;

Read-only flag to check if a given object is of type DirectionalLight.

###  Vector3 position;

This is set equal to [page:Object3D.DEFAULT_UP] (0, 1, 0), so that the light
shines from the top down.

###  DirectionalLightShadow shadow;

A [page:DirectionalLightShadow] used to calculate shadows for this light.

###  Object3D target;

The DirectionalLight points from its [page:.position position] to
target.position. The default position of the target is `(0, 0, 0)`.  
*Note*: For the target's position to be changed to anything other than the default, it must be added to the [page:Scene scene] using

  
```ts  
scene.add( light.target );  
```  

This is so that the target's [page:Object3D.matrixWorld matrixWorld] gets
automatically updated each frame.  
  
It is also possible to set the target to be another object in the scene
(anything with a [page:Object3D.position position] property), like so:

  
```ts  
const targetObject = new THREE.Object3D(); scene.add(targetObject);
light.target = targetObject;  
```  

The directionalLight will now track the target object.

## Methods

See the base [page:Light Light] class for common methods.

###  function dispose( ): undefined;

Frees the GPU-related resources allocated by this instance. Call this method
whenever this instance is no longer used in your app.

###  function copy( source: DirectionalLight ): this;

Copies value of all the properties from the [page:DirectionalLight source] to
this DirectionalLight.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

