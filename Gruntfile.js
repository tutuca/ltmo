var webpack = require('webpack');

module.exports = function (grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        lib: './node_modules',
        src: './assets',
        out: './static',
        module: {
          loaders: [
            {
              test: /\.(js$|jsx)$/,
              exclude: /node_modules/,
              loader: 'babel',
              query: {
                presets: ['es2015']
              }
            }
          ]
        },
        sass: {
            options: {
                includePaths: [
                    '<%= lib%>/bootstrap-sass/assets/stylesheets',
                    '<%= lib%>/font-awesome/scss/',
                ]
            },
            dist: {
                options: {
                    outputStyle: 'compact'
                },
                files: {
                    '<%= out%>/css/style.css': '<%= src%>/sass/style.scss'
                }
            }
        },
        copy: {
            main: {
                files: [
                   {
                      flatten: true,
                      cwd: '<%= lib%>/font-awesome/fonts/',
                      src: ['*.ttf', '*.eot', '*.svg', '*.woff', '*.woff2'],
                      dest: '<%= out%>/fonts/',
                      expand: true
                    },
                    {
                      flatten: true,
                      cwd: '<%= src%>/img/',
                      src: ['*.png', '*.jpg', '*.gif'],
                      dest: '<%= out%>/img/',
                      expand: true
                    },
                    {
                      flatten: true,
                      cwd: '<%= lib%>/bootstrap-sass/assets/fonts/bootstrap',
                      src: ['*.ttf', '*.eot', '*.svg', '*.woff', '*.woff2'],
                      dest: '<%= out%>/fonts/bootstrap/',
                      expand: true
                    },
                ]
            }
        },
        webpack: {
            main: {
                entry: {
                    main: "<%= src%>/js/ltmo.js"
                },
                output: {
                    path: "<%= out%>/js",
                    filename: "ltmo.js",
                },
                devtool: 'source-map',
                watch: true,
                module: '<%= module%>'
            },
            prod: {
                entry: {
                    main: "<%= src%>/js/ltmo.js"
                },
                output: {
                    path: "<%= out%>/js",
                    filename: "ltmo.min.js",
                },
                module: '<%= module%>',
                devtool: 'source-map',
                plugins: [
                    new webpack.optimize.UglifyJsPlugin(),
                ]
            }
        },
        watch: {
            scss: {
                files: [
                    '<%= src%>/sass/*.scss'
                ],
                tasks: ['sass']
            },
            config: {
                files: [
                    'Gruntfile.js',
                    'bower.json',
                    'package.json'
                ],
                tasks: ['dev-build']
            }
        }
    });
    // Plugin loading
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-webpack');
    // Task definition
    grunt.registerTask('build', ['webpack:main', 'webpack:prod', 'copy', 'sass']);
    grunt.registerTask('dev-build', ['webpack:main', 'copy', 'sass', 'watch']);
    grunt.registerTask('default', ['dev-build']);
};