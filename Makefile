APP := scuole

local/db-fetch:
	aws s3 cp s3://backups.texastribune.org/schools/schools-pg.dump backups/pg.dump

local/db-restore:
	dropdb ${APP} --if-exists
	createdb ${APP}
	pg_restore --dbname ${APP} --no-privileges --no-owner backups/pg.dump

local/reset-db:
	dropdb ${APP} --if-exists
	createdb ${APP}
	psql -d ${APP} -c 'CREATE EXTENSION postgis;'
	pipenv run python manage.py migrate

data/create-superuser:
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell --plain

# Create state, region, and county models (w/ name, geographic coordinates, etc.)
data/bootstrap-areas:
	python manage.py bootstrapstates
	python manage.py bootstrapregions
	python manage.py bootstrapcounties

# Create district and campus models (w/ name, geographic coordinates, etc.)
data/bootstrap-entities:
	python manage.py bootstrapdistricts_v2 2021-2022
	python manage.py dedupedistrictslugs
	python manage.py bootstrapcampuses_v2 2021-2022
	python manage.py dedupecampusslugs

# Update AskTED information
data/update-directories:
	python manage.py updatedistrictdirectory
	python manage.py updatedistrictsuperintendents
	python manage.py updatecampusdirectory
	python manage.py updatecampusprincipals

# Load in the latest year's TAPR data with v2 script
data/latest-school:
	python manage.py loadtaprdata_v2 2021-2022

# Load in all past TAPR data
# python manage.py loadtaprdata 2022-2023 --bulk
	
data/all-schools:
	python manage.py loadtaprdata 2021-2022 --bulk
	python manage.py loadtaprdata 2020-2021 --bulk
	python manage.py loadtaprdata 2019-2020 --bulk
	python manage.py loadtaprdata 2018-2019 --bulk
	python manage.py loadtaprdata 2017-2018 --bulk
	python manage.py loadtaprdata 2016-2017 --bulk
	python manage.py loadtaprdata 2015-2016 --bulk
	python manage.py loadtaprdata 2014-2015 --bulk
	python manage.py loadtaprdata 2013-2014 --bulk
	python manage.py loadtaprdata 2012-2013 --bulk

# Add the latest cohort year here when you're adding new data
# Run the command for the latest year to update the explorer
data/all-cohorts:
	python manage.py loadallcohorts 1998
	python manage.py loadallcohorts 1999
	python manage.py loadallcohorts 2000
	python manage.py loadallcohorts 2001
	python manage.py loadallcohorts 2002
	python manage.py loadallcohorts 2003
	python manage.py loadallcohorts 2004
	python manage.py loadallcohorts 2005
	python manage.py loadallcohorts 2006
	python manage.py loadallcohorts 2007
	python manage.py loadallcohorts 2008
	python manage.py loadallcohorts 2009
	python manage.py loadallcohorts 2010
	python manage.py loadallcohorts 2011
	python manage.py loadallcohorts 2012

local/reset-db-bootstrap-areas: local/reset-db data/bootstrap-areas

local/reset-db-bootstrap-areas-entities: local/reset-db-bootstrap-areas data/bootstrap-entities

local/reset-db-bootstrap-areas-entities-directories: local/reset-db-bootstrap-areas-entities data/update-directories

local/reset-db-bootstrap-latest: local/reset-db-bootstrap-areas-entities-directories data/latest-school

local/reset-db-bootstrap-over-time: local/reset-db data/all-schools data/all-cohorts

local/cohorts: local/reset-db-bootstrap-areas data/all-cohorts

local/all: local/reset-db-bootstrap-areas data/bootstrap-edu data/all-schools data/all-cohorts

# If you have having a hard time getting `docker-entrypoint.sh` to run locally
# You can use this to rebuild the npm files and then run the python server
# Useful for when you're making js or css changes
local/npm_reset:
	npm run build
	python manage.py collectstatic --noinput
	python manage.py runserver

docker/pull:
	@echo "Getting a fresh copy of master..."
	git checkout master
	git pull

docker/build:
	@echo "Building app..."
	@docker build \
		--tag ${APP} \
		.

docker/interactive:
	@echo "Running interactive mode..."
	@docker run \
		--name ${APP}-interactive \
		--interactive \
		--tty \
		--rm \
		--volume=`pwd`/data:/usr/src/app/data \
		--entrypoint=/bin/bash \
		--env-file=env-docker \
		${APP}

docker/run:
	@echo "Running app..."
	-@docker stop ${APP} && docker rm -v ${APP}
	@docker run \
		--name ${APP} \
		--detach \
		--volume /usr/src/app/scuole/assets \
		--env-file=env-docker \
		${APP}

docker/run-debug:
	@echo "Running app in debug mode..."
	-@docker stop ${APP} && docker rm -v ${APP}
	@docker run \
		--name ${APP} \
		--detach \
		--link ${APP}-db:db \
		--env DJANGO_DEBUG="True" \
		--env DATABASE_URL="postgis://docker:docker@db/docker" \
		${APP}

docker/db-data:
	@echo "Attempting to create data volume (if needed)..."
	@docker create \
		--name ${APP}-db-data \
		--entrypoint /bin/echo \
		mdillon/postgis:9.4 "Data-only" 2>/dev/null || true

docker/db: docker/db-data
	@echo "Starting database container..."
	@docker start ${APP}-db 2>/dev/null || \
		docker run --detach \
		--env=POSTGRES_USER=docker \
		--env=POSTGRES_PASSWORD=docker \
		--volumes-from ${APP}-db-data \
		--publish 5432:5432 \
		--name ${APP}-db \
		mdillon/postgis:9.4

docker/pg-interactive:
	@echo "Starting interactive terminal to the database..."
	@docker run --interactive \
		--tty \
		 --rm \
		--link ${APP}-db:postgres \
		mdillon/postgis:9.4 \
		/bin/bash

docker/nginx-build:
	@echo "Building nginx container..."
	@docker build \
		--tag=${APP}-nginx \
		--file Dockerfile.nginx \
		.

docker/nginx: docker/nginx-build
	@echo "Running nginx container..."
	-@docker stop ${APP}-nginx && docker rm -v ${APP}-nginx
	@docker run \
		--detach \
		--name ${APP}-nginx \
		--volumes-from ${APP} \
		--link ${APP}:web \
		--publish 80:80 \
		${APP}-nginx

docker/shell:
	docker exec -ti scuole_web_1 /bin/sh

# Build app and its services, run the app, and load the app on a web server
docker/kickstart: docker/build docker/run docker/nginx

# For when containers from previous builds are lingering/take up space
free-space:
	-docker system prune -f

# Fire up Docker locally
compose/local:
	docker-compose -f docker-compose.local.yml build web proxy
	docker-compose -f docker-compose.local.yml down
	docker-compose -f docker-compose.local.yml up

# What we use to deploy scuole changes to the production server
# define services that make up the app with the docker-compose.yml file, and build them
# `down` stops and removes previously started containers
# `up -d` starts containers in the background with the defined services and leaves them running
compose/production-deploy:
	make free-space
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build web proxy
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# What we use to deploy scuole changes to the test server
compose/test-deploy:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml build web proxy
	docker-compose -f docker-compose.yml -f docker-compose.override.yml down
	docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d

compose/admin-update-askted:
	docker-compose -f docker-compose.yml -f docker-compose.admin.yml run --rm asktedupdate

# Run this to create an image and get into the docker container
# Runs as an ash shell (what Alpine Linux uses, which is the Docker image base, basically the same as bash)
compose/container:
	docker-compose -f docker-compose.yml run --entrypoint ash web
