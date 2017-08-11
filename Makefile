APP := scuole

local/reset-db:
	dropdb ${APP} --if-exists
	createdb ${APP}
	psql -d ${APP} -c 'CREATE EXTENSION postgis;'
	python manage.py migrate

data/bootstrap:
	python manage.py bootstrapstates
	python manage.py bootstrapregions
	python manage.py bootstrapcounties
	python manage.py bootstrapdistricts 2015-2016
	python manage.py bootstrapcampuses 2015-2016

data/base: data/bootstrap
	python manage.py loadtaprdata 2015-2016 --bulk

data/base-all: data/bootstrap
	python manage.py loadtaprdata 2015-2016 --bulk
	python manage.py loadtaprdata 2014-2015 --bulk
	python manage.py loadtaprdata 2013-2014 --bulk
	python manage.py loadtaprdata 2012-2013 --bulk

local/reset-db-and-bootstrap: local/reset-db data/base

local/reset-db-and-bootstrap-over-time: local/reset-db data/base-all

local/cohorts: local/reset-db
	python manage.py bootstrapstates
	python manage.py bootstrapregions
	python manage.py bootstrapcounties
	python manage.py loadallcohorts 2006
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell --plain

docker/pull:
	@echo "Getting a fresh copy of master..."
	git checkout master
	git pull

docker/build:
	@echo "Building app..."
	@docker build \
		--tag ${APP} \
		.

docker/build-static:
	@echo "Building static assets compiler..."
	@docker build \
		--tag ${APP}-assets \
		--file Dockerfile.assets \
		.

docker/interactive:
	@echo "Running interactive mode..."
	@docker run \
		--name ${APP}-interactive \
		--interactive \
		--tty \
		--rm \
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
		--volumes-from ${APP}-assets \
		--env-file=env-docker \
		${APP}

docker/run-debug:
	@echo "Running app in debug mode..."
	-@docker stop ${APP} && docker rm -v ${APP}
	@docker run \
		--name ${APP} \
		--detach \
		--link ${APP}-db:db \
		--volume /usr/src/app/scuole/assets \
		--volumes-from ${APP}-assets \
		--env DJANGO_DEBUG="True" \
		--env DATABASE_URL="postgis://docker:docker@db/docker" \
		${APP}

docker/static-compile: docker/build-static
	@echo "Compiling static assets..."
	-@docker stop ${APP}-assets && docker rm -v ${APP}-assets
	@docker run \
		--name ${APP}-assets \
		--tty \
		--volume /usr/src/app/scuole/static \
		${APP}-assets

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

docker/kickstart: docker/pull docker/build docker/static-compile docker/run docker/nginx
