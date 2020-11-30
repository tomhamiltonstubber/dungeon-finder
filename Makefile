black = black -S -l 120 --target-version py38

.PHONY: install
install:
	pip install -r src/requirements.txt

.PHONY: install-dev
install-dev: install
	pip install -r tests/requirements.txt

.PHONY: install-others
install-others:
	yarn install

.PHONY: format
format:
	isort src
	$(black) src

.PHONY: lint
lint:
	flake8 src
	isort --check-only src
	$(black) --check src

.PHONY: test
test:
	pytest tests/ --cov=src

.PHONY: reset-db
reset-db:
	psql -h localhost -U postgres -c "DROP DATABASE IF EXISTS dungeonfinder"
	psql -h localhost -U postgres -c "CREATE DATABASE dungeonfinder"


.PHONY: reset-test-db
reset-test-db:
	psql -h localhost -U postgres -c "DROP DATABASE IF EXISTS dungeonfinder_test"
	psql -h localhost -U postgres -c "CREATE DATABASE dungeonfinder_test"
