/* global document,window,COORDS,SHAPE */

// import google from 'google';
// import zoomMap from './utils/zoomMap';

import './utils/campusList';
import './utils/metricNavs';
import './utils/reminderBar';

let map, nav, hoveredStateId;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';
const texasBounds = [[-106.645645, 25.837059], [-93.50782, 36.500454]];

function initialize() {
  const tooltip = document.getElementById('map-tooltip');
  COORDS.features = COORDS.features.map((d, i) => {
    d.id = i;
    return d;
  });
  let coordinates = SHAPE.geometry.coordinates[0][0];
  const bounds = coordinates.reduce(function(bounds, coord) {
    return bounds.extend(coord);
  }, new mapboxgl.LngLatBounds(coordinates[0], coordinates[0]));

  map = new mapboxgl.Map({
    container: 'map-district',
    //style: 'mapbox://styles/texastribune/cj73zub8131we2so5cd7hxhci'
    style: 'mapbox://styles/mapbox/light-v9',
    maxBounds: texasBounds,
  });

  nav = new mapboxgl.NavigationControl();
  map.addControl(nav, 'top-right');

  map.fitBounds(bounds, {
    padding: 20,
  });

  map.on('load', () => {
    map.addSource('schools', {
      type: 'geojson',
      data: COORDS,
    });
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

    map.addLayer({
      id: 'school',
      type: 'circle',
      source: 'schools',
      paint: {
        'circle-radius': 3.5,
        'circle-opacity': 0.8,
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
      if (e.features.length > 0) {
        if (hoveredStateId) {
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

        tooltip.classList.add('map-tooltip--visible');
        tooltip.textContent = e.features[0].properties['name'];
      }
    });

    map.on('mouseout', 'school', function(e) {
      tooltip.classList.remove('map-tooltip--visible');
      tooltip.textContent = '';
      map.setFeatureState(
        { source: 'schools', id: hoveredStateId },
        { hover: false }
      );
    });

    map.on('click', 'school', function(e) {
      if (e.features.length > 0) {
        window.location.href = e.features[0].properties.name
          .toLowerCase()
          .replace(/\s+/g, '-');
      }
    });
  });
}
initialize();
//google.maps.event.addDomListener(window, 'load', initialize);
