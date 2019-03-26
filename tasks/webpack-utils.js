// native
const path = require('path');

// packages
const CaseSensitivePathsPlugin = require('case-sensitive-paths-webpack-plugin');
const glob = require('fast-glob');
const webpack = require('webpack');

// internal
const paths = require('./paths');
const { nodeEnv } = require('./env');

// configuration
const jsRegex = /\.(mjs|js|jsx)$/;
const jsRegexDependencies = /\.(mjs|js)$/;
const jsxPragma = 'h';

const getEntryPacks = () => {
  const entryPacks = glob.sync('*.(js|jsx)', {
    absolute: true,
    cwd: paths.staticSrcScriptPacks,
  });

  const packs = entryPacks.reduce((acc, curr) => {
    const { name } = path.parse(curr.toString());
    acc[name] = [curr];

    return acc;
  }, {});

  return packs;
};

const presetEnvOptions = {
  modules: false,
  exclude: ['transform-regenerator', 'transform-async-to-generator'],
  ignoreBrowserslistConfig: true,
  targets: { ie: '11' },
  useBuiltIns: false,
};

const configureBabelLoader = () => {
  return {
    test: jsRegex,
    include: paths.staticSrcScripts,
    loader: 'babel-loader',
    options: {
      presets: [['@babel/preset-env', presetEnvOptions]],
      plugins: [
        '@babel/plugin-syntax-dynamic-import',
        '@babel/plugin-proposal-class-properties',
        ['@babel/plugin-transform-react-jsx', { pragma: jsxPragma }],
        [
          '@babel/plugin-transform-runtime',
          {
            corejs: false,
            helpers: true,
            regenerator: false,
            useESModules: true,
          },
        ],
      ],
      cacheDirectory: true,
    },
  };
};

const configureBabelDependenciesLoader = () => {
  return {
    test: jsRegexDependencies,
    exclude: /@babel(?:\/|\\{1,2})runtime/,
    loader: 'babel-loader',
    options: {
      sourceType: 'unambiguous',
      presets: [['@babel/preset-env', presetEnvOptions]],
      plugins: [
        '@babel/plugin-syntax-dynamic-import',
        [
          '@babel/plugin-transform-runtime',
          {
            corejs: false,
            helpers: true,
            regenerator: false,
            useESModules: true,
          },
        ],
      ],
    },
  };
};

const generateBaseConfig = () => {
  return {
    entry: { ...getEntryPacks() },
    resolve: {
      extensions: ['.wasm', '.mjs', '.js', '.json'],
    },
    module: {
      strictExportPresence: true,
      rules: [
        { parser: { requireEnsure: false } },
        {
          oneOf: [configureBabelLoader(), configureBabelDependenciesLoader()],
        },
      ],
    },
    plugins: [
      new webpack.DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify(nodeEnv),
      }),
      new CaseSensitivePathsPlugin(),
    ],
    node: {
      __dirname: false,
      __filename: false,
      Buffer: false,
      console: false,
      fs: 'empty',
      net: 'empty',
      process: false,
      setImmediate: false,
      tls: 'empty',
    },
  };
};

module.exports = { generateBaseConfig };
