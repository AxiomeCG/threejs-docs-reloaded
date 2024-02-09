[page:Loader] →

# [name]

[name] can be used to load cube maps. The loader returns an instance of
[page:CubeTexture] and expects the cube map to be defined as six separate
images representing the sides of a cube. Other cube map definitions like
vertical and horizontal cross, column and row layouts are not supported.

The loaded [page:CubeTexture] is in sRGB color space. Meaning the
[page:Texture.colorSpace colorSpace] property is set to `THREE.SRGBColorSpace`
by default.

## Code Example

  
```ts  
const scene = new THREE.Scene();  
scene.background = new THREE.CubeTextureLoader()  
.setPath( 'textures/cubeMaps/' )  
.load( [  
'px.png',  
'nx.png',  
'py.png',  
'ny.png',  
'pz.png',  
'nz.png'  
] );  
```  

## Examples

[example:webgl_materials_cubemap materials / cubemap]  
[example:webgl_materials_cubemap_dynamic materials / cubemap / dynamic]  
[example:webgl_materials_cubemap_refraction materials / cubemap / refraction]

## Constructor

### [name]( [param:LoadingManager manager] )

[page:LoadingManager manager] — The [page:LoadingManager loadingManager] for
the loader to use. Default is [page:LoadingManager
THREE.DefaultLoadingManager].  
  
Creates a new [name].

## Properties

See the base [page:Loader] class for common properties.

## Methods

See the base [page:Loader] class for common methods.

###  [method:CubeTexture load]( [param:String urls], [param:Function onLoad],
[param:Function onProgress], [param:Function onError] )

[page:String urls] — array of 6 urls to images, one for each side of the
CubeTexture. The urls should be specified in the following order: pos-x,
neg-x, pos-y, neg-y, pos-z, neg-z. They can also be
[link:https://developer.mozilla.org/en-
US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs Data URIs].  
Note that, by convention, cube maps are specified in a coordinate system in
which positive-x is to the right when looking up the positive-z axis -- in
other words, using a left-handed coordinate system. Since three.js uses a
right-handed coordinate system, environment maps used in three.js will have
pos-x and neg-x swapped.  
[page:Function onLoad] (optional) — Will be called when load completes. The
argument will be the loaded [page:CubeTexture texture].  
[page:Function onProgress] (optional) — This callback function is currently
not supported.  
[page:Function onError] (optional) — Will be called when load errors.  

Begin loading from url and pass the loaded [page:CubeTexture texture] to
onLoad. The method also returns a new texture object which can directly be
used for material creation.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

