# [name]

Buffered scene graph property that allows weighted accumulation; used
internally.

## Constructor

### [name]( [param:PropertyBinding binding], [param:String typeName],
[param:Number valueSize] )

\-- binding  
\-- typeName  
\-- valueSize  

## Properties

### <br/> PropertyBinding binding; <br/>

### <br/> TypedArray buffer; <br/>

Buffer with size [page:PropertyMixer valueSize] * 4.  
  
This has the layout: [ incoming | accu0 | accu1 | orig ]  
  
Interpolators can use .buffer as their .result and the data then goes to
'incoming'. 'accu0' and 'accu1' are used frame-interleaved for the cumulative
result and are compared to detect changes. 'orig' stores the original state of
the property.

### <br/> Number cumulativeWeight; <br/>

Default is `0`.

### <br/> Number cumulativeWeightAdditive; <br/>

Default is `0`.

### <br/> Number valueSize; <br/>

### <br/> Number referenceCount; <br/>

Default is `0`.

### <br/> Number useCount; <br/>

Default is `0`.

## Methods

###  [method:undefined accumulate]( [param:Number accuIndex], [param:Number
weight] )

Accumulate data in [page:PropertyMixer.buffer buffer][accuIndex] 'incoming'
region into 'accu[i]'.  
If weight is `0` this does nothing.

### [method:undefined accumulateAdditive]( [param:Number weight] )

Accumulate data in the 'incoming' region into 'add'.  
If weight is `0` this does nothing.

### [method:undefined apply]( [param:Number accuIndex] )

Apply the state of [page:PropertyMixer.buffer buffer] 'accu[i]' to the binding
when accus differ.

### [method:undefined saveOriginalState]( )

Remember the state of the bound property and copy it to both accus.

### [method:undefined restoreOriginalState]( )

Apply the state previously taken via 'saveOriginalState' to the binding.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

