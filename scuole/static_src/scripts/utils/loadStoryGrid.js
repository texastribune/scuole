import map from 'lodash/collection/map'
import reqwest from 'reqwest'

const FEED_URL = 'http://rsstojson.texastribune.org/public-education'

function htmlify (data) {
  return `<div class="story-box-container">
          <a class="story-box" href="${data.url}">
            <div class="story-box__media">
              <img class="story-box__image" src="${data.leadArt}" alt="Placeholder image">
            </div>
            <div class="story-box__body">
              <h3 class="story-box__header">${data.title}</h3>
              <p class="story-box__prose">${data.description}</p>
            </div>
          </a>
        </div>`
}

function loadStories (destEl) {
  reqwest({
    url: FEED_URL,
    method: 'get',
    type: 'json',
    contentType: 'application/json',
    crossOrigin: true,
    success: (res) => {
      let output = map(res.data.slice(0, 6), (entry) => {
        return htmlify(entry)
      })

      destEl.innerHTML = output.join('')
    }
  })
}

let el = document.querySelector('#js-story-box')
if (el) loadStories(el)
