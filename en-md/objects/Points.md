[page:Object3D] →

# Points

A class for displaying points. The points are rendered by the
[page:WebGLRenderer] using [link:https://developer.mozilla.org/en-
US/docs/Web/API/WebGLRenderingContext/drawElements gl.POINTS].

## Constructor

###  function Points( geometry: BufferGeometry, material: Material ): void;

[page:BufferGeometry geometry] — (optional) an instance of
[page:BufferGeometry]. Default is a new [page:BufferGeometry].  
[page:Material material] — (optional) a [page:Material]. Default is a new
[page:PointsMaterial].

## Properties

See the base [page:Object3D] class for common properties.

###  BufferGeometry geometry;

An instance of [page:BufferGeometry] (or derived classes), defining the
object's structure.

###  Boolean isPoints;

Read-only flag to check if a given object is of type Points.

###  Material material;

An instance of [page:Material], defining the object's appearance. Default is a
[page:PointsMaterial].

###  Array morphTargetInfluences;

An array of weights typically from 0-1 that specify how much of the morph is
applied. Undefined by default, but reset to a blank array by
[page:Points.updateMorphTargets updateMorphTargets].

###  Object morphTargetDictionary;

A dictionary of morphTargets based on the morphTarget.name property. Undefined
by default, but rebuilt [page:Points.updateMorphTargets updateMorphTargets].

## Methods

See the base [page:Object3D] class for common methods.

###  function raycast( raycaster: Raycaster, intersects: Array ): undefined;

Get intersections between a casted ray and this Points.
[page:Raycaster.intersectObject] will call this method.

###  function clone( ): Points;

Returns a clone of this Points object and its descendants.

###  function updateMorphTargets( ): undefined;

Updates the morphTargets to have no influence on the object. Resets the
[page:Points.morphTargetInfluences morphTargetInfluences] and
[page:Points.morphTargetDictionary morphTargetDictionary] properties.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

