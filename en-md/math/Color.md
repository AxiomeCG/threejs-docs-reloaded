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

###  function Color( r: Color_Hex_or_String, g: Float, b: Float ): void;

[page:Color_Hex_or_String r] - (optional) If arguments [page:Float g] and
[page:Float b] are defined, the red component of the color. If they are not
defined, it can be a
[link:https://en.wikipedia.org/wiki/Web_colors#Hex_triplet hexadecimal
triplet] (recommended), a CSS-style string, or another `Color` instance.  
[page:Float g] - (optional) If it is defined, the green component of the
color.  
[page:Float b] - (optional) If it is defined, the blue component of the color.  
  
Note that standard method of specifying color in three.js is with a
[link:https://en.wikipedia.org/wiki/Web_colors#Hex_triplet hexadecimal
triplet], and that method is used throughout the rest of the documentation.  
  
When all arguments are defined then [page:Color_Hex_or_String r] is the red
component, [page:Float g] is the green component and [page:Float b] is the
blue component of the color.  
When only [page:Color_Hex_or_String r] is defined:  

  * It can be a [link:https://en.wikipedia.org/wiki/Web_colors#Hex_triplet hexadecimal triplet] representing the color (recommended).
  * It can be an another Color instance.
  * It can be a CSS-style string. For example:
    * 'rgb(250, 0,0)'
    * 'rgb(100%,0%,0%)'
    * 'hsl(0, 100%, 50%)'
    * '#ff0000'
    * '#f00'
    * 'red'

## Properties

###  Boolean isColor;

Read-only flag to check if a given object is of type Color.

###  Float r;

Red channel value between `0` and `1`. Default is `1`.

###  Float g;

Green channel value between `0` and `1`. Default is `1`.

###  Float b;

Blue channel value between `0` and `1`. Default is `1`.

## Methods

###  function add( color: Color ): this;

Adds the RGB values of [page:Color color] to the RGB values of this color.

###  function addColors( color1: Color, color2: Color ): this;

Sets this color's RGB values to the sum of the RGB values of [page:Color
color1] and [page:Color color2].

###  function addScalar( s: Number ): this;

Adds [page:Number s] to the RGB values of this color.

###  function applyMatrix3( m: Matrix3 ): this;

Applies the transform [page:Matrix3 m] to this color's RGB components.

###  function clone( ): Color;

Returns a new Color with the same [page:.r r], [page:.g g] and [page:.b b]
values as this one.

###  function copy( color: Color ): this;

Copies the [page:.r r], [page:.g g] and [page:.b b] parameters from
[page:Color color] in to this color.

###  function convertLinearToSRGB( ): this;

Converts this color from linear space to sRGB space.

###  function convertSRGBToLinear( ): this;

Converts this color from sRGB space to linear space.

###  function copyLinearToSRGB( color: Color ): this;

[page:Color color] — Color to copy.  
Copies the given color into this color, and then converts this color from
linear space to sRGB space.

###  function copySRGBToLinear( color: Color ): this;

[page:Color color] — Color to copy.  
Copies the given color into this color, and then converts this color from sRGB
space to linear space.

###  function equals( color: Color ): Boolean;

Compares the RGB values of [page:Color color] with those of this object.
Returns true if they are the same, false otherwise.

###  function fromArray( array: Array, offset: Integer ): this;

[page:Array array] - [page:Array] of floats in the form [ [page:Float r],
[page:Float g], [page:Float b] ].  
[page:Integer offset] - An optional offset into the array.  
  
Sets this color's components based on an array formatted like [ [page:Float
r], [page:Float g], [page:Float b] ].

###  function fromBufferAttribute( attribute: BufferAttribute, index: Integer
): this;

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets this color's components from the [page:BufferAttribute attribute].

###  function getHex( colorSpace: string ): Integer;

Returns the hexadecimal value of this color.

###  function getHexString( colorSpace: string ): String;

Returns the hexadecimal value of this color as a string (for example,
'FFFFFF').

###  function getHSL( target: Object, colorSpace: string ): Object;

[page:Object target] — the result will be copied into this Object. Adds h, s
and l keys to the object (if not already present).  
  
