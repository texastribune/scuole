// packages
const colors = require('ansi-colors');

// local
const { parallel, series } = require('./utils');

// tasks
const clean = require('./clean');
const copy = require('./copy');
const images = require('./images');
const scripts = require('./scripts');
const styles = require('./styles');

async function build() {
  const runner = series([clean, scripts, parallel([images, styles]), copy]);

  await runner();
}

build()
  .then(() => {
    console.log(colors.bold.green('The build was a success!'));
  })
  .catch(err => {
    console.log(colors.bold.red('Build failed.'));
    console.log(err);
  });
