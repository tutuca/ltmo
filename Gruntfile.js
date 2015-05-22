module.exports = function(grunt) {
  'use strict';
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      options: {
        includePaths: [
          './cloth/lib/bootstrap-sass-official/assets/stylesheets',
          './cloth/lib/font-awesome/scss/'
        ]
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          './static/css/style.css': './cloth/sass/style.scss'
        }        
      }
    },
    copy: {
      main: {
        files: [
          {
            flatten:true,
            cwd: './cloth/lib/font-awesome/fonts/',
            src: ['*.ttf', '*.eot', '*.svg', '*.woff'],
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
    concat: {
      options: {
        separator: ';',
      },
      lib: {
        src: [
          './cloth/lib/jquery/dist/jquery.js',
          './cloth/lib/bootstrap-sass-official/assets/javascripts/bootstrap/dropdown.js',
          './cloth/lib/bootstrap-sass-official/assets/javascripts/bootstrap/tab.js'
        ],
        dest: './static/js/lib.js'
      },
      main: {
        src: [
          'assets/js/scripts.js'
        ],
        dest: './static/js/main.js'
      },
    },
    uglify: {
      options: {
        mangle: true,
        sourceMap: true,
      },
      lib: {
        files: {
          './static/js/lib.min.js': './static/js/lib.js',
        }
      },
      main: {
        files: {
          './static/js/main.min.js': './static/js/main.js',
        }
      }
    },
    watch: {
      scss: {
        files: [
         //watched files
          'assets/scss/*.scss',
          ],
        tasks: ['sass'],
      },
      js : {
        files: [
          'assets/js/*.js',
        ],
        tasks: ['copy:main', 'concat:main'],
      },
      config: {
        files: [
          'Gruntfile.js',
          'bower.json',
          'package.json'
        ],
        tasks: ['copy', 'concat', 'sass'],
      }
    }
  });
  // Plugin loading
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');

  // Task definition
  grunt.registerTask('build', ['copy', 'sass', 'concat', 'uglify']);
  grunt.registerTask('default', ['build', 'watch']);

};