Convert this Color's [page:.r r], [page:.g g] and [page:.b b] values to
[link:https://en.wikipedia.org/wiki/HSL_and_HSV HSL] format and returns an
object of the form:  
```ts  
{ h: 0, s: 0, l: 0 }  
```  

###  function getRGB( target: Color, colorSpace: string ): Color;

[page:Color target] — the result will be copied into this object.  
  
Returns the RGB values of this color as an instance of [page:Color].

###  function getStyle( colorSpace: string ): String;

Returns the value of this color as a CSS style string. Example:
`rgb(255,0,0)`.

###  function lerp( color: Color, alpha: Float ): this;

[page:Color color] - color to converge on.  
[page:Float alpha] - interpolation factor in the closed interval `[0, 1]`.  
  
Linearly interpolates this color's RGB values toward the RGB values of the
passed argument. The alpha argument can be thought of as the ratio between the
two colors, where `0.0` is this color and `1.0` is the first argument.

###  function lerpColors( color1: Color, color2: Color, alpha: Float ): this;

[page:Color color1] - the starting [page:Color].  
[page:Color color2] - [page:Color] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Sets this color to be the color linearly interpolated between [page:Color
color1] and [page:Color color2] where alpha is the percent distance along the
line connecting the two colors - alpha = 0 will be [page:Color color1], and
alpha = 1 will be [page:Color color2].

###  function lerpHSL( color: Color, alpha: Float ): this;

[page:Color color] - color to converge on.  
[page:Float alpha] - interpolation factor in the closed interval `[0, 1]`.  
  
Linearly interpolates this color's HSL values toward the HSL values of the
passed argument. It differs from the classic [page:.lerp] by not interpolating
straight from one color to the other, but instead going through all the hues
in between those two colors. The alpha argument can be thought of as the ratio
between the two colors, where 0.0 is this color and 1.0 is the first argument.

###  function multiply( color: Color ): this;

Multiplies this color's RGB values by the given [page:Color color]'s RGB
values.

###  function multiplyScalar( s: Number ): this;

Multiplies this color's RGB values by [page:Number s].

###  function offsetHSL( h: Float, s: Float, l: Float ): this;

Adds the given [page:Float h], [page:Float s], and [page:Float l] to this
color's values. Internally, this converts the color's [page:.r r], [page:.g g]
and [page:.b b] values to HSL, adds [page:Float h], [page:Float s], and
[page:Float l], and then converts the color back to RGB.

###  function set( r: Color_Hex_or_String, g: Float, b: Float ): this;

[page:Color_Hex_or_String r] - (optional) If arguments [page:Float g] and
[page:Float b] are defined, the red component of the color. If they are not
defined, it can be a
[link:https://en.wikipedia.org/wiki/Web_colors#Hex_triplet hexadecimal
triplet] (recommended), a CSS-style string, or another `Color` instance.  
[page:Float g] - (optional) If it is defined, the green component of the
color.  
[page:Float b] - (optional) If it is defined, the blue component of the color.  
  
See the Constructor above for full details about possible arguments. Delegates
to [page:.copy], [page:.setStyle], [page:.setRGB] or [page:.setHex] depending
on input type.

###  function setFromVector3( vector: Vector3 ): this;

Sets this colors's [page:.r r], [page:.g g] and [page:.b b] components from
the x, y, and z components of the specified [page:Vector3 vector].

###  function setHex( hex: Integer, colorSpace: string ): this;

[page:Integer hex] —
[link:https://en.wikipedia.org/wiki/Web_colors#Hex_triplet hexadecimal
triplet] format.  
  
Sets this color from a hexadecimal value.

###  function setHSL( h: Float, s: Float, l: Float, colorSpace: string ):
this;

[page:Float h] — hue value between `0.0` and `1.0`  
[page:Float s] — saturation value between `0.0` and `1.0`  
[page:Float l] — lightness value between `0.0` and `1.0`  
  
Sets color from HSL values.

###  function setRGB( r: Float, g: Float, b: Float, colorSpace: string ):
this;

[page:Float r] — Red channel value between `0.0` and `1.0`.  
[page:Float g] — Green channel value between `0.0` and `1.0`.  
[page:Float b] — Blue channel value between `0.0` and `1.0`.  
  
Sets this color from RGB values.

###  function setScalar( scalar: Float ): this;

[page:Float scalar] — a value between `0.0` and `1.0`.  
  
Sets all three color components to the value [page:Float scalar].

###  function setStyle( style: String, colorSpace: string ): this;

[page:String style] — color as a CSS-style string.  
  
Sets this color from a CSS-style string. For example, "rgb(250, 0,0)",
"rgb(100%, 0%, 0%)", "hsl(0, 100%, 50%)", "#ff0000", "#f00", or "red" ( or any
[link:https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart X11 color
name] - all 140 color names are supported ).  
Translucent colors such as "rgba(255, 0, 0, 0.5)" and "hsla(0, 100%, 50%,
0.5)" are also accepted, but the alpha-channel coordinate will be discarded.  
  
Note that for X11 color names, multiple words such as Dark Orange become the
string 'darkorange'.

###  function setColorName( style: String, colorSpace: string ): this;

[page:String style] — color name ( from
[link:https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart X11 color
names] ).  
  
Sets this color from a color name. Faster than [page:.setStyle] method if you
don't need the other CSS-style formats.  
  
For convenience, the list of names is exposed in Color.NAMES as a hash:  
```ts  
Color.NAMES.aliceblue // returns 0xF0F8FF  
```  

###  function sub( color: Color ): this;

Subtracts the RGB components of the given color from the RGB components of
this color. If this results in a negative component, that component is set to
zero.

###  function toArray( array: Array, offset: Integer ): Array;

[page:Array array] - An optional array to store the color to.  
[page:Integer offset] - An optional offset into the array.  
  
Returns an array of the form [ r, g, b ].

###  function toJSON( ): Number;

This methods defines the serialization result of Color. Returns the color as a
hexadecimal value.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

