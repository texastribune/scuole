import './utils/metricNavs';
import './utils/reminderBar';
import loadJsonScript from './utils/loadJsonScript';

let map, nav;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';

function initialize() {
  const SHAPE = loadJsonScript('shape');

  map = new mapboxgl.Map({
    container: 'map-state',
    style: 'mapbox://styles/mapbox/light-v9',
  });

  map.fitBounds(SHAPE.bbox, { duration: 0, padding: 30 });

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
