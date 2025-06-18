migrate:
    poetry run python manage.py migrate
run-server:
    poetry run python manage.py runserver
make-migrations:
    poetry run python manage.py makemigrations

docker-up:
    docker compose up -d
docker-down:
    docker compose down
init_db:
    poetry run python manage.py init_db
lint:
    black . && isort .