from django.urls import path
from FilmReviewApp import views

app_name = "FilmReviewApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user, name="user"),
    path("logout/", views.logout, name="logout"),
    path("movie/<int:movie_id>/<int:user_id>", views.movie, name="movie"),
    path("review/<int:movie_id>/", views.review, name="review"),
]
