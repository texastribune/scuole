/* global document,google,window,COORDS,SHAPE */

'use strict';

var map;

function initialize() {
  var mapCanvas = document.getElementById('map-district');

  var mapOptions = {
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(mapCanvas, mapOptions);
  if (SHAPE.geometry) {
    map.data.addGeoJson(SHAPE);
  }
  map.data.addGeoJson(COORDS);

  map.data.setStyle({
    fillColor: 'green',
    strokeWeight: 1
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
