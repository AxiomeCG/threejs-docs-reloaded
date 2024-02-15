# Color

Class representing a color.

Iterating through a Color instance will yield its components (r, g, b) in the
corresponding order.

## Code Examples

A Color can be initialised in any of the following ways:

  
```ts  
//empty constructor - will default whiteconst color1 = new
THREE.Color();//Hexadecimal color (recommended)const color2 = new THREE.Color(
0xff0000 );//RGB stringconst color3 = new THREE.Color("rgb(255, 0, 0)");const
color4 = new THREE.Color("rgb(100%, 0%, 0%)");//X11 color name - all 140 color
names are supported.//Note the lack of CamelCase in the nameconst color5 = new
THREE.Color( 'skyblue' );//HSL stringconst color6 = new THREE.Color("hsl(0,
100%, 50%)");//Separate RGB values between 0 and 1const color7 = new
THREE.Color( 1, 0, 0 );  
```  

## Constructor

### Color

  
  
```ts  
function Color( r: Color_Hex_or_String, g: Float, b: Float ): void;  
```  

[r](#) - (optional) If arguments [g](#) and [b](#) are defined, the red
component of the color. If they are not defined, it can be a <a
href="https://en.wikipedia.org/wiki/Web_colors#Hex_triplet">hexadecimal
triplet</a> (recommended), a CSS-style string, or another `Color` instance.  
[g](#) - (optional) If it is defined, the green component of the color.  
[b](#) - (optional) If it is defined, the blue component of the color.  
  
Note that standard method of specifying color in three.js is with a <a
href="https://en.wikipedia.org/wiki/Web_colors#Hex_triplet">hexadecimal
triplet</a>, and that method is used throughout the rest of the documentation.  
  
When all arguments are defined then [r](#) is the red component, [g](#) is the
green component and [b](#) is the blue component of the color.  
When only [r](#) is defined:  

  * It can be a <a href="https://en.wikipedia.org/wiki/Web_colors#Hex_triplet">hexadecimal triplet</a> representing the color (recommended).
  * It can be an another Color instance.
  * It can be a CSS-style string. For example:
    * 'rgb(250, 0,0)'
    * 'rgb(100%,0%,0%)'
    * 'hsl(0, 100%, 50%)'
    * '#ff0000'
    * '#f00'
    * 'red'

## Properties

### isColor

  
  
```ts  
isColor: Boolean;  
```  

Read-only flag to check if a given object is of type Color.

### r

  
  
```ts  
r: Float;  
```  

Red channel value between `0` and `1`. Default is `1`.

### g

  
  
```ts  
g: Float;  
```  

Green channel value between `0` and `1`. Default is `1`.

### b

  
  
```ts  
b: Float;  
```  

Blue channel value between `0` and `1`. Default is `1`.

## Methods

### add

  
  
```ts  
function add( color: Color ): this;  
```  

Adds the RGB values of [color](en\math\Color.html) to the RGB values of this
color.

### addColors

  
  
```ts  
function addColors( color1: Color, color2: Color ): this;  
```  

Sets this color's RGB values to the sum of the RGB values of
[color1](en\math\Color.html) and [color2](en\math\Color.html).

### addScalar

  
  
```ts  
function addScalar( s: Number ): this;  
```  

Adds [s](#) to the RGB values of this color.

### applyMatrix3

  
  
```ts  
function applyMatrix3( m: Matrix3 ): this;  
```  

Applies the transform [m](en\math\Matrix3.html) to this color's RGB
components.

### clone

  
  
```ts  
function clone( ): Color;  
```  

Returns a new Color with the same [.r](#r), [.g](#g) and [.b](#b) values as
this one.

### copy

  
  
```ts  
function copy( color: Color ): this;  
```  

Copies the [.r](#r), [.g](#g) and [.b](#b) parameters from [.olor](#olor) in
to this color.

### convertLinearToSRGB

  
  
```ts  
function convertLinearToSRGB( ): this;  
```  

Converts this color from linear space to sRGB space.

### convertSRGBToLinear

  
  
```ts  
function convertSRGBToLinear( ): this;  
```  

Converts this color from sRGB space to linear space.

### copyLinearToSRGB

  
  
```ts  
function copyLinearToSRGB( color: Color ): this;  
```  

[color](en\math\Color.html) — Color to copy.  
Copies the given color into this color, and then converts this color from
linear space to sRGB space.

### copySRGBToLinear

  
  
```ts  
function copySRGBToLinear( color: Color ): this;  
```  

[color](en\math\Color.html) — Color to copy.  
Copies the given color into this color, and then converts this color from sRGB
space to linear space.

### equals

  
  
```ts  
function equals( color: Color ): Boolean;  
```  

Compares the RGB values of [color](en\math\Color.html) with those of this
object. Returns true if they are the same, false otherwise.

### fromArray

  
  
```ts  
function fromArray( array: Array, offset: Integer ): this;  
```  

[array](#) - [Array](#) of floats in the form [ [r](#), [g](#), [b](#) ].  
[offset](#) - An optional offset into the array.  
  
Sets this color's components based on an array formatted like [ [r](#),
[g](#), [b](#) ].

### fromBufferAttribute

  
  
```ts  
function fromBufferAttribute( attribute: BufferAttribute, index: Integer ):
this;  
```  

[attribute](en\core\BufferAttribute.html) - the source attribute.  
[index](#) - index in the attribute.  
  
Sets this color's components from the
[attribute](en\core\BufferAttribute.html).

### getHex

  
  
```ts  
function getHex( colorSpace: string ): Integer;  
```  

Returns the hexadecimal value of this color.

### getHexString

  
  
```ts  
function getHexString( colorSpace: string ): String;  
```  

Returns the hexadecimal value of this color as a string (for example,
'FFFFFF').

### getHSL

  
  
```ts  
function getHSL( target: Object, colorSpace: string ): Object;  
```  

[target](#) — the result will be copied into this Object. Adds h, s and l keys
to the object (if not already present).  
  
Convert this Color's [.r](#r), [.g](#g) and [.b](#b) values to <a
href="https://en.wikipedia.org/wiki/HSL_and_HSV">HSL</a> format and returns an
object of the form:  
```ts  
{ h: 0, s: 0, l: 0 }  
```  

### getRGB

  
  
```ts  
function getRGB( target: Color, colorSpace: string ): Color;  
```  

[target](en\math\Color.html) — the result will be copied into this object.  
  
Returns the RGB values of this color as an instance of
[Color](en\math\Color.html).

### getStyle

  
  
```ts  
function getStyle( colorSpace: string ): String;  
```  

Returns the value of this color as a CSS style string. Example:
`rgb(255,0,0)`.

### lerp

  
  
```ts  
function lerp( color: Color, alpha: Float ): this;  
```  

[color](en\math\Color.html) - color to converge on.  
[alpha](#) - interpolation factor in the closed interval `[0, 1]`.  
  
Linearly interpolates this color's RGB values toward the RGB values of the
passed argument. The alpha argument can be thought of as the ratio between the
two colors, where `0.0` is this color and `1.0` is the first argument.

### lerpColors

  
  
```ts  
function lerpColors( color1: Color, color2: Color, alpha: Float ): this;  
```  

[color1](en\math\Color.html) - the starting [Color](en\math\Color.html).  
[color2](en\math\Color.html) - [Color](en\math\Color.html) to interpolate
towards.  
[alpha](#) - interpolation factor, typically in the closed interval `[0, 1]`.  
  
Sets this color to be the color linearly interpolated between
[color1](en\math\Color.html) and [color2](en\math\Color.html) where alpha is
the percent distance along the line connecting the two colors - alpha = 0 will
be [color1](en\math\Color.html), and alpha = 1 will be
[color2](en\math\Color.html).

### lerpHSL

  
  
```ts  
function lerpHSL( color: Color, alpha: Float ): this;  
```  

[color](en\math\Color.html) - color to converge on.  
[alpha](#) - interpolation factor in the closed interval `[0, 1]`.  
  
Linearly interpolates this color's HSL values toward the HSL values of the
passed argument. It differs from the classic [.lerp](#) by not interpolating
straight from one color to the other, but instead going through all the hues
in between those two colors. The alpha argument can be thought of as the ratio
between the two colors, where 0.0 is this color and 1.0 is the first argument.

### multiply

  
  
```ts  
function multiply( color: Color ): this;  
```  

Multiplies this color's RGB values by the given [color](en\math\Color.html)'s
RGB values.

### multiplyScalar

  
  
```ts  
function multiplyScalar( s: Number ): this;  
```  

Multiplies this color's RGB values by [s](#).

### offsetHSL

  
  
```ts  
function offsetHSL( h: Float, s: Float, l: Float ): this;  
```  

Adds the given [.loat](#loat), [.loat](#loat), and [.loat](#loat) to this
color's values. Internally, this converts the color's [.r](#r), [.g](#g) and
[.b](#b) values to HSL, adds [.loat](#loat), [.loat](#loat), and
[.loat](#loat), and then converts the color back to RGB.

### set

  
  
```ts  
function set( r: Color_Hex_or_String, g: Float, b: Float ): this;  
```  

[r](#) - (optional) If arguments [g](#) and [b](#) are defined, the red
component of the color. If they are not defined, it can be a <a
href="https://en.wikipedia.org/wiki/Web_colors#Hex_triplet">hexadecimal
triplet</a> (recommended), a CSS-style string, or another `Color` instance.  
[g](#) - (optional) If it is defined, the green component of the color.  
[b](#) - (optional) If it is defined, the blue component of the color.  
  
See the Constructor above for full details about possible arguments. Delegates
to [.copy](#), [.setStyle](#), [.setRGB](#) or [.setHex](#) depending on input
type.

### setFromVector3

  
  
```ts  
function setFromVector3( vector: Vector3 ): this;  
```  

Sets this colors's [.r](#r), [.g](#g) and [.b](#b) components from the x, y,
and z components of the specified [.ector3](#ector3).

### setHex

  
  
```ts  
function setHex( hex: Integer, colorSpace: string ): this;  
```  

[hex](#) — <a
href="https://en.wikipedia.org/wiki/Web_colors#Hex_triplet">hexadecimal
triplet</a> format.  
  
Sets this color from a hexadecimal value.

### setHSL

  
  
```ts  
function setHSL( h: Float, s: Float, l: Float, colorSpace: string ): this;  
```  

[h](#) — hue value between `0.0` and `1.0`  
[s](#) — saturation value between `0.0` and `1.0`  
[l](#) — lightness value between `0.0` and `1.0`  
  
Sets color from HSL values.

### setRGB

  
  
```ts  
function setRGB( r: Float, g: Float, b: Float, colorSpace: string ): this;  
```  

[r](#) — Red channel value between `0.0` and `1.0`.  
[g](#) — Green channel value between `0.0` and `1.0`.  
[b](#) — Blue channel value between `0.0` and `1.0`.  
  
Sets this color from RGB values.

### setScalar

  
  
```ts  
function setScalar( scalar: Float ): this;  
```  

[scalar](#) — a value between `0.0` and `1.0`.  
  
Sets all three color components to the value [scalar](#).

### setStyle

  
  
```ts  
function setStyle( style: String, colorSpace: string ): this;  
```  

[style](#) — color as a CSS-style string.  
  
Sets this color from a CSS-style string. For example, "rgb(250, 0,0)",
"rgb(100%, 0%, 0%)", "hsl(0, 100%, 50%)", "#ff0000", "#f00", or "red" ( or any
<a href="https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart">X11
color name</a> \- all 140 color names are supported ).  
Translucent colors such as "rgba(255, 0, 0, 0.5)" and "hsla(0, 100%, 50%,
0.5)" are also accepted, but the alpha-channel coordinate will be discarded.  
  
Note that for X11 color names, multiple words such as Dark Orange become the
string 'darkorange'.

### setColorName

  
  
```ts  
function setColorName( style: String, colorSpace: string ): this;  
```  

[style](#) — color name ( from <a
href="https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart">X11
color names</a> ).  
  
Sets this color from a color name. Faster than [.setStyle](#) method if you
don't need the other CSS-style formats.  
  
For convenience, the list of names is exposed in Color.NAMES as a hash:  
```ts  
Color.NAMES.aliceblue // returns 0xF0F8FF  
```  

### sub

  
  
```ts  
function sub( color: Color ): this;  
```  

Subtracts the RGB components of the given color from the RGB components of
this color. If this results in a negative component, that component is set to
zero.

### toArray

  
  
```ts  
function toArray( array: Array, offset: Integer ): Array;  
```  

[array](#) - An optional array to store the color to.  
[offset](#) - An optional offset into the array.  
  
Returns an array of the form [ r, g, b ].

### toJSON

  
  
```ts  
function toJSON( ): Number;  
```  

This methods defines the serialization result of Color. Returns the color as a
hexadecimal value.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/math/Color.js">src/math/Color.js</a>

