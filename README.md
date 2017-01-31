# scuole
*(It's Italian for "schools.")*

Public Schools 3!

## Install

This project assumes you are using the provided docker postgreSQL database build. Make sure docker is up and running, then run:

```sh
make docker/db
```

This will create the data volume and instance of PostgreSQL for Django. To ensure Django knows where to look, you need to set the `DATABASE_URL`. If you are not using the docker provided database, use `DATABASE_URL` to tell the app what you've done instead.

```sh
export DATABASE_URL=postgres://docker:docker@docker.local:5432/docker
```

From there, the app should be runnable as normal.

Create your virtual environment:

```sh
mkvirtualenv scuole-dev
```

Then install the requirements:

```sh
pip install -r requirements/local.txt
```

Check for any migrations:

```sh
python manage.py migrate
```

Then see if it'll run:

```sh
python manage.py runserver
```

All good? Let's go!

## Admin

This likely won't have an admin interface, but you are welcome to use it to check out how things are getting loaded. First, you'll need to create a super user. (If you ever blow away your database, you'll have to do it again!)

```sh
python manage.py createsuperuser
```

Then, after a `python manage.py runserver`, you can visit [http://localhost:8000/admin](http://localhost:8000/admin) and use the credentials you setup to get access. Every thing will be set to read-only, so there's no risk of borking anything.

-------------
## Setup

Make sure you have the latest updates ...

    git pull origin 2016-update

... And that you're on the `master` branch: 

    git checkout -b master

Change your working directory to `scuole` and activate your virtual environment:

    cd scuole
    workon scuole-dev

Remind your computer where the data is. Do this every time you close the Terminal, or your computer:

    source .env

Reset the database for the *freshest* data:

    make local/reset-db

Make a new database:

    make data/base

Open a python shell in your Terminal:

    python manage.py shell_plus

Now you're ready to extract data!

----
## Usage

NOTE: Save all of your scripts in their own .py files for easy future access.

First, load the Python CSV library: 

    import csv

Import the District and DistrictStats models. You can replace each instance of 'district' with 'state' or 'campus' for state or campus data. Change the `year__name` for older data.

    from scuole.districts.models import District, DistrictStats

    district_stats = DistrictStats.objects.filter(year__name='2015-2016')

Copy-paste the fields you need in the array. A list of some of the field names can be found in `scuole > scuole > stats > schemas > tapr > schema.py`

    fields = [
        'all_students_count'
    ]

Change `student_count.csv` to the filename of your choice and add fields in the `writer.writerow` arrays. Don't forget to declare each new field in a new line before `field_data`.

    with open('student_count.csv', 'w') as fo:
        writer = csv.writer(fo)
        writer.writerow(['district', 'district_id', 'district_url']+fields)
        for stat in district_stats:
            district_name = stat.district.name
            district_id = stat.district.tea_id
            district_url = stat.district.get_absolute_url()
            field_data = [getattr(stat, i) for i in fields]
            writer.writerow([district_name, district_id, district_url] + field_data)

You may have to hit `enter` twice to run the script, but once it's done your .csv file can be found in your `scuole` folder! If it's a large dataset, wait a few minutes before opening the .csv file or it may appear incomplete.

Once you're done, type `exit()` to stop the python shell.
