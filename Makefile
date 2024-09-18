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

all: runserver

runserver: run_local_server
migrate: local_migrate_database
makemigrations: local_makemigrations_database
collectstatic: local_collectstatic_static_files
createsuperuser: local_createsuperuser_database

up: docker-up
build: docker-build
build-no-cache: docker-build-no-cache
clear: docker-clear-cache


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
