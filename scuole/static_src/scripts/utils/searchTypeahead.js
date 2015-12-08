import classie from 'desandro-classie'
import debounce from 'lodash/function/debounce'
import forEach from 'lodash/collection/each'
import reqwest from 'reqwest'

const DEBOUNCE_FOR = 350 // in milliseconds
const QUERY_URL = '/lookup/'

class Typeahead {
  constructor (input) {
    this.input = document.querySelector(input)
    this.index = -1

    // create a container for typeahead, put input inside of it
    this.container = document.createElement('div')
    classie.add(this.container, 'typeahead')
    this.input.parentNode.insertBefore(this.container, this.input)
    this.container.appendChild(this.input)

    // create <ul> for options, add to typeahead container
    this.ul = document.createElement('ul')

    classie.add(this.ul, 'listbox')
    classie.add(this.ul, 'listbox--hidden')
    this.container.appendChild(this.ul)

    // events
    this.input.addEventListener('input', debounce((event) => this.respondToInput(event), DEBOUNCE_FOR))
    this.input.addEventListener('blur', (event) => this.close(event))
    this.input.addEventListener('keydown', (event) => this.keyEvents(event))

    // do not let blur event fire if someone is clicking
    this.ul.addEventListener('mousedown', (event) => {
      event.preventDefault()
    })

    document.addEventListener('touchend', (event) => {
      if (event.target !== this.container && !this.container.contains(event.target)) {
        this.close()
        document.activeElement.blur()
      }
    })
  }

  isValidLength () {
    let valueLength = this.input.value.length

    if (valueLength > 0 && valueLength >= 2) {
      return true
    } else {
      return false
    }
  }

  respondToInput () {
    if (!this.isValidLength()) return this.close()

    reqwest({
      url: QUERY_URL,
      method: 'get',
      data: {q: this.input.value},
      success: (response) => this.addData(response)
    })
  }

  addData (data) {
    if (data.results.length === 0) return this.close()

    this.index = -1
    this.ul.innerHTML = ''
    let fragment = document.createDocumentFragment()

    forEach(data.results, (item) => {
      let li = document.createElement('li')
      let html = `<a class="listbox__link" href="${item.url}">
                    <p class="listbox__label">${item.type}</p>
                    <p class="listbox__title">${item.name}</p>
                  </a>`
      li.innerHTML = html

      fragment.appendChild(li)
    })

    this.ul.appendChild(fragment)
    this.open()
    this.goto(0)
  }

  open () {
    classie.remove(this.ul, 'listbox--hidden')
  }

  close () {
    classie.add(this.ul, 'listbox--hidden')
    this.index = -1
  }

  move (direction) {
    let liCount = this.ul.children.length

    if (direction === 'up') {
      // if it's above zero, go back one more, otherwise stay here
      let i = this.index > 0 ? this.index - 1 : this.index
      this.goto(i)
    }

    if (direction === 'down') {
      // if we haven't gone further than the <li> length, go down one, otherwise stay here
      let i = this.index < liCount - 1 ? this.index + 1 : this.index
      this.goto(i)
    }
  }

  goto (i) {
    let lis = this.ul.children

    if (this.index > -1) {
      classie.remove(lis[this.index], 'listbox--selected')
    }

    if (i > -1 && lis.length > 0) {
      let li = lis[i]
      classie.add(li, 'listbox--selected')
      li.scrollIntoView(false)

      this.index = i
    }
  }

  select () {
    if (this.index < 0) return

    let li = this.ul.children[this.index]
    li.querySelector('a').click()
  }

  keyEvents (event) {
    let key = event.keyCode || event.which

    if (key === 13) { // enter
      event.preventDefault()
      this.select()
    } else if (key === 27) { // esc
      this.close()
    } else if (key === 38) { // up
      event.preventDefault()
      this.move('up')
    } else if (key === 40) { // down
      event.preventDefault()
      this.move('down')
    }
  }
}

let typeahead = new Typeahead('#search')
