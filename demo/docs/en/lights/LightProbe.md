[Object3D](en\core\Object3D.html) → [Light](en\lights\Light.html) →

# LightProbe

Light probes are an alternative way of adding light to a 3D scene. Unlike
classical light sources (e.g. directional, point or spot lights), light probes
do not emit light. Instead they store information about light passing through
3D space. During rendering, the light that hits a 3D object is approximated by
using the data from the light probe.

Light probes are usually created from (radiance) environment maps. The class
[LightProbeGenerator](#) can be used to create light probes from instances of
[CubeTexture](en\textures\CubeTexture.html) or
[WebGLCubeRenderTarget](en\renderers\WebGLCubeRenderTarget.html). However,
light estimation data could also be provided in other forms e.g. by WebXR.
This enables the rendering of augmented reality content that reacts to real
world lighting.

The current probe implementation in three.js supports so-called diffuse light
probes. This type of light probe is functionally equivalent to an irradiance
environment map.

## Examples

[example:webgl_lightprobe WebGL / light probe ]  
[example:webgl_lightprobe_cubecamera WebGL / light probe / cube camera ]

## Constructor

### LightProbe

  
  
```ts  
function LightProbe( sh: SphericalHarmonics3, intensity: Float ): void;  
```  

[sh](en\math\SphericalHarmonics3.html) - (optional) An instance of
[SphericalHarmonics3](en\math\SphericalHarmonics3.html).  
[intensity](#) - (optional) Numeric value of the light probe's intensity.
Default is `1`.  
  
Creates a new LightProbe.

## Properties

See the base [Light](en\lights\Light.html) class for common properties. The
[color](#) property is currently not evaluated and thus has no effect.

### isLightProbe

  
  
```ts  
isLightProbe: Boolean;  
```  

Read-only flag to check if a given object is of type LightProbe.

### sh

  
  
```ts  
sh: SphericalHarmonics3;  
```  

A light probe uses spherical harmonics to encode lighting information.

## Methods

See the base [Light](en\lights\Light.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/LightProbe.js">src/lights/LightProbe.js</a>

