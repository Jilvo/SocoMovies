from rest_framework import viewsets

from .models import Actor, Movie, Review
from .serializers import (ActorSerializer, MovieReadSerializer,
                          MovieWriteSerializer, ReviewSerializer)


class MovieViewSet(viewsets.ModelViewSet):
    """ViewSet for managing movies with actors."""

    queryset = Movie.objects.all().order_by("id")

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MovieReadSerializer
        return MovieWriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for managing reviews of movies."""

    queryset = Review.objects.all().order_by("id")
    serializer_class = ReviewSerializer


class ActorViewSet(viewsets.ModelViewSet):
    """ViewSet for managing actors in movies."""

    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
