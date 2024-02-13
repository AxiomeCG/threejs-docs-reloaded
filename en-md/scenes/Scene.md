[page:Object3D] →

# Scene

Scenes allow you to set up what and where is to be rendered by three.js. This
is where you place objects, lights and cameras.

## Constructor

###  function Scene( ): void;

Create a new scene object.

## Properties

###  Object background;

Defines the background of the scene. Default is `null`. Valid inputs are:

  * A [page:Color] for defining a uniform colored background.
  * A [page:Texture] for defining a (flat) textured background.
  * Texture cubes ([page:CubeTexture]) or equirectangular textures for defining a skybox.

Note: Any camera related configurations like `zoom` or `view` are ignored.

###  Float backgroundBlurriness;

Sets the blurriness of the background. Only influences environment maps
assigned to [page:Scene.background]. Valid input is a float between `0` and
`1`. Default is `0`.

###  Float backgroundIntensity;

Attenuates the color of the background. Only applies to background textures.
Default is `1`.

###  Texture environment;

Sets the environment map for all physical materials in the scene. However,
it's not possible to overwrite an existing texture assigned to
[page:MeshStandardMaterial.envMap]. Default is `null`.

###  Fog fog;

A [page:Fog fog] instance defining the type of fog that affects everything
rendered in the scene. Default is `null`.

###  Boolean isScene;

Read-only flag to check if a given object is of type Scene.

###  Material overrideMaterial;

Forces everything in the scene to be rendered with the defined material.
Default is `null`.

## Methods

###  function toJSON( meta: Object ): Object;

meta -- object containing metadata such as textures or images for the scene.  
Convert the scene to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

