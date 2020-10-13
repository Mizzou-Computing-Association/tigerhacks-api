default:
	@ echo "install - Install Python deps"
	@ echo "run - Start app"
	@ echo "test - Run tests"
	@ echo "lint - Run linter & code formatter"
	@ echo "db - Start Docker database"
	@ echo "stop-db - Stop Docker database"
	@ echo "rm-db - Delete Docker database"
	@ echo "refresh-db - Reset the database"

install:
	pip install -r requirements/dev.txt

run:
	flask run --host=0.0.0.0

test:
	flask test

lint:
	flask lint

db:
	docker run -p 3307:3306 --name th_api_dev_db tigerhacks_api/dev_db

refresh-db: stop-db rm-db build-db db

build-db:
	docker build -f docker/database/Dockerfile -t tigerhacks_api/dev_db .

stop-db:
	- docker stop th_api_dev_db

rm-db: stop-db
	- docker rm th_api_dev_db

