/* global COORDS */

import './utils/metricNavs';
import './utils/reminderBar';

let map, nav, marker;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';
const texasBounds = [[-106.645645, 25.837059], [-93.50782, 36.500454]];

function initialize() {
  console.log(COORDS);
  map = new mapboxgl.Map({
    container: 'map-campus',
    //style: 'mapbox://styles/texastribune/cj73zub8131we2so5cd7hxhci'
    style: 'mapbox://styles/mapbox/streets-v9',
    maxBounds: texasBounds,
    center: COORDS.coordinates,
    zoom: 13,
  });
  marker = new mapboxgl.Marker().setLngLat(COORDS.coordinates).addTo(map);
  // var mapCanvas = document.getElementById('map-campus');
  // var latlng = new google.maps.LatLng(
  //   COORDS.coordinates[1],
  //   COORDS.coordinates[0]
  // );

  // console.log(COORDS)
  // var mapOptions = {
  //   center: latlng,
  //   zoom: 14,
  //   mapTypeId: google.maps.MapTypeId.ROADMAP,
  //   draggable: false,
  //   scrollwheel: false,
  // };

  // var map = new google.maps.Map(mapCanvas, mapOptions);

  // new google.maps.Marker({
  //   map: map,
  //   animation: google.maps.Animation.DROP,
  //   position: latlng,
  // });

  // mapCanvas.addEventListener('click', () => {
  //   map.setOptions({
  //     draggable: true,
  //     scrollwheel: true,
  //   });
  // });
}

initialize();
