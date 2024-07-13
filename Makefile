# DEV ?= 1

# ifeq ($(DEV), 1)
# 	COMPOSE_FILE = "./docker-compose.dev.yml"
# else
# 	COMPOSE_FILE = "./docker-compose.yml"
# endif

run:
	su -c 'sudo docker compose -f "./docker-compose.yml" up'

COMPOSE_FILE = "./docker-compose.yml"

init: docker-down docker-pull docker-build docker-up
up: docker-up
down: docker-down
restart: docker-down docker-up


COMPOSE_CMD = sudo docker-compose -f $(COMPOSE_FILE)

##################### COMMON COMMANDS
docker-up:
	$(COMPOSE_CMD) up

docker-pull:
	$(COMPOSE_CMD) pull

docker-down:
	$(COMPOSE_CMD) down --remove-orphans

docker-build:
	$(COMPOSE_CMD) build
