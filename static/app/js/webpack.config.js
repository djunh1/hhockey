module.exports = {
    entry: [
    './index.js'
    ],
    output: {
        filename: "index_bundle.js",
        path: __dirname + '/dist'
    },
    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader"}
        ]
    }
};