# PropertyMixer

Buffered scene graph property that allows weighted accumulation; used
internally.

## Constructor

###  function PropertyMixer( binding: PropertyBinding, typeName: String,
valueSize: Number ): void;

\-- binding  
\-- typeName  
\-- valueSize  

## Properties

###  PropertyBinding binding;

###  TypedArray buffer;

Buffer with size [page:PropertyMixer valueSize] * 4.  
  
This has the layout: [ incoming | accu0 | accu1 | orig ]  
  
Interpolators can use .buffer as their .result and the data then goes to
'incoming'. 'accu0' and 'accu1' are used frame-interleaved for the cumulative
result and are compared to detect changes. 'orig' stores the original state of
the property.

###  Number cumulativeWeight;

Default is `0`.

###  Number cumulativeWeightAdditive;

Default is `0`.

###  Number valueSize;

###  Number referenceCount;

Default is `0`.

###  Number useCount;

Default is `0`.

## Methods

###  function accumulate( accuIndex: Number, weight: Number ): undefined;

Accumulate data in [page:PropertyMixer.buffer buffer][accuIndex] 'incoming'
region into 'accu[i]'.  
If weight is `0` this does nothing.

###  function accumulateAdditive( weight: Number ): undefined;

Accumulate data in the 'incoming' region into 'add'.  
If weight is `0` this does nothing.

###  function apply( accuIndex: Number ): undefined;

Apply the state of [page:PropertyMixer.buffer buffer] 'accu[i]' to the binding
when accus differ.

###  function saveOriginalState( ): undefined;

Remember the state of the bound property and copy it to both accus.

###  function restoreOriginalState( ): undefined;

Apply the state previously taken via 'saveOriginalState' to the binding.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

