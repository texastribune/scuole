'use strict';

// var bumper = document.getElementById('js-bumper');
// var bumperCheck = document.getElementById('js-bumper-check');
//
// window.addEventListener('scroll', function() {
//   var pageYOffset = window.pageYOffset;
//   var elementTop = bumperCheck.getBoundingClientRect().top + pageYOffset;
//
//   if (elementTop < pageYOffset) {
//     bumper.classList.add('sticky');
//   } else {
//     bumper.classList.remove('sticky');
//   }
// });

var metricsButtons = document.querySelectorAll('.metrics-jumper__item');
var metricsHeaders = document.querySelectorAll('.js-metrics-header');

for (var i = 0, il = metricsHeaders.length; i < il; i++) {
  console.log(metricsHeaders[i]);
}
