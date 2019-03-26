import '../utils/campusList';
import '../utils/metricNavs';
import '../utils/reminderBar';
import '../utils/loadStoryGrid';
import '../utils/adLoader';
import '../utils/searchTypeahead';
import loadJsonScript from '../utils/loadJsonScript';
import bbox from '@turf/bbox';

let map, nav, hoveredStateId;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';

function initialize() {
  const SHAPE = loadJsonScript('shape');
  const COORDS = loadJsonScript('coords');
  const bounds = bbox(COORDS);

  const tooltip = document.getElementById('map-tooltip');
  COORDS.features = COORDS.features.map((d, i) => {
    d.id = i;
    return d;
  });

  if (SHAPE.geometry) {
    map = new mapboxgl.Map({
      container: 'map-district',
      style: 'mapbox://styles/mapbox/light-v9',
      center: [-99.9018, 31.3915],
      zoom: 4.25,
    });

    map.fitBounds(SHAPE.bbox, { duration: 0, padding: 30 });
  } else {
    //district is only a school
    map = new mapboxgl.Map({
      container: 'map-district',
      style: 'mapbox://styles/mapbox/light-v9',
    });

    map.fitBounds(bounds, { duration: 0, padding: 30, maxZoom: 13 });
  }

  nav = new mapboxgl.NavigationControl({ showCompass: false });
  map.addControl(nav, 'top-right');

  map.on('load', () => {
    map.addSource('schools', {
      type: 'geojson',
      data: COORDS,
    });

    if (SHAPE.geometry) {
      map.addLayer({
        id: 'district',
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
        id: 'districtOutline',
        type: 'line',
        source: {
          type: 'geojson',
          data: SHAPE,
        },
        paint: {},
      });
    }
    map.addLayer({
      id: 'school',
      type: 'circle',
      source: 'schools',
      paint: {
        'circle-radius': 4,
        'circle-opacity': 0.5,
        'circle-color': '#09B6AE',
        'circle-stroke-width': [
          'case',
          ['boolean', ['feature-state', 'hover'], false],
          1,
          0,
        ],
      },
    });

    map.on('mousemove', 'school', function(e) {
      map.getCanvas().style.cursor = 'pointer';
      if (e.features.length > 0) {
        const { clientX, clientY } = e.originalEvent;
        const { left, top } = document
          .getElementById('map-district')
          .getBoundingClientRect();
        const leftOffset = clientX - left;
        const topOffset = clientY - top;

        if (hoveredStateId != null) {
          map.setFeatureState(
            { source: 'schools', id: hoveredStateId },
            { hover: false }
          );
        }
        hoveredStateId = e.features[0].id;
        map.setFeatureState(
          { source: 'schools', id: hoveredStateId },
          { hover: true }
        );
        map.getCanvas().style.cursor = 'pointer';
        tooltip.classList.add('map-tooltip--visible');
        tooltip.textContent = e.features[0].properties['name'];
        const { width } = tooltip.getBoundingClientRect();
        tooltip.style.left = `${leftOffset - width / 2}px`;
        tooltip.style.top = `${topOffset + 20}px`;
      }
    });

    map.on('mouseout', 'school', function(e) {
      map.setFeatureState(
        { source: 'schools', id: hoveredStateId },
        { hover: false }
      );
      tooltip.classList.remove('map-tooltip--visible');
      tooltip.textContent = '';
      map.getCanvas().style.cursor = '';
    });

    map.on('click', 'school', function(e) {
      console.log(e.features[0].properties);
      console.log(e.features[0].properties.name);
      if (e.features.length > 0) {
        window.location.href = `${window.location.href}${
          e.features[0].properties.slug
        }`;
      }
    });
  });
}
initialize();
