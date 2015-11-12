/* global document,google,window,SHAPE */

'use strict';

var map;

function initialize() {
  var mapCanvas = document.getElementById('map-state');

  var mapOptions = {
    zoom: 6,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(mapCanvas, mapOptions);
  if (SHAPE.geometry) {
    map.data.addGeoJson(SHAPE);
  }

  map.data.setStyle({
    fillColor: '#C2C2C2',
    fillOpacity: 0.3,
    strokeWeight: 1,
    icon: {
      path: google.maps.SymbolPath.CIRCLE,
      scale: 3,
      fillColor: '#09B6AE',
      fillOpacity: 0.8,
      strokeWeight: 1
    }
  });

  zoom(map);
}

function zoom(map) {
  var bounds = new google.maps.LatLngBounds();

  map.data.forEach(function(feature) {
    if (feature.getGeometry()) {
      processPoints(feature.getGeometry(), bounds.extend, bounds);
    }
  });

  map.fitBounds(bounds);
}

function processPoints(geometry, callback, thisArg) {
  if (geometry instanceof google.maps.LatLng) {
    callback.call(thisArg, geometry);
  } else if (geometry instanceof google.maps.Data.Point) {
    callback.call(thisArg, geometry.get());
  } else {
    geometry.getArray().forEach(function(g) {
      processPoints(g, callback, thisArg);
    });
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
