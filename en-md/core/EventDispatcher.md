# [name]

JavaScript events for custom objects.  
[link:https://github.com/mrdoob/eventdispatcher.js EventDispatcher on GitHub]

## Code Example

  
```ts  
// Adding events to a custom object  
class Car extends EventDispatcher {  
start() {  
this.dispatchEvent( { type: 'start', message: 'vroom vroom!' } );  
}  
};  
  
// Using events with the custom object  
const car = new Car();  
car.addEventListener( 'start', function ( event ) {  
alert( event.message );  
} );  
  
car.start();  
```  

## Constructor

### [name]()

Creates EventDispatcher object.

## Methods

### [method:undefined addEventListener]( [param:String type], [param:Function
listener] )

type - The type of event to listen to.  
listener - The function that gets called when the event is fired.

Adds a listener to an event type.

### [method:Boolean hasEventListener]( [param:String type], [param:Function
listener] )

type - The type of event to listen to.  
listener - The function that gets called when the event is fired.

Checks if listener is added to an event type.

### [method:undefined removeEventListener]( [param:String type],
[param:Function listener] )

type - The type of the listener that gets removed.  
listener - The listener function that gets removed.

Removes a listener from an event type.

### [method:undefined dispatchEvent]( [param:Object event] )

event - The event that gets fired.

Fire an event type.

## Source

[link:https://github.com/mrdoob/three.js/blob/master/src/[path].js
src/[path].js]

