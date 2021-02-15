# scuole
*(It's Italian for "schools.")*

Public Schools 3!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Setup](#setup)
  - [Make sure Docker is up and running](#make-sure-docker-is-up-and-running)
  - [Fire up pipenv](#fire-up-pipenv)
  - [Install dependencies via pipenv](#install-dependencies-via-pipenv)
    - [Troubleshooting](#troubleshooting)
  - [Run pipenv](#run-pipenv)
  - [Install npm packages](#install-npm-packages)
  - [If this is your first time loading the app, load in last year's data](#if-this-is-your-first-time-loading-the-app-load-in-last-years-data)
  - [If this is not your first time loading the app, run outstanding migrations](#if-this-is-not-your-first-time-loading-the-app-run-outstanding-migrations)
  - [Fire up the server](#fire-up-the-server)
- [Updating and deploying](#updating-and-deploying)
    - [Updating entities](#updating-entities)
    - [Updating AskTED data](#updating-askted-data)
    - [Updating TAPR data](#updating-tapr-data)
    - [Updating cohorts data](#updating-cohorts-data)
    - [Updating the CSS styling and other static assets](#updating-the-css-styling-and-other-static-assets)
  - [Deploying code changes](#deploying-code-changes)
    - [Deploying on the test server](#deploying-on-the-test-server)
    - [Deploying on the production server](#deploying-on-the-production-server)
  - [Deploying the data](#deploying-the-data)
    - [Deploying on the test server](#deploying-on-the-test-server-1)
    - [For the sitemap](#for-the-sitemap)
- [Troubleshooting](#troubleshooting-1)
  - [What is the best place to view the data?](#what-is-the-best-place-to-view-the-data)
  - [I'm seeing models being imported that are not supposed to be.](#im-seeing-models-being-imported-that-are-not-supposed-to-be)
  - [Why is my operation getting killed when I run `make compose/test-deploy` and `make compose/production-deploy`?](#why-is-my-operation-getting-killed-when-i-run-make-composetest-deploy-and-make-composeproduction-deploy)
  - [Django doesn't know where the the database is.](#django-doesnt-know-where-the-the-database-is)
  - [I'm seeing a duplicate key error when loading new data into the database.](#im-seeing-a-duplicate-key-error-when-loading-new-data-into-the-database)
  - [My deployment isn't working because there are "active endpoints".](#my-deployment-isnt-working-because-there-are-active-endpoints)
- [Workspace](#workspace)
- [Admin](#admin)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Setup

This project assumes you are using the provided Docker PostgreSQL database build. 

### Make sure Docker is up and running

```sh
make docker/db
```

This will create the data volume and instance of PostgreSQL for Django. 

### Fire up pipenv

```sh
pipenv --three
```

### Install dependencies via pipenv

```sh
pipenv install --dev
```

Locally, we are using Pipfile and Pipfile.lock files to manage dependencies. On the staging and production servers, we are using a Dockerfile, which installs dependencies from a `requirements.txt` file.

We need to always make sure these are in sync. For instance, if you are pulling updates from dependabot, changes will be made to the Pipfile.lock file but will never make it over to the `requirements.txt` file, which is used on staging/production.

A temporary workaround is to generate a `requirements.txt` file that's based on the Pipfile, using the [`pipenv-to-requirements`](https://pypi.org/project/pipenv-to-requirements/) package. You can do this simply by running:

```sh
pipenv run pipenv_to_requirements -f
```

This will generate a `requirements.txt` file in the root directory, which will be used by the Dockerfile when creating/editing the containers for staging and production. It also creates a `requirements-dev.txt` file, which currently isn't being used.

In the future, we will be switching to using Docker locally to manage dependencies rather than relying on pipenv. Several files have been created to start this process:

```sh
Dockerfile.local
docker-entrypoint-local.sh
docker-compose.local.yml
```

At the moment, however, this is still a work in progress.

#### Troubleshooting

If there's a problem installing `psycopg2` when installing pipenv dependencies, you may need to the pg_config path by running pg_config and then reinstalling it.

```sh
pg_config --bindir
export PATH=$PATH:path/to/pg/config
pip3 install psycopg2
```

### Run pipenv

```sh
pipenv shell
```

You'll need to activate the shell to run any of the Python commands. When on the staging or production servers, you'll run `docker run -it` to get inside the Docker container to run commands.

### Install npm packages

```sh
npm install
npm run build
```

### If this is your first time loading the app, load in last year's data

If this is your first time loading the app, you'll probably want to load in last year's data to start off. These commands will drop your database (which doesn't exist yet), create a new one and run migrations before loading in the data:

```sh
make local/reset-db
sh bootstrap.sh
```

`bootstrap.sh` is a compilation of commands from the `Makefile` that load in the latest data (for the state, regions, counties, districts, campuses, etc.) and create models from them.

If you're having trouble with the data, it might be because your `.env` file is not getting used. That file is where we set up the `DATA_FOLDER`, as explained in the [setup doc](https://github.com/texastribune/data-visuals-guides/blob/master/explorers-setup.md#schools). But you can also get around using that file by typing:

```sh
export DATA_FOLDER=~/Documents/tribune/github/scuole-house/scuole-data/
```

This environmental variable should be set before running any commands that load in data.

### If this is not your first time loading the app, run outstanding migrations

If this is not your first time loading the app, run this to catch up with any outstanding migrations you might have:

```sh
python manage.py migrate
```

### Fire up the server

```sh
sh docker-entrypoint.sh
```

This will collect static files, as well as fire up a local server.

If that doesn't work, try:

```sh
python manage.py collectstatic --noinput
python manage.py runserver
```

All good? Let's go! There are also other commands in scuole's `Makefile` at your disposal so check them out.

## Updating and deploying

Every year, we need to update cohorts, TAPR, district boundaries, campus coordinates, and the entities files for districts and campuses. Ideally, we would update AskTED every quarter. 

There are two types of data updates. One type is when you manually download the data, format it, and load it into the appropriate folder in `scuole-data`. The app then grabs the latest data from `scuole-data`. Another type is when you run a command to download the latest data directly from the website. Updating AskTED is an example of this. See [`scuole-data`](https://github.com/texastribune/scuole-data) for instructions on how to download and format the data used in `scuole`.

### Updating entities

In this explorer, we can see data for the entire state, regions, districts, and campuses. Regions typically don't change from year to year, but districts and campuses can be added or removed. As a result, we have to update the district and campus models every year.

First, make sure you've created new district and campus `entities.csv` files — instructions are in [scuole-data](https://github.com/texastribune/scuole-data). We use these files to create the models.

Next, remove the existing district and campus models (they're might be a better way to refresh them, we're going with this for now). Get into the shell, and start the Python terminal.

```sh
pipenv shell
python manage.py shell
```

Once you're in the Python terminal, run this:

```sh
from scuole.districts.models import District
district = District.objects.all()
district.delete()
from scuole.campuses.models import Campus
campus = Campus.objects.all()
campus.delete()
exit()
```

Then, run `make data/bootstrap-entities` to create the district and campus models.

### Updating AskTED data

**Updating locally**

Run `pipenv shell`, followed by `make data/update-directories` to update the data. You can also run each command in that block separately, your choice! 

**Updating on the test and production servers**

First, get inside the Docker container:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --entrypoint=ash --env-file=env-docker schools/web
```

Then, run this command to load the latest AskTED data:

```sh
make data/update-directories
```

If you run into any duplicate key errors during the AskTED update, refer to the [Troubleshooting section](https://github.com/texastribune/scuole#troubleshooting) for instructions on how to clear a table. You'll need to clear the table that is throwing this error, and reload the data.

Some of the data we load will be pulled from the [AskTED website](http://mansfield.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile2.aspx]). There may be data formatting errors with some of the data as its being pulled in. For instance, some of the phone numbers may be invalid. Right now, we have a `phoneNumberFormat` function in the `updatedistrictsuperintendents`, `updatecampusdirectory` and `updatecampusprincipals`. You'll need to edit this function or create new ones if you're running into problems loading the data from AskTED.

### Updating TAPR data

First, follow the instructions in this [Confluence document](https://texastribune.atlassian.net/wiki/spaces/APPS/pages/163844/How+to+update+Public+Schools+2019) to download and format the TAPR data.

Once you're done adding the latest data to `scuole-data`, you'll need to change the year in `make data/latest-school` to the latest year. You'll also need to add another line to load in the latest year to `make data/all-schools` — i.e. for 2019-2020, add `python manage.py loadtaprdata 2019-2020 --bulk`.

**Updating locally**

Run `pipenv shell`, followed by `make data/latest-school` to update the data.

**Updating on the test and production servers**

First, get inside the Docker container:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --entrypoint=ash --env-file=env-docker schools/web
```

Then, run this command to load the latest TAPR data:

```sh
make data/latest-school
```

### Updating cohorts data

First, check out [`scuole-data`](https://github.com/texastribune/scuole-data#cohorts) for instructions on how to download and format the latest cohorts data.

**Updating locally**

Next, you'll need to add a line to `data/all-cohorts` in the `Makefile` in `scuole` with the latest year. Then, run `pipenv shell`, followed by `python manage.py loadallcohorts <latest year>` to update the data locally.

Lastly, you will need to change the `latest_cohort_year` variable in the `scuole/cohorts/views.py` file to reference the latest cohorts school year. Also, make sure the `scuole/cohorts/schema/cohorts/schema.py` has the correct years (i.e. you'll need to change the year in `8th Grade (FY 2009)` for the reference `'enrolled_8th': '8th Grade (FY 2009)'`, along with the rest of the references.)

**Updating on the test and production servers**

First, get inside the Docker container:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --entrypoint=ash --env-file=env-docker schools/web
```

Then, run the Python command to load the latest batch of cohorts data:

```sh
python manage.py loadallcohorts <latest year>
```

### Updating the CSS styling and other static assets

**Updating locally**

If you make changes to the styles, you'll need to run `npm run build` again to rebuild the `main.css` file in the `assets/` folder that the templates reference. 

Then, run `pipenv shell`, followed by `python manage.py collectstatic --noinput` to recollect static files. You'll also need to do a hard refresh in whatever browser you're running the explorer in to fetch the new styles.

### Deploying code changes

Push all your changes to [Github](https://github.com/texastribune/scuole). We'll deploy on the test server first, and then the production servers.

Make sure your set up with `ssh` — check out [this doc](https://github.com/texastribune/data-visuals-guides/blob/master/explorers-setup.md#schools) for more info.

#### Deploying on the test server

```sh
ssh schools-test
cd scuole
git checkout master
git pull
make compose/test-deploy
```

Once you run these, make sure everything is working on the [test url](https://schools-test.texastribune.org/). 

#### Deploying on the production server

After checking the test site, you'll need to repeat those steps on the two production servers: `schools-prod` and `schools-prod-2`. You must do both servers — if you don't, the published app will switch between new and old code.

```sh
ssh schools-prod
cd scuole
git pull
make compose/production-deploy
```

Congrats, your changes are now [live](schools.texastribune.org)!

### Deploying data changes/new data

Deploying the data on the test and production servers will be similar to loading it in locally.

#### Deploying on the test server

First, make sure all of your changes are pushed to [Github](https://github.com/texastribune/scuole-data). Then, log into the test server and pull the changes in `scuole-data`.

```sh
ssh schools-test
cd scuole-data
git pull
```

Then, go back to `scuole`. 

```
cd ../scuole
git checkout master
git pull 
```

Next, let's get into the Docker container:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --net=scuole_default --entrypoint=ash --env-file=env-docker schools/web
```

<!---
Alternative to the above command that needs a more recent version of docker-compose on production to work:
docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --volume /home/ubuntu/scuole-data:/home/ubuntu/scuole/data:ro --entrypoint ash web
-->

Then, run the commands to load in new data, as documented above.

```sh
python manage.py loadallcohorts 2008
```

Exit out of the Python shell and your Docker container with `Ctrl + P + Q`. Run the following command to build and deploy the data changes to the test site.

```sh
make compose/test-deploy
```

Your changes should now be on the [test server](schools-test.texastribune.org)! Now we're ready for production a.k.a. the big time.

Fortunately, you only need to push data changes to one server. For `schools-prod`, we will need to pull down Github changes:

```sh
ssh schools-prod
cd scuole-data
git pull
cd ../scuole
git pull
```

The command to get into the Docker containers on the production servers will change a little bit. You won't need the `--net` parameter anymore:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --entrypoint=ash --env-file=env-docker schools/web
```

Run the commands to load in new data. Here's an example:

```sh
python manage.py loadallcohorts 2008
```

Now, deploy:

```sh
make compose/production-deploy
```

Once that's done, check the [live site](https://schools.texastribune.org/). Your changes should be there! Now go home, your work here is done.

#### For the sitemap

When we add new urls, we also need to update the sitemap (`sitemap.xml`) to include those paths. Fortunately, Django has functions that allow us to generate all of the urls associated with an object's views.

To see an example, view any of the `sitemaps.py` files. You'll need to add the sitemap to the `config/urls.py` file, and view the updated sitemap locally at `localhost:8000/sitemap.xml`. 

After verifying that the sitemap looks OK locally, copy the content starting from the `<urlset>` tag in `sitemap.xml` and paste it into `scuole/static_src/sitemap.xml` before deploying. You can also run `python manage.py collectstatic --noinput` on the test and production servers to get the updated sitemap.

## Troubleshooting

### What is the best place to view the data?

[TablePlus](https://tableplus.com/) is recommended. Hook it up to the `scuole` PostgreSQL database!

### I'm seeing models being imported that are not supposed to be.

The easiest solution is to follow the instructions from the answer for the duplicate key error and selectively delete some models. There are probably better solutions for this ...

### Why is my operation getting killed when I run `make compose/test-deploy` and `make compose/production-deploy`?

This may be due to memory issues. It typically gets killed when packages are being installed in the Docker container. If you try a couple more times (wait a little), the application should deploy.

### Django doesn't know where the the database is.

To ensure Django knows where to look, you may need to set the `DATABASE_URL`. If you are not using the Docker provided database, use `DATABASE_URL` to tell the app what you've done instead. We haven't needed to set this lately.

```sh
export DATABASE_URL=postgres://docker:docker@docker.local:5432/docker
```

If you get the error `django.db.utils.OperationalError: could not translate host name "docker.local" to address: nodename nor servname provided, or not known`, unset `DATABASE_URL` in your environment by running `unset DATABASE_URL` in the terminal. From there, the app should be runnable as normal.

### I'm seeing a duplicate key error when loading new data into the database.

Sometimes an update can throw a duplicate key error. A brute force solution is clearing out all of the objects from the table, and running the update again.

- Run `ssh schools-test`. ALWAYS do this on the test server first.
- Run `docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --net=scuole_default --entrypoint=ash --env-file=env-docker schools/web` to get into the test server Docker environment.
- Run `python manage.py shell` to get into the Python shell to run Django commands.
- If you want to clear `Superintendents`, for example, you'd need to import the District models by running `from scuole.districts.models import Superintendent` in the Python shell. You can get the syntax for the import by going to the Python file in `scuole` that updates that particular model and coping the line of code importing it.
- Save the models in a variable: `super = Superintendent.objects.all()`.
- `print(super)` to make sure you're clearing the right thing.
- `super.delete()` to delete them all.
- `exit()` to exit out of the Python shell.
- Run your update command again.

You may need to run this process when updating cohorts data — if the cohorts data upload for the latest year is failing because there are too many regional or county cohorts, it may be because you've tried to upload the data more than once and there are duplicates. 

You'll need to filter for the latest year by filtering for the objects with the highest `year_id` so you can delete them. You can find the highest `year_id` by looking at the objects in Table Plus. Then, you'll run:

```
from scuole.counties.models import CountyCohorts
latest = CountyCohorts.objects.filter(year_id=14)
print(latest) # to check if these are the objects we want to delete
latest.delete()
```

If you see the error `django.db.utils.OperationalError: could not translate host name "db" to address: Name does not resolve` when deploying/updating data, it could mean that the app doesn't know where to look for the database. Running `make compose/test-deploy` does some of the setup, and might fix the issue.

### My deployment isn't working because there are "active endpoints".

If you run into `ERROR: error while removing network: network <network-name> id <network-id> has active endpoints` while deploying to test or production, it means you need to clear out some lingering endpoints.

- Run `docker network ls` to get a list of networks.
- Grab the id of `scuole_default` and run `docker network inspect <scuole_default-id>`
- You'll see a bunch of objects in the `Container` property. Each of them should have an endpoint ID and a name. The name is the endpoint name.
- Run `docker network disconnect -f <scuole_default-id> <endpoint-name>` for each of the endpoints.
- Try test deploying again. It should work this time around!

[Source of this information](https://github.com/moby/moby/issues/17217)

## Workspace

The `workspace` directory is used for incorporating the schools database with other datasets we run across in our reporting. These include:

1) A-F scores

For this, we merge the slugs for campuses in our schools app with their A-F scores from TEA. This is done so we can link to their pages in the schools app when showing them in our [grade lookup tool](https://www.texastribune.org/2019/08/15/texas-schools-grades-accountability/). The spreadsheet with A-F scores from TEA gets put into the `raw_data` manually. The other spreadsheet you'll need is one with slugs for each campus in our schools app. It can be generated by running:

```sh
python manage.py exportslugs
```

After those files are in the `raw_data` directory, run everything inside of `analysis.ipynb` to spit out a merged spreadsheet in the `output` directory, which will then be loaded into a Google spreadsheet and used with the lookup tool.

## Admin

This likely won't have an admin interface, but you are welcome to use it to check out how things are getting loaded. First, you'll need to create a super user. (If you ever blow away your database, you'll have to do it again!)

```sh
python manage.py createsuperuser
```

Then, after a `python manage.py runserver`, you can visit [http://localhost:8000/admin](http://localhost:8000/admin) and use the credentials you setup to get access. Every thing will be set to read-only, so there's no risk of borking anything.
