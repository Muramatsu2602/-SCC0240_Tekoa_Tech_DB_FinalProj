.PHONY: start stop

build:
	docker-compose build

start: build
	docker-compose up -d
	docker-compose run app bash

stop:
	docker-compose down
