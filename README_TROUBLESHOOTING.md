# scuole troubleshooting

  - [When setting up my local server, I have a problem installing `psycopg2` when installing pipenv dependencies](#when-setting-up-my-local-server-i-have-a-problem-installing-psycopg2-when-installing-pipenv-dependencies)
  - [What is the best place to view the data?](#what-is-the-best-place-to-view-the-data)
  - [I'm seeing models being imported that are not supposed to be](#im-seeing-models-being-imported-that-are-not-supposed-to-be)
  - [Why is my operation getting killed when I run `make compose/test-deploy` and `make compose/production-deploy`?](#why-is-my-operation-getting-killed-when-i-run-make-composetest-deploy-and-make-composeproduction-deploy)
  - [Django doesn't know where the the database is](#django-doesnt-know-where-the-the-database-is)
  - [I'm seeing a duplicate key error when loading new data into the database](#im-seeing-a-duplicate-key-error-when-loading-new-data-into-the-database)
  - [My deployment isn't working because there are "active endpoints"](#my-deployment-isnt-working-because-there-are-active-endpoints)
  - [I'm having trouble debugging errors with Docker](#im-having-trouble-debugging-errors-with-docker)
  - [Django can't find the GDAL library](#django-cant-find-the-gdal-library)

### When setting up my local server, I have a problem installing `psycopg2` when installing pipenv dependencies

If there's a problem installing `psycopg2` when installing pipenv dependencies, you may need to the pg_config path by running pg_config and then reinstalling it.

```sh
pg_config --bindir
export PATH=$PATH:path/to/pg/config
pip3 install psycopg2
```

### What is the best place to view the data?

[TablePlus](https://tableplus.com/) is recommended. Hook it up to the `scuole` PostgreSQL database!

### I'm seeing models being imported that are not supposed to be

The easiest solution is to follow the instructions from the answer for the duplicate key error and selectively delete some models. There are probably better solutions for this ...

### Why is my operation getting killed when I run `make compose/test-deploy` and `make compose/production-deploy`?

This may be due to memory issues. It typically gets killed when packages are being installed in the Docker container.

You can run `make free-space` to get rid of unused Docker containers. You can also remove containers one by one by running `docker container ls` to see each container and its ID, followed by `docker rm -f <container-id>`. To see the size of each container, run `docker container ls --all --size`.

### Django doesn't know where the the database is

To ensure Django knows where to look, you may need to set the `DATABASE_URL`. If you are not using the Docker provided database, use `DATABASE_URL` to tell the app what you've done instead. We haven't needed to set this lately.

```sh
export DATABASE_URL=postgres://docker:docker@docker.local:5432/docker
```

If you get the error `django.db.utils.OperationalError: could not translate host name "docker.local" to address: nodename nor servname provided, or not known`, unset `DATABASE_URL` in your environment by running `unset DATABASE_URL` in the terminal. From there, the app should be runnable as normal.

### I'm seeing a duplicate key error when loading new data into the database

Sometimes an update can throw a duplicate key error. A brute force solution is clearing out all of the objects from the table, and running the update again.

- Run `ssh schools-test`. ALWAYS do this on the test server first.
- Run `docker exec -i -t scuole_web_1 /bin/ash` to get into the `web` Docker container.
- Run `python manage.py shell` to get into the Python shell to run Django commands.
- If you want to clear `Superintendents`, for example, you'd need to import the District models by running `from scuole.districts.models import Superintendent` in the Python shell. You can get the syntax for the import by going to the Python file in `scuole` that updates that particular model and coping the line of code importing it.
- Save the models in a variable: `super = Superintendent.objects.all()`.
- `print(super)` to make sure you're clearing the right thing.
- `super.delete()` to delete them all.
- `exit()` to exit out of the Python shell.
- Run your update command again.

You can also do this in the local server by getting into the Python Terminal by running `python manage.py shell` and then running similar steps for the models you want to delete.

```python
python manage.py shell
from scuole.districts.models import Superintendent
super = Superintendent.objects.all()
print(super) # to check if these are the objects we want to delete
super.delete()
exit()
```

You may need to run this process when updating cohorts data — if the cohorts data upload for the latest year is failing because there are too many regional or county cohorts, it may be because you've tried to upload the data more than once and there are duplicates.

```python
python manage.py shell
from scuole.counties.models import CountyCohorts
countycohorts = CountyCohorts.objects.all()
print(countycohorts) # to check if these are the objects we want to delete
countycohorts.delete()
exit()
```

You'll need to delete the `StateCohorts`, `RegionCohorts` and `CountyCohorts` data in the database. Make sure you run `python manage.py loadallcohorts` afterwards (without the latest year) so you load in data dating back to 1997 — otherwise, the stacked area charts will not show up (RR note: loadallcohorts requires a param, I think it's best to step into the Docker shell and run `make data/all-cohorts`).

If you see the error `django.db.utils.OperationalError: could not translate host name "db" to address: Name does not resolve` when deploying/updating data, it could mean that the app doesn't know where to look for the database. Running `make compose/test-deploy` does some of the setup, and might fix the issue.

### My deployment isn't working because there are "active endpoints"

If you run into `ERROR: error while removing network: network <network-name> id <network-id> has active endpoints` while deploying to test or production, it means you need to clear out some lingering endpoints.

- Run `docker network ls` to get a list of networks.
- Grab the id of `scuole_default` and run `docker network inspect <scuole_default-id>`
- You'll see a bunch of objects in the `Container` property. Each of them should have an endpoint ID and a name. The name is the endpoint name.
- Run `docker network disconnect -f <scuole_default-id> <endpoint-name>` for each of the endpoints.
- Try test deploying again. It should work this time around!

[Source of this information](https://github.com/moby/moby/issues/17217)

### I'm having trouble debugging errors with Docker

Here are some commands to help you out:

- List all running containers - `docker ps`
- Stop all running services on containers: `docker-compose down`
- Delete all containers: `docker rm -f $(docker ps -a -q)`
- Delete all volumes: `docker volume rm $(docker volume ls -q)`
- Build images of services: `docker-compose build <service>` (The service name is optional, if you don’t add a service it will build everything)
- Start all services on containers: `docker-compose up -d`
  
In addition, check out `docker-compose.yml` and `docker-compose.override.yml`, which are configurations for the services being built and used by default.

### Django can't find the GDAL library

You may encounter the following error when running `make local/reset-db`:

```plaintext
django.core.exceptions.ImproperlyConfigured: Could not find the GDAL library
(tried "gdal", "GDAL", "gdal3.3.0", "gdal3.2.0", "gdal3.1.0",
"gdal3.0.0", "gdal2.4.0", "gdal2.3.0", "gdal2.2.0", "gdal2.1.0", "gdal2.0.0").
Is GDAL installed? If it is, try setting GDAL_LIBRARY_PATH in your settings.
```

Run `which psql` to find which Postgres installation you are using. If the command prints `/usr/local/bin/psql`, you are probably using the Homebrew installation of Postgres. In this case, you can install GDAL by running `brew install GDAL`.

Postgres.app includes GDAL by default. If you are using Postgres.app, you may need to [configure your PATH](https://postgresapp.com/documentation/cli-tools.html) so Django can find GDAL.