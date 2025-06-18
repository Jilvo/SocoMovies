from django.db import models
from django.db.models import Avg


class Actor(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        full = f"{self.first_name} {self.last_name}".strip()
        return full or "<Unnamed Actor>"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies", blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} – {self.rating}"
