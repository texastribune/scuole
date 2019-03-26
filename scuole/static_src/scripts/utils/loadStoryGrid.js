/* global BLANK_STORY_IMAGE */

import map from 'lodash.map';
import reqwest from 'reqwest';

const FEED_URL =
  'https://www.texastribune.org/api/stories/?format=json&limit=6&tag=subject-public-education';

function htmlify(data) {
  let content = '';

  content += `<div class="story-box-container">
                <a class="story-box" href="${data.url}">
                  <div class="story-box__media">
                    <img class="story-box__image" src="${data.lead_art.url ||
                      window.BLANK_STORY_IMAGE}" alt="Placeholder image">
                  </div>
                  <div class="story-box__body">
                    <h3 class="story-box__header">${data.headline}</h3>
                    <p class="story-box__prose">${data.short_summary}</p>
                  </div>
                </a>
              </div>`;

  return content;
}

function loadStories(destEl) {
  reqwest({
    url: FEED_URL,
    method: 'get',
    type: 'json',
    contentType: 'application/json',
    crossOrigin: true,
    success: res => {
      let output = map(res.results.slice(0, 6), results => {
        return htmlify(results);
      });

      destEl.innerHTML = output.join('');
    },
  });
}

let el = document.querySelector('#js-story-box');
if (el) loadStories(el);
