import '../utils/metricNavs';
import '../utils/reminderBar';
import '../utils/loadStoryGrid';
import '../utils/adLoader';
import '../utils/searchTypeahead';
import loadJsonScript from '../utils/loadJsonScript';

mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';

function initialize() {
  const COORDS = loadJsonScript('coords');

  const map = new mapboxgl.Map({
    container: 'map-campus',
    style: 'mapbox://styles/mapbox/light-v9',
    center: COORDS.geometry.coordinates,
    zoom: 13,
    minZoom: 10,
    maxZoom: 15,
    scrollZoom: false,
    dragPan: false,
  });

  const nav = new mapboxgl.NavigationControl({ showCompass: false });
  map.addControl(nav, 'top-right');

  map.on('click', () => {
    map.dragPan.enable();
    map.scrollZoom.enable();
  });
  
  // disable map rotation using right click + drag
  map.dragRotate.disable();

  // disable map rotation using touch rotation gesture
  map.touchZoomRotate.disableRotation();

  const marker = new mapboxgl.Marker();

  marker.setLngLat(COORDS.geometry.coordinates).addTo(map);
}

initialize();
