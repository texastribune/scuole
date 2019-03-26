// packages
const colors = require('ansi-colors');
const fs = require('fs-extra');

// local
const paths = require('./paths');

module.exports = async () => {
  // fonts
  await fs.copy(paths.staticSrcFonts, paths.staticDistFonts, {
    dereference: true,
  });

  // favicon
  await fs.copy(paths.staticSrcFavicon, paths.staticDistFavicon, {
    dereference: true,
  });

  // robots.txt
  await fs.copy(paths.staticSrcRobots, paths.staticDistRobots, {
    dereference: true,
  });

  // sitemap.xml
  await fs.copy(paths.staticSrcSitemap, paths.staticDistSitemap, {
    dereference: true,
  });
};
