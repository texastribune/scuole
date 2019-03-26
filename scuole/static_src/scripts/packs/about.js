import '../utils/loadStoryGrid';
import '../utils/adLoader';
import '../utils/searchTypeahead';

import scrollMonitor from 'scrollmonitor';

const aboutMenu = document.querySelector('#about-menu');
const aboutMenuMonitor = scrollMonitor.create(aboutMenu);

aboutMenuMonitor.lock();

aboutMenuMonitor.exitViewport(function() {
  aboutMenu.classList.remove('attach-to-top');
});

aboutMenuMonitor.enterViewport(function() {
  aboutMenu.classList.add('attach-to-top');
});
