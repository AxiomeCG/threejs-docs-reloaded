[page:Object3D] → [page:Light] → [page:LightProbe]

# [name]

Light probes are an alternative way of adding light to a 3D scene.
AmbientLightProbe is the light estimation data of a single ambient light in
the scene. For more information about light probes, go to [page:LightProbe].

## Constructor

### [name]( [param:Color color], [param:Float intensity] )

[page:Color color] - (optional) An instance of Color, string representing a
color or a number representing a color.  
[page:Float intensity] - (optional) Numeric value of the light probe's
intensity. Default is `1`.  
  
Creates a new [name].

## Properties

See the base [page:LightProbe LightProbe] class for common properties.

### <br/> Boolean isAmbientLightProbe; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

See the base [page:LightProbe LightProbe] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

