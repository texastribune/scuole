/* global document,google,window,COORDS */

'use strict';

var map;
var marker;

function initialize() {
  var mapCanvas = document.getElementById('map-campus');
  var latlng = new google.maps.LatLng(COORDS.coordinates[1], COORDS.coordinates[0]);

  var mapOptions = {
    center: latlng,
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(mapCanvas, mapOptions);

  marker = new google.maps.Marker({
    map: map,
    animation: google.maps.Animation.DROP,
    position: latlng
  });
}

google.maps.event.addDomListener(window, 'load', initialize);
