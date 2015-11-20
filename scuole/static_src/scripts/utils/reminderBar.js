import scrollMonitor from 'scrollmonitor'

let reminderBar = document.querySelector('#js-reminder-bar')
let reminderBarTrigger = document.querySelector('#js-reminder-bar-trigger')

let monitor = scrollMonitor.create(reminderBarTrigger)

monitor.enterViewport(() => {
  reminderBar.classList.remove('reminder-bar--appear')
})

monitor.exitViewport(() => {
  reminderBar.classList.add('reminder-bar--appear')
})

if (!monitor.isInViewport) {
  reminderBar.classList.add('reminder-bar--appear')
}
