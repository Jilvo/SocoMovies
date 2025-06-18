from django.urls import reverse
from movies.models import Actor, Movie, Review
from rest_framework import status
from rest_framework.test import APITestCase


class MovieAPITestCase(APITestCase):
    def setUp(self):
        """Set up test data for movies and actors."""
        self.actor1 = Actor.objects.create(first_name="John", last_name="Doe")
        self.actor2 = Actor.objects.create(first_name="Jane", last_name="Smith")
        self.movie = Movie.objects.create(
            title="Test Movie", description="A test movie."
        )
        self.movie.actors.set([self.actor1, self.actor2])
        self.review = Review.objects.create(movie=self.movie, rating=4)

    def test_list_movies(self):
        """Test listing movies with actors included."""
        url = reverse("movie-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn("results", data)
        self.assertGreaterEqual(len(data["results"]), 1)
        first = data["results"][0]
        self.assertEqual(first["id"], self.movie.id)
        self.assertEqual(first["title"], self.movie.title)

    def test_retrieve_movie(self):
        """Test retrieving a movie with actors included."""
        url = reverse("movie-detail", args=[self.movie.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["id"], self.movie.id)
        self.assertEqual(data["description"], self.movie.description)
        self.assertIn("actors", data)

    def test_create_movie_with_actors_by_id(self):
        """Test creating a movie with actors by ID."""
        url = reverse("movie-list")
        payload = {
            "title": "New Movie",
            "description": "Created via API",
            "actors": [1, 2],
        }
        response = self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertEqual(data["title"], payload["title"])
        actor_ids = data.get("actors") or [a["id"] for a in data.get("actors", [])]
        self.assertCountEqual(actor_ids, payload["actors"])

    def test_update_movie_actors(self):
        """Test updating movie actors by ID."""
        url = reverse("movie-detail", args=[self.movie.id])
        new_actor = Actor.objects.create(first_name="Alice", last_name="Wonder")
        payload = {
            "actors": [
                new_actor.id,
            ]
        }
        response = self.client.patch(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
