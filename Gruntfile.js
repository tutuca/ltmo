module.exports = function(grunt) {
  'use strict';
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      options: {
        includePaths: [
          './node_modules/bootstrap-sass/assets/stylesheets',
          './node_modules/font-awesome/scss/'
        ]
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          './static/css/style.css': './cloth/scss/style.scss'
        }        
      }
    },
    copy: {
      main: {
        files: [
          {
            flatten:true,
            cwd: './node_modules/font-awesome/fonts/',
            src: ['*.*'],
            dest: './static/fonts/',
            expand: true
          },
          {
            flatten:true,
            cwd: './cloth/img/',
            src: ['*.png', '*.jpg', '*.gif'],
            dest: './static/img/',
            expand: true
          },
        ]
      }
    },
    webpack: {
      main: {
        entry: {
          main: "./cloth/main.js",
        },
        output: {
            path: "./static/js",
            publicPath: "/static/js",
            filename: "main.js",

        },
        module: {
            loaders: [
                { test: /\.jsx?$/, exclude: /node_modules/, loader: "babel" }
            ]
        },
      },
    },
    watch: {
      scss: {
        files: [
         //watched files
          './cloth/*.scss',
          ],
        tasks: ['sass'],
      },
      js : {
        files: [
          './cloth/**/*.jsx',
          './cloth/**/*.js',
          './cloth/*.js',
        ],
        tasks: ['copy:main', 'webpack:main'],
      },
      config: {
        files: [
          'Gruntfile.js',
          'bower.json',
          'package.json'
        ],
        tasks: ['copy', 'sass', 'webpack'],
      }
    }
  });
  // Plugin loading
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-webpack');
  grunt.loadNpmTasks('grunt-sass');

  // Task definition
  grunt.registerTask('build', ['copy', 'sass', 'webpack']);
  grunt.registerTask('default', ['build', 'watch']);

};