# SocoMovies.io

## Contents

- **Backend**: Django REST Framework API, managed with Poetry.
- **Frontend**: Vue.js application.
- **Docker**: Docker Compose configuration to run both services together.


## Prerequisites

- Docker & Docker Compose installed.

## Quick Start with Docker Compose

1. Clone the repository:
   ```bash
   git clone https://github.com/Jilvo/SocoMovies.io.git
   cd <repository-directory>
   ```

Project use Poetry
back-end :
poetry run python manage.py runserver


docker build -t soco-backend-service .


just doc


for dockerfile 

➜  soco-backend-service git:(main) ✗ poetry env info --path

/home/jilvo/soco_movies.io/SocoMovies.io/soco-backend-service/.venv
➜  soco-backend-service git:(main) ✗ source $(poetry env info --path)/bin/activate

(soco-backend-service-py3.12) ➜  soco-backend-service git:(main) ✗ python manage.py runserver