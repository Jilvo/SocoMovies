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


class MovieReadSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors", "reviews", "average_rating")

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(avg_rating=Avg("rating"))["avg_rating"]
        return round(avg, 2) if avg is not None else None


class MovieWriteSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "actors")

    def create(self, validated_data):
        actors = validated_data.pop("actors", [])
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        return movie

    def update(self, instance, validated_data):
        actors = validated_data.pop("actors", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if actors is not None:
            instance.actors.set(actors)
        return instance
