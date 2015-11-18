import forEach from 'lodash/collection/each'

module.exports = (elementList, activeElement, activeClass, inactiveClass) => {
  forEach(elementList, function (el) {
    if (el === activeElement) {
      el.classList.remove(inactiveClass)
      el.classList.add(activeClass)
    } else {
      el.classList.remove(activeClass)
      el.classList.add(inactiveClass)
    }
  })
}
