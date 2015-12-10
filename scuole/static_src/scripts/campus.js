/* global COORDS */

import google from 'google'

import './utils/metricNavs'
import './utils/reminderBar'

function initialize () {
  var mapCanvas = document.getElementById('map-campus')
  var latlng = new google.maps.LatLng(COORDS.coordinates[1], COORDS.coordinates[0])

  var mapOptions = {
    center: latlng,
    zoom: 14,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    draggable: false,
    scrollwheel: false
  }

  var map = new google.maps.Map(mapCanvas, mapOptions)

  new google.maps.Marker({
    map: map,
    animation: google.maps.Animation.DROP,
    position: latlng
  })

  mapCanvas.addEventListener('click', () => {
    map.setOptions({
      draggable: true,
      scrollwheel: true
    })
  })
}

google.maps.event.addDomListener(window, 'load', initialize)
