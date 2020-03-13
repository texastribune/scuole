# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Added
### Changed
### Removed
### Fixed

## [1.1.0] - 2020-03-13
### Changed
- `Makefile` - switch data loading commands to 2018-2019
- `README.md` - add more documentation 
- `loadtaprdata_v2.py` - add print statments, change functions to handle discrepancies in ID's (sometimes ID's are normalized to ints and don't have the prefixed zeros), adjust for
new codes in accountability ratings, remove 2017-2018 condition for campuses (they now 
also have accountability ratings)
- `reference.py` - add more choices to account for new ratings in 2018-2019
