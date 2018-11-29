/* global SHAPE */

// import google from 'google';
// import zoomMap from './utils/zoomMap';
import './utils/metricNavs';
import './utils/reminderBar';

let map, nav;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';
const usBounds = [[-171.791110603, 18.91619], [-66.96466, 71.3577635769]];

function initialize() {
  const features = SHAPE.geometry.coordinates.map(d => d[0]);

  const coordinates = features.reduce((flat, toFlatten) => {
    return flat.concat(toFlatten);
  }, []);

  const bounds = coordinates.reduce(function(bounds, coord) {
    return bounds.extend(coord);
  }, new mapboxgl.LngLatBounds(coordinates[0], coordinates[0]));
  map = new mapboxgl.Map({
    container: 'map-state',
    //style: 'mapbox://styles/texastribune/cj73zub8131we2so5cd7hxhci'
    style: 'mapbox://styles/mapbox/light-v9',
    // center: [-99.9018, 31.9686],
    // zoom: 3.7
    maxBounds: usBounds,
  });

  map.fitBounds(bounds, {
    padding: 40,
  });
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
  //   let mapOptions = {
  //     zoom: 6,
  //     mapTypeId: google.maps.MapTypeId.ROADMAP,
  //     draggable: false,
  //     scrollwheel: false,
  //   };

  //   let map = new google.maps.Map(mapCanvas, mapOptions);
  //   if (SHAPE.geometry) {
  //     map.data.addGeoJson(SHAPE);
  //   }

  //   map.data.setStyle({
  //     fillColor: '#C2C2C2',
  //     fillOpacity: 0.3,
  //     strokeWeight: 1,
  //     icon: {
  //       path: google.maps.SymbolPath.CIRCLE,
  //       scale: 3,
  //       fillColor: '#09B6AE',
  //       fillOpacity: 0.8,
  //       strokeWeight: 1,
  //     },
  //   });

  //   zoomMap(map);

  //   mapCanvas.addEventListener('click', () => {
  //     map.setOptions({
  //       draggable: true,
  //       scrollwheel: true,
  //     });
  //   });
}

initialize();
