# scuole
*(It's Italian for "schools.")*

Public Schools 3!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Setup](#setup)
- [Updating and deploying](#updating-and-deploying)
  - [Changes to the code](#changes-to-the-code)
  - [Changes to the data](#changes-to-the-data)
- [Updating data](#updating-data)
- [Troubleshooting](#troubleshooting)
- [Workspace](#workspace)
- [Admin](#admin)
- [To-dos](#to-dos)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Setup

This project assumes you are using the provided docker PostgreSQL database build. Make sure docker is up and running, then run:

```sh
make docker/db
```

This will create the data volume and instance of PostgreSQL for Django. 

Fire up pipenv:

```sh
pipenv --three
```

Install dependencies via pipenv:

```sh
pipenv install --dev
```

Run pipenv:

```sh
pipenv shell
```

If there's a problem installing `psycopg2` when installing pipenv dependencies, you may need to the pg_config path by running pg_config and then reinstalling it.

```sh
pg_config --bindir
export PATH=$PATH:path/to/pg/config
pip3 install psycopg2
```

Next, install npm packages:

```sh
npm install
npm run build
```

If this is your first time using the app, you'll probably want to load in last year's data to start off. These commands will drop your database (which doesn't exist yet), create a new one and run migrations before loading in the data:

```sh
make local/reset-db
sh bootstrap.sh
```

If you're having trouble with the data, it might be because your `.env` file is not getting used. In that file is where we set up the `DATA_FOLDER` as explained in the [setup doc](https://github.com/texastribune/data-visuals-guides/blob/master/explorers-setup.md#schools). But you can also get around using that file by typing:

```sh
export DATA_FOLDER=~/Documents/tribune/github/scuole-house/scuole-data/
```

This should be run before running any commands that load in data.

If this is not your first time loading the app, you can run this to catch up with any outstanding migrations you might have:

```sh
python manage.py migrate
```

Some of the data we load will be pulled from the [AskTed website](http://mansfield.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile2.aspx]). There may be data formatting errors with some of the data as its being pulled in. For instance, some of the phone numbers may be invalid. Right now, we have a `phoneNumberFormat` function in the `updatedistrictsuperintendents`, `updatecampusdirectory` and `updatecampusprincipals`. You may need to edit this function or create new ones if you're running into problems loading the data from AskTed.

Once the data is loaded, you can run the following command:

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

### Changes to the code

If you're making changes to just the code and not the data, first you need to push all your changes locally to [Github](https://github.com/texastribune/scuole). Then you can run:

```sh
ssh schools-test
cd scuole
git pull
git checkout test-server
git rebase master  
make compose/test-deploy
```

Once you run these, make sure everything is working on the [test url](https://schools-test.texastribune.org/). If so, then you'll need to repeat those steps on the two production servers: `schools-prod` and `schools-prod-2`.

```sh
ssh schools-prod
cd scuole
git pull
make compose/production-deploy
```

Congrats, you're changes are now [live](schools.texastribune.org)!

### Changes to the data

#### Updating data

There are two types of data updates. One type is when you manually download the data, format it, and load it into the appropriate folder in `scuole-data`. You'll then need to deploy the latest data in `scuole-data` (instructions in the deploy section). 

Another type is when you run a command to download the latest data directly from the website. Updating AskTED is an example of this. You'll need to ssh onto the appropriate server (test or production) and run a series of commands to pull the latest data before deploying it to the server.

See [`scuole-data`](https://github.com/texastribune/scuole-data) for more descriptions about the data used in `scuole`. `scuole-data` also has instructions on how to clean and download TAPR and cohorts data.

**For cohorts**
You'll need to add a line to `data/all-cohorts` in the `Makefile` in `scuole` with the latest year. Then, run 
`python manage.py loadallcohorts <latest year>` during the update.

**For AskTED**
Run `make data/update-directories` to update the data. You can also run each command in that block separately, your choice!

If you run into any duplicate key errors during the AskTED update, refer to the Troublshooting section below for instructions on how to clear a table. 

You'll need to clear the table that is throwing this error, and reload the data. This error happens because the update may be trying to insert something that has the same ID as something else.

**For TAPR**
Refer to this [Confluence document](https://texastribune.atlassian.net/wiki/spaces/APPS/pages/163844/How+to+update+Public+Schools+2019).

If you're making changes to the data, we will first deploy to the test server and then production. This process will involve getting into the Docker container on the server, loading in the new data and deploying it live.

If you're not set up with the ssh yet, check out [this doc](https://github.com/texastribune/data-visuals-guides/blob/master/explorers-setup.md#schools) for more info.

First, make sure all of your changes are pushed to [Github](https://github.com/texastribune/scuole). Then log into the server and pull those changes:

```sh
ssh schools-test
cd scuole-data
git pull
cd ../scuole
git pull
git checkout test-server
git rebase master  
```

Now let's get into the Docker container:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --net=scuole_default --entrypoint=ash --env-file=env-docker schools/web
```

<!---
Alternative to the above command that needs a more recent version of docker-compose on production to work:
docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --volume /home/ubuntu/scuole-data:/home/ubuntu/scuole/data:ro --entrypoint ash web
-->

And run the update to your data, which would look something like:

```sh
python manage.py loadallcohorts 2008
```

Now exit out of the python shell and your Docker container with `Ctrl + P + Q`. If you have code changes as well, you can push them live by running:

```sh
make compose/test-deploy
```

Your changes should now be on the [test server](schools-test.texastribune.org)! Now we're ready for production a.k.a. the big time.

Just a quick reminder: Schools has TWO production databases. For `schools-prod`, we will need to pull down Github changes:

```sh
ssh schools-prod
cd scuole-data
git pull
cd ../scuole
git pull
```

If your making data changes, the command to get into the Docker containers on the prod servers will change a little bit. You won't need the `--net` parameter anymore:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --entrypoint=ash --env-file=env-docker schools/web
```

Now go ahead make your changes. Here's an example:

```sh
python manage.py loadallcohorts 2008
```

And deploy:

```sh
make compose/production-deploy
```

Fortunately, you only need to push data changes to one server.

Once that's done, check the live site. Your changes should be there! Now go home, your work here is done.

## Troubleshooting

To ensure Django knows where to look, you may need to set the `DATABASE_URL`. If you are not using the Docker provided database, use `DATABASE_URL` to tell the app what you've done instead. We haven't needed to set this lately.

```sh
export DATABASE_URL=postgres://docker:docker@docker.local:5432/docker
```

If you get the error `django.db.utils.OperationalError: could not translate host name "docker.local" to address: nodename nor servname provided, or not known`, unset `DATABASE_URL` in your environment by running `unset DATABASE_URL` in the terminal. From there, the app should be runnable as normal.

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


## To-dos

* Figure out if we're using `requirements.txt` or `Pipfile.lock`. Right now, the test server is using `requirements.txt` and has pending git changes. The local and production versions are using `Pipfile.lock`. This is why we use the `make compose/test-deploy` command on the test server and not on production.

