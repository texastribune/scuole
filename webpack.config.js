var path = require('path')
var webpack = require('webpack')

module.exports = {
  context: path.join(__dirname, 'scuole/static_src/scripts'),
  entry: {
    campus: './campus.js',
    district: './district.js',
    state: './state.js',
    commons: [
      './utils/loadStoryGrid.js',
      './utils/adLoader.js',
      './utils/searchTypeahead.js'
    ]
  },
  output: {
    path: path.join(__dirname, '/scuole/static/scripts'),
    filename: '[name].js',
    chunkFilename: '[id].chunk.js'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015']
        }
      }
    ]
  },
  resolve: {
    extensions: ['', '.js', '.json']
  },
  externals: {
    google: 'google'
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin({
      name: 'commons',
      minChunks: 2
    })
  ]
}
