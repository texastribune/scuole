/* global scrollMonitor */

'use strict';

// I want forEach, rawr
var forEach = Function.prototype.call.bind(Array.prototype.forEach);

function applyActiveButtonClass (elementList, activeElement, activeClass, inactiveClass) {
  forEach(elementList, function (el) {
    if (el === activeElement) {
      el.classList.remove(inactiveClass);
      el.classList.add(activeClass);
    } else {
      el.classList.remove(activeClass);
      el.classList.add(inactiveClass);
    }
  });
}

var metricNav = document.querySelector('#metrics-nav');

var metricNavWatcher = scrollMonitor.create(metricNav, 20);
metricNavWatcher.lock();

metricNavWatcher.stateChange(function () {
  console.log('fired');
  if (this.isAboveViewport) {
    metricNav.classList.add('attach-to-top');
  } else {
    metricNav.classList.remove('attach-to-top');
  }
});

var metricJumpers = Array.prototype.slice.call(document.querySelectorAll('.js-metric-jumper'));

forEach(metricJumpers, function (jumper) {
  jumper.addEventListener('click', function (e) {
    var activeEl = e.target;

    applyActiveButtonClass(metricJumpers, activeEl, 'btn-dark', 'btn-gray-ghost');

    var attr = activeEl.getAttribute('data-jumper');

    var el = document.querySelector('#' + attr);
    window.scrollTo(0, el.getBoundingClientRect().top + window.pageYOffset - 10);
  });
});
