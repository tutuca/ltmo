module.exports = function(grunt) {
    'use strict';
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-browserify'); 
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        browserify: {
            all: {
                src: ['cloth/js/main.js'],
                dest: 'static/js/app.js'
            }
        },
        uglify: {
            all: {
                options: {
                    sourceMap: true
                },
                files: {
                    'static/js/app.min.js': ['static/js/app.js']
                }
            }
        },
        sass: {
            options: {
                includePaths: ['cloth/sass'],
                sourceComments: 'none'
            },
            dist: {
                options: {
                    outputStyle: 'expanded'
                },
                files: {
                    'static/css/styles.css': 'cloth/sass/styles.scss'
                }
            }
        },
        watch: {
            js: {
                files: ['cloth/js/*.js', 'cloth/js/**/*.js'],
                tasks: ['browserify', 'uglify']
            },
            sass: {
                files: ['cloth/scss/*.scss',
                        'cloth/scss/**/*.scss'],
                tasks: ['sass:dist  ']
            }
        }
    });

    grunt.registerTask('build', ['sass', 'browserify', 'uglify']);
    grunt.registerTask('default', ['build','watch']);
};
