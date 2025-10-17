import map from 'lodash.map';
import reqwest from 'reqwest';

const FEED_URL = 'https://www.texastribune.org/wp-json/wp/v2/posts?categories=21&per_page=6&orderby=date&order=desc';

function htmlify(data) {
  let content = '';

  // Strip HTML tags from excerpt
  const excerpt = data.excerpt.rendered.replace(/<[^>]*>/g, '').trim();

  content += `<div class="story-box-container">
                <a class="story-box" href="${data.link}">
                  <div class="story-box__media">
                    <img class="story-box__image" src="${data.jetpack_featured_media_url || window.BLANK_STORY_IMAGE}" alt="Placeholder image">
                  </div>
                  <div class="story-box__body">
                    <h3 class="story-box__header">${data.title.rendered}</h3>
                    <p class="story-box__prose">${excerpt}</p>
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
      let output = map(res.slice(0, 6), results => {
        return htmlify(results);
      });

      destEl.innerHTML = output.join('');
    },
  });
}

let el = document.querySelector('#js-story-box');
if (el) loadStories(el);