
run:
	flask run --host=0.0.0.0

test:
	flask test

lint:
	flask lint

run-db:
	docker run -p 3307:3306 --name th_api_db tigerhacks-api/dev-db

build-db:
	docker build -f docker/database/Dockerfile -t tigerhacks-api/dev-db .