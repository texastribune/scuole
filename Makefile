APP := scuole

# create a backup container in case we need to roll back 4/3/25
backup-containers:
	@echo "📦 Creating backup of current docker images..."
	@TIMESTAMP=$$(date +%Y%m%d_%H%M%S); \
	BACKUP_DIR=./docker-backups; \
	mkdir -p $$BACKUP_DIR; \
	docker save -o $$BACKUP_DIR/web-backup-$$TIMESTAMP.tar $$(docker-compose -f docker-compose.yml -f docker-compose.prod.yml images -q web); \
	docker save -o $$BACKUP_DIR/proxy-backup-$$TIMESTAMP.tar $$(docker-compose -f docker-compose.yml -f docker-compose.prod.yml images -q proxy); \
	echo "Backup saved to $$BACKUP_DIR with timestamp $$TIMESTAMP"

# clear up disk space by purging all backups 4/3/25
backup-purge:
	@echo "🧹 Cleaning up old container backups..."
	@BACKUP_DIR=~/docker-backups; \
	if [ -d "$$BACKUP_DIR" ]; then \
		echo "Removing all backup files older than 7 days..."; \
		find $$BACKUP_DIR -name "*.tar" -type f -mtime +7 -delete; \
		find $$BACKUP_DIR -name "*.yml.backup-*" -type f -mtime +7 -delete; \
		echo "Keeping a maximum of 3 most recent backups..."; \
		cd $$BACKUP_DIR && ls -t web-backup-*.tar | tail -n +4 | xargs -r rm; \
		cd $$BACKUP_DIR && ls -t proxy-backup-*.tar | tail -n +4 | xargs -r rm; \
		echo "Backup cleanup complete."; \
	else \
		echo "Backup directory not found. Nothing to clean."; \
	fi

# Fire up Docker locally
compose/local:
	docker-compose -f docker-compose.local.yml build --build-arg ENVIRONMENT=local web proxy
	docker-compose -f docker-compose.local.yml down
	docker-compose -f docker-compose.local.yml up

# Deploy scuole to the production server
# define services that make up the app with the docker-compose.yml file, and build them
# `down` stops and removes previously started containers
# `up -d` starts containers in the background with the defined services and leaves them running
compose/production-deploy:
	make free-space
	backup-containers
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build --build-arg ENVIRONMENT=production web proxy
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
	@echo "✅ Deployment completed successfully!"
	@make backups-purge

# Deploy scuole to the test server
# might want to create a separate ENVIRONMENT for staging, but production had been the default and relies on config/settings/production.py with no alterations
# docker image prune -a will clean more aggressively on staging, to address resource buildup from repetitive testing
compose/test-deploy:
	docker image prune -a
	backup-containers
	docker-compose -f docker-compose.yml -f docker-compose.override.yml build --build-arg ENVIRONMENT=production web proxy
	docker-compose -f docker-compose.yml -f docker-compose.override.yml down
	docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d
	@echo "✅ Deployment completed successfully!"
	@make backups-purge

compose/admin-update-askted:
	docker-compose -f docker-compose.yml -f docker-compose.admin.yml run --rm asktedupdate

# Run this to create an image and get into the docker container
# Runs as an ash shell (what Alpine Linux uses, which is the Docker image base, basically the same as bash)
compose/container:
	docker-compose -f docker-compose.yml run --entrypoint ash web



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

# Load in all past TAPR data
data/all-schools:
	python manage.py loadtaprdata 2023-2024 --bulk
	python manage.py loadtaprdata 2022-2023 --bulk
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

data/bootstrap: data/bootstrap-areas data/bootstrap-entities data/update-directories data/all-cohorts data/latest-school
	@echo "Bootstrap complete"

# Create state, region, and county models (w/ name, geographic coordinates, etc.)
data/bootstrap-areas:
	python manage.py bootstrapstates
	python manage.py bootstrapregions
	python manage.py bootstrapcounties

# Create district and campus models (w/ name, geographic coordinates, etc.)
data/bootstrap-entities:
	python manage.py bootstrapdistricts_v2 2023-2024
	python manage.py dedupedistrictslugs
	python manage.py bootstrapcampuses_v2 2023-2024
	python manage.py dedupecampusslugs

data/create-superuser:
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell --plain

# Load in the latest year's TAPR data with v3 script (RR version added 3/3/25)
data/latest-school:
	python manage.py loadtaprdata_v3 2023-2024
	
# Update AskTED information
data/update-directories:
	python manage.py updatedistrictdirectory
	python manage.py updatedistrictsuperintendents
	python manage.py updatecampusdirectory
	python manage.py updatecampusprincipals



docker/build:
	@echo "Building app..."
	@docker build \
		--tag ${APP} \
		.

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
		
docker/db-data:
	@echo "Attempting to create data volume (if needed)..."
	@docker create \
		--name ${APP}-db-data \
		--entrypoint /bin/echo \
		mdillon/postgis:9.4 "Data-only" 2>/dev/null || true

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

# Build app and its services, run the app, and load the app on a web server
docker/kickstart: docker/build docker/run docker/nginx

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
		
docker/nginx-build:
	@echo "Building nginx container..."
	@docker build \
		--tag=${APP}-nginx \
		--file Dockerfile.nginx \
		.

docker/pg-interactive:
	@echo "Starting interactive terminal to the database..."
	@docker run --interactive \
		--tty \
		 --rm \
		--link ${APP}-db:postgres \
		mdillon/postgis:9.4 \
		/bin/bash

