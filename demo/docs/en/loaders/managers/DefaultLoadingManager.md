# DefaultLoadingManager

A global instance of the
[LoadingManager](en\loaders\managers\LoadingManager.html), used by most
loaders when no custom manager has been specified.  
  
This will be sufficient for most purposes, however there may be times when you
desire separate loading managers for say, textures and models.

## Code Example

You can optionally set the [onStart](#), [onLoad](#), [onProgress](#),
[onError](#) functions for the manager. These will then apply to any loaders
using the DefaultLoadingManager.  
  
Note that these shouldn't be confused with the similarly named functions of
individual loaders, as they are intended for displaying information about the
overall status of loading, rather than dealing with the data that has been
loaded.

  
```ts  
THREE.DefaultLoadingManager.onStart = function ( url, itemsLoaded, itemsTotal
) { console.log( 'Started loading file: ' + url + '.\nLoaded ' + itemsLoaded +
' of ' + itemsTotal + ' files.' );};THREE.DefaultLoadingManager.onLoad =
function ( ) { console.log( 'Loading
Complete!');};THREE.DefaultLoadingManager.onProgress = function ( url,
itemsLoaded, itemsTotal ) { console.log( 'Loading file: ' + url + '.\nLoaded '
+ itemsLoaded + ' of ' + itemsTotal + ' files.'
);};THREE.DefaultLoadingManager.onError = function ( url ) { console.log(
'There was an error loading ' + url );};  
```  

## Properties

See the [LoadingManager](en\loaders\managers\LoadingManager.html) page for
details of properties.

## Methods

See the [LoadingManager](en\loaders\managers\LoadingManager.html) page for
details of methods.

## Source

<a
href="https://github.com/mrdoob/three.js/blob/master/src/loaders/LoadingManager.js">src/loaders/LoadingManager.js</a>

