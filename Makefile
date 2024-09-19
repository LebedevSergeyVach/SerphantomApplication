PY = poetry run python

DOCKER_COMPOSE = ./docker-compose.yml
DOCKER_COMPOSE_SERVER = sudo docker compose -f

BUILD = build
UP = up

MANAGE = advertisements/manage.py
RUNSERVER = runserver
MIGRATE = migrate
MAKEMIGRATIONS = makemigrations
COLLECTSTATIC = collectstatic
CREATESUPERUSER = createsuperuser

FLAGS_NO_CACHE = --force-rm --no-cache

.PHONY: all

all: help

runserver: run_local_server
migrate: local_migrate_database
makemigrations: local_makemigrations_database
collectstatic: local_collectstatic_static_files
createsuperuser: local_createsuperuser_database

up: docker-up
build: docker-build
build-no-cache: docker-build-no-cache
clear: docker-clear-cache

help: help-makefile


run_local_server:
	@$(PY) $(MANAGE) $(RUNSERVER)

local_migrate_database:
	@$(PY) $(MANAGE) $(MIGRATE)

local_makemigrations_database:
	@$(PY) $(MANAGE) $(MAKEMIGRATIONS)

local_collectstatic_static_files:
	@$(PY) $(MANAGE) $(COLLECTSTATIC)

local_createsuperuser_database:
	@$(PY) $(MANAGE) $(CREATESUPERUSER)


docker-up:
	@$(DOCKER_COMPOSE_SERVER) "$(DOCKER_COMPOSE)" $(UP)

docker-build:
	@$(DOCKER_COMPOSE_SERVER) "$(DOCKER_COMPOSE)" $(BUILD)

docker-build-no-cache:
	@$(DOCKER_COMPOSE_SERVER) "$(DOCKER_COMPOSE)" $(BUILD) $(FLAGS_NO_CACHE)

docker-clear-cache:
	@yes y | sudo docker container prune && yes y | sudo docker builder prune && sudo docker image prune -a -f


help-makefile:
	@echo -e "Makefile fot SerphantomApplication\n"
	@echo -e "Django Framework:\nrunserver        ->  starting a local server\nmigrate          ->  starting database and project migration\nmakemigrations   ->  preparing to launch database and project migrations\ncollectstatic    ->  collecting static files in the staticfiles directory\ncreatesuperuser  ->  creating a superuser in the framework database\n"
	@echo -e "Docker-compose on server:\nup               ->  starting the operation of the assembled docker container\nbuild            ->  starting the build of the docker container of the project\nbuild-no-cache   ->  running a docker project container build without using the cache\nclear            ->  starting to clear the cache from docker builder, container, image"
