- [Setup on your local server](#initial-setup-on-your-local-server)
  - [Clone or download the two scuole repositories in your local computer](#clone-or-download-the-two-scuole-repositories-in-your-local-computer)
  - [Make sure Docker is up and running](#make-sure-docker-is-up-and-running)
  - [Fire up pipenv](#fire-up-pipenv)
  - [Install dependencies via pipenv](#install-dependencies-via-pipenv)
  - [Run pipenv](#run-pipenv)
  - [Install npm packages](#install-npm-packages)
  - [If this is your first time loading the app, load in last year's data](#if-this-is-your-first-time-loading-the-app-load-in-last-years-data)
  - [If this is not your first time loading the app, run outstanding migrations](#if-this-is-not-your-first-time-loading-the-app-run-outstanding-migrations)
- [Fire up the server](#fire-up-the-server)

## Initial setup on your local server

So you want to update the schools database? That's great! This README will take you through the many steps involved in that process. This README also assumes that you're new at updating the schools database and are starting from the beginning.

If you're a veteran and want some quick deploy instructions you can skip to [here](#quick-deploy).

For everyone else, we'll go through a chronological order of operations:

1) Set up schools in your local computer
2) Upload the latest school data from `scuole_data` repo into your local schools database
3) Update the database in the [test server](https://schools-test.texastribune.org/)
4) Update the database in our production servers

The end result should look [like this](https://schools.texastribune.org/).

Great! Let's get started!

### Clone or download the two scuole repositories in your local computer

The schools database has two repositories: `scuole` (a.k.a. this one, which has the actual Django app) and [`scuole-data`](https://github.com/texastribune/scuole-data) which is a repository for all of the data you've downloaded from Texas Education Agency and Texas Higher Ed Coordinating Board (for cohorts data). You'll want to clone or download both and keep them in a directory where you can find them.

### Make sure Docker is up and running

This project assumes you are using the provided Docker PostgreSQL database build. Also, make sure that your Postgres is updated and running. You can open up the [PostGres](https://postgresapp.com/) to check in on it.

```sh
make docker/db
```

This will create the data volume and instance of PostgreSQL for Django.

### Fire up pipenv

Make sure you're using at least Python 3.7 to create your pipenv environment. The following will create the environment using the default Python 3 interpreter on your system.

```sh
pipenv --python 3
```

### Install dependencies via pipenv

```sh
pipenv install --dev
```

**Note:** If you're running into problems installing `psycopg2` when installing pipenv dependencies, see the [troubleshooting readme](README_TROUBLESHOOTING.md).

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

### Run pipenv

You'll next need to activate the shell to run any of the Python commands. 

```sh
pipenv shell
```

### Install npm packages

```sh
npm install
npm run build
```

### If this is your first time loading the app, load in last year's data

If this is your first time loading the app, you'll probably want to load in last year's data to start off. 

First things first, create a `.env` file in this app. Find the directory where you downloaded the `scuole-data` repository in your computer and then add it as a variable called `DATA_FOLDER`:

```sh
export DATA_FOLDER=/your/local/path/to/scuole-data/
```

Replace the path shown above with the path to `scuole-data/` on your computer. This environmental variable should be set before running any commands that load in data.

Next, these commands will drop your database (which doesn't exist yet), create a new one and run migrations before loading in the data. `bootstrap.sh` is a compilation of commands from the `Makefile` that load in last year's schools data (for the state, regions, counties, districts, campuses, etc.) and create models from them:

```sh
make local/reset-db
sh bootstrap.sh
```

Some warnings/errors you might see at this stage: 
* `No such file or directory`- verify that the path specified in the output matches the path to `DATA_FOLDER`, i.e. data files in your `scuole-data` directory. This should be set in the .env file as described above. If you're really stuck, running `export DATA_FOLDER=/your/local/path/to/scuole-data/` in the Terminal command line will correct the path temporarily, but you'll need to do this again every time you start a new session.
* `No shape data for Odyssey Academy Inc`- this is expected for Charter schools, but you should see shapes successfully created for all ISDs (e.g. `Creating Galveston ISD (084902)`)

Pay close attention to all of these errors. If you need to debug and update code, you'll need to iterate on those two commands (`make local/reset-db` and `sh bootstrap.sh`) until it works without major errors.

## Fire up the server

If you haven't already, make sure Docker is running and step into a pipenv shell.

```sh
make docker/db 
pipenv shell
```

Next, collect static files and fire up the server. Previous instructions suggested ```sh docker-entrypoint.sh``` but in my experience this breaks the css. Try this instead:

```sh
python manage.py collectstatic --noinput
python manage.py runserver
```

Open up the schools database in your [local server](http://localhost:8000/) and make sure that all of the information is there and the pages are working correctly. You can compare it to the [live version of the school's database](https://schools.texastribune.org/). All good? Let's go! There are also other commands in scuole's [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) at your disposal so check them out.