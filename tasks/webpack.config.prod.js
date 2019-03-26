// native
const path = require('path');

// packages
const AssetsWebpackPlugin = require('assets-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const webpack = require('webpack');

// internal
const { generateBaseConfig } = require('./webpack-utils');
const paths = require('./paths');

const config = Object.assign({}, generateBaseConfig(), {
  mode: 'production',
  bail: true,
  devtool: 'source-map',
  output: {
    path: paths.staticDistScripts,
    publicPath: 'scripts',
    filename: '[name].[chunkhash:10].js',
  },
  optimization: {
    runtimeChunk: 'single',
    splitChunks: {
      chunks: 'all',
      name: false,
    },
    // switch the production minifier to Terser
    minimizer: [
      new TerserPlugin({
        cache: true,
        parallel: true,
        sourceMap: true,
        terserOptions: {
          output: { comments: false },
        },
      }),
    ],
  },
});

config.plugins.push(
  new webpack.HashedModuleIdsPlugin(),
  new AssetsWebpackPlugin({
    entrypoints: true,
    filename: 'manifest.json',
    prettyPrint: true,
    useCompilerPath: true,
  })
);

module.exports = [config];
