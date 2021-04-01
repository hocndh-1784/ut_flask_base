help:
	@echo "  deps        install dependencies using pip"
	@echo "  init        copy examples secret files"
	@echo "  clean       remove compiled files"
	@echo "  migrate     migrate data"
	@echo "  lint        check style with flake8"
	@echo "  auto-lint   auto format code pep8 with black and isort"
	@echo "  test        run all test suites"
	@echo "  coverage    coverage all test suites"

deps:
	pip install -r requirements/requirements-dev.txt

init:
	cp env .env
	cp settings/example.development.py settings/development.py
	cp settings/example.unittest.py settings/unittest.py
	cp settings/example.setting.secret.ini settings/setting.secret.ini

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

migrate:
	/bin/bash migrations/migrate.sh

lint:
	flake8 --exclude=migrations,venv,settings --max-line-length=119 .

auto-lint:
	black . --exclude=migrations,venv --line-length=119
	isort . --skip migrations --skip venv

test:
	pytest .

coverage:
	coverage run -m pytest
	coverage html --include='apps/*' -d ./coverage
