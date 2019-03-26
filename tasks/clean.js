// packages
const fs = require('fs-extra');

// local
const paths = require('./paths');

module.exports = async () => {
  await Promise.all([paths.staticDist].map(p => fs.remove(p)));
};
