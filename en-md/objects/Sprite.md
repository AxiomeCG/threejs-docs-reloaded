[page:Object3D] →

# Sprite

A sprite is a plane that always faces towards the camera, generally with a
partially transparent texture applied.  
  
Sprites do not cast shadows, setting  
```ts  
castShadow = true  
```  
will have no effect.

## Code Example

  
```ts  
const map = new THREE.TextureLoader().load( 'sprite.png' ); const material =
new THREE.SpriteMaterial( { map: map } ); const sprite = new THREE.Sprite(
material ); scene.add( sprite );  
```  

## Constructor

###  function Sprite( material: Material ): void;

[page:Material material] - (optional) an instance of [page:SpriteMaterial].
Default is a white [page:SpriteMaterial].  
  
Creates a new Sprite.

## Properties

See the base [page:Object3D] class for common properties.

###  Boolean isSprite;

Read-only flag to check if a given object is of type Sprite.

###  SpriteMaterial material;

An instance of [page:SpriteMaterial], defining the object's appearance.
Default is a white [page:SpriteMaterial].

###  Vector2 center;

The sprite's anchor point, and the point around which the sprite rotates. A
value of (0.5, 0.5) corresponds to the midpoint of the sprite. A value of (0,
0) corresponds to the lower left corner of the sprite. The default is (0.5,
0.5).

## Methods

See the base [page:Object3D] class for common methods.

###  function clone( ): Sprite;

Returns a clone of this Sprite object and any descendants.

###  function copy( sprite: Sprite ): this;

Copies the properties of the passed sprite to this one.

###  function raycast( raycaster: Raycaster, intersects: Array ): undefined;

Get intersections between a casted ray and this sprite.
[page:Raycaster.intersectObject]() will call this method. The raycaster must
be initialized by calling [page:Raycaster.setFromCamera]() before raycasting
against sprites.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

