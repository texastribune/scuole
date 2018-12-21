const path = require('path');
const webpack = require('webpack');

const CaseSensitivePathsPlugin = require('case-sensitive-paths-webpack-plugin');

module.exports = {
  context: path.join(__dirname, 'scuole/static_src/scripts'),
  entry: {
    // about: './about.js',
    campus: './campus.js',
    cohorts: './cohorts.js',
    cohortsLanding: './cohorts-landing.js',
    district: './district.js',
    state: './state.js',
    commons: [
      './utils/loadStoryGrid.js',
      './utils/adLoader.js',
      './utils/searchTypeahead.js',
    ],
  },
  output: {
    path: path.join(__dirname, '/scuole/static/scripts'),
    filename: '[name].js',
    chunkFilename: '[id].chunk.js',
  },
  module: {
    strictExportPresence: true,
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: [['es2015', { modules: false }]],
          plugins: [
            'syntax-dynamic-import',
            [
              'transform-es2015-classes',
              {
                loose: true,
              },
            ],
            ['transform-react-jsx', { pragma: 'h' }],
            ['transform-object-rest-spread', { useBuiltIns: true }],
          ],
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.json', '.jsx'],
  },
  plugins: [
    new CaseSensitivePathsPlugin(),
    new webpack.optimize.ModuleConcatenationPlugin(),
    new webpack.optimize.CommonsChunkPlugin({
      name: 'commons',
      minChunks: 2,
    }),
  ],
  node: {
    fs: 'empty',
    net: 'empty',
    tls: 'empty',
    setImmediate: false,
  },
};
