import forEach from 'lodash/collection/each'
import findOne from 'lodash/collection/find'
import scrollMonitor from 'scrollMonitor'

import activeButtonClass from './utils/activeButtonClass'

let metricNav = document.querySelector('#metrics-nav')

let metricSection = document.querySelector('#metrics-section')
let metricSectionWatcher = scrollMonitor.create(metricSection, {
  top: 20
})

metricSectionWatcher.partiallyExitViewport(function () {
  if (this.isAboveViewport) {
    metricNav.classList.remove('attach-to-top')
    metricNav.classList.add('attach-to-bottom')
  }

  if (this.isBelowViewport) {
    metricNav.classList.remove('attach-to-top')
  }
})

metricSectionWatcher.enterViewport(function () {
  if (this.isAboveViewport) {
    metricNav.classList.remove('attach-to-top')
    metricNav.classList.add('attach-to-bottom')
  }
})

metricSectionWatcher.fullyEnterViewport(function () {
  metricNav.classList.remove('attach-to-bottom')
  metricNav.classList.add('attach-to-top')
})

let metricJumpers = document.querySelectorAll('.js-metric-jumper')

forEach(metricJumpers, (jumper) => {
  jumper.addEventListener('click', function (e) {
    let activeEl = e.target

    activeButtonClass(metricJumpers, activeEl, 'btn-dark', 'btn-gray-ghost')

    let attr = activeEl.getAttribute('data-jumper')

    let el = document.querySelector('#' + attr)
    window.scrollTo(0, el.getBoundingClientRect().top + window.pageYOffset - 10)
  })
})

let metricJumperHeaders = document.querySelectorAll('.js-metrics-block')

forEach(metricJumperHeaders, (header) => {
  let monitor = scrollMonitor.create(header, 20)

  monitor.stateChange(() => {
    // if the section isn't in view at all, skip
    if (!monitor.isInViewport) return

    if (monitor.isInViewport && monitor.isAboveViewport) {
      let el = findOne(metricJumpers, jumper => header.id === jumper.getAttribute('data-jumper'))
      activeButtonClass(metricJumpers, el, 'btn-dark', 'btn-gray-ghost')
    }
  })
})
