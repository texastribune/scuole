###############
# ASSET BUILD #
###############
# front-end files including CSS, javascript, images, etc.
FROM node:25 as assets

WORKDIR /usr/src/app

# Copy over package.json and gang
COPY package.json /usr/src/app
COPY package-lock.json /usr/src/app

# Install dependencies
RUN npm ci

# Copy over the rest of the front-end app
COPY tasks /usr/src/app/tasks
COPY scuole/static_src /usr/src/app/scuole/static_src

# Run build command
RUN ["npm", "run", "build"]

##############
# BASE IMAGE #
##############

FROM python:3.10-alpine
#FROM python:3.10.0-alpine3.14

##################################
# ARGS AND ENVIRONMENT VARIABLES #
##################################
# set default environment to local. To build for production (give it a human-readable name!):
# docker build --build-arg ENVIRONMENT=production -t myappname 
ARG ENVIRONMENT=local
ENV DJANGO_SETTINGS_MODULE=config.settings.${ENVIRONMENT}
ENV SECRET_KEY=quux


#####################################
# INSTALL DEPENDENCIES AND APP CODE #
#####################################

WORKDIR /usr/src/app

# Install system dependencies (including GeoDjango libs)
RUN apk update && \
  apk upgrade && \
  apk add --no-cache \
  gcc \
  gdal-dev \
  geos-dev \
  make \
  musl-dev \
  proj-dev \
  postgresql-dev \
  && rm -rf /var/cache/apk/*

# Add GeoDjango environment variables
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so
ENV GEOS_LIBRARY_PATH=/usr/lib/libgeos_c.so
ENV PROJ_LIBRARY_PATH=/usr/lib/libproj.so

# Symlink for the geo libraries
# RUN ln -s /usr/lib/libgeos_c.so.1 /usr/local/lib/libgeos_c.so \
#   && ln -s /usr/lib/libgdal.so.20 /usr/lib/libgdal.so

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Create the folder to work in
# RUN mkdir -p /usr/src/app
# WORKDIR /usr/src/app

# Grab requirements into Docker container
COPY requirements/base.txt requirements/base.txt
COPY requirements/local.txt requirements/local.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements/base.txt
RUN pip install --no-cache-dir -r requirements/local.txt

# Bring over the rest of the app
COPY . /usr/src/app

# Bring over the static assets from the first stage
COPY --from=assets /usr/src/app/scuole/static /usr/src/app/scuole/static

####################
# RUNTIME SETTINGS #
####################
# Expose the port for Docker
EXPOSE 8000

# Production runs gunicorn served on port 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
