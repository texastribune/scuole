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

# Let Django know we're using production settings
ENV DJANGO_SETTINGS_MODULE config.settings.production
ENV SECRET_KEY quux

# Expose the port for Docker
EXPOSE 8000

# Production runs gunicorn served on port 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
