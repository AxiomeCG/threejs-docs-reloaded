[page:Object3D] →

# Light

Abstract base class for lights - all other light types inherit the properties
and methods described here.

## Constructor

###  function Light( color: Integer, intensity: Float ): void;

[page:Integer color] - (optional) hexadecimal color of the light. Default is
0xffffff (white).  
[page:Float intensity] - (optional) numeric value of the light's
strength/intensity. Default is `1`.  
  
Creates a new Light. Note that this is not intended to be called directly (use
one of derived classes instead).

## Properties

See the base [page:Object3D Object3D] class for common properties.

###  Color color;

Color of the light. Defaults to a new [page:Color] set to white, if not passed
in the constructor.  

###  Float intensity;

The light's intensity, or strength.  
When [page:WebGLRenderer.useLegacyLights legacy lighting mode] is disabled,
the units of intensity depend on the type of light.  
Default - `1.0`.

###  Boolean isLight;

Read-only flag to check if a given object is of type Light.

## Methods

See the base [page:Object3D Object3D] class for common methods.

###  function dispose( ): undefined;

Abstract dispose method for classes that extend this class; implemented by
subclasses that have disposable GPU-related resources.

###  function copy( source: Light ): this;

Copies the value of [page:.color color] and [page:.intensity intensity] from
the [page:Light source] light into this one.

###  function toJSON( meta: Object ): Object;

meta -- object containing metadata such as materials, textures for objects.  
Convert the light to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

