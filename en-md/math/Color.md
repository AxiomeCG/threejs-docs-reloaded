# [name]

Class representing a color.

Iterating through a [name] instance will yield its components (r, g, b) in the
corresponding order.

## Code Examples

A Color can be initialised in any of the following ways:

  
```ts  
//empty constructor - will default white  
const color1 = new THREE.Color();  
  
//Hexadecimal color (recommended)  
const color2 = new THREE.Color( 0xff0000 );  
  
//RGB string  
const color3 = new THREE.Color("rgb(255, 0, 0)");  
const color4 = new THREE.Color("rgb(100%, 0%, 0%)");  
  
//X11 color name - all 140 color names are supported.  
//Note the lack of CamelCase in the name  
const color5 = new THREE.Color( 'skyblue' );  
  
//HSL string  
const color6 = new THREE.Color("hsl(0, 100%, 50%)");  
  
//Separate RGB values between 0 and 1  
const color7 = new THREE.Color( 1, 0, 0 );  
```  

## Constructor

###  [name]( [param:Color_Hex_or_String r], [param:Float g], [param:Float b] )

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

### <br/> Boolean isColor; <br/>

Read-only flag to check if a given object is of type [name].

### <br/> Float r; <br/>

Red channel value between `0` and `1`. Default is `1`.

### <br/> Float g; <br/>

Green channel value between `0` and `1`. Default is `1`.

### <br/> Float b; <br/>

Blue channel value between `0` and `1`. Default is `1`.

## Methods

### <br/> function add( color: Color ): add; <br/>

Adds the RGB values of [page:Color color] to the RGB values of this color.

### <br/> function addColors( color1: Color, color2: Color ): addColors; <br/>

Sets this color's RGB values to the sum of the RGB values of [page:Color
color1] and [page:Color color2].

### <br/> function addScalar( s: Number ): addScalar; <br/>

Adds [page:Number s] to the RGB values of this color.

### <br/> function applyMatrix3( m: Matrix3 ): applyMatrix3; <br/>

Applies the transform [page:Matrix3 m] to this color's RGB components.

### [method:Color clone]()

Returns a new Color with the same [page:.r r], [page:.g g] and [page:.b b]
values as this one.

### <br/> function copy( color: Color ): copy; <br/>

Copies the [page:.r r], [page:.g g] and [page:.b b] parameters from
[page:Color color] in to this color.

### <br/> function convertLinearToSRGB( ): convertLinearToSRGB; <br/>

Converts this color from linear space to sRGB space.

### <br/> function convertSRGBToLinear( ): convertSRGBToLinear; <br/>

Converts this color from sRGB space to linear space.

### <br/> function copyLinearToSRGB( color: Color ): copyLinearToSRGB; <br/>

[page:Color color] — Color to copy.  
Copies the given color into this color, and then converts this color from
linear space to sRGB space.

### <br/> function copySRGBToLinear( color: Color ): copySRGBToLinear; <br/>

[page:Color color] — Color to copy.  
Copies the given color into this color, and then converts this color from sRGB
space to linear space.

### [method:Boolean equals]( [param:Color color] )

Compares the RGB values of [page:Color color] with those of this object.
Returns true if they are the same, false otherwise.

### <br/> function fromArray( array: Array, offset: Integer ): fromArray;
<br/>

[page:Array array] - [page:Array] of floats in the form [ [page:Float r],
[page:Float g], [page:Float b] ].  
[page:Integer offset] - An optional offset into the array.  
  
Sets this color's components based on an array formatted like [ [page:Float
r], [page:Float g], [page:Float b] ].

### <br/> function fromBufferAttribute( attribute: BufferAttribute, index:
Integer ): fromBufferAttribute; <br/>

[page:BufferAttribute attribute] - the source attribute.  
[page:Integer index] - index in the attribute.  
  
Sets this color's components from the [page:BufferAttribute attribute].

###  [method:Integer getHex]( [param:string colorSpace] = SRGBColorSpace )

Returns the hexadecimal value of this color.

###  [method:String getHexString]( [param:string colorSpace] = SRGBColorSpace
)

Returns the hexadecimal value of this color as a string (for example,
'FFFFFF').

###  [method:Object getHSL]( [param:Object target], [param:string colorSpace]
= LinearSRGBColorSpace )

[page:Object target] — the result will be copied into this Object. Adds h, s
and l keys to the object (if not already present).  
  
Convert this Color's [page:.r r], [page:.g g] and [page:.b b] values to
[link:https://en.wikipedia.org/wiki/HSL_and_HSV HSL] format and returns an
object of the form:  
```ts  
{  
h: 0,  
s: 0,  
l: 0  
}  
```  

###  [method:Color getRGB]( [param:Color target], [param:string colorSpace] =
LinearSRGBColorSpace )

[page:Color target] — the result will be copied into this object.  
  
Returns the RGB values of this color as an instance of [page:Color].

###  [method:String getStyle]( [param:string colorSpace] = SRGBColorSpace )

Returns the value of this color as a CSS style string. Example:
`rgb(255,0,0)`.

### <br/> function lerp( color: Color, alpha: Float ): lerp; <br/>

