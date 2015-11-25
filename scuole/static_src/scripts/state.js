/* global SHAPE */

import google from 'google'
import zoomMap from './utils/zoomMap'

import './utils/metricNavs'
import './utils/reminderBar'

function initialize () {
  let mapCanvas = document.getElementById('map-state')

  let mapOptions = {
    zoom: 6,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  let map = new google.maps.Map(mapCanvas, mapOptions)
  if (SHAPE.geometry) {
    map.data.addGeoJson(SHAPE)
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
      strokeWeight: 1
    }
  })

  zoomMap(map)
}

google.maps.event.addDomListener(window, 'load', initialize)
