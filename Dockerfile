FROM ubuntu
ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_VERSION="1.3.2"
RUN apt-get update && apt-get install -y apt-transport-https
RUN DEBIAN_FRONTEND=noninteractive apt install -y nginx python3 python3-pip gunicorn sudo nano postgresql-contrib libpq-dev
COPY . /srv/telegram_admin
WORKDIR /srv/telegram_admin
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 - && \
    poetry --version
RUN poetry install --no-root
RUN poetry run mypy . --config-file mypy.ini --no-namespace-packages
RUN cp /srv/telegram_admin/nginx.conf /etc/nginx/sites-available/default
RUN chown -R www-data:www-data /srv && chmod +x /srv/telegram_admin/entrypoint.sh && chmod +x /srv