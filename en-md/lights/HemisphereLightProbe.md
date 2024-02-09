[page:Object3D] → [page:Light] → [page:LightProbe]

# [name]

Light probes are an alternative way of adding light to a 3D scene.
HemisphereLightProbe is the light estimation data of a single hemisphere light
in the scene. For more information about light probes, go to
[page:LightProbe].

## Constructor

###  [name]( [param:Color skyColor], [param:Color groundColor], [param:Float
intensity] )

[page:Color skyColor] - (optional) An instance of Color, string representing a
color or a number representing a color.  
[page:Color groundColor] - (optional) An instance of Color, string
representing a color or a number representing a color.  
[page:Float intensity] - (optional) Numeric value of the light probe's
intensity. Default is `1`.  
  
Creates a new [name].

## Properties

See the base [page:LightProbe LightProbe] class for common properties.

### <br/> Boolean isHemisphereLightProbe; <br/>

Read-only flag to check if a given object is of type [name].

## Methods

See the base [page:LightProbe LightProbe] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

