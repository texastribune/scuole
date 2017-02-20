FROM texastribune/python-node-gis-alpine

# Create the folder to work in
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Grab the requirements folder, then install production
COPY requirements /usr/src/app/requirements
RUN pip install --no-cache-dir -r requirements/production.txt

# Bring over the package.json for dependencies, then install
COPY package.json /usr/src/app/
RUN npm install && npm cache clean

# Bring over the rest of the app
COPY . /usr/src/app

# Compile assets
RUN npm run build && rm -rf node_modules

# Collect static
RUN DJANGO_SETTINGS_MODULE=config.settings.production \
    SECRET_KEY=quux \
    DISABLE_SENTRY=True \
      python manage.py collectstatic --no-input

# Production runs gunicorn served on port 8000
ENTRYPOINT ["./docker-entrypoint.sh"]
