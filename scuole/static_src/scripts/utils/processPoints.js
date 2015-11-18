import google from 'google'

function processPoints (geometry, callback, thisArg) {
  if (geometry instanceof google.maps.LatLng) {
    callback.call(thisArg, geometry)
  } else if (geometry instanceof google.maps.Data.Point) {
    callback.call(thisArg, geometry.get())
  } else {
    geometry.getArray().forEach(function (g) {
      processPoints(g, callback, thisArg)
    })
  }
}

module.exports = processPoints
