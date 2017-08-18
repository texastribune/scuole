import forEach from 'lodash/collection/each';
import findOne from 'lodash/collection/find';
import scrollMonitor from 'scrollmonitor';

import activeButtonClass from './activeButtonClass';

let metricNav = document.querySelector('#metrics-nav');

let metricSection = document.querySelector('#metrics-section');
let metricSectionWatcher = scrollMonitor.create(metricSection, {
  top: 60,
});

let metricJumpers = document.querySelectorAll('.js-metric-jumper');

forEach(metricJumpers, jumper => {
  jumper.addEventListener('click', function(e) {
    let activeEl = e.target;

    activeButtonClass(metricJumpers, activeEl, 'btn-link', 'btn-gray-ghost');

    let attr = activeEl.getAttribute('data-jumper');

    let el = document.querySelector('#' + attr);
    window.scrollTo(
      0,
      el.getBoundingClientRect().top + window.pageYOffset - 50
    );
  });
});

let metricJumperHeaders = document.querySelectorAll('.js-metrics-block');

forEach(metricJumperHeaders, header => {
  let monitor = scrollMonitor.create(header, 20);

  monitor.stateChange(() => {
    // if the section isn't in view at all, skip
    if (!monitor.isInViewport) return;

    if (monitor.isInViewport && monitor.isAboveViewport) {
      let el = findOne(
        metricJumpers,
        jumper => header.id === jumper.getAttribute('data-jumper')
      );
      activeButtonClass(metricJumpers, el, 'btn-link', 'btn-gray-ghost');
    }
  });
});
