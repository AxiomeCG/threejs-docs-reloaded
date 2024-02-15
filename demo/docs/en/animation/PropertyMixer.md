# PropertyMixer

Buffered scene graph property that allows weighted accumulation; used
internally.

## Constructor

### PropertyMixer

  
  
```ts  
function PropertyMixer( binding: PropertyBinding, typeName: String, valueSize:
Number ): void;  
```  

\-- binding  
\-- typeName  
\-- valueSize  

## Properties

### binding

  
  
```ts  
binding: PropertyBinding;  
```  

### buffer

  
  
```ts  
buffer: TypedArray;  
```  

Buffer with size [valueSize](en\animation\PropertyMixer.html) * 4.  
  
This has the layout: [ incoming | accu0 | accu1 | orig ]  
  
Interpolators can use .buffer as their .result and the data then goes to
'incoming'. 'accu0' and 'accu1' are used frame-interleaved for the cumulative
result and are compared to detect changes. 'orig' stores the original state of
the property.

### cumulativeWeight

  
  
```ts  
cumulativeWeight: Number;  
```  

Default is `0`.

### cumulativeWeightAdditive

  
  
```ts  
cumulativeWeightAdditive: Number;  
```  

Default is `0`.

### valueSize

  
  
```ts  
valueSize: Number;  
```  

### referenceCount

  
  
```ts  
referenceCount: Number;  
```  

Default is `0`.

### useCount

  
  
```ts  
useCount: Number;  
```  

Default is `0`.

## Methods

### accumulate

  
  
```ts  
function accumulate( accuIndex: Number, weight: Number ): undefined;  
```  

Accumulate data in [buffer](#)[accuIndex] 'incoming' region into 'accu[i]'.  
If weight is `0` this does nothing.

### accumulateAdditive

  
  
```ts  
function accumulateAdditive( weight: Number ): undefined;  
```  

Accumulate data in the 'incoming' region into 'add'.  
If weight is `0` this does nothing.

### apply

  
  
```ts  
function apply( accuIndex: Number ): undefined;  
```  

Apply the state of [buffer](#) 'accu[i]' to the binding when accus differ.

### saveOriginalState

  
  
```ts  
function saveOriginalState( ): undefined;  
```  

Remember the state of the bound property and copy it to both accus.

### restoreOriginalState

  
  
```ts  
function restoreOriginalState( ): undefined;  
```  

Apply the state previously taken via 'saveOriginalState' to the binding.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/animation/PropertyMixer.js">src/animation/PropertyMixer.js</a>

