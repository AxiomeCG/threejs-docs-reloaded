[page:Object3D] →

# [name]

Scenes allow you to set up what and where is to be rendered by three.js. This
is where you place objects, lights and cameras.

## Constructor

### [name]()

Create a new scene object.

## Properties

### <br/> Object background; <br/>

Defines the background of the scene. Default is `null`. Valid inputs are:

  * A [page:Color] for defining a uniform colored background.
  * A [page:Texture] for defining a (flat) textured background.
  * Texture cubes ([page:CubeTexture]) or equirectangular textures for defining a skybox. 

Note: Any camera related configurations like `zoom` or `view` are ignored.

### <br/> Float backgroundBlurriness; <br/>

Sets the blurriness of the background. Only influences environment maps
assigned to [page:Scene.background]. Valid input is a float between `0` and
`1`. Default is `0`.

### <br/> Float backgroundIntensity; <br/>

Attenuates the color of the background. Only applies to background textures.
Default is `1`.

### <br/> Texture environment; <br/>

Sets the environment map for all physical materials in the scene. However,
it's not possible to overwrite an existing texture assigned to
[page:MeshStandardMaterial.envMap]. Default is `null`.

### <br/> Fog fog; <br/>

A [page:Fog fog] instance defining the type of fog that affects everything
rendered in the scene. Default is `null`.

### <br/> Boolean isScene; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Material overrideMaterial; <br/>

Forces everything in the scene to be rendered with the defined material.
Default is `null`.

## Methods

### [method:Object toJSON]( [param:Object meta] )

meta -- object containing metadata such as textures or images for the scene.  
Convert the scene to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

