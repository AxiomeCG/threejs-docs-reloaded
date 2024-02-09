[page:Object3D] → [page:Light] →

# [name]

Light probes are an alternative way of adding light to a 3D scene. Unlike
classical light sources (e.g. directional, point or spot lights), light probes
do not emit light. Instead they store information about light passing through
3D space. During rendering, the light that hits a 3D object is approximated by
using the data from the light probe.

Light probes are usually created from (radiance) environment maps. The class
[page:LightProbeGenerator] can be used to create light probes from instances
of [page:CubeTexture] or [page:WebGLCubeRenderTarget]. However, light
estimation data could also be provided in other forms e.g. by WebXR. This
enables the rendering of augmented reality content that reacts to real world
lighting.

The current probe implementation in three.js supports so-called diffuse light
probes. This type of light probe is functionally equivalent to an irradiance
environment map.

## Examples

[example:webgl_lightprobe WebGL / light probe ]  
[example:webgl_lightprobe_cubecamera WebGL / light probe / cube camera ]

## Constructor

### [name]( [param:SphericalHarmonics3 sh], [param:Float intensity] )

[page:SphericalHarmonics3 sh] - (optional) An instance of
[page:SphericalHarmonics3].  
[page:Float intensity] - (optional) Numeric value of the light probe's
intensity. Default is `1`.  
  
Creates a new [name].

## Properties

See the base [page:Light Light] class for common properties. The
[page:Light.color color] property is currently not evaluated and thus has no
effect.

### <br/> Boolean isLightProbe; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> SphericalHarmonics3 sh; <br/>

A light probe uses spherical harmonics to encode lighting information.

## Methods

See the base [page:Light Light] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

