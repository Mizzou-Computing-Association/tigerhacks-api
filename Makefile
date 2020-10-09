
run:
	flask run --host=0.0.0.0

test:
	flask test

lint:
	flask lint

run-dev-db: build-db
	- docker stop th_api_dev_db
	- docker rm th_api_dev_db
	docker run -p 3307:3306 --name th_api_dev_db tigerhacks_api/dev_db

build-dev-db:
	docker build -f docker/database/Dockerfile -t tigerhacks_api/dev_db .