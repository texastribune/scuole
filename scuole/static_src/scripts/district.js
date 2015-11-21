/* global document,window,COORDS,SHAPE */

import google from 'google'
import zoomMap from './utils/zoomMap'

import'./utils/campusList'

var map

function initialize () {
  var mapCanvas = document.getElementById('map-district')

  var mapOptions = {
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  map = new google.maps.Map(mapCanvas, mapOptions)
  if (SHAPE.geometry) {
    map.data.addGeoJson(SHAPE)
  }
  map.data.addGeoJson(COORDS)

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
