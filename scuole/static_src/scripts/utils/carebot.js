/* global ga */

import CarebotTracker from 'carebot-tracker';

var tracker = new CarebotTracker.ScrollTracker('main', (percent, seconds) => {
  var eventData = {
    hitType: 'event',
    eventCategory: window.location.pathname,
    eventAction: 'scroll-depth',
    eventLabel: percent,
    eventValue: seconds,
  };

  ga('send', eventData);
});
