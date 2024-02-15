# EventDispatcher

JavaScript events for custom objects.  
<a href="https://github.com/mrdoob/eventdispatcher.js">EventDispatcher on
GitHub</a>

## Code Example

  
```ts  
// Adding events to a custom object class Car extends EventDispatcher {
start() { this.dispatchEvent( { type: 'start', message: 'vroom vroom!' } ); }
}; // Using events with the custom object const car = new Car();
car.addEventListener( 'start', function ( event ) { alert( event.message ); }
); car.start();  
```  

## Constructor

### EventDispatcher

  
  
```ts  
function EventDispatcher( ): void;  
```  

Creates EventDispatcher object.

## Methods

### addEventListener

  
  
```ts  
function addEventListener( type: String, listener: Function ): undefined;  
```  

type - The type of event to listen to.  
listener - The function that gets called when the event is fired.

Adds a listener to an event type.

### hasEventListener

  
  
```ts  
function hasEventListener( type: String, listener: Function ): Boolean;  
```  

type - The type of event to listen to.  
listener - The function that gets called when the event is fired.

Checks if listener is added to an event type.

### removeEventListener

  
  
```ts  
function removeEventListener( type: String, listener: Function ): undefined;  
```  

type - The type of the listener that gets removed.  
listener - The listener function that gets removed.

Removes a listener from an event type.

### dispatchEvent

  
  
```ts  
function dispatchEvent( event: Object ): undefined;  
```  

event - The event that gets fired.

Fire an event type.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/core/EventDispatcher.js">src/core/EventDispatcher.js</a>

