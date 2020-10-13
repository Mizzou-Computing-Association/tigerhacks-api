# TigerHacks 2020 API

Built with love, sweat, and grease by @ccarterlandis and @Ulincsys.

Lines starting with `$` denote a Bash command.

### Running locally

Run the following commands to bootstrap the environment:

```bash

# clone & enter the repo
$ git clone https://github.com/Mizzou-Computing-Association/tigerhacks_api.git
$ cd tigerhacks_api

# install Python dependencies
$ pip install -r requirements/dev.txt

# copy default credentials
$ cp .env-example .env

# start the database
$ make db

# start the server
$ flask run
```

Make sure everything is configured correctly in the `.env` file. For **local** development, using the packaged Docker database container, you can use the following config as a jumping-off point (this is also in `.env-example`):
```
# Environment variable overrides for local development
FLASK_APP=tigerhacks_api/__init__.py
FLASK_DEBUG=1
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://th2020admin:th2020adminpassword@localhost:3307/tigerhacks_api
GUNICORN_WORKERS=1
LOG_LEVEL=debug
SECRET_KEY=not-so-secret
SEND_FILE_MAX_AGE_DEFAULT=0
```

#### Database (development)

Below are the make commands for interacting with the database container.

```bash

# start the database container in the background
$ make db

# stop the database container
$ make stop-db;

# delete the database container (must be stopped first)
$ make rm-db;

# stop and removing the container, rebuild the image, then start the database container
$ make refresh-db;
```

#### API Keys

All requests must include a valid API key. The API key will be automatically set when the server first connects to the database, and will use the same key until the database is reset. The server will print your API key every time it starts up.

Include the API key as in header called `X-TigerHacks-API-Key` when making the request to `api/register`. The server will respond appropriately if you did not pass a key at all, or you passed an incorrect key.
