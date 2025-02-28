# scuole

*(It's Italian for "schools.")*

Public Schools 3!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

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
- [Updating data on your local server](#updating-data-on-your-local-server)
  - [Updating district boundaries and campus coordinates](#updating-district-boundaries-and-campus-coordinates)
  - [Updating district and campus entities](#updating-district-and-campus-entities)
  - [Updating AskTED data](#updating-askted-data)
  - [Updating TAPR data](#updating-tapr-data)
  - [Checking the local server](#checking-the-local-server)
  - [Updating cohorts data](#updating-cohorts-data)
  - [Updating the CSS styling and other static assets](#updating-the-css-styling-and-other-static-assets)
  - [More small changes](#more-small-changes)
  - [Updating the sitemap](#updating-the-sitemap)
- [Deploying on the test servers](#deploying-on-the-test-servers)
  - [Configure your computer to ssh into our test and production servers](#configure-your-computer-to-ssh-into-our-test-and-production-servers)
  - [Deploying on the test server](#deploying-on-the-test-server)
  - [Deploying code changes on the test server](#deploying-code-changes-on-the-test-server)
  - [Deploying data updates on the test server](#deploying-data-updates-on-the-test-server)
  - [Factchecking](#factchecking)
- [Deploying on production servers](#deploying-on-production-servers)
  - [Deploying code changes on the production server](#deploying-code-changes-on-the-production-server)
  - [Deploying data updates on the production server](#deploying-data-updates-on-the-production-server)
- [Quick deploy](#quick-deploy)
  - [Deploying code changes](#deploying-code-changes)
  - [Deploying data changes/new data](#deploying-data-changesnew-data)
- [Troubleshooting](#troubleshooting)
  - [When setting up my local server, I have a problem installing `psycopg2` when installing pipenv dependencies](#when-setting-up-my-local-server-i-have-a-problem-installing-psycopg2-when-installing-pipenv-dependencies)
  - [What is the best place to view the data?](#what-is-the-best-place-to-view-the-data)
  - [I'm seeing models being imported that are not supposed to be](#im-seeing-models-being-imported-that-are-not-supposed-to-be)
  - [Why is my operation getting killed when I run `make compose/test-deploy` and `make compose/production-deploy`?](#why-is-my-operation-getting-killed-when-i-run-make-composetest-deploy-and-make-composeproduction-deploy)
  - [Django doesn't know where the the database is](#django-doesnt-know-where-the-the-database-is)
  - [I'm seeing a duplicate key error when loading new data into the database](#im-seeing-a-duplicate-key-error-when-loading-new-data-into-the-database)
  - [My deployment isn't working because there are "active endpoints"](#my-deployment-isnt-working-because-there-are-active-endpoints)
  - [I'm having trouble debugging errors with Docker](#im-having-trouble-debugging-errors-with-docker)
  - [Django can't find the GDAL library](#django-cant-find-the-gdal-library)
- [Workspace](#workspace)
- [Admin](#admin)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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

**Note:** If you're running into problems installing `psycopg2` when installing pipenv dependencies, you can troubleshoot [here](#when-setting-up-my-local-server-i-have-a-problem-installing-psycopg2-when-installing-pipenv-dependencies).

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
export DATA_FOLDER=~/your/local/path/to/scuole-data/
```

Replace the path shown above with the path to `scuole-data/` on your computer. This environmental variable should be set before running any commands that load in data.

Next, these commands will drop your database (which doesn't exist yet), create a new one and run migrations before loading in the data:

```sh
make local/reset-db
sh bootstrap.sh
```

`bootstrap.sh` is a compilation of commands from the `Makefile` that load in last year's schools data (for the state, regions, counties, districts, campuses, etc.) and create models from them.

If get an error that the app can't find the data, it might be because your `.env` file is not getting used correctly. But you can also get around using that file by finding the directory where you downloaded the `scuole-data` repo in your local computer and typing in your terminal:

```sh
export DATA_FOLDER=~/your/local/path/to/scuole-data/
```

Again, replace the path shown above with the path to `scuole-data/` on your computer. If you do it this way, remember that you have to type that every time you start a new session on your terminal.

### If this is not your first time loading the app, run outstanding migrations

If this is not your first time loading the app, run this to catch up with any outstanding migrations you might have:

```sh
python manage.py migrate
```

### Fire up the server

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

## Updating data on your local server

Every year, we need to update cohorts, TAPR, district boundaries, campus coordinates and the entities files for districts and campuses.

There are two types of data downloads supporting the scuole app:
1) **Manually download**. The [`scuole-data`](https://github.com/texastribune/scuole-data) repo contains Jupyter notebooks that guide you through formatting and organizing data where the app can access it. If data is incorrectly formatted, you may see errors while working through this repo.
2) **Automatic download**. This involves running a command which downloads the latest data directly from a website. We use this process for updating AskTED directory info.

There are also two sections to the schools database:
1) [Schools Explorer](https://schools.texastribune.org/) which has a page for every district and campus (school) that has the latest metric.  
2) [Higher Education Outcomes Explorer](https://schools.texastribune.org/outcomes/) where we publish cohort information for regions and counties.  
  
When running the scripts to update the School Explorer, **make sure you follow this order when updating the data:** 

1) District boundaries and campus coordinates
2) District and campus entities
3) AskTED
4) TAPR

Updating the Higher Education cohorts explorer is a separate process which can be run independently from the schools explorer part whenever we get new data. 

To get started, assuming your `.env` file is not getting loaded correctly, you can specify the location of `scuole-data` by typing the following in your terminal (in my case the path is ~/Documents/data-projects/schools-explorer/scuole-data):

```sh
export DATA_FOLDER=~/your/local/path/to/scuole-data/

### Updating district boundaries and campus coordinates

We're starting with the simplest one! All you have to do is update the GEOJSONs of the districts and coordinates of the campuses by following the instructions in the [`scuole-data`](https://github.com/texastribune/scuole-data#district-boundaries-and-campus-coordinates) repository. If you're already at this step, it means you've done everything in [`scuole-data`](https://github.com/texastribune/scuole-data) so you're already done with this step.

We will be connecting the new district and campus geographic data by running the script in the following step.

### Updating district and campus entities

In this explorer, we can see data for the entire state, regions, districts, and campuses. Regions typically don't change from year to year, but districts and campuses can be added or removed. As a result, we have to update the district and campus models every year by deleting all existing districts and campus models and using a list provided by TEA to read them to the database. This section relies on district and campus `entities.csv` files created in `scuole-data` to create the models.

First, go to the `data/bootstrap-entities` in the [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) and change the year to the year you are updating for (ex: 2021-2022) for both `bootstrapdistricts_v2` and `bootstrapcampuses_v2`.

Then, you'll get into the shell and start the Python terminal.

```sh
pipenv shell
python manage.py shell
```

Once you're in the Python terminal, run the following to delete the existing district and campus models:

```sh
from scuole.districts.models import District
district = District.objects.all()
district.delete()
from scuole.campuses.models import Campus
campus = Campus.objects.all()
campus.delete()
exit()
```

And finally, run `make data/bootstrap-entities` to re-create the district and campus models with the latest list of districts and campus. This will also connect the district boundaries and campus coordinates from the previous step to their proper entities.

### Updating AskTED data

In this explorer, we have a section at the top of the page of every district and campus (under the map of the district or campus location) where we have school addresses and contact information, along with superintendent and principal contact information. We get this data from [AskTED](https://tealprod.tea.state.tx.us/tea.askted.web/Forms/Home.aspx) which contains a file called [`Download School and District File with Site Address`](https://tealprod.tea.state.tx.us/Tea.AskTed.Web/Forms/DownloadSite.aspx).

To update the data, run:
 
```sh
pipenv shell
make data/update-directories
```

You can also run each command in that block separately, your choice!

If you run into any duplicate key errors during the AskTED update, refer to the [Troubleshooting section](https://github.com/texastribune/scuole#im-seeing-a-duplicate-key-error-when-loading-new-data-into-the-database) for instructions on how to clear the models. You'll need to clear the model that is throwing this error, and reload the data.

There may be data formatting errors with some of the data as its being pulled in. For instance, some of the phone numbers may be invalid. Right now, we have a `phoneNumberFormat` function in the `updatedistrictsuperintendents`, `updatecampusdirectory` and `updatecampusprincipals`. You'll need to edit this function or create new ones if you're running into problems loading the data from AskTED.

However, if you're running into an `Operation Timed Out` error, it's possible that the AskTED has changed the urls where the script can download the data. You will have to go into [`constants.py`](https://github.com/texastribune/scuole/blob/master/scuole/core/constants.py) and change them. 

As of 2023, the spreadsheet was available through [`this link`](https://tealprod.tea.state.tx.us/Tea.AskTed.Web/Forms/DownloadSite.aspx) so it's simple for the script to directly download all of the data we need.

Before 2023, it involved hitting a download button in order to get the correct spreadsheet. We got around that by using a POST request using variables we set up in [`constants.py`](https://github.com/texastribune/scuole/blob/master/scuole/core/constants.py) called `ASKTED_DIRECTORY_VIEWSTATE` or `ASKTED_DIRECTORY_VIEWSTATE`. If they ever change it back to needing to hit a download button, we would need to reset those variables again. To check for the correct values, I look on AskTED's website for the correct download URL, hit the download file button, open up the `Network` tab in the console, look at the request the download file button triggered and check the `Payload` tab.

### Updating TAPR data

This is the big one! This dataset contains all school and district performance scores, student and teacher staff info, graduation rates, attendance, SAT/ACT scores and more. These are the numbers that populate in each district and campus page. Again, if you haven't downloaded, formatted and set up this data following the instructions in the [`scuole-data`](https://github.com/texastribune/scuole-data#district-boundaries-and-campus-coordinates) repository, I strongly recommend you do so.

Once you're done, you'll need to change the year in `make data/latest-school` in the [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) to the latest year (ex: 2021-2022). 

You'll also need to add another line to load in the latest year to `make data/all-schools` also in the [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile). An example, if you're updating for 2021-2022, add `python manage.py loadtaprdata 2021-2022 --bulk`. This is so that if you reset your database or if someone who is new to updating the schools database is setting up, they can upload the data that you are about to add.

To update the data, run:

```sh
pipenv shell
make data/latest-school
```

FYI, the scripts will update data first for the state, then the regions, then the districts and then finally, for the campuses.

Again, if you're running into apostrophe errors and zfill errors, please go back to [`scuole-data`](https://github.com/texastribune/scuole-data#district-boundaries-and-campus-coordinates) repository and format it correctly. 

In addition, sometimes TEA likes to change up accountability ratings by adding new ones. For example, for the 2021-2022 year, scores that were D or Fs were labeled `Not Rated: SB 1365`. When that happens, you might need to go into [`reference.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/models/reference.py) and add them as RATING CHOICES. If you do that, you're changing the models, so don't forget to run `python manage.py makemigrations` and then run `python manage.py migrate`.

### Checking the local server

Either run 

```sh
sh docker-entrypoint.sh
```
or

```sh
python manage.py runserver
```

to fire up the local server. Make sure that statewide, district and campus pages in the school database on your local server are working. If you see any data missing, it might be because TEA changed the column names for some metrics. You can check if there's a disconnect by checking the header name in the spreadsheet you have in the `scuole-data` repository with what's in [`schema_v2.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/schemas/tapr/schema_v2.py). FYI, `short_code` in the schema file is the first letter of the header that pertains to the dataset it belongs to (if it's district data, it's D, if it's campus data, it's C). You can find a full list by going to [`mapping.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/schemas/tapr/mapping.py). 

If they're a mismatch, you can do the following things:

* Either change the column header name in `scuole-data` repository
* or, if you think the change is permananent change the letters in the column header, change the column header in [`schema_v2.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/schemas/tapr/schema_v2.py).


### Updating cohorts data

This is where we update the [Higher Education outcomes cohorts](https://schools.texastribune.org/outcomes/) data. Because this isn't directly connected to the school explorer updates, these can be done either before and after those updates.

First, make sure you have already followed the [`scuole-data`](https://github.com/texastribune/scuole-data#cohorts) instructions on how to download and format the latest cohorts data.

After you've put the latest cohorts data in `scuole-data`, you'll need to add a line to `data/all-cohorts` in the [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) in `scuole` with the latest year. An example, if you're updating for 2012, add `python manage.py loadallcohorts 2012`. Again, this is so that if you reset your database or if someone who is new to updating the schools database is setting up, they can upload the data that you are about to add.

Then, get inside the Python shell:

```sh
pipenv shell
```

Load the data by running:

```sh
python manage.py loadallcohorts <latest year>
```

If you get the error "There should be only XX cohorts", you'll need to delete the `StateCohorts`, `RegionCohorts` and `CountyCohorts` data in the database — the error is likely because old cohorts data does not get cleared out when new data is loaded. [Follow the instructions in the duplicate key error section](https://github.com/texastribune/scuole#im-seeing-a-duplicate-key-error-when-loading-new-data-into-the-database) to delete the data. Make sure you run `python manage.py loadallcohorts` afterwards (without the latest year) so you load in data dating back to 1997 — otherwise, the stacked area charts will not show up.

Also, you will need to change the `latest_cohort_year` variable in **all of the functions** in the [`scuole/cohorts/views.py`](https://github.com/texastribune/scuole/blob/master/scuole/cohorts/views.py) file to reference the latest cohorts school year.

Lastly, make sure the [`scuole/cohorts/schemas/cohorts/schema.py`](https://github.com/texastribune/scuole/blob/master/scuole/cohorts/schemas/cohorts/schema.py) has the correct years (i.e. you'll need to change the year in `8th Grade (FY 2009)` for the reference `'enrolled_8th': '8th Grade (FY 2009)'`, along with the rest of the references.)

### Updating the CSS styling and other static assets

If you make changes to the styles, you'll need to run `npm run build` again to rebuild the `main.css` file in the `assets/` folder that the templates reference.

Then, run `pipenv shell`, followed by `python manage.py collectstatic --noinput` to recollect static files. You'll also need to do a hard refresh in whatever browser you're running the explorer in to fetch the new styles.

### More small changes

1) Update the "Last updated" date on the landing page at `scuole/templates/landing.html`. If you're updating cohorts data, also update the "Last updated" date on the cohorts landing page at `scuole/templates/cohorts_landing.html`.
2) We have several spots in our templates that include metadata about when this explorer was last updated, such as:

- Template: `scuole/templates/base.html`, variable: `dateModified`
- Template: `scuole/templates/cohorts_base.html`, variable: `dateModified` (only modify if you are updating the cohorts data)
- Template: `scuole/templates/includes/meta.html`, variable: `article:modified_time`

You need to change those! They are (probably) important for search.

### Updating the sitemap

When we add new urls, we also need to update the sitemap (`sitemap.xml`) to include those paths. Fortunately, Django has functions that allow us to generate all of the urls associated with an object's views.

To see an example, view any of the `sitemaps.py` files. You'll need to add the sitemap to the `config/urls.py` file, and view the updated sitemap locally at `localhost:8000/sitemap.xml`.

After verifying that the sitemap looks OK locally, copy the content starting from the `<urlset>` tag in `sitemap.xml` and paste it into `scuole/static_src/sitemap.xml` before deploying. You can also run `python manage.py collectstatic --noinput` on the test and production servers to get the updated sitemap.

## Deploying on the test servers

When everything looks good locally, it's time to update the data in the test servers. But first, we need to make sure we can get in the servers.

### Configure your computer to ssh into our test and production servers

In order to get into the test and production servers, you will need to `ssh` into the server. That means you'll need to add some configuration into your computer's ssh configuration file (`.ssh/config`). 

If you haven't created one in your local computer yet, create a directory called `.ssh` by running `mkdir -p ~/.ssh && chmod 700 ~/.ssh` or creating it manually in your User folder. Create a config file by running `touch ~/.ssh/config` and `chmod 600 ~/.ssh/config` to change its permissions.

Open up the `config` file with your favorite text editor. The `Hosts` you are adding are `schools-prod-1`, `schools-prod-2` and `schools-test`. In 1Password's Data Visuals vault, find a file called `Scuole SSH configuration` and copy and paste the contents to the `config` file.

When you're done, save that file and quit.

Next, in 1Password's Data Visuals vault, find two files called `tribtalk-kb.pem`and `Newsapps SSH key`. Create a new directory called `trib` either manually or by running `mkdir -p ~/.ssh/trib && chmod 700 ~/.ssh/trib`. Copy and paste the two files from 1Password using a text editor and save them as `tribtalk-kp.pem` and `newsapps.pem` respectively in your `trib` directory. These are your RSA private keys that will give you permission to `ssh` into the server.

One last step is to make sure both `pem` files have the correct permissions. This can be done by running `chmod 400 ~/.ssh/trib/tribtalk-kp.pem` and `chmod 400 ~/.ssh/trib/newsapps.pem` respectively.

Next, let Engineering know that you have everything set up, and you need to access the servers and they need to whitelist your I.P. address using [Amazon VPC security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html). Once that's set, you will be able to access the server.

In order to test this out, `ssh` into the `schools-test` server by running `ssh schools-test` in your Terminal.

If this is your first time `ssh`-ing into the server, it will give you a prompt something along the lines of:

```
The authenticity of host 'ec2-XX-XXX-XXX-XXX.compute-1.amazonaws.com (XX.XXX.XXX.XXX)' can't be established. 
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Reply 'yes' and you should be in!

If you get an error like this:

```
kex_exchange_identification: Connection closed by remote host
Connection closed by UNKNOWN port 65535
```

It means your I.P. address is still not whitelisted, and you'll have to check back with Engineering.

### Deploying on the test server

First, make sure you have pushed all your changes to Github repos of [scuole](https://github.com/texastribune/scuole) and [scuole-data](https://github.com/texastribune/scuole-data) and merged them into the master branch. These are the versions that are going to be pulled into the test server.

Before you update the data, **YOU MUST DEPLOY ALL OF THE CODE CHANGES FIRST.** This is important, especially if you made any code changes that pertain to the updating process.

### Deploying code changes on the test server

First, we will `ssh` into the `schools-test` server.

```sh
ssh schools-test
```

If you haven't been able to get into any `ssh` server, see the previous section to configure your computer or ask Engineering for help.

The server will have a repository of the `scuole` project. We will need to pull all of the code changes you made into the `scuole` in the test server that you pushed and merged to master.

```sh
cd scuole
git checkout master
git pull
```

When you see all of your code changes get pulled in from the Github repo, it's time to rebuild images of the application and restart the Docker containers with the new images on the test host machines by running:

```sh
make compose/test-deploy
```

Make sure Docker containers are running by running `docker ps` (There should be a container for `web`, `db` and `proxy` services - see `docker-compose.override.yml` for more details).

Once you run these, make sure  your code changes made it through by going to [schools-test](https://schools-test.texastribune.org/). Remeber that these are only code changes, you haven't updated your data yet on the test server so don't expect to see the latest data up on the test server.

### Deploying data updates on the test server

Now, we need to get all of our data changes from `scuole-data` to the test server.

First, get out of the `scuole` repo and get into the `scuole-data` repo:

```sh
cd ..
cd scuole-data
```

Next, get the latest data from your master branch:

```sh
git checkout master
git pull
```

You should see the latest data pulled into the test server from Github.

Next, get inside the Docker container:

```sh
docker exec -i -t scuole_web_1 /bin/ash
```

This is where we will run all of the scripts needed to update the data.

Let's run all migrations so the database is all set up.

```
python manage.py migrate
```

Now, let's update the data in the schools explorer part of the site. **Remember that there's an order to this:**

1) District boundaries and campus coordinates
2) District and campus entities
3) AskTED
4) TAPR

**Updating district boundaries and campus coordinates and district and campus entities**

Just like in the local server, get into the Python terminal and remove the district and campus models:

```sh
python manage.py shell
from scuole.districts.models import District
district = District.objects.all()
district.delete()
from scuole.campuses.models import Campus
campus = Campus.objects.all()
campus.delete()
exit()
```

Lastly, run `make data/bootstrap-entities` to create the district and campus models.

**Updating AskTED**

Run this command to load the latest AskTED data:

```sh
make data/update-directories
```

**Updating TAPR**

Run this command to load the latest TAPR data:

```sh
make data/latest-school
```

If you were able to run this in your local server, then you shouldn't run into any errors! Check if your data updated correctly by going into the [schools-test](https://schools-test.texastribune.org/) url.

**Updating Cohorts**

Run this command to load the latest cohorts data:

```sh
python manage.py loadallcohorts <latest year>
```

If you were able to run this in your local server, then you shouldn't run into any errors! Check if your data updated correctly by going into the [schools-test](https://schools-test.texastribune.org/) url. Congrats! You have just finished updating the test server!

### Factchecking

One final task before deploying it into production is to fact check a few schools to see if the data loaded in correctly. Every year, we recruit other data team members to help out with this process.

We set up a [Schools Explorer Factchecking Google Doc](https://docs.google.com/spreadsheets/d/1z-Zk5pH4n6VEJqMNAYqwlj1cGHnZJXvDP3BCEApWYaY/edit#gid=1870015234) that we update every year to help out the fact-checking process. You want data team members to check at least a few schools and districts with the TAPR data that [TEA makes available](https://rptsvr1.tea.texas.gov/perfreport/tapr/tapr_srch.html?srch=C).

We set up a similar Google Doc to fact check the [Cohorts data](https://docs.google.com/spreadsheets/d/1cBrMpJ9c-h1tSiubhqMj_K5beYiOTfonND_FsTwfbwI/edit#gid=1870015234).

You should also make sure you fact check the statewide numbers in your database with the numbers TEA has.

In addition, you want to hoedown and ask for copy editors to look over any changes to the text or to the disclaimers.

## Deploying on production servers

Hooray! We're ready to update the production servers and deploy it live. Scary! but there are two production servers: `schools-prod-1` and `schools-prod-2` so that means while one is updating, the other is still up.

The other good news is that deployment is similar to how you deployed in the `test` server so much of it should look familiar.

### Deploying code changes on the production server

After checking the test site, you'll need to deploy the code changes on the two production servers: `schools-prod-1` and `schools-prod-2`. You must do both servers — if you don't, the published app will switch between new and old code.

Remember, **YOU MUST DEPLOY ALL OF THE CODE CHANGES FIRST.**

First, we will `ssh` into the `schools-prod-1` server.

```sh
ssh schools-prod-1
```

The server will have a repository of the `scuole` project. We will need to pull all of the code changes you made into the `scuole` into the production server.

```sh
cd scuole
git checkout master
git pull
```

When you see all of your code changes get pulled in from the Github repo, it's time to rebuild images of the application and restart the Docker containers with the new images on the production host machines by running:

```sh
make compose/production-deploy
```

Make sure Docker containers are running by running `docker ps` (There should be a container for `web` and `proxy` services - no `db` container is necessary to be running in the production servers).

If everything runs successfully, run the same steps above for the `schools-prod-2` server.

Congrats, your code changes are now [live](schools.texastribune.org)!

### Deploying data updates on the production server

We're almost there! Now we just need to update the data in the production server. Deploying the data on the production servers will be similar to loading it in locally and on the test server. Fortunately, you only need to push data changes to one server - `schools-prod-1`. Let's go back to `schools-prod-1` server:

```sh
ssh schools-prod-1
```

Let's get all of our new data from the `scuole-data` Github:

```sh
cd scuole-data
git checkout master
git pull
```

You should see the latest data pulled into the production server from Github.

Next, get inside the Docker container:

```sh
docker exec -i -t scuole_web_1 /bin/ash
```

This is where we will run all of the scripts needed to update the data.

Let's run all migrations so the database is all set up.

```
python manage.py migrate
```

First, let's update the data in the schools explorer part of the site. **Remember that there's an order to this:**

1) District boundaries and campus coordinates
2) District and campus entities
3) AskTED
4) TAPR

**Updating district boundaries and campus coordinates and district and campus entities**

Just like in the local and test server, get into the Python terminal and remove the district and campus models:

```sh
python manage.py shell
from scuole.districts.models import District
district = District.objects.all()
district.delete()
from scuole.campuses.models import Campus
campus = Campus.objects.all()
campus.delete()
exit()
```

Lastly, run `make data/bootstrap-entities` to create the district and campus models.

**Updating AskTED**

Run this command to load the latest AskTED data:

```sh
make data/update-directories
```

**Updating TAPR**

Run this command to load the latest TAPR data:

```sh
make data/latest-school
```

**Updating Cohorts**

Run this command to load the latest cohorts data:

```sh
python manage.py loadallcohorts <latest year>
```

Once that's done, check the [live site](https://schools.texastribune.org/). Your changes should be there!

One final thing is that you should make sure you bust the cache for the schools explorer metadata on [Twitter's card validator](https://cards-dev.twitter.com/validator). You can do this by adding a query param to the card URL, like this: `https://schools.texastribune.org/?hello` and previewing the card.

## Quick deploy

Here are the bare bones instructions for updating data and code on the test and production servers, after you're satisfied with your changes locally. To read more, check out the [Updating data](#updating-data) and [Deploying on the test servers](#deploying-on-the-test-servers) and [Deploying on the production servers](#deploying-on-production-servers) sections.

### Deploying code changes

These changes need to be made on the `schools-test`, `schools-prod-1` and `schools-prod-2` servers.

1) Get onto the host machine: `ssh schools-test` (`schools-test` is the host machine. Use `schools-prod-1` and `schools-prod-2` to get onto the production machines.)
2) Get into the code repo: `cd scuole`
3) Get any code changes: `git pull`
4) Rebuild and restart Docker services and containers: `make compose/test-deploy` (`make compose/production-deploy` on the production servers)
5) Make sure Docker containers are running: `docker ps` (There should a container for `web`, `db` and `proxy` services for `schools-test` but only `web` and `proxy` for `schools-prod-1` and `schools-prod-2`)

### Deploying data changes/new data

These changes only need to be made on the `schools-test` and `schools-prod-1` servers.

6) Get into the data repo: `cd scuole-data`
7) Get the latest data: `git pull`
8) Get into the `web` container to make data updates: `docker exec -i -t scuole_web_1 /bin/ash`
9) Run migrations so the database is all set up: `python manage.py migrate`
10) If you're doing a new update and need to update the campus and district models, run through the commands [here](#updating-entities)
11) After you've created new models, run through the rest of the data update:

- AskTED: `make data/update-directories`
- TAPR: `make data/latest-school`
- Cohorts: `python manage.py loadallcohorts <latest-year>`

Before publishing, make sure you make these [small changes](#more-small-changes). 

## Troubleshooting

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

You'll need to delete the `StateCohorts`, `RegionCohorts` and `CountyCohorts` data in the database. Make sure you run `python manage.py loadallcohorts` afterwards (without the latest year) so you load in data dating back to 1997 — otherwise, the stacked area charts will not show up.

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
