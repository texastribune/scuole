#!/bin/sh

# Refer to Makefile for these commands
# create the areas
make data/bootstrap-areas

# create the entities
make data/bootstrap-entities

# initial update on directory
make data/update-directories

# cohorts
make data/all-cohorts

# add latest year
make data/latest-school
