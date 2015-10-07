/* global document,google,window,COORDS */

'use strict';

var map;

function initialize() {
  var mapCanvas = document.getElementById('map');
  var latlng = new google.maps.LatLng(COORDS[0], COORDS[1]);

  var mapOptions = {
    center: latlng,
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };

  map = new google.maps.Map(mapCanvas, mapOptions);

  new google.maps.Marker({
    position: latlng,
    map: map
  });

  var panorama = new google.maps.StreetViewPanorama(
      document.getElementById('pano'), {
        position: latlng,
      });

  map.setStreetView(panorama);
}

google.maps.event.addDomListener(window, 'load', initialize);
