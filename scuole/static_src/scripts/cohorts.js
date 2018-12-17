/* global SHAPE */

import './utils/cohortsNav';
import './utils/metricNavs';
import './utils/reminderBar';

import { h, render } from 'preact';
import ChartGrid from './utils/components/ChartGrid';

const data = window.data;

const ethnicityData = [
  {
    title: 'Black',
    data: data.black,
  },
  {
    title: 'Hispanic',
    data: data.hispanic,
  },
  {
    title: 'White',
    data: data.white,
  },
  {
    title: 'Other',
    data: data.other,
  },
];

const genderData = [
  {
    title: 'Female',
    data: data.female,
  },
  {
    title: 'Male',
    data: data.male,
  },
];

const economicData = [
  {
    title: 'Economically disadvantaged',
    data: data.economically_disadvantaged,
  },
  {
    title: 'Not economically disadvantaged',
    data: data.not_economically_disadvantaged,
  },
];

render(
  <ChartGrid title="ethnicity" chartData={ethnicityData} />,
  document.getElementById('ethnicity-status-charts')
);

render(
  <ChartGrid title="gender" chartData={genderData} />,
  document.getElementById('gender-status-charts')
);

render(
  <ChartGrid title="economic status" chartData={economicData} />,
  document.getElementById('economic-status-charts')
);
let map, nav;
mapboxgl.accessToken =
  'pk.eyJ1IjoidGV4YXN0cmlidW5lIiwiYSI6ImNqb3lxOXg4cTJsdm8zdHBpbTUyaG9sYXcifQ.HM6pBNV6vnvQBg7v4X5nFw';

function initialize() {
  if (!SHAPE) return;
  let coordinates = SHAPE.geometry.coordinates[0];
  console.log(coordinates);
  if (coordinates.length == 1 || coordinates.length == 3) {
    //BEAUMOUNT OR TEXAS
    coordinates = coordinates[0];
  }
  const bounds = coordinates.reduce(function(bounds, coord) {
    return bounds.extend(coord);
  }, new mapboxgl.LngLatBounds(coordinates[0], coordinates[0]));
  map = new mapboxgl.Map({
    container: 'map-container',
    style: 'mapbox://styles/mapbox/light-v9',
    center: [-99.9018, 31.3915],
    zoom: 4.25,
  });

  nav = new mapboxgl.NavigationControl({ showCompass: false });
  map.addControl(nav, 'top-right');

  map.fitBounds(bounds, {
    padding: 20,
  });

  map.on('load', () => {
    map.addLayer({
      id: 'region',
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
      id: 'regionOutline',
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
