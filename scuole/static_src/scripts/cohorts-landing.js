import './utils/cohortsNav';
import zoomMap from './utils/zoomMap';

import google from 'google';

function initialize() {
  const tooltip = document.getElementById('map-tooltip');
  const mapCanvas = document.getElementById('map-regions');

  const mapOptions = {
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    draggable: false,
    scrollwheel: false,
    fullscreenControl: false,
  };

  const map = new google.maps.Map(mapCanvas, mapOptions);
  if (SHAPE) {
    map.data.addGeoJson(SHAPE);
  }

  map.data.setStyle({
    fillColor: '#C2C2C2',
    fillOpacity: 0.3,
    strokeWeight: 1,
  });

  map.data.addListener('mouseover', event => {
    const feature = event.feature;

    tooltip.classList.add('map-tooltip--visible');
    tooltip.textContent = feature.getProperty('region_name_with_city');
    map.data.revertStyle();
    map.data.overrideStyle(feature, { fillColor: '#9b9b9b', strokeWeight: 2 });
  });

  map.data.addListener('mouseout', event => {
    tooltip.classList.remove('map-tooltip--visible');
    tooltip.textContent = '';
    map.data.revertStyle();
  });

  map.data.addListener('click', event => {
    const feature = event.feature;
    window.location.href = feature.getProperty('url');
  });

  zoomMap(map);

  mapCanvas.addEventListener('click', () => {
    map.setOptions({
      draggable: true,
      scrollwheel: true,
    });
  });
}

google.maps.event.addDomListener(window, 'load', initialize);
