'use strict'

var gulp = require('gulp')
var $ = require('gulp-load-plugins')()

var autoprefixer = require('autoprefixer')
var bs = require('browser-sync').create()

gulp.task('styles', function () {
  return gulp.src('./scuole/static_src/scss/*.scss')
    .pipe($.sourcemaps.init())
    .pipe($.sass({
      includePaths: ['node_modules'],
      precision: 10
    }).on('error', $.sass.logError))
    .pipe($.postcss([
      autoprefixer({
        browsers: ['last 2 versions']
      })
    ]))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('./scuole/static/styles'))
    .pipe(bs.stream({
      match: '**/*.css'
    }))
    .pipe($.size({title: 'styles'}))
})

gulp.task('images', function () {
  return gulp.src('./scuole/static_src/images/**/*')
    .pipe($.imagemin({
      progressive: true,
      interlaced: true
    }))
    .pipe(gulp.dest('./scuole/static/images'))
    .pipe($.size({title: 'images'}))
})

gulp.task('fonts', function () {
  return gulp.src('./scuole/static_src/fonts/**/*')
    .pipe(gulp.dest('./scuole/static/fonts'))
    .pipe($.size({title: 'fonts'}))
})

gulp.task('serve', ['styles', 'images', 'fonts'], function () {
  bs.init({
    logConnections: true,
    logPrefix: 'SCHOOLS',
    notify: false,
    open: false,
    proxy: 'localhost:8000',
    tunnel: true,
    xip: true
  })

  gulp.watch('./scuole/static_src/scss/**/*.scss', ['styles'])
})

gulp.task('build', ['styles', 'images', 'fonts'])
