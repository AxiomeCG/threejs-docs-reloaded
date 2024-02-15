[Object3D](en\core\Object3D.html) →

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

### Sprite

  
  
```ts  
function Sprite( material: Material ): void;  
```  

[material](en\materials\Material.html) - (optional) an instance of
[SpriteMaterial](en\materials\SpriteMaterial.html). Default is a white
[SpriteMaterial](en\materials\SpriteMaterial.html).  
  
Creates a new Sprite.

## Properties

See the base [Object3D](en\core\Object3D.html) class for common properties.

### isSprite

  
  
```ts  
isSprite: Boolean;  
```  

Read-only flag to check if a given object is of type Sprite.

### material

  
  
```ts  
material: SpriteMaterial;  
```  

An instance of [SpriteMaterial](en\materials\SpriteMaterial.html), defining
the object's appearance. Default is a white
[SpriteMaterial](en\materials\SpriteMaterial.html).

### center

  
  
```ts  
center: Vector2;  
```  

The sprite's anchor point, and the point around which the sprite rotates. A
value of (0.5, 0.5) corresponds to the midpoint of the sprite. A value of (0,
0) corresponds to the lower left corner of the sprite. The default is (0.5,
0.5).

## Methods

See the base [Object3D](en\core\Object3D.html) class for common methods.

### clone

  
  
```ts  
function clone( ): Sprite;  
```  

Returns a clone of this Sprite object and any descendants.

### copy

  
  
```ts  
function copy( sprite: Sprite ): this;  
```  

Copies the properties of the passed sprite to this one.

### raycast

  
  
```ts  
function raycast( raycaster: Raycaster, intersects: Array ): undefined;  
```  

Get intersections between a casted ray and this sprite.
[Raycaster.intersectObject](#)() will call this method. The raycaster must be
initialized by calling [Raycaster.setFromCamera](#)() before raycasting
against sprites.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/objects/Sprite.js">src/objects/Sprite.js</a>

