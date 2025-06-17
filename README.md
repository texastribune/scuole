# scuole

*(It's Italian for "schools.")*

Public Schools 3!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Intro](#intro)
  - [About the Servers](#about-the-servers)
  - [About the Data](#about-the-data)
- [Run outstanding migrations](#run-outstanding-migrations)
- [Fire up the server](#fire-up-the-server-with-latest-stable-dataset)
- [Integrate new data](#integrate-new-data)
  - [Update Makefile to reflect current year](#update-makefile-to-reflect-current-year)
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
- [Workspace](#workspace)
- [Admin](#admin)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Intro
If this is your first time setting up the schools database, please start with [README_SETUP.md](README_SETUP.md). The remainder of this Readme is focused on running updates to data in the Schools Explorer. Every year, we need to update cohorts, TAPR, district boundaries, campus coordinates and the entities files for districts and campuses.

### About the Servers
The Schools Explorer has a local, staging, and production setup, which can be mostly standardized through Docker containerization. Production has two servers, which is handy in case you want to test deployment to one while keeping the other intact in case you need to quickly roll back changes. 

The local and staging environment both connect to local PostgreSQL databases with the PostGIS extension, whereas production uses an external Postgres database hosted on AWS.

### About the Data
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

To get started, make sure your `.env` file is getting loaded correctly.  the following in your terminal (in my case the path is ~/Documents/data-projects/schools-explorer/scuole-data):

```sh
echo $DATA_FOLDER
```

If this returns nothing or points to the wrong folder, you can manually specify the location of `scuole-data` by typing `export DATA_FOLDER=~/your/local/path/to/scuole-data/`in terminal.

## Run outstanding migrations

If you or another developer have made changes to data structures (models) in Django, you'll need to run the following to catch up with any outstanding migrations you might have:

```sh
python manage.py migrate
```

## Fire up the server with latest stable dataset

Make sure Docker is running and step into a Docker shell.

```sh
make docker/db 
make docker/shell
```

If you're actively troubleshooting/debugging newly integrated data, you may need to roll back the database to the last stable instance. To do so, first go to the `data/bootstrap-entities` in the [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) and change the year to the last stable year (e.g. 2021-2022) for both `bootstrapdistricts_v2` and `bootstrapcampuses_v2`.

If you need to start from a clean slate, load in the prior year's data; first `make local/reset-db`, then `sh bootstrap.sh`. This may take ~10 minutes to run.

Next, collect static files and fire up the server. Previous instructions suggested ```sh docker-entrypoint.sh``` but in my experience this breaks the css. Try this instead:

```sh
python manage.py collectstatic --noinput
python manage.py runserver
```

Open up the schools database in your [local server](http://localhost:8000/) and make sure that all of the information is there and the pages are working correctly. You can compare it to the [live version of the school's database](https://schools.texastribune.org/).

All good? Let's go! There are also other commands in scuole's [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) at your disposal so check them out.

## Integrate new data

If you're server's running in Terminal, you'll need open a new tab in terminal and get into another Docker shell.

```sh
make docker/shell
```

### Update Makefile to reflect current year

You'll need to update the Makefile in three places to ensure the scripts pull your latest data.

1) Go to the `data/bootstrap-entities` in the [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) and change the year to the year you are updating for (ex: 2021-2022) for both `bootstrapdistricts_v2` and `bootstrapcampuses_v2`.

```sh
data/bootstrap-entities:
	python manage.py bootstrapdistricts_v2 2021-2022
	python manage.py dedupedistrictslugs
	python manage.py bootstrapcampuses_v2 2021-2022
	python manage.py dedupecampusslugs
  ```

2) For `data/latest-school`, change the year to the latest year (e.g. 2022-2023). 
3) For `data/all-schools` update the add another line to load in the latest year. As an example, if you're updating for 2022-2023, add `python manage.py loadtaprdata 2022-2023 --bulk`. This is so that if you reset your database or if someone who is new to updating the schools database is setting up, they can upload the data that you are about to add.


### Updating district boundaries and campus coordinates

If you've already updated the GEOJSONs of the districts and coordinates of the campuses as instructed in the [`scuole-data`](https://github.com/texastribune/scuole-data#district-boundaries-and-campus-coordinates) repo, you're already done with this step. We will be connecting this new district and campus geographic data by running the script in the following step.

### Updating district and campus entities

In this explorer, we can see data for the entire state, regions, districts, and campuses. Regions typically don't change from year to year, but districts and campuses can be added or removed. As a result, we have to update the district and campus models every year by deleting all existing districts and campus models and using a list provided by TEA to read them to the database. This section relies on district and campus `entities.csv` files created in `scuole-data` to create the models.

Start the Python terminal.

```sh
python manage.py shell
```

From the Python terminal, run the following to delete the existing district and campus models (runtime ~1 minute):

```sh
from scuole.districts.models import District
district = District.objects.all()
district.delete()
from scuole.campuses.models import Campus
campus = Campus.objects.all()
campus.delete()
exit()
```

And finally, run the following to re-create the district and campus models with the latest list of districts and campus. This will also connect the district boundaries and campus coordinates from the previous step to their proper entities (runtime ~2 minutes).

```sh
make data/bootstrap-entities
```

### Updating AskTED data

In this explorer, we have a section at the top of the page of every district and campus (under the map of the district or campus location) where we have school addresses and contact information, along with superintendent and principal contact information. We get this data from [AskTED](https://tealprod.tea.state.tx.us/tea.askted.web/Forms/Home.aspx) which contains a file called [`Download School and District File with Site Address`](https://tealprod.tea.state.tx.us/Tea.AskTed.Web/Forms/DownloadSite.aspx).

To update the data, run (runtime ~2 minutes):
 
```sh
make data/update-directories
```

**troubleshooting notes**  
If you run into any duplicate key errors during the AskTED update, refer to the [troubleshooting readme](README_TROUBLESHOOTING.md) for instructions on how to clear the models. You'll need to clear the model that is throwing this error, and reload the data.

There may be data formatting errors with some of the data as its being pulled in. For instance, some of the phone numbers may be invalid. Right now, we have a `phoneNumberFormat` function in the `updatedistrictsuperintendents`, `updatecampusdirectory` and `updatecampusprincipals`. You'll need to edit this function or create new ones if you're running into problems loading the data from AskTED.

However, if you're running into an `Operation Timed Out` error, it's possible that the AskTED has changed the urls where the script can download the data. You will have to go into [`constants.py`](https://github.com/texastribune/scuole/blob/master/scuole/core/constants.py) and change them. 

As of 2023, the spreadsheet was available through [`this link`](https://tealprod.tea.state.tx.us/Tea.AskTed.Web/Forms/DownloadSite.aspx) so it's simple for the script to directly download all of the data we need.

Before 2023, it involved hitting a download button in order to get the correct spreadsheet. We got around that by using a POST request using variables we set up in [`constants.py`](https://github.com/texastribune/scuole/blob/master/scuole/core/constants.py) called `ASKTED_DIRECTORY_VIEWSTATE` or `ASKTED_DIRECTORY_VIEWSTATE`. If they ever change it back to needing to hit a download button, we would need to reset those variables again. To check for the correct values, I look on AskTED's website for the correct download URL, hit the download file button, open up the `Network` tab in the console, look at the request the download file button triggered and check the `Payload` tab.

### Updating TAPR data

This is the big one! This dataset contains all school and district performance scores, student and teacher staff info, graduation rates, attendance, SAT/ACT scores and more. These are the numbers that populate in each district and campus page.

To update the data, run:

```sh
make data/latest-school
```

FYI, the scripts will update data first for the state, then the regions, then the districts and then finally, for the campuses.

Sometimes TEA likes to change up accountability ratings by adding new ones. For example, for the 2021-2022 year, scores that were D or Fs were labeled `Not Rated: SB 1365`. When that happens, you might need to go into [`reference.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/models/reference.py) and add them as RATING CHOICES. If you do that, you're changing the models, so don't forget to run `python manage.py makemigrations` and then run `python manage.py migrate`.

### Checking the local server

Either run ```docker-entrypoint.sh``` or ```python manage.py runserver``` to fire up the [local server](http://localhost:8000/). Make sure that statewide, district and campus pages in the school database on your local server are working. If you see any data missing, it might be because TEA changed the column names for some metrics. You can check if there's a disconnect by checking the header name in the spreadsheet you have in the `scuole-data` repository with what's in [`schema_v2.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/schemas/tapr/schema_v2.py). FYI, `short_code` in the schema file is the first letter of the header that pertains to the dataset it belongs to (if it's district data, it's D, if it's campus data, it's C). You can find a full list by going to [`mapping.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/schemas/tapr/mapping.py). 

If they're a mismatch, you can do the following things:

* Either change the column header name in `scuole-data` repository
* or, if you think the change is permananent change the letters in the column header, change the column header in [`schema_v2.py`](https://github.com/texastribune/scuole/blob/master/scuole/stats/schemas/tapr/schema_v2.py).


### Updating cohorts data

This is where we update the [Higher Education outcomes cohorts](https://schools.texastribune.org/outcomes/) data. Because this isn't directly connected to the school explorer updates, these can be done either before and after those updates.

First, make sure you have already followed the [`scuole-data`](https://github.com/texastribune/scuole-data#cohorts) instructions on how to download and format the latest cohorts data.

After you've put the latest cohorts data in `scuole-data`, you'll need to add a line to `data/all-cohorts` in the [`Makefile`](https://github.com/texastribune/scuole/blob/master/Makefile) in `scuole` with the latest year. An example, if you're updating for 2012, add `python manage.py loadallcohorts 2012`. Again, this is so that if you reset your database or if someone who is new to updating the schools database is setting up, they can upload the data that you are about to add.

Then, get inside the ?Python? shell:

```sh
# pipenv shell
make docker/shell
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

Then, run `make docker/shell`, followed by `python manage.py collectstatic --noinput` to recollect static files. You'll also need to do a hard refresh in whatever browser you're running the explorer in to fetch the new styles.

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

Once you run these, make sure  your code changes made it through by going to [schools-test](https://schools-test.texastribune.org/). Remember that these are only code changes, you haven't updated your data yet on the test server so don't expect to see the latest data up on the test server.

### Deploying data updates on the test server

Now, we need to get all of our data changes from `scuole-data` to the test server.

First, get out of the `scuole` repo and get into the `scuole-data` repo:

```sh
cd ../scuole-data
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

Make sure Docker containers are running by running `docker ps` (There should be a container for `web` and `proxy` services - no `db` container is necessary to be running in the production servers). If one or more containers are missing you can check their status with `docker ps -a`.

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
