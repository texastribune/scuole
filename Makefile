APP := scuole

local/reset-db:
	dropdb ${APP} --if-exists
	createdb ${APP}
	psql -d ${APP} -c 'CREATE EXTENSION postgis;'
	python manage.py migrate

data/base:
	python manage.py bootstrapstates
	python manage.py bootstrapregions
	python manage.py bootstrapcounties
	python manage.py bootstrapdistricts
	python manage.py bootstrapcampuses
	python manage.py loadtaprdata 2014-2015

local/reset-db-and-bootstrap: local/reset-db data/base

docker/pull:
	@echo "Getting a fresh copy of master..."
	git checkout master
	git pull

docker/build:
	@echo "Building app..."
	@docker build \
		--tag ${APP} \
		.

docker/build-assets:
	@echo "Building asset compiler..."
	@docker build \
		--tag ${APP}-node \
		--file Dockerfile.assets \
		.

docker/run: docker/pull docker/build docker/static-compile
	@echo "Running app..."
	-@docker stop ${APP} && docker rm -v ${APP}
	@docker run \
		--name ${APP} \
		--detach \
		--volumes-from ${APP}-assets \
		--env-file=env-docker \
		${APP}

docker/run-debug: docker/build docker/static-compile
	@echo "Running app in debug mode..."
	@docker run \
		--name ${APP} \
		--detach \
		--publish 8000:8000 \
		--link ${APP}-db:db \
		--volumes-from ${APP}-assets \
		--env-file env-docker \
		--env DJANGO_DEBUG="True" \
		${APP}

docker/static-assets:
	@echo "Attempting to create static assets volume (if needed)..."
	@docker create \
		--name ${APP}-assets \
		--volume /usr/src/app/scuole/static \
		--entrypoint /bin/echo \
		${APP} "Data-only" 2>/dev/null || true

docker/static-compile: docker/build-assets docker/static-assets
	@echo "Compiling static assets..."
	@docker run \
		--interactive \
		--tty \
		--rm \
		--volumes-from ${APP}-assets \
		${APP}-node

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
