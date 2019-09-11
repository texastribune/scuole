# scuole
*(It's Italian for "schools.")*

Public Schools 3!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Setup](#setup)
- [Deploy](#deploy)
- [Workspace](#workspace)
- [Admin](#admin)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Setup

This project assumes you are using the provided docker postgreSQL database build. Make sure docker is up and running, then run:

```sh
make docker/db
```

This will create the data volume and instance of PostgreSQL for Django. To ensure Django knows where to look, you need to set the `DATABASE_URL`. If you are not using the docker provided database, use `DATABASE_URL` to tell the app what you've done instead.

```sh
export DATABASE_URL=postgres://docker:docker@docker.local:5432/docker
```

From there, the app should be runnable as normal.

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

If you're having trouble with the data, it might be because your `.env` file is not getting use. In that file is where we set up the `DATA_FOLDER` as explained in the [setup doc](https://github.com/texastribune/data-visuals-guides/blob/master/explorers-setup.md#schools). But you can also get around using that file by typing:

```sh
export DATA_FOLDER=~/Documents/tribune/github/scuole-house/scuole-data/
```

Before running any commands that load in data.

If this is not your first time loading the app, you can run this to catch up with any outstanding migrations you might have:

```sh
python manage.py migrate
```

The data we load will be pulled from the [AskTed website](http://mansfield.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile2.aspx]). As you go through this, you may have data formatting errors with some of the data being pulled in. For instance, some of the phone numbers may be invalid. Right now, we have a `phoneNumberFormat` function in the `updatedistrictsuperintendents`, `updatecampusdirectory` and `updatecampusprincipals`. You may need to edit this function or create new ones if you're running into problems loading the data from AskTed.

There are also other commands in makefile at your disposal so check them out.

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

All good? Let's go!

## Deploy

Once you've made changes, make sure they are showing up on local. Once you've verified this, we can deploy to production. This projces will involve getting into the Docker container on the production server, loading in the new data and deploying it live.

First, however, let's create a Docker container on your local machine to make sure it's working. This will mirror what we'll do on production later. Make sure you're in the `scuole` directory and run:

```sh
docker-compose -f docker-compose.yml run --volume /Users/chrisessig/Documents/tribune/github/scuole-house/scuole-data:/usr/src/app/data/:ro -e DATABASE_URL=postgis://chrisessig@host.docker.internal/scuole --entrypoint ash web
```

You will need to change the `/Users/chrisessig/Documents/tribune/github/scuole-house/scuole-data` path to the correct path for your data folder. Also change the `chrisessig` user to whoever owns the `scuole` database on your local machine. To find that out, run:

```sh
psql -c "\l"
```

If this works correctly, this will log you into the Docker container and give you a new shell. Once inside, install the dependencies:

```sh
pipenv install --dev --system
```

And run your update, which would look something like:

```sh
python manage.py loadallcohorts 2008
```

If nothing blows up, it worked. Now we're ready to do the same on production. First get out of the shell and push all your changes to [Github](https://github.com/texastribune/scuole). Then log into the server and pull those changes:

```sh
ssh schools-prod
cd scoule-data
git pull
cd ../scoule 
git pull
```

If you're not set up with the ssh yet, check out [this doc](https://github.com/texastribune/data-visuals-guides/blob/master/explorers-setup.md#schools) for more info.

Once you're on the production server, you can run:

```sh
docker run -it --rm --volume=/home/ubuntu/scuole-data:/usr/src/app/data/:ro --entrypoint=ash --env-file=env-docker schools/web
```

<!---
Alternative to the above command that's not working at the moment:
docker-compose -f docker-compose.yml -f docker-compose.prod.yml run --volume /home/ubuntu/scuole-data:/home/ubuntu/scuole/data:ro --entrypoint ash web
-->

Now run the same command you ran earlier to update the data:

```sh
python manage.py loadallcohorts 2008
```

Once that's ran, go ahead and get into the Django shell and make sure you can see your changes:

```sh
python manage.py shell
```

For instance, if you're updating cohorts, make sure the data is correct:

```python
from scuole.states.models import *
StateCohorts.objects.get(year__name = '2007-2008',ethnicity='African American',gender='',economic_status='').enrolled_8th
```

You will need to change the school year to fit the year you are updating. Once that's done, it should spit out the number you see in the "Class size" for black students in first table under "Ethnicity" on the page. You can also modify your query to be whatever you want to check on the page.

Now exit out of the python shell and your Docker container and run the following command. This will push up code changes.

```sh
make compose/production-deploy
```

Now check the live site. Your changes should be there! Now go home, your work here is done.

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

