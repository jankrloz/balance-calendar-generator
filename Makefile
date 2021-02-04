SHELL=/bin/bash

ifndef VERBOSE
.SILENT:
endif

VENV_PATH := .venv
export COMPOSE_PROJECT_NAME=table-to-core-model

DOCKER-COMPOSE=docker-compose \
		-f ./docker-compose.yml

venv:
	@echo "Creating virtual environment ..."
	@if [ ! -d $(VENV_PATH) ]; then python3 -m venv --copies $(VENV_PATH); fi;

install: venv
	@echo "Installing dependencies locally"
	@( \
		source $(VENV_PATH)/bin/activate; \
		pip install -qU pip; \
		pip install -r requirements.txt; \
	)

build.force: PARAMS = --no-cache
build build.force:
	$(DOCKER-COMPOSE) build --parallel --force-rm --pull $(PARAMS)

start: install
	echo "*** Starting up services ***"
	$(DOCKER-COMPOSE) up -d

restart: stop start

start.fresh: clean build start
	echo "*** Fresh starting up services ***"

stop:
	echo "*** Stopping services ***"
	$(DOCKER-COMPOSE) down

clean:
	echo "*** Cleaning up services ***"
	$(DOCKER-COMPOSE) rm -fsv

clean.full:
	echo "*** BOOM! ***"
	$(DOCKER-COMPOSE) down -v --rmi all

bash:
	$(DOCKER-COMPOSE) run main /bin/sh

status:
	echo "*** Status of containers ***"
	$(DOCKER-COMPOSE) ps


debug: PARAMS = -f
logs debug: start
	echo "*** Showing containers logs ***"
	$(DOCKER-COMPOSE) logs -t $(PARAMS)


black:
	@black . --exclude=venv --check;

isort:
	@isort --check-only;

autoflake:
	@autoflake --recursive --exclude venv --check --remove-all-unused-imports --remove-unused-variables ./;

mypy:
	@mypy app.py core;

lint: black isort mypy autoflake

lint-fix:
	@( \
		black . --exclude=$(VENV_PATH); \
		isort --force-single-line-imports --quiet --apply -l=250 .; \
		autoflake --recursive --exclude $(VENV_PATH) --in-place --remove-all-unused-imports ./; \
	)
