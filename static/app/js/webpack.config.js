//require our dependencies
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    entry: [
    './index.js'
    ],
    output: {
        filename: "[name]-[hash].js",
        path: __dirname + '/dist'
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),

        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jquery': 'jquery'
            })
    ],
    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader",
                query: {
                    presets:['react']
                }
            }
        ]
    },
    resolve: {
        modulesDirectories: ['node_modules'],
        extensions: ['', '.js', '.jsx']
    }
};