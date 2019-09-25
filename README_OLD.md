But first, let's create a Docker container on your local machine to make sure it's working. This will mirror what we'll do on test/production servers later. Make sure you're in the `scuole` directory and run:

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

```sh
python manage.py shell
```

For instance, if you're updating cohorts, make sure the data is correct:

```python
from scuole.states.models import *
StateCohorts.objects.get(year__name = '2007-2008',ethnicity='African American',gender='',economic_status='').enrolled_8th
```

You will need to change the school year to fit the year you are updating. Once that's done, it should spit out the number you see in the "Class size" column for "Black" students in first table under "Ethnicity" on the page.

Alternatively, you can make your own query and check something else on the page.
