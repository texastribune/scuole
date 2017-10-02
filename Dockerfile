FROM node:8 AS asset-build-deps

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
COPY package.json yarn.lock /usr/src/app/
RUN yarn && yarn cache clean
COPY . /usr/src/app
RUN yarn build

FROM python:3.5

# Install the geo libs needed to interact with GeoDjango
RUN apt-get update && apt-get install -y --no-install-recommends \
  binutils \
  libproj-dev \
  gdal-bin \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Create the folder to work in
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Grab the requirements folder, then install production
COPY requirements /usr/src/app/requirements
RUN pip install --no-cache-dir -r requirements/production.txt

# Bring over the rest of the app
COPY . /usr/src/app
COPY --from=asset-build-deps /usr/src/app/scuole/static /usr/src/app/scuole/static

# Let Django know we're using production settings
ENV DJANGO_SETTINGS_MODULE config.settings.production
ENV SECRET_KEY quux

# Expose the port for Docker
EXPOSE 8000

# Production runs gunicorn served on port 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
