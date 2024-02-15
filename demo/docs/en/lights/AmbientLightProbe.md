[Object3D](en\core\Object3D.html) → [Light](en\lights\Light.html) →
[LightProbe](en\lights\LightProbe.html)

# AmbientLightProbe

Light probes are an alternative way of adding light to a 3D scene.
AmbientLightProbe is the light estimation data of a single ambient light in
the scene. For more information about light probes, go to
[LightProbe](en\lights\LightProbe.html).

## Constructor

### AmbientLightProbe

  
  
```ts  
function AmbientLightProbe( color: Color, intensity: Float ): void;  
```  

[color](en\math\Color.html) - (optional) An instance of Color, string
representing a color or a number representing a color.  
[intensity](#) - (optional) Numeric value of the light probe's intensity.
Default is `1`.  
  
Creates a new AmbientLightProbe.

## Properties

See the base [LightProbe](en\lights\LightProbe.html) class for common
properties.

### isAmbientLightProbe

  
  
```ts  
isAmbientLightProbe: Boolean;  
```  

Read-only flag to check if a given object is of type AmbientLightProbe.

## Methods

See the base [LightProbe](en\lights\LightProbe.html) class for common methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/AmbientLightProbe.js">src/lights/AmbientLightProbe.js</a>

