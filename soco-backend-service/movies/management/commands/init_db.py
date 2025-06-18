from django.core.management.base import BaseCommand
from movies.models import Actor, Movie, Review


class Command(BaseCommand):
    help = "Populate the database with sample data."

    def handle(self, *args, **options):

        sample_actors = [
            {"first_name": "Leonardo", "last_name": "DiCaprio"},
            {"first_name": "Joseph", "last_name": "Gordon-Levitt"},
            {"first_name": "Ellen", "last_name": "Page"},
            {"first_name": "Christian", "last_name": "Bale"},
            {"first_name": "Hugh", "last_name": "Jackman"},
            {"first_name": "Matthew", "last_name": "McConaughey"},
            {"first_name": "Anne", "last_name": "Hathaway"},
            {"first_name": "Tom", "last_name": "Hardy"},
            {"first_name": "Harry", "last_name": "Styles"},
        ]
        actors = {}
        for data in sample_actors:
            actor, _ = Actor.objects.get_or_create(
                first_name=data["first_name"], last_name=data["last_name"]
            )
            key = f"{data['first_name']} {data['last_name']}"
            actors[key] = actor
        self.stdout.write(self.style.SUCCESS(f"{len(actors)} actors ensured."))

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
            {
                "title": "Interstellar",
                "description": "Voyage spatial pour sauver l'humanité.",
                "actors": ["Matthew McConaughey", "Anne Hathaway"],
            },
            {
                "title": "The Prestige",
                "description": "Deux magiciens rivaux dans le Londres victorien.",
                "actors": ["Christian Bale", "Hugh Jackman"],
            },
            {
                "title": "Dunkirk",
                "description": "Évacuations de Dunkerque pendant la Seconde Guerre mondiale.",
                "actors": ["Tom Hardy", "Harry Styles"],
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

        reviews_data = [
            {"movie_title": "Inception", "rating": 1},
            {"movie_title": "The Dark Knight", "rating": 1},
            {"movie_title": "Interstellar", "rating": 2},
            {"movie_title": "The Prestige", "rating": 2},
            {"movie_title": "Dunkirk", "rating": 3},
            {"movie_title": "Inception", "rating": 3},
            {"movie_title": "The Dark Knight", "rating": 4},
            {"movie_title": "Interstellar", "rating": 4},
            {"movie_title": "The Prestige", "rating": 5},
            {"movie_title": "Dunkirk", "rating": 5},
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
