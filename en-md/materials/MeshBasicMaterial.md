[page:Material] →

# [name]

A material for drawing geometries in a simple shaded (flat or wireframe) way.  
  
This material is not affected by lights.

## Constructor

### [name]( [param:Object parameters] )

[page:Object parameters] - (optional) an object with one or more properties
defining the material's appearance. Any property of the material (including
any property inherited from [page:Material]) can be passed in here.  
  
The exception is the property [page:Hexadecimal color], which can be passed in
as a hexadecimal string and is `0xffffff` (white) by default.
[page:Color.set]( color ) is called internally.

## Properties

See the base [page:Material] class for common properties.

### <br/> Texture alphaMap; <br/>

The alpha map is a grayscale texture that controls the opacity across the
surface (black: fully transparent; white: fully opaque). Default is null.  
  
Only the color of the texture is used, ignoring the alpha channel if one
exists. For RGB and RGBA textures, the [page:WebGLRenderer WebGL] renderer
will use the green channel when sampling this texture due to the extra bit of
precision provided for green in DXT-compressed and uncompressed RGB 565
formats. Luminance-only and luminance/alpha textures will also still work as
expected.

### <br/> Texture aoMap; <br/>

The red channel of this texture is used as the ambient occlusion map. Default
is null. The aoMap requires a second set of UVs.

### <br/> Float aoMapIntensity; <br/>

Intensity of the ambient occlusion effect. Default is `1`. Zero is no
occlusion effect.

### <br/> Color color; <br/>

[page:Color] of the material, by default set to white (0xffffff).

### <br/> Integer combine; <br/>

How to combine the result of the surface's color with the environment map, if
any.  
  
Options are [page:Materials THREE.MultiplyOperation] (default),
[page:Materials THREE.MixOperation], [page:Materials THREE.AddOperation]. If
mix is chosen, the [page:.reflectivity] is used to blend between the two
colors.

### <br/> Texture envMap; <br/>

The environment map. Default is null.

### <br/> Boolean fog; <br/>

Whether the material is affected by fog. Default is `true`.

### <br/> Texture lightMap; <br/>

The light map. Default is null. The lightMap requires a second set of UVs.

### <br/> Float lightMapIntensity; <br/>

Intensity of the baked light. Default is `1`.

### <br/> Texture map; <br/>

The color map. May optionally include an alpha channel, typically combined
with [page:Material.transparent .transparent] or [page:Material.alphaTest
.alphaTest]. Default is null.

### <br/> Float reflectivity; <br/>

How much the environment map affects the surface; also see [page:.combine].
The default value is `1` and the valid range is between `0` (no reflections)
and `1` (full reflections).

### <br/> Float refractionRatio; <br/>

The index of refraction (IOR) of air (approximately 1) divided by the index of
refraction of the material. It is used with environment mapping modes
[page:Textures THREE.CubeRefractionMapping] and [page:Textures
THREE.EquirectangularRefractionMapping]. The refraction ratio should not
exceed `1`. Default is `0.98`.

### <br/> Texture specularMap; <br/>

Specular map used by the material. Default is null.

### <br/> Boolean wireframe; <br/>

Render geometry as wireframe. Default is `false` (i.e. render as flat
polygons).

### <br/> String wireframeLinecap; <br/>

Define appearance of line ends. Possible values are "butt", "round" and
"square". Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineCap
2D Canvas lineCap] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

### <br/> String wireframeLinejoin; <br/>

Define appearance of line joints. Possible values are "round", "bevel" and
"miter". Default is 'round'.  
  
This corresponds to the
[link:https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D/lineJoin
2D Canvas lineJoin] property and it is ignored by the [page:WebGLRenderer
WebGL] renderer.

### <br/> Float wireframeLinewidth; <br/>

Controls wireframe thickness. Default is `1`.  
  
Due to limitations of the
[link:https://www.khronos.org/registry/OpenGL/specs/gl/glspec46.core.pdf
OpenGL Core Profile] with the [page:WebGLRenderer WebGL] renderer on most
platforms linewidth will always be `1` regardless of the set value.

## Methods

See the base [page:Material] class for common methods.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

