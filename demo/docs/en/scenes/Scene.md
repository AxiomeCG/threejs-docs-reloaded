[Object3D](en\core\Object3D.html) →

# Scene

Scenes allow you to set up what and where is to be rendered by three.js. This
is where you place objects, lights and cameras.

## Constructor

### Scene

  
  
```ts  
function Scene( ): void;  
```  

Create a new scene object.

## Properties

### background

  
  
```ts  
background: Object;  
```  

Defines the background of the scene. Default is `null`. Valid inputs are:

  * A [Color](en\math\Color.html) for defining a uniform colored background.
  * A [Texture](en\textures\Texture.html) for defining a (flat) textured background.
  * Texture cubes ([CubeTexture](en\textures\CubeTexture.html)) or equirectangular textures for defining a skybox.

Note: Any camera related configurations like `zoom` or `view` are ignored.

### backgroundBlurriness

  
  
```ts  
backgroundBlurriness: Float;  
```  

Sets the blurriness of the background. Only influences environment maps
assigned to [Scene.background](#). Valid input is a float between `0` and `1`.
Default is `0`.

### backgroundIntensity

  
  
```ts  
backgroundIntensity: Float;  
```  

Attenuates the color of the background. Only applies to background textures.
Default is `1`.

### environment

  
  
```ts  
environment: Texture;  
```  

Sets the environment map for all physical materials in the scene. However,
it's not possible to overwrite an existing texture assigned to
[MeshStandardMaterial.envMap](#). Default is `null`.

### fog

  
  
```ts  
fog: Fog;  
```  

A [fog](en\scenes\Fog.html) instance defining the type of fog that affects
everything rendered in the scene. Default is `null`.

### isScene

  
  
```ts  
isScene: Boolean;  
```  

Read-only flag to check if a given object is of type Scene.

### overrideMaterial

  
  
```ts  
overrideMaterial: Material;  
```  

Forces everything in the scene to be rendered with the defined material.
Default is `null`.

## Methods

### toJSON

  
  
```ts  
function toJSON( meta: Object ): Object;  
```  

meta -- object containing metadata such as textures or images for the scene.  
Convert the scene to three.js <a
href="https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4">JSON
Object/Scene format</a>.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/scenes/Scene.js">src/scenes/Scene.js</a>

