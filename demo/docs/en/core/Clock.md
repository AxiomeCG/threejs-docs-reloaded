# Clock

Object for keeping track of time. This uses <a
href="https://developer.mozilla.org/en-
US/docs/Web/API/Performance/now">performance.now</a> if it is available,
otherwise it reverts to the less accurate <a
href="https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Date/now">Date.now</a>.

## Constructor

### Clock

  
  
```ts  
function Clock( autoStart: Boolean ): void;  
```  

autoStart — (optional) whether to automatically start the clock when
[.getDelta](#)() is called for the first time. Default is `true`.

## Properties

### autoStart

  
  
```ts  
autoStart: Boolean;  
```  

If set, starts the clock automatically when [.getDelta](#)() is called for the
first time. Default is `true`.

### startTime

  
  
```ts  
startTime: Float;  
```  

Holds the time at which the clock's [start](#) method was last called. Default
is `0`.

### oldTime

  
  
```ts  
oldTime: Float;  
```  

Holds the time at which the clock's [start](#), [.getElapsedTime](#)() or
[.getDelta](#)() methods were last called. Default is `0`.

### elapsedTime

  
  
```ts  
elapsedTime: Float;  
```  

Keeps track of the total time that the clock has been running. Default is `0`.

### running

  
  
```ts  
running: Boolean;  
```  

Whether the clock is running or not. Default is `false`.

## Methods

### start

  
  
```ts  
function start( ): undefined;  
```  

Starts clock. Also sets the [.startTime](#) and [.oldTime](#) to the current
time, sets [.elapsedTime](#) to `0` and [.running](#) to `true`.

### stop

  
  
```ts  
function stop( ): undefined;  
```  

Stops clock and sets [oldTime](#) to the current time.

### getElapsedTime

  
  
```ts  
function getElapsedTime( ): Float;  
```  

Get the seconds passed since the clock started and sets [.oldTime](#) to the
current time.  
If [.autoStart](#) is `true` and the clock is not running, also starts the
clock.

### getDelta

  
  
```ts  
function getDelta( ): Float;  
```  

Get the seconds passed since the time [.oldTime](#) was set and sets
[.oldTime](#) to the current time.  
If [.autoStart](#) is `true` and the clock is not running, also starts the
clock.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/Clock.js">src/core/Clock.js</a>

