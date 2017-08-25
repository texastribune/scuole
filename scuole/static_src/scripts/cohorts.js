/* global SHAPE */

import './utils/cohortsNav';
import './utils/metricNavs';
import './utils/reminderBar';

import google from 'google';
import zoomMap from './utils/zoomMap';

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

function initialize() {
  if (!SHAPE) return;

  const mapCanvas = document.getElementById('map-container');

  const mapOptions = {
    zoom: 6,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    draggable: false,
    scrollwheel: false,
  };

  const map = new google.maps.Map(mapCanvas, mapOptions);
  if (SHAPE.geometry) {
    map.data.addGeoJson(SHAPE);
  }

  map.data.setStyle({
    fillColor: '#C2C2C2',
    fillOpacity: 0.3,
    strokeWeight: 1,
    icon: {
      path: google.maps.SymbolPath.CIRCLE,
      scale: 3,
      fillColor: '#09B6AE',
      fillOpacity: 0.8,
      strokeWeight: 1,
    },
  });

  zoomMap(map);

  const mapClicker = () => {
    map.setOptions({
      draggable: true,
      scrollwheel: true,
    });

    mapCanvas.removeEventListener('click', mapClicker, false);
  };

  mapCanvas.addEventListener('click', mapClicker, false);
}

google.maps.event.addDomListener(window, 'load', initialize);
