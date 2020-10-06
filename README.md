# TigerHacks 2020 API

Built with love, sweat, and grease by @ccarterlandis and @Ulincsys.

### Running locally

Run the following commands to bootstrap the environment:

```bash
cd tigerhacks_api
pip install -r requirements/dev.txt
flask run --host=0.0.0.0 #server has hot-reloading, no -e is needed
```
Make sure everything is configured correctly in `.env`.

For **local** development, using the packaged Docker database container, you can use the following config as a jumping-off point:
```
# Environment variable overrides for local development
FLASK_APP=tigerhacks_api/__init__.py
FLASK_DEBUG=1
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://th2020admin:th2020adminpassword@localhost:3307/tigerhacks-api
GUNICORN_WORKERS=1
LOG_LEVEL=debug
SECRET_KEY=not-so-secret
SEND_FILE_MAX_AGE_DEFAULT=0
```

#### Database (development)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
$ make build-db #build the Docker DB image
$ make run-db #start a container with image
$ docker stop th_api_dev_db; docker rm th_api_dev_db; #to stop and remove the database
```

## Deployment

**DON'T FORGET TO CHANGE THE PASSWORD & SECRETS FOR THE ADMINS + THE DB**

Without Docker:
```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
export DATABASE_URL="<YOUR DATABASE URL>"
npm run build   # build assets with webpack
flask run       # start the flask server
```

## Shell

To open the interactive shell, run

```bash
flask shell # If running locally without Docker
```

By default, you will have access to the flask `app`.

## Running Tests/Linter

To run all tests, run

```bash
flask test # If running locally without Docker
```

To run the linter, run

```bash
flask lint # If running locally without Docker
```

The `lint` command will attempt to fix any linting/style errors in the code. If you only want to know if the code will pass CI and do not wish for the linter to make changes, add the `--check` argument.

## Docs

Coming soon!

## CI/CD

Coming soon!

<!--
## Docker Quickstart

This app can be run completely using `Docker` and `docker-compose`. **Using Docker is recommended, as it guarantees the application is run using compatible versions of Python and Node**.

There are three main services:

To run the development version of the app

```bash
docker-compose up flask-dev
```

To run the production version of the app

```bash
docker-compose up flask-prod
```

The list of `environment:` variables in the `docker-compose.yml` file takes precedence over any variables specified in `.env`.

To run any commands using the `Flask CLI`

```bash
docker-compose run --rm manage <<COMMAND>>
```

Therefore, to initialize a database you would run

```bash
docker-compose run --rm manage db init
docker-compose run --rm manage db migrate
docker-compose run --rm manage db upgrade
```

A docker volume `node-modules` is created to store NPM packages and is reused across the dev and prod versions of the application. For the purposes of DB testing with `sqlite`, the file `dev.db` is mounted to all containers. This volume mount should be removed from `docker-compose.yml` if a production DB server is used.
 -->