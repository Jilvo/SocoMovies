from rest_framework import viewsets

from .models import Movie, Review,Actor
from .serializers import ActorSerializer, MovieReadSerializer, MovieWriteSerializer, ReviewSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MovieReadSerializer
        return MovieWriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
