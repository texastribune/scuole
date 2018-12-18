/* global SHAPE */

// import google from 'google';
// import zoomMap from './utils/zoomMap';
import './utils/metricNavs';
import './utils/reminderBar';

let map, nav;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';
//const usBounds = [[-171.791110603, 18.91619], [-66.96466, 71.3577635769]];

function initialize() {
  map = new mapboxgl.Map({
    container: 'map-state',
    style: 'mapbox://styles/mapbox/light-v9',
    center: [-99.9018, 31.3915],
    zoom: 3.5,
  });

  nav = new mapboxgl.NavigationControl({ showCompass: false });
  map.addControl(nav, 'top-right');

  map.on('load', () => {
    map.addLayer({
      id: 'state',
      type: 'fill',
      source: {
        type: 'geojson',
        data: SHAPE,
      },
      paint: {
        'fill-color': '#C2C2C2',
        'fill-opacity': 0.3,
        'fill-outline-color': '#000',
      },
    });

    map.addLayer({
      id: 'stateOutline',
      type: 'line',
      source: {
        type: 'geojson',
        data: SHAPE,
      },
      paint: {},
    });
  });
}

initialize();
