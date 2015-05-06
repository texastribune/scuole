# scuole
*(It's Italian for "schools.")*

Public Schools 3!

# Setup

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
