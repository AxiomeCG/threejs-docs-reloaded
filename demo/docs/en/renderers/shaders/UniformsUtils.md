# UniformsUtils

Provides utility functions for managing uniforms.

## Methods

### clone

  
  
```ts  
function clone( src: Object ): Object;  
```  

src -- An object representing uniform definitions.  
  
Clones the given uniform definitions by performing a deep-copy. That means if
the [value](#) of a uniform refers to an object like a
[Vector3](en\math\Vector3.html) or [Texture](en\textures\Texture.html), the
cloned uniform will refer to a new object reference.

### merge

  
  
```ts  
function merge( uniforms: Array ): Object;  
```  

uniforms -- An array of objects containing uniform definitions.  
  
Merges the given uniform definitions into a single object. Since the method
internally uses [.clone](#)(), it performs a deep-copy when producing the
merged uniform definitions.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/renderers/shaders/UniformsUtils.js">src/renderers/shaders/UniformsUtils.js</a>

