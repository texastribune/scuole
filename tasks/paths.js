// native
const path = require('path');

// packages
const fs = require('fs-extra');

const projectDirectory = fs.realpathSync(process.cwd());

function resolveProject(relativePath) {
  return path.resolve(projectDirectory, relativePath);
}

module.exports = {
  projectDirectory,
  staticDist: resolveProject('scuole/static'),
  staticDistFavicon: resolveProject('scuole/static/root/favicon.ico'),
  staticDistFonts: resolveProject('scuole/static/fonts'),
  staticDistImages: resolveProject('scuole/static/images'),
  staticDistRobots: resolveProject('scuole/static/root/robots.txt'),
  staticDistScripts: resolveProject('scuole/static/scripts'),
  staticDistSitemap: resolveProject('scuole/static/root/sitemap.xml'),
  staticDistStyles: resolveProject('scuole/static/styles'),
  staticSrc: resolveProject('scuole/static_src'),
  staticSrcFavicon: resolveProject('scuole/static_src/favicon.ico'),
  staticSrcFonts: resolveProject('scuole/static_src/fonts'),
  staticSrcImages: resolveProject('scuole/static_src/images'),
  staticSrcRobots: resolveProject('scuole/static_src/robots.txt'),
  staticSrcScripts: resolveProject('scuole/static_src/scripts'),
  staticSrcScriptPacks: resolveProject('scuole/static_src/scripts/packs'),
  staticSrcSitemap: resolveProject('scuole/static_src/sitemap.xml'),
  staticSrcStyles: resolveProject('scuole/static_src/styles'),
};
