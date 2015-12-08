import classie from 'desandro-classie'
import scrollMonitor from 'scrollmonitor'

let reminderBar = document.querySelector('#js-reminder-bar')
let reminderBarTrigger = document.querySelector('#js-reminder-bar-trigger')

let monitor = scrollMonitor.create(reminderBarTrigger)

monitor.enterViewport(() => {
  classie.remove(reminderBar, 'reminder-bar--appear')
})

monitor.exitViewport(() => {
  classie.add(reminderBar, 'reminder-bar--appear')
})

if (!monitor.isInViewport) {
  classie.add(reminderBar, 'reminder-bar--appear')
}
