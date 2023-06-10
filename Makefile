.PHONY: start stop

build:
	sudo docker-compose build

start: build
	sudo docker-compose up -d
	sudo docker-compose run app bash

stop:
	sudo docker-compose down