docker/pull:
	@echo "Getting a fresh copy of master..."
	git checkout master
	git pull

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

#docker exec -ti scuole_web_1 /bin/sh
docker/shell:
	docker exec -ti scuole-web-1 /bin/sh



# For when containers from previous builds are lingering/take up space
free-space:
	-docker system prune -f

# added 4/3/25
health-check:
	@echo "🩺 Performing health check..."
	@sleep 10
	@if [ -z "$$(docker-compose -f docker-compose.yml -f docker-compose.prod.yml ps -q web)" ]; then \
		echo "❌ ERROR: Web container failed to start!"; \
		echo "See backup files in ~/docker-backups for manual recovery"; \
		exit 1; \
	fi
	@echo "✅ Container health check passed!"
	@echo "Checking for errors in logs..."
	@if docker logs $$(docker-compose -f docker-compose.yml -f docker-compose.prod.yml ps -q web) 2>&1 | grep -i "error\|exception\|failed" > /dev/null; then \
		echo "⚠️ Warning: Possible errors detected in web container logs."; \
		echo "Check logs with: docker logs $$(docker-compose -f docker-compose.yml -f docker-compose.prod.yml ps -q web)"; \
	else \
		echo "✅ No obvious errors in container logs."; \
	fi
	@echo "✅ Health check complete."

local/all: local/reset-db-bootstrap-areas data/bootstrap-edu data/all-schools data/all-cohorts

local/cohorts: local/reset-db-bootstrap-areas data/all-cohorts

local/db-fetch:
	aws s3 cp s3://backups.texastribune.org/schools/schools-pg.dump backups/pg.dump

local/db-restore:
	dropdb ${APP} --if-exists
	createdb ${APP}
	pg_restore --dbname ${APP} --no-privileges --no-owner backups/pg.dump

# If you have having a hard time getting `docker-entrypoint.sh` to run locally
# You can use this to rebuild the npm files and then run the python server
# Useful for when you're making js or css changes
local/npm_reset:
	npm run build
	python manage.py collectstatic --noinput
	python manage.py runserver

# 3/6/25 updated from pipenv to Docker
#pipenv run python manage.py migrate
local/reset-db:
	dropdb ${APP} --if-exists
	createdb ${APP}
	psql -d ${APP} -c 'CREATE EXTENSION postgis;'
	docker-compose exec web python manage.py migrate	

local/reset-db-bootstrap-areas: local/reset-db data/bootstrap-areas

local/reset-db-bootstrap-areas-entities: local/reset-db-bootstrap-areas data/bootstrap-entities

local/reset-db-bootstrap-areas-entities-directories: local/reset-db-bootstrap-areas-entities data/update-directories

local/reset-db-bootstrap-latest: local/reset-db-bootstrap-areas-entities-directories data/latest-school

local/reset-db-bootstrap-over-time: local/reset-db data/all-schools data/all-cohorts

# Restore from backup (works for both staging and production)
restore-from-backup:
	@echo "🔍 Looking for available backups..."
	@BACKUP_DIR=~/docker-backups; \
	if [ ! -d "$$BACKUP_DIR" ]; then \
		echo "❌ ERROR: Backup directory not found at $$BACKUP_DIR"; \
		exit 1; \
	fi; \
	if [ -z "$(TIMESTAMP)" ]; then \
		echo "Available backups:"; \
		ls -lt $$BACKUP_DIR/web-backup-*.tar | head -5 | awk '{print $$9}' | sed 's/.*web-backup-\(.*\)\.tar/\1/'; \
		echo ""; \
		echo "Usage: make restore-from-backup TIMESTAMP=YYYYMMDD_HHMMSS"; \
		echo "Example: make restore-from-backup TIMESTAMP=20240403_123045"; \
		exit 1; \
	fi; \
	if [ ! -f "$$BACKUP_DIR/web-backup-$(TIMESTAMP).tar" ] || [ ! -f "$$BACKUP_DIR/proxy-backup-$(TIMESTAMP).tar" ]; then \
		echo "❌ ERROR: Backup files for timestamp $(TIMESTAMP) not found"; \
		echo "Available backups:"; \
		ls -lt $$BACKUP_DIR/web-backup-*.tar | head -5 | awk '{print $$9}' | sed 's/.*web-backup-\(.*\)\.tar/\1/'; \
		exit 1; \
	fi; \
	echo "⚠️ WARNING: This will restore to backup from $(TIMESTAMP)"; \
	echo "Continue? [y/N] "; \
	read answer; \
	if [ "$$answer" != "y" ]; then \
		echo "Restoration aborted."; \
		exit 1; \
	fi; \
	echo "🔄 Restoring from backup $(TIMESTAMP)..."; \
	echo "Loading backup images..."; \
	docker load -i $$BACKUP_DIR/web-backup-$(TIMESTAMP).tar; \
	docker load -i $$BACKUP_DIR/proxy-backup-$(TIMESTAMP).tar; \
	echo "Stopping current containers..."; \
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down; \
	echo "Starting containers with backed up images..."; \
	docker tag $$(docker images | grep "web.*backup-$(TIMESTAMP)" | awk '{print $$1":"$$2}') web:latest; \
	docker tag $$(docker images | grep "proxy.*backup-$(TIMESTAMP)" | awk '{print $$1":"$$2}') proxy:latest; \
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d; \
	echo "✅ Restoration complete. Run 'make health-check' to verify."