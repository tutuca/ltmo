var webpack = require('webpack');
module.exports = {
    entry: [
      'webpack/hot/only-dev-server',
      "./cloth/app.js"
    ],
    output: {
        path: __dirname + '/static',
        filename: "app.js"
    },
    module: {
        loaders: [
            { test: /\.js?$/, loaders: ['react-hot', 'babel'], exclude: /node_modules/ },
            { test: /\.js$/, exclude: /node_modules/, loader: 'babel'},
        ]
    },
    plugins: [
      new webpack.NoErrorsPlugin()
    ],
    devServer: {
        contentBase: "./static",
        noInfo: true,
        hot: true,
        inline: true
    }
};