from rest_framework import serializers

from .models import Actor, Avg, Movie, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "rating", "created_at", "movie")
        read_only_fields = ("created_at",)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors", "reviews", "average_rating")

    def create(self, validated_data):
        actors_data = validated_data.pop("actors", [])
        movie = Movie.objects.create(**validated_data)
        for actor in actors_data:
            obj, _ = Actor.objects.get_or_create(**actor)
            movie.actors.add(obj)
        return movie

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return round(avg, 2) if avg is not None else None

    def update(self, instance, validated_data):
        actors_data = validated_data.pop("actors", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if actors_data is not None:
            instance.actors.clear()
            for actor in actors_data:
                obj, _ = Actor.objects.get_or_create(**actor)
                instance.actors.add(obj)
        return instance
