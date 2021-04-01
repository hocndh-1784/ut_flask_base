# U1 unit test homework

## Installation and Config

### Require

- OS: Linux
- Python: python3 (python 3.8 is recommended)
- Mysql: mysql  Ver 14.14 Distrib 5.7.24, for Linux (x86_64) (if needed)
- Redis: Redis server v=5.0.3
- Nginx: nginx version: nginx/1.13.12
- Docker: Docker version 18.09.0
- Docker-compose: docker-compose version 1.23.1
- Supervisord: v3.3.1

### Setup environment for development and unittest

- Install `virtualenv`

```bash
pip install virtualenv
```

- Create virtual environment:

```bash
virtualenv -p python3 venv
```

- Active and install dependencies:

```bash
source ./venv/bin/activate
cd project_folder && make deps
```


### Configuration


```bash
cd project_folder     # if needed
make init # to copy secret files
```

- Create database and re-config settings, env file. Example:


```python
# project_folder/settings/development.py

from settings.common import *

# SQLAlchemy override
SQLALCHEMY_DATABASE_URI = 'mysql://test:123456@localhost:3306/database_test'

# Redis override
REDIS_DB = 0
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_TTL = 60

```

```bash
# project_folder/.env

DYNACONF_SETTINGS=settings.development
```

- Make migrations and migrate. Example:

```bash
cd project_folder     # if needed
export APP_ENV=development
make migrate          # if needed
```
Fix if error migrate: https://stackoverflow.com/questions/32311366/alembic-util-command-error-cant-find-identifier

- Add host if environment is development


## Run server

### Run server dev local

```bash
cd project_folder     # if needed
python manager.py
```

### Build with docker

```bash
cd project_folder     # if needed
docker-compose up -d --build
```

## Style Guide for Python Code

- Auto format code with black and isort

```bash
make auto-lint
```

## Unittest


### Configuration

Copy settings file and edit the value according to the `unittest` environment:

```bash
cd project_folder     # if needed
cp settings/unittest.py.orig settings/unittest.py

```

- Re-config settings, env file. Example:


```python
# microservices/settings/unittest.py

from settings.common import *

# SQLAlchemy override
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

# Redis settings
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_TTL = 60

```

```bash
# microservices/.env

DYNACONF_SETTINGS=settings.unittest
```
### Command line
Run all test case
```bash
make test
```

Check style with flake8:

```bash
make lint
```

Coverage all test suites:

```bash
make coverage
```

Coverage with html view

```bash
coverage html
```
