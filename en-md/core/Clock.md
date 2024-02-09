# [name]

Object for keeping track of time. This uses
[link:https://developer.mozilla.org/en-US/docs/Web/API/Performance/now
performance.now] if it is available, otherwise it reverts to the less accurate
[link:https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Date/now
Date.now].

## Constructor

### [name]( [param:Boolean autoStart] )

autoStart — (optional) whether to automatically start the clock when
[page:.getDelta]() is called for the first time. Default is `true`.

## Properties

### <br/> Boolean autoStart; <br/>

If set, starts the clock automatically when [page:.getDelta]() is called for
the first time. Default is `true`.

### <br/> Float startTime; <br/>

Holds the time at which the clock's [page:Clock.start start] method was last
called. Default is `0`.

### <br/> Float oldTime; <br/>

Holds the time at which the clock's [page:Clock.start start],
[page:.getElapsedTime]() or [page:.getDelta]() methods were last called.
Default is `0`.

### <br/> Float elapsedTime; <br/>

Keeps track of the total time that the clock has been running. Default is `0`.

### <br/> Boolean running; <br/>

Whether the clock is running or not. Default is `false`.

## Methods

### [method:undefined start]()

Starts clock. Also sets the [page:.startTime] and [page:.oldTime] to the
current time, sets [page:.elapsedTime] to `0` and [page:.running] to `true`.

### [method:undefined stop]()

Stops clock and sets [page:Clock.oldTime oldTime] to the current time.

### [method:Float getElapsedTime]()

Get the seconds passed since the clock started and sets [page:.oldTime] to the
current time.  
If [page:.autoStart] is `true` and the clock is not running, also starts the
clock.

### [method:Float getDelta]()

Get the seconds passed since the time [page:.oldTime] was set and sets
[page:.oldTime] to the current time.  
If [page:.autoStart] is `true` and the clock is not running, also starts the
clock.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

