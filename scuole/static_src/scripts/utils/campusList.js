import classie from 'desandro-classie'
import forEach from 'lodash/collection/each'

let campusGroups = document.querySelectorAll('.js-campus-list-group')

forEach(campusGroups, (group) => {
  let campusItems = group.querySelectorAll('.campus-list-item')
  let button = group.querySelector('button')

  if (!button) return

  button.addEventListener('click', (e) => {
    let buttonText = button.textContent
    button.textContent = buttonText === '+ More' ? '- Less' : '+ More'

    forEach(campusItems, (item) => {
      classie.toggle(item, 'campus-list-item--display')
    })
  })
})
