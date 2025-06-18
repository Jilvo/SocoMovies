from django.urls import reverse
from movies.models import Actor, Movie, Review
from rest_framework import status
from rest_framework.test import APITestCase


class ReviewAPITestCase(APITestCase):
    def setUp(self):
        """Set up test data for reviews."""
        self.actor = Actor.objects.create(first_name="Test", last_name="Actor")
        self.movie = Movie.objects.create(title="Review Movie")
        self.movie.actors.add(self.actor)
        self.review = Review.objects.create(movie=self.movie, rating=5)

    def test_list_reviews(self):
        """Test listing reviews for a movie."""
        url = reverse("review-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn("results", data)
        self.assertGreaterEqual(len(data["results"]), 1)
        first = data["results"][0]
        self.assertEqual(first["rating"], self.review.rating)

    def test_create_review(self):
        """Test creating a review for a movie."""
        url = reverse("review-list")
        payload = {"movie": self.movie.id, "rating": 3}
        response = self.client.post(url, data=payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertEqual(data["rating"], payload["rating"])
        self.assertEqual(data["movie"], payload["movie"])

    def test_retrieve_review(self):
        """Test retrieving a specific review."""
        url = reverse("review-detail", args=[self.review.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["movie"], self.movie.id)
        self.assertEqual(data["rating"], self.review.rating)
