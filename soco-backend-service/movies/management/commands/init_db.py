# Place this file in movies/management/commands/init_db.py
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from movies.models import Actor, Movie, Review


class Command(BaseCommand):
    help = "Create a superuser and populate the database with sample data."

    # def add_arguments(self, parser):
    #     parser.add_argument('--username', default='admin', help='Username for the superuser')
    #     parser.add_argument('--email', default='admin@example.com', help='Email for the superuser')
    #     parser.add_argument('--password', default='admin123', help='Password for the superuser')

    def handle(self, *args, **options):
        # User = get_user_model()
        # username = options['username']
        # email = options['email']
        # password = options['password']

        # # Create superuser if not exists
        # if not User.objects.filter(username=username).exists():
        #     User.objects.create_superuser(username=username, email=email, password=password)
        #     self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created."))
        # else:
        #     self.stdout.write(f"Superuser '{username}' already exists.")

        # Sample actors with first and last names
        sample_actors = [
            {"first_name": "Leonardo", "last_name": "DiCaprio"},
            {"first_name": "Joseph", "last_name": "Gordon-Levitt"},
            {"first_name": "Elliot", "last_name": "Page"},
        ]
        actors = {}
        for data in sample_actors:
            actor, _ = Actor.objects.get_or_create(
                first_name=data["first_name"], last_name=data["last_name"]
            )
            key = f"{data['first_name']} {data['last_name']}"
            actors[key] = actor
        self.stdout.write(self.style.SUCCESS(f"{len(actors)} actors ensured."))

        # Sample movies
        movies_data = [
            {
                "title": "Inception",
                "description": "Film de science-fiction de Christopher Nolan.",
                "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
            },
            {
                "title": "The Dark Knight",
                "description": "Batman face au Joker.",
                "actors": [],
            },
        ]
        for data in movies_data:
            movie, created = Movie.objects.get_or_create(
                title=data["title"], defaults={"description": data["description"]}
            )
            if created:
                for actor_name in data["actors"]:
                    if actor_name in actors:
                        movie.actors.add(actors[actor_name])
                self.stdout.write(self.style.SUCCESS(f"Movie '{movie.title}' created."))
            else:
                self.stdout.write(f"Movie '{movie.title}' already exists.")

        # Sample reviews (no comment field on Review model)
        reviews_data = [
            {"movie_title": "Inception", "rating": 5},
            {"movie_title": "The Dark Knight", "rating": 4},
        ]
        for rev in reviews_data:
            movie = Movie.objects.get(title=rev["movie_title"])
            review, created = Review.objects.get_or_create(
                movie=movie, rating=rev["rating"]
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Review for '{movie.title}' with rating {rev['rating']} created."
                    )
                )
            else:
                self.stdout.write(f"Review for '{movie.title}' already exists.")

        self.stdout.write(self.style.SUCCESS("Database initialization complete."))