[page:Color color] - color to converge on.  
[page:Float alpha] - interpolation factor in the closed interval `[0, 1]`.  
  
Linearly interpolates this color's RGB values toward the RGB values of the
passed argument. The alpha argument can be thought of as the ratio between the
two colors, where `0.0` is this color and `1.0` is the first argument.

### <br/> function lerpColors( color1: Color, color2: Color, alpha: Float ):
lerpColors; <br/>

[page:Color color1] - the starting [page:Color].  
[page:Color color2] - [page:Color] to interpolate towards.  
[page:Float alpha] - interpolation factor, typically in the closed interval
`[0, 1]`.  
  
Sets this color to be the color linearly interpolated between [page:Color
color1] and [page:Color color2] where alpha is the percent distance along the
line connecting the two colors - alpha = 0 will be [page:Color color1], and
alpha = 1 will be [page:Color color2].

### <br/> function lerpHSL( color: Color, alpha: Float ): lerpHSL; <br/>

[page:Color color] - color to converge on.  
[page:Float alpha] - interpolation factor in the closed interval `[0, 1]`.  
  
Linearly interpolates this color's HSL values toward the HSL values of the
passed argument. It differs from the classic [page:.lerp] by not interpolating
straight from one color to the other, but instead going through all the hues
in between those two colors. The alpha argument can be thought of as the ratio
between the two colors, where 0.0 is this color and 1.0 is the first argument.

### <br/> function multiply( color: Color ): multiply; <br/>

Multiplies this color's RGB values by the given [page:Color color]'s RGB
values.

### <br/> function multiplyScalar( s: Number ): multiplyScalar; <br/>

Multiplies this color's RGB values by [page:Number s].

### <br/> function offsetHSL( h: Float, s: Float, l: Float ): offsetHSL; <br/>

Adds the given [page:Float h], [page:Float s], and [page:Float l] to this
color's values. Internally, this converts the color's [page:.r r], [page:.g g]
and [page:.b b] values to HSL, adds [page:Float h], [page:Float s], and
[page:Float l], and then converts the color back to RGB.

### <br/> function set( r: Color_Hex_or_String, g: Float, b: Float ): set;
<br/>

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

### <br/> function setFromVector3( vector: Vector3 ): setFromVector3; <br/>

Sets this colors's [page:.r r], [page:.g g] and [page:.b b] components from
the x, y, and z components of the specified [page:Vector3 vector].

### <br/> function setHex( hex: Integer, colorSpace: string ): setHex; <br/>

[page:Integer hex] —
[link:https://en.wikipedia.org/wiki/Web_colors#Hex_triplet hexadecimal
triplet] format.  
  
Sets this color from a hexadecimal value.

### <br/> function setHSL( h: Float, s: Float, l: Float, colorSpace: string ):
setHSL; <br/>

[page:Float h] — hue value between `0.0` and `1.0`  
[page:Float s] — saturation value between `0.0` and `1.0`  
[page:Float l] — lightness value between `0.0` and `1.0`  
  
Sets color from HSL values.

### <br/> function setRGB( r: Float, g: Float, b: Float, colorSpace: string ):
setRGB; <br/>

[page:Float r] — Red channel value between `0.0` and `1.0`.  
[page:Float g] — Green channel value between `0.0` and `1.0`.  
[page:Float b] — Blue channel value between `0.0` and `1.0`.  
  
Sets this color from RGB values.

### <br/> function setScalar( scalar: Float ): setScalar; <br/>

[page:Float scalar] — a value between `0.0` and `1.0`.  
  
Sets all three color components to the value [page:Float scalar].

### <br/> function setStyle( style: String, colorSpace: string ): setStyle;
<br/>

[page:String style] — color as a CSS-style string.  
  
Sets this color from a CSS-style string. For example, "rgb(250, 0,0)",
"rgb(100%, 0%, 0%)", "hsl(0, 100%, 50%)", "#ff0000", "#f00", or "red" ( or any
[link:https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart X11 color
name] - all 140 color names are supported ).  
Translucent colors such as "rgba(255, 0, 0, 0.5)" and "hsla(0, 100%, 50%,
0.5)" are also accepted, but the alpha-channel coordinate will be discarded.  
  
Note that for X11 color names, multiple words such as Dark Orange become the
string 'darkorange'.

### <br/> function setColorName( style: String, colorSpace: string ):
setColorName; <br/>

[page:String style] — color name ( from
[link:https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart X11 color
names] ).  
  
Sets this color from a color name. Faster than [page:.setStyle] method if you
don't need the other CSS-style formats.  
  
For convenience, the list of names is exposed in Color.NAMES as a hash:  
```ts  
Color.NAMES.aliceblue // returns 0xF0F8FF  
```  

### <br/> function sub( color: Color ): sub; <br/>

Subtracts the RGB components of the given color from the RGB components of
this color. If this results in a negative component, that component is set to
zero.

###  [method:Array toArray]( [param:Array array], [param:Integer offset] )

[page:Array array] - An optional array to store the color to.  
[page:Integer offset] - An optional offset into the array.  
  
Returns an array of the form [ r, g, b ].

### [method:Number toJSON]()

This methods defines the serialization result of [name]. Returns the color as
a hexadecimal value.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]
