# Frustum

<a href="http://en.wikipedia.org/wiki/Frustum">Frustums</a> are used to
determine what is inside the camera's field of view. They help speed up the
rendering process - objects which lie outside a camera's frustum can safely be
excluded from rendering.  
  
This class is mainly intended for use internally by a renderer for calculating
a [camera](en\cameras\Camera.html) or [shadowCamera](#)'s frustum.

## Constructor

### Frustum

  
  
```ts  
function Frustum( p0: Plane, p1: Plane, p2: Plane, p3: Plane, p4: Plane, p5:
Plane ): void;  
```  

[p0](en\math\Plane.html) - (optional) defaults to a new
[Plane](en\math\Plane.html).  
[p1](en\math\Plane.html) - (optional) defaults to a new
[Plane](en\math\Plane.html).  
[p2](en\math\Plane.html) - (optional) defaults to a new
[Plane](en\math\Plane.html).  
[p3](en\math\Plane.html) - (optional) defaults to a new
[Plane](en\math\Plane.html).  
[p4](en\math\Plane.html) - (optional) defaults to a new
[Plane](en\math\Plane.html).  
[p5](en\math\Plane.html) - (optional) defaults to a new
[Plane](en\math\Plane.html).  
  
Creates a new Frustum.

## Properties

### planes

  
  
```ts  
planes: Array;  
```  

Array of 6 [planes](en\math\Plane.html).

## Methods

### clone

  
  
```ts  
function clone( ): Frustum;  
```  

Return a new Frustum with the same parameters as this one.

### containsPoint

  
  
```ts  
function containsPoint( point: Vector3 ): Boolean;  
```  

[point](en\math\Vector3.html) - [Vector3](en\math\Vector3.html) to test.  
  
Checks to see if the frustum contains the [point](en\math\Vector3.html).

### copy

  
  
```ts  
function copy( frustum: Frustum ): this;  
```  

[frustum](en\math\Frustum.html) - The frustum to copy  
  
Copies the properties of the passed [frustum](en\math\Frustum.html) into this
one.

### intersectsBox

  
  
```ts  
function intersectsBox( box: Box3 ): Boolean;  
```  

[box](en\math\Box3.html) - [Box3](en\math\Box3.html) to check for
intersection.  
  
Return true if [box](en\math\Box3.html) intersects with this frustum.

### intersectsObject

  
  
```ts  
function intersectsObject( object: Object3D ): Boolean;  
```  

Checks whether the [object](en\core\Object3D.html)'s [bounding sphere](#) is
intersecting the Frustum.  
  
Note that the object must have a [geometry](en\core\BufferGeometry.html) so
that the bounding sphere can be calculated.

### intersectsSphere

  
  
```ts  
function intersectsSphere( sphere: Sphere ): Boolean;  
```  

[sphere](en\math\Sphere.html) - [Sphere](en\math\Sphere.html) to check for
intersection.  
  
Return true if [sphere](en\math\Sphere.html) intersects with this frustum.

### intersectsSprite

  
  
```ts  
function intersectsSprite( sprite: Sprite ): Boolean;  
```  

Checks whether the [sprite](en\objects\Sprite.html) is intersecting the
Frustum.  
  

### set

  
  
```ts  
function set( p0: Plane, p1: Plane, p2: Plane, p3: Plane, p4: Plane, p5: Plane
): this;  
```  

Sets the frustum from the passed planes. No plane order is implied.  
Note that this method only copies the values from the given objects.

### setFromProjectionMatrix

  
  
```ts  
function setFromProjectionMatrix( matrix: Matrix4 ): this;  
```  

[.atrix4](#atrix4) - Projection [Matrix4](en\math\Matrix4.html) used to set
the [.planes](#planes)  
  
Sets the frustum planes from the projection matrix.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Frustum.js">src/math/Frustum.js</a>

