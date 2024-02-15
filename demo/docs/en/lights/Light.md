[Object3D](en\core\Object3D.html) →

# Light

Abstract base class for lights - all other light types inherit the properties
and methods described here.

## Constructor

### Light

  
  
```ts  
function Light( color: Integer, intensity: Float ): void;  
```  

[color](#) - (optional) hexadecimal color of the light. Default is 0xffffff
(white).  
[intensity](#) - (optional) numeric value of the light's strength/intensity.
Default is `1`.  
  
Creates a new Light. Note that this is not intended to be called directly (use
one of derived classes instead).

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### color

  
  
```ts  
color: Color;  
```  

Color of the light. Defaults to a new [Color](en\math\Color.html) set to
white, if not passed in the constructor.  

### intensity

  
  
```ts  
intensity: Float;  
```  

The light's intensity, or strength.  
When [legacy lighting mode](#) is disabled, the units of intensity depend on
the type of light.  
Default - `1.0`.

### isLight

  
  
```ts  
isLight: Boolean;  
```  

Read-only flag to check if a given object is of type Light.

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### dispose

  
  
```ts  
function dispose( ): undefined;  
```  

Abstract dispose method for classes that extend this class; implemented by
subclasses that have disposable GPU-related resources.

### copy

  
  
```ts  
function copy( source: Light ): this;  
```  

Copies the value of [.color](#color) and [.intensity](#intensity) from the
[.ight](#ight) light into this one.

### toJSON

  
  
```ts  
function toJSON( meta: Object ): Object;  
```  

meta -- object containing metadata such as materials, textures for objects.  
Convert the light to three.js <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/lights/Light.js">src/lights/Light.js</a>

