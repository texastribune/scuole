#!/bin/sh

# Refer to Makefile for these commands
# create state, region, and county models
make data/bootstrap-areas

# create district and campus models
make data/bootstrap-entities

# initial AskTED update on directory
make data/update-directories

# add cohorts data
make data/all-cohorts

# add latest year's TAPR data
make data/latest-school
