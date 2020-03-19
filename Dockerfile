FROM node:10 as assets

# Create the folder to work in
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy over package.json and gang
COPY package.json /usr/src/app
COPY package-lock.json /usr/src/app

# Install dependencies
RUN npm ci

# Bring over the rest of the app
COPY tasks /usr/src/app/tasks
COPY scuole/static_src /usr/src/app/scuole/static_src

# Run build command
RUN ["npm", "run", "build"]

FROM python:3.7-alpine

# Install the geo libs needed to interact with GeoDjango
RUN apk update && \
  apk upgrade && \
  apk add --no-cache \
  --repository http://dl-3.alpinelinux.org/alpine/edge/main/ \
  --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
  gcc \
  gdal \
  geos \
  make \
  musl-dev \
  proj \
  postgresql-dev \
  && rm -rf /var/cache/apk/*

# Symlink for the geo libraries
RUN ln -s /usr/lib/libgeos_c.so.1 /usr/local/lib/libgeos_c.so \
  && ln -s /usr/lib/libgdal.so.20 /usr/lib/libgdal.so

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Create the folder to work in
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Grab requirements and install
# COPY Pipfile Pipfile.lock /usr/src/app/
# RUN pipenv install --system --verbose --deploy
COPY requirements /usr/src/app/requirements/
RUN pip install -r requirements/base.txt

# Bring over the rest of the app
COPY . /usr/src/app

# Bring over the assets
COPY --from=assets /usr/src/app/scuole/static /usr/src/app/scuole/static

# Let Django know we're using production settings
ENV DJANGO_SETTINGS_MODULE config.settings.production
ENV SECRET_KEY quux

# Expose the port for Docker
EXPOSE 8000

# Production runs gunicorn served on port 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
