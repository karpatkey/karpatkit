CONFIG_PATH ?= kkit_config.json
image := karpatkit
path := src/karpatkit src/defabipedia
repo_dir := $(shell git rev-parse --show-toplevel)
docker_run := docker run --rm -i \
  --user kkit \
  -v $(PWD):/repo \
  -e KARPATKIT_CACHE_ENABLE=$(KARPATKIT_CACHE_ENABLE) \
  -e KARPATKIT_CACHE_CLEAR=$(KARPATKIT_CACHE_CLEAR) \
  -e KKIT_CFG=$(CONFIG_PATH)



.PHONY: install-pre-commit
install-pre-commit:
	@cp $(repo_dir)/.pre-commit $(repo_dir)/.git/hooks/pre-commit
	@echo "The pre-commit hook has been installed."


.PHONY: build
build:
	@docker build -t $(image) .


.PHONY: build-if-no-image
build-if-no-image:
	@docker inspect --type=image $(image) > /dev/null || docker build -t $(image) .


.PHONY: shell
shell: build-if-no-image
	@$(docker_run) -t -v $(PWD)/src/karpatkit:/usr/local/lib/python3.10/site-packages/karpatkit -v $(PWD)/src/defabipedia:/usr/local/lib/python3.10/site-packages/defabipedia $(image) bash

.PHONY: test
test: build-if-no-image
	@$(docker_run) $(image) pytest -vs src/karpatkit/tests


.PHONY: lint-black
lint-black: build-if-no-image
	@echo "Check black..."
	@echo "=============="
	@$(docker_run) $(image) black --fast --check $(path)


.PHONY: lint-isort
lint-isort: build-if-no-image
	@echo "Check isort..."
	@echo "=============="
	@$(docker_run) $(image) isort --check $(path)

.PHONY: lint-pretty_json
lint-pretty_json: build-if-no-image
	@echo "Check pretty_json..."
	@echo "=============="
	@$(docker_run) $(image) pretty_json --check $(path)


.PHONY: lint-flake8
lint-flake8: build-if-no-image
	@echo "Check flake8..."
	@echo "==============="
	@$(docker_run) $(image) flake8 $(path)


.PHONY: lint
lint: lint-black lint-isort lint-flake8 lint-pretty_json
	@echo "Linter rules [OK]"


.PHONY: black
black: build-if-no-image  ## Apply black.
	@echo
	@echo "Applying black..."
	@echo "================="
	@echo
	@$(docker_run) $(image) black --fast $(path)
	@echo


.PHONY: isort
isort: build-if-no-image  ## Apply isort.
	@echo "Applying isort..."
	@echo "================="
	@echo
	@$(docker_run) $(image) isort $(path)

.PHONY: pretty-json
pretty-json: build-if-no-image
	@echo "Applying pretty_json..."
	@echo "================="
	@echo
	@$(docker_run) $(image) pretty_json $(path)

.PHONY: pretty
pretty: isort black pretty-json


.PHONY: cacheclear
cacheclear: build-if-no-image
	@echo "Clearing the API requests cache..."
	@echo "=================================="
	@echo
	@$(docker_run) $(image) python -c "import karpatkit.cache as c; c.clear()" 
