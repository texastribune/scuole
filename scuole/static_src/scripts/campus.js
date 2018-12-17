/* global COORDS */

import './utils/metricNavs';
import './utils/reminderBar';

let map, nav, marker;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';
const texasBounds = [[-106.645645, 25.837059], [-93.50782, 36.500454]];

function initialize() {
  map = new mapboxgl.Map({
    container: 'map-campus',
    style: 'mapbox://styles/mapbox/light-v9',
    maxBounds: texasBounds,
    center: COORDS.coordinates,
    zoom: 12,
  });

  nav = new mapboxgl.NavigationControl({ showCompass: false });
  map.addControl(nav, 'top-right');

  marker = new mapboxgl.Marker().setLngLat(COORDS.coordinates).addTo(map);
}

initialize();
