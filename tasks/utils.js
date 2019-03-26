// native
const path = require('path');

/**
 * List of image file extensions for use in tasks.
 *
 * @type {String[]}
 */
const validImageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg'];

/**
 * Helper to swap out a file path's extension.
 *
 * @param {String} npath
 * @param {String} ext
 * @returns {String}
 */
const replaceExtension = (npath, ext) => {
  if (typeof npath !== 'string') {
    return npath;
  }

  if (npath.length === 0) {
    return npath;
  }

  const newFileName = path.basename(npath, path.extname(npath)) + ext;
  return path.join(path.dirname(npath), newFileName);
};

/**
 * Helper to run a collection of Promise-returning functions in parallel.
 *
 * @param {Array<Function>} fns
 * @returns {Function}
 */
const parallel = fns => () => Promise.all(fns.map(fn => fn()));

/**
 * Helper to run a series of Promise-returning functions in a series.
 *
 * @param {Array<Function>} fns
 * @returns {Function}
 */
const series = fns => async () => {
  for (const fn of fns) {
    await fn();
  }
};

module.exports = { parallel, replaceExtension, series, validImageExtensions };
