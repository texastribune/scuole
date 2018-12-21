import './utils/cohortsNav';
import loadJsonScript from './utils/loadJsonScript';

let map, nav, hoveredStateId;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';

function initialize() {
  const SHAPE = loadJsonScript('shape');
  const tooltip = document.getElementById('map-tooltip');

  SHAPE.features = SHAPE.features.map(d => {
    d.id = d.properties['region_name_with_city'].split(' ')[1];
    return d;
  });
  map = new mapboxgl.Map({
    container: 'map-regions',
    style: 'mapbox://styles/mapbox/light-v9',
    center: [-99.9018, 31.3915],
    zoom: 4.25,
  });
  nav = new mapboxgl.NavigationControl({ showCompass: false });
  map.addControl(nav, 'top-right');

  // map.setMaxBounds(map.getBounds());

  map.on('load', () => {
    map.addSource('regions', {
      type: 'geojson',
      data: SHAPE,
    });

    map.addLayer({
      id: 'region',
      type: 'fill',
      source: 'regions',
      paint: {
        'fill-color': '#C2C2C2',
        'fill-opacity': [
          'case',
          ['boolean', ['feature-state', 'hover'], false],
          1,
          0.3,
        ],
        'fill-outline-color': '#000',
      },
    });

    map.addLayer({
      id: 'regionOutline',
      type: 'line',
      source: {
        type: 'geojson',
        data: SHAPE,
      },
      paint: {},
    });
  });

  map.on('mousemove', 'region', function(e) {
    map.getCanvas().style.cursor = 'pointer';
    if (e.features.length > 0) {
      const { clientX, clientY } = e.originalEvent;
      const { left, top } = document
        .getElementById('map-regions')
        .getBoundingClientRect();
      const leftOffset = clientX - left;
      const topOffset = clientY - top;
      if (hoveredStateId != null) {
        map.setFeatureState(
          { source: 'regions', id: hoveredStateId },
          { hover: false }
        );
      }
      hoveredStateId = e.features[0].properties['region_name_with_city'].split(
        ' '
      )[1];
      map.setFeatureState(
        { source: 'regions', id: hoveredStateId },
        { hover: true }
      );

      tooltip.classList.add('map-tooltip--visible');
      tooltip.textContent = e.features[0].properties['region_name_with_city'];
      const { width } = tooltip.getBoundingClientRect();
      tooltip.style.left = `${leftOffset - width / 2}px`;
      tooltip.style.top = `${topOffset + 20}px`;
    }
  });

  map.on('mouseout', 'region', function(e) {
    tooltip.classList.remove('map-tooltip--visible');
    tooltip.textContent = '';
    map.setFeatureState(
      { source: 'regions', id: hoveredStateId },
      { hover: false }
    );
    map.getCanvas().style.cursor = '';
  });

  map.on('click', 'region', function(e) {
    if (e.features.length > 0) {
      window.location.href = e.features[0].properties.url;
    }
  });
}

initialize();
