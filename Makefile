
run:
	flask run --host=0.0.0.0

test:
	flask test

lint:
	flask lint

db:
	docker run --name th_api_db -e MYSQL_ROOT_PASSWORD=tigerhacks2020 mysql:latest