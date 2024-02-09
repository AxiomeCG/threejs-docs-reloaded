[page:Object3D] → [page:Camera] →

# [name]

Camera that uses [link:https://en.wikipedia.org/wiki/Orthographic_projection
orthographic projection].  
  
In this projection mode, an object's size in the rendered image stays constant
regardless of its distance from the camera.  
  
This can be useful for rendering 2D scenes and UI elements, amongst other
things.

## Code Example

  
```ts  
const camera = new THREE.OrthographicCamera( width / - 2, width / 2, height /
2, height / - 2, 1, 1000 );  
scene.add( camera );  
```  

## Examples

[example:webgl_camera camera ]  
[example:webgl_interactive_cubes_ortho interactive / cubes / ortho ]  
[example:webgl_materials_cubemap_dynamic materials / cubemap / dynamic]  
[example:webgl_postprocessing_advanced postprocessing / advanced ]  
[example:webgl_postprocessing_dof2 postprocessing / dof2 ]  
[example:webgl_postprocessing_godrays postprocessing / godrays ]  
[example:webgl_rtt rtt ]  
[example:webgl_shadowmap shadowmap ]

## Constructor

### [name]( [param:Number left], [param:Number right], [param:Number top],
[param:Number bottom], [param:Number near], [param:Number far] )

left — Camera frustum left plane.  
right — Camera frustum right plane.  
top — Camera frustum top plane.  
bottom — Camera frustum bottom plane.  
near — Camera frustum near plane.  
far — Camera frustum far plane.  
  
Together these define the camera's
[link:https://en.wikipedia.org/wiki/Viewing_frustum viewing frustum].

## Properties

See the base [page:Camera] class for common properties.  
Note that after making changes to most of these properties you will have to
call [page:OrthographicCamera.updateProjectionMatrix .updateProjectionMatrix]
for the changes to take effect.

### <br/> Float bottom; <br/>

Camera frustum bottom plane.

### <br/> Float far; <br/>

Camera frustum far plane. Default is `2000`.  
  
Must be greater than the current value of [page:.near near] plane.

### <br/> Boolean isOrthographicCamera; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Float left; <br/>

Camera frustum left plane.

### <br/> Float near; <br/>

Camera frustum near plane. Default is `0.1`.  
  
The valid range is between `0` and the current value of the [page:.far far]
plane. Note that, unlike for the [page:PerspectiveCamera], `0` is a valid
value for an OrthographicCamera's near plane.

### <br/> Float right; <br/>

Camera frustum right plane.

### <br/> Float top; <br/>

Camera frustum top plane.

### <br/> Object view; <br/>

Set by [page:OrthographicCamera.setViewOffset setViewOffset]. Default is
`null`.

### <br/> number zoom; <br/>

Gets or sets the zoom factor of the camera. Default is `1`.

## Methods

See the base [page:Camera] class for common methods.

### [method:undefined setViewOffset]( [param:Float fullWidth], [param:Float
fullHeight], [param:Float x], [param:Float y], [param:Float width],
[param:Float height] )

fullWidth — full width of multiview setup  
fullHeight — full height of multiview setup  
x — horizontal offset of subcamera  
y — vertical offset of subcamera  
width — width of subcamera  
height — height of subcamera  
  
Sets an offset in a larger [link:https://en.wikipedia.org/wiki/Viewing_frustum
viewing frustum]. This is useful for multi-window or multi-monitor/multi-
machine setups. For an example on how to use it see
[page:PerspectiveCamera.setViewOffset PerspectiveCamera].

### [method:undefined clearViewOffset]()

Removes any offset set by the .setViewOffset method.

### [method:undefined updateProjectionMatrix]()

Updates the camera projection matrix. Must be called after any change of
parameters.

### [method:Object toJSON]([param:Object meta])

meta -- object containing metadata such as textures or images in objects'
descendants.  
Convert the camera to three.js
[link:https://github.com/mrdoob/three.js/wiki/JSON-Object-Scene-format-4 JSON
Object/Scene format].

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

