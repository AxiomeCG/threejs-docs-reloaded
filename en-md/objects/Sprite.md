[page:Object3D] →

# [name]

A sprite is a plane that always faces towards the camera, generally with a
partially transparent texture applied.  
  
Sprites do not cast shadows, setting  
```ts castShadow = true ```  
will have no effect.

## Code Example

  
```ts  
const map = new THREE.TextureLoader().load( 'sprite.png' );  
const material = new THREE.SpriteMaterial( { map: map } );  
  
const sprite = new THREE.Sprite( material );  
scene.add( sprite );  
```  

## Constructor

### [name]( [param:Material material] )

[page:Material material] - (optional) an instance of [page:SpriteMaterial].
Default is a white [page:SpriteMaterial].  
  
Creates a new [name].

## Properties

See the base [page:Object3D] class for common properties.

### <br/> Boolean isSprite; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> SpriteMaterial material; <br/>

An instance of [page:SpriteMaterial], defining the object's appearance.
Default is a white [page:SpriteMaterial].

### <br/> Vector2 center; <br/>

The sprite's anchor point, and the point around which the sprite rotates. A
value of (0.5, 0.5) corresponds to the midpoint of the sprite. A value of (0,
0) corresponds to the lower left corner of the sprite. The default is (0.5,
0.5).

## Methods

See the base [page:Object3D] class for common methods.

### [method:Sprite clone]()

Returns a clone of this Sprite object and any descendants.

### <br/> function copy( sprite: Sprite ): copy; <br/>

Copies the properties of the passed sprite to this one.

###  [method:undefined raycast]( [param:Raycaster raycaster], [param:Array
intersects] )

Get intersections between a casted ray and this sprite.
[page:Raycaster.intersectObject]() will call this method. The raycaster must
be initialized by calling [page:Raycaster.setFromCamera]() before raycasting
against sprites.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

