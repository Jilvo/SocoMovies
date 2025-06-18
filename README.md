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

2. From the root of the project (where `docker-compose.yml` is located), run:

   ```bash
   docker compose up --build
   ```

- Backend will be available at http://localhost:8000/api/

- Frontend will be available at http://localhost:80

# If needed:
you can init movies with 
   ```bash
   poetry run python manage.py init_db
   ```