COMPOSE_PATH = ./compose.yaml
COMPOSE = docker compose -f $(COMPOSE_PATH)

all: up

up:
	@$(COMPOSE) up -d --build

start:
	@$(COMPOSE) start

stop:
	@$(COMPOSE) stop

down:
	@$(COMPOSE) down

clean:
	@make down
	@docker system prune -f
	@docker volume rm $$(docker volume ls -q)

dev-config:
	python3 -m venv ./venv;
	. ./venv/bin/activate; \
	pip3 install --upgrade pip;\
	pip3 install -r ./requirements.dev --no-cache-dir;\
	pre-commit install;

dev-run-server:
	make dev-config; \
	. ./venv/bin/activate;\
	python3 ./django/project/manage.py runserver
