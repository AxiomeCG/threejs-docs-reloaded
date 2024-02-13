# EventDispatcher

JavaScript events for custom objects.  
[link:https://github.com/mrdoob/eventdispatcher.js EventDispatcher on GitHub]

## Code Example

  
```ts  
// Adding events to a custom object class Car extends EventDispatcher {
start() { this.dispatchEvent( { type: 'start', message: 'vroom vroom!' } ); }
}; // Using events with the custom object const car = new Car();
car.addEventListener( 'start', function ( event ) { alert( event.message ); }
); car.start();  
```  

## Constructor

###  function EventDispatcher( ): void;

Creates EventDispatcher object.

## Methods

###  function addEventListener( type: String, listener: Function ): undefined;

type - The type of event to listen to.  
listener - The function that gets called when the event is fired.

Adds a listener to an event type.

###  function hasEventListener( type: String, listener: Function ): Boolean;

type - The type of event to listen to.  
listener - The function that gets called when the event is fired.

Checks if listener is added to an event type.

###  function removeEventListener( type: String, listener: Function ):
undefined;

type - The type of the listener that gets removed.  
listener - The listener function that gets removed.

Removes a listener from an event type.

###  function dispatchEvent( event: Object ): undefined;

event - The event that gets fired.

Fire an event type.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

