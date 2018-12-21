import google from 'google';
import processPoints from './processPoints';

export default map => {
  let bounds = new google.maps.LatLngBounds();
  map.data.forEach(function(feature) {
    if (feature.getGeometry()) {
      processPoints(feature.getGeometry(), bounds.extend, bounds);
    }
  });

  map.fitBounds(bounds);
};
