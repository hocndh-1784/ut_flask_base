FROM python:3.8

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Copy code
ENV APP /code
RUN mkdir $APP
COPY . /code
WORKDIR $APP

# Install dependencies
RUN pip install -r requirements/common.txt

# Config supervisor
COPY settings/supervisor/supervisord_local.conf /etc/supervisor/conf.d
COPY settings/supervisor/supervisord.conf /etc/supervisor

# Config env
COPY ./env /code/.env

# Migrate data
CMD ["/bin/bash", "/code/migrations/migrate.sh"]

# Runserver
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
