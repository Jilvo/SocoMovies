from django.contrib import admin

from .models import Actor, Movie, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    filter_horizontal = ("actors",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "rating", "created_at")
    list_filter = ("rating",)
