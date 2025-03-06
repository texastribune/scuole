#!/bin/sh

#3/6/25 RR replicated this in Makefile as "bootstrap/data". Can hopefully get rid of this file.

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
