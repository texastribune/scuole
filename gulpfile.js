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

gulp.task('favicon', function () {
  return gulp.src('./scuole/static_src/favicon.ico')
    .pipe(gulp.dest('./scuole/static'))
    .pipe($.size({title: 'favicon'}))
})

gulp.task('robots', function () {
  return gulp.src('./scuole/static_src/robots.txt')
    .pipe(gulp.dest('./scuole/static'))
    .pipe($.size({title: 'robots'}))
})

gulp.task('sitemap', function () {
  return gulp.src('./scuole/static_src/sitemap.xml')
    .pipe(gulp.dest('./scuole/static'))
    .pipe($.size({title: 'sitemap'}))
})

gulp.task('serve', ['styles', 'images', 'fonts', 'favicon'], function () {
  bs.init({
    logConnections: true,
    logPrefix: 'SCHOOLS',
    notify: false,
    open: false,
    proxy: 'localhost:8000',
    xip: true
  })

  gulp.watch('./scuole/static_src/scss/**/*.scss', ['styles'])
})

gulp.task('build', ['styles', 'images', 'fonts', 'favicon', 'robots', 'sitemap'])

gulp.task('default', ['build'])